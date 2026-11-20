# -*- coding: utf-8 -*-
"""v1.8 · 19 语言 APK 构建流水线（无 Gradle：aapt2 + javac + d8 + zipalign + apksigner）。

产物：dist/apk_build/out/MissingPhoneClass-1.8-<lang>.apk
  - label 新书名《你缺失的那门手机课 · v1.8》
  - versionCode 3 / versionName 1.8-r3（覆盖安装 versionCode ≤2 的旧包）
  - WebView 壳：JS + domStorage + 返回键回退 + 悬浮「更新」按钮
  - 应用内检查更新：更新源默认 GitHub Release（apk-v* 通道，24h 节流自动检查）
    发现新版本 → 下载对应语言 APK → PackageInstaller 安装确认（API≥24）
  - assets: index.html（v1.8/<lang>.html）+ announcements.json（离线公告）

更新通道约定（UpdateManager 与发布脚本共同遵守）：
  tag:   apk-v<书版号>-r<修订号>，如 apk-v1.8-r3；修订号必须与 APK 的 versionCode 一致
  资产:  MissingPhoneClass-<书版号>-<lang>.apk
"""
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(r'C:\Users\18948\Documents\GitHub\Your-Missing-Phone-Class')
SDK = Path(r'C:\Users\18948\AppData\Local\Android\Sdk')
BT = SDK / 'build-tools' / '37.0.0'
JDK = Path(r'C:\Program Files\Java\jdk-26.0.2.1') / 'bin'
AJAR = SDK / 'platforms' / 'android-34' / 'android.jar'
WORK = ROOT / 'dist' / 'apk_build' / 'work'
OUT = ROOT / 'dist' / 'apk_build' / 'out'
KS = ROOT / 'dist' / 'apk_build' / 'phoneclass.keystore'
KS_PASS = 'phoneclass2026'
LANGS = ['ar', 'de', 'el', 'en', 'es', 'fr', 'he', 'id', 'it', 'ja',
         'ko', 'lzh', 'ms', 'pt', 'ru', 'th', 'yue', 'zh-CN', 'zh-TW']
PKG = {'zh-CN': 'zhcn', 'zh-TW': 'zhtw'}  # 其余语言码即包名后缀
LABEL = '你缺失的那门手机课 · v1.8'

# 测试构建可用环境变量覆盖：APK_VC / APK_VN / APK_OUT / APK_LANGS（逗号分隔）/ APK_API（检查更新源）
import os
VC = int(os.environ.get('APK_VC', '4'))
VN = os.environ.get('APK_VN', '1.8-r4')
OUT = Path(os.environ.get('APK_OUT', str(OUT)))
UPD_API = os.environ.get('APK_API',
    'https://api.github.com/repos/ClassTechStar/Your-Missing-Phone-Class/releases?per_page=20')
if os.environ.get('APK_LANGS'):
    LANGS = [l for l in LANGS if l in os.environ['APK_LANGS'].split(',')]

# 每语言 UI 文案：(悬浮按钮, 发现新版本, 立即更新, 稍后, 下载中, 已是最新, 失败, 安装未完成)
UPD = {
 'ar': ('تحديث', 'إصدار جديد متاح: ', 'تحديث الآن', 'لاحقًا', 'جارٍ تنزيل التحديث…',
        'أنت تستخدم أحدث إصدار', 'تعذّر التحقق من التحديثات', 'لم يكتمل التثبيت'),
 'de': ('Update', 'Neue Version verfügbar: ', 'Jetzt aktualisieren', 'Später',
        'Update wird heruntergeladen…', 'Du bist auf dem neuesten Stand',
        'Update-Prüfung fehlgeschlagen', 'Installation nicht abgeschlossen'),
 'el': ('Ενημέρωση', 'Νέα έκδοση διαθέσιμη: ', 'Ενημέρωση τώρα', 'Αργότερα',
        'Λήψη ενημέρωσης…', 'Έχετε την τελευταία έκδοση',
        'Ο έλεγχος ενημέρωσης απέτυχε', 'Η εγκατάσταση δεν ολοκληρώθηκε'),
 'en': ('Update', 'New version available: ', 'Update now', 'Later',
        'Downloading update…', 'You are up to date',
        'Update check failed', 'Installation not completed'),
 'es': ('Actualizar', 'Nueva versión disponible: ', 'Actualizar ahora', 'Más tarde',
        'Descargando actualización…', 'Ya tienes la última versión',
        'No se pudo comprobar si hay actualizaciones', 'Instalación no completada'),
 'fr': ('Mise à jour', 'Nouvelle version disponible : ', 'Mettre à jour', 'Plus tard',
        'Téléchargement de la mise à jour…', 'Vous êtes à jour',
        'Échec de la vérification des mises à jour', 'Installation non terminée'),
 'he': ('עדכון', 'גרסה חדשה זמינה: ', 'עדכון עכשיו', 'מאוחר יותר', 'מוריד עדכון…',
        'הגרסה מעודכנת', 'בדיקת העדכונים נכשלה', 'ההתקנה לא הושלמה'),
 'id': ('Perbarui', 'Versi baru tersedia: ', 'Perbarui sekarang', 'Nanti',
        'Mengunduh pembaruan…', 'Sudah versi terbaru',
        'Gagal memeriksa pembaruan', 'Pemasangan tidak selesai'),
 'it': ('Aggiorna', 'Nuova versione disponibile: ', 'Aggiorna ora', 'Più tardi',
        'Download aggiornamento…', 'Sei già aggiornato',
        'Verifica degli aggiornamenti non riuscita', 'Installazione non completata'),
 'ja': ('更新', '新しいバージョンがあります: ', '今すぐ更新', '後で',
        '更新をダウンロード中…', '最新版です',
        '更新の確認に失敗しました', 'インストールが完了しませんでした'),
 'ko': ('업데이트', '새 버전 사용 가능: ', '지금 업데이트', '나중에',
        '업데이트 다운로드 중…', '최신 버전입니다',
        '업데이트 확인 실패', '설치가 완료되지 않았습니다'),
 'lzh': ('更新', '新版既出：', '即刻更新', '緩圖', '方取新版…',
         '已為最新', '稽新未成', '未竟安裝'),
 'ms': ('Kemas kini', 'Versi baharu tersedia: ', 'Kemas kini sekarang', 'Nanti',
        'Memuat turun kemas kini…', 'Sudah versi terkini',
        'Gagal menyemak kemas kini', 'Pemasangan tidak selesai'),
 'pt': ('Atualizar', 'Nova versão disponível: ', 'Atualizar agora', 'Mais tarde',
        'Baixando atualização…', 'Você já está atualizado',
        'Falha ao verificar atualizações', 'Instalação não concluída'),
 'ru': ('Обновление', 'Доступна новая версия: ', 'Обновить сейчас', 'Позже',
        'Скачивание обновления…', 'У вас последняя версия',
        'Не удалось проверить обновления', 'Установка не завершена'),
 'th': ('อัปเดต', 'มีเวอร์ชันใหม่: ', 'อัปเดตเลย', 'ภายหลัง',
        'กำลังดาวน์โหลดอัปเดต…', 'คุณใช้เวอร์ชันล่าสุดแล้ว',
        'ตรวจสอบอัปเดตไม่สำเร็จ', 'การติดตั้งไม่สำเร็จ'),
 'yue': ('更新', '有新版本：', '而家更新', '遲啲先', '下載更新中…',
         '已經係最新版', '檢查更新失敗', '安裝未完成'),
 'zh-CN': ('更新', '发现新版本：', '立即更新', '稍后再说', '正在下载更新…',
           '已是最新版本', '检查更新失败，请稍后重试', '安装未完成'),
 'zh-TW': ('更新', '發現新版本：', '立即更新', '稍後再說', '正在下載更新…',
           '已是最新版本', '檢查更新失敗，請稍後重試', '安裝未完成'),
}

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', **kw)
    if r.returncode != 0:
        raise SystemExit(f'FAIL {" ".join(map(str, cmd[:4]))}:\n{r.stdout}\n{r.stderr}')
    return r

# ── 0. keystore（一次性）──
if not KS.exists():
    run([str(JDK / 'keytool.exe'), '-genkeypair', '-v', '-keystore', str(KS), '-alias', 'phoneclass',
         '-keyalg', 'RSA', '-keysize', '2048', '-validity', '9000',
         '-storepass', KS_PASS, '-keypass', KS_PASS,
         '-dname', 'CN=ClassTechStar, O=PhoneClass, C=CN'])
    print('keystore 已生成')

# ── 1. 共享壳源码与图标 ──
shutil.rmtree(WORK, ignore_errors=True)
(WORK / 'src' / 'com' / 'classtechstar' / 'phoneclass').mkdir(parents=True)
(WORK / 'assets').mkdir(parents=True)
(WORK / 'res').mkdir(parents=True)

MAIN_ACTIVITY = """package com.classtechstar.phoneclass;

import android.app.Activity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.FrameLayout;

public class MainActivity extends Activity {
    private WebView web;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        web = new WebView(this);
        WebSettings st = web.getSettings();
        st.setJavaScriptEnabled(true);
        st.setDomStorageEnabled(true);
        st.setAllowFileAccess(true);
        st.setLoadWithOverviewMode(true);
        st.setUseWideViewPort(true);
        web.setWebViewClient(new WebViewClient());
        web.loadUrl("file:///android_asset/index.html");

        FrameLayout root = new FrameLayout(this);
        root.addView(web, new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT));

        Button up = new Button(this);
        up.setText("@LABEL@");
        up.setAllCaps(false);
        up.setTextSize(12);
        up.setAlpha(0.72f);
        up.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { UpdateManager.check(MainActivity.this, true); }
        });
        FrameLayout.LayoutParams lp = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.WRAP_CONTENT, FrameLayout.LayoutParams.WRAP_CONTENT,
                Gravity.BOTTOM | Gravity.START);
        int d = Math.round(12 * getResources().getDisplayMetrics().density);
        lp.setMargins(d, 0, 0, d);
        root.addView(up, lp);
        setContentView(root);

        UpdateManager.autoCheck(this);
    }

    @Override protected void onResume() {
        super.onResume();
        UpdateManager.onResumed(this);
    }

    @Override public void onBackPressed() {
        if (web != null && web.canGoBack()) web.goBack(); else super.onBackPressed();
    }
}
"""

UPDATE_MANAGER = """package com.classtechstar.phoneclass;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.PendingIntent;
import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageInfo;
import android.content.pm.PackageInstaller;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Handler;
import android.os.Looper;
import android.provider.Settings;
import android.util.JsonReader;
import android.util.JsonToken;
import android.util.Log;
import android.widget.Toast;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

/**
 * 应用内检查更新与自动安装。更新源默认 GitHub Release：
 * 取仓库 Releases（新到旧）中第一个 tag 匹配 apk-v<书版>-r<修订> 的发布，
 * 修订号大于本包 versionCode 即视为有更新；下载对应语言资产后
 * API 24+ 走 PackageInstaller 会话安装，更早版本走 ACTION_VIEW 安装。
 */
public class UpdateManager {
    private static final String TAG = "PhoneClassUpdate";
    /** 本壳对应的语言码（与资产名一致，如 zh-CN）。 */
    static final String LANG = "@LANG@";
    /** 更新源（默认 GitHub Release 的 apk-v* 通道；可用 APK_API 环境变量替换为测试源）。 */
    static final String RELEASES_API = "@API@";
    static final String TXT_LABEL = "@LABEL@";
    static final String TXT_FOUND = "@FOUND@";
    static final String TXT_INSTALL = "@INSTALL@";
    static final String TXT_LATER = "@LATER@";
    static final String TXT_DOWNLOADING = "@DL@";
    static final String TXT_LATEST = "@LATEST@";
    static final String TXT_FAIL = "@FAIL@";
    static final String TXT_INST_FAIL = "@INSTFAIL@";

    private static final long THROTTLE_MS = 24L * 60 * 60 * 1000;
    private static final Handler UI = new Handler(Looper.getMainLooper());
    private static boolean checking;
    private static String pendingInstallPath;
    private static ProgressDialog progress;

    /** 启动自动检查：24 小时节流，被「稍后」跳过的修订号不再打扰。 */
    static void autoCheck(final Activity a) {
        SharedPreferences sp = a.getSharedPreferences("update", Activity.MODE_PRIVATE);
        if (System.currentTimeMillis() - sp.getLong("last", 0) < THROTTLE_MS) return;
        check(a, false);
    }

    /** 手动/自动检查入口。 */
    static void check(final Activity a, final boolean manual) {
        if (checking) return;
        checking = true;
        new Thread(new Runnable() { @Override public void run() {
            String[] hitRes = null;
            String errRes = null;
            try { hitRes = queryLatest(a); }
            catch (Exception e) { Log.w(TAG, "query failed", e); errRes = String.valueOf(e.getMessage()); }
            final String[] hit = hitRes;
            final String err = errRes;
            markNow(a);
            checking = false;
            if (hit != null) {
                long skip = a.getSharedPreferences("update", Activity.MODE_PRIVATE).getLong("skip_rev", 0);
                if (!manual && parseRev(hit[0]) <= skip) return;
                UI.post(new Runnable() { @Override public void run() { offer(a, hit); } });
            } else if (manual) {
                UI.post(new Runnable() { @Override public void run() {
                    toast(a, err == null ? TXT_LATEST : TXT_FAIL);
                }});
            }
        }}).start();
    }

    /** 安装权限回来之后续接安装。 */
    static void onResumed(Activity a) {
        if (pendingInstallPath == null) return;
        File f = new File(pendingInstallPath);
        pendingInstallPath = null;
        if (Build.VERSION.SDK_INT >= 26 && !a.getPackageManager().canRequestPackageInstalls()) return;
        install(a, f);
    }

    // ── 查询 ──
    private static String[] queryLatest(Activity a) throws Exception {
        HttpURLConnection c = (HttpURLConnection) new URL(RELEASES_API).openConnection();
        c.setConnectTimeout(10000);
        c.setReadTimeout(15000);
        c.setRequestProperty("Accept", "application/vnd.github+json");
        c.setRequestProperty("User-Agent", "PhoneClass-App");
        int code = c.getResponseCode();
        InputStream raw = code >= 400 ? c.getErrorStream() : c.getInputStream();
        if (raw == null) throw new IllegalStateException("HTTP " + code);
        JsonReader r = new JsonReader(new InputStreamReader(raw, "UTF-8"));
        try {
            r.beginArray();
            while (r.hasNext()) {
                String tag = null, body = null;
                boolean skip = false;
                List<String[]> assets = new ArrayList<String[]>();
                r.beginObject();
                while (r.hasNext()) {
                    String n = r.nextName();
                    if ("tag_name".equals(n)) tag = r.nextString();
                    else if ("draft".equals(n)) { if (r.nextBoolean()) skip = true; }
                    else if ("prerelease".equals(n)) { if (r.nextBoolean()) skip = true; }
                    else if ("body".equals(n)) {
                        if (r.peek() == JsonToken.NULL) r.nextNull(); else body = r.nextString();
                    } else if ("assets".equals(n)) {
                        r.beginArray();
                        while (r.hasNext()) {
                            String an = null, au = null;
                            r.beginObject();
                            while (r.hasNext()) {
                                String k = r.nextName();
                                if ("name".equals(k)) an = r.nextString();
                                else if ("browser_download_url".equals(k)) au = r.nextString();
                                else r.skipValue();
                            }
                            r.endObject();
                            if (an != null && au != null) assets.add(new String[]{an, au});
                        }
                        r.endArray();
                    } else r.skipValue();
                }
                r.endObject();
                if (skip || tag == null || !tag.startsWith("apk-v")) continue;
                if (parseRev(tag) <= currentCode(a)) break;  // 最新 apk 发布即基准
                String want = assetFor(tag);
                for (String[] as : assets) {
                    if (want.equals(as[0])) return new String[]{tag, as[1], excerpt(body)};
                }
                break;  // 最新 apk 发布缺本语言资产：不再向更旧的发布回溯
            }
            r.endArray();
        } finally {
            try { r.close(); } catch (Exception ignore) { }
            c.disconnect();
        }
        return null;
    }

    static long parseRev(String tag) {
        int i = tag.lastIndexOf("-r");
        try { return Long.parseLong(tag.substring(i + 2)); } catch (Exception e) { return 0; }
    }

    private static long currentCode(Activity a) {
        try {
            PackageInfo p = a.getPackageManager().getPackageInfo(a.getPackageName(), 0);
            return p.versionCode;
        } catch (Exception e) { return 0; }
    }

    private static String assetFor(String tag) {
        String ver = tag.substring("apk-v".length(), tag.lastIndexOf("-r"));
        return "MissingPhoneClass-" + ver + "-" + LANG + ".apk";
    }

    private static String excerpt(String body) {
        if (body == null) return "";
        String b = body.replace("\\r", "").trim();
        return b.length() > 300 ? b.substring(0, 300) + "…" : b;
    }

    private static void markNow(Activity a) {
        a.getSharedPreferences("update", Activity.MODE_PRIVATE)
                .edit().putLong("last", System.currentTimeMillis()).apply();
    }

    // ── 提示与下载 ──
    private static void offer(final Activity a, final String[] hit) {
        String verName;
        try {
            PackageInfo p = a.getPackageManager().getPackageInfo(a.getPackageName(), 0);
            verName = p.versionName;
        } catch (Exception e) { verName = "?"; }
        String notes = hit[2];
        String msg = (notes.isEmpty() ? "" : notes + "\\n\\n")
                + verName + "  →  " + hit[0];
        new AlertDialog.Builder(a)
                .setTitle(TXT_FOUND + hit[0])
                .setMessage(msg)
                .setPositiveButton(TXT_INSTALL, new DialogInterface.OnClickListener() {
                    @Override public void onClick(DialogInterface d, int w) {
                        downloadAndInstall(a, hit[0], hit[1]);
                    }
                })
                .setNegativeButton(TXT_LATER, new DialogInterface.OnClickListener() {
                    @Override public void onClick(DialogInterface d, int w) {
                        a.getSharedPreferences("update", Activity.MODE_PRIVATE)
                                .edit().putLong("skip_rev", parseRev(hit[0])).apply();
                    }
                })
                .show();
    }

    private static void downloadAndInstall(final Activity a, final String tag, final String url) {
        final File dir = a.getExternalFilesDir("update");
        if (dir == null) { toast(a, TXT_FAIL); return; }
        final File f = new File(dir, "update-" + tag + ".apk");
        progress = new ProgressDialog(a);
        progress.setTitle(TXT_DOWNLOADING);
        progress.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
        progress.setMax(100);
        progress.setCancelable(false);
        progress.show();
        new Thread(new Runnable() { @Override public void run() {
            try {
                HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
                c.setConnectTimeout(15000);
                c.setReadTimeout(30000);
                c.setRequestProperty("User-Agent", "PhoneClass-App");
                int code = c.getResponseCode();
                if (code >= 400) throw new IllegalStateException("HTTP " + code);
                long total = c.getContentLength();
                InputStream in = c.getInputStream();
                FileOutputStream out = new FileOutputStream(f);
                byte[] buf = new byte[1 << 15];
                long done = 0;
                int n;
                while ((n = in.read(buf)) > 0) {
                    out.write(buf, 0, n);
                    done += n;
                    if (total > 0) {
                        final int pct = (int) (done * 100 / total);
                        UI.post(new Runnable() { @Override public void run() {
                            if (progress != null) progress.setProgress(pct);
                        }});
                    }
                }
                out.close();
                in.close();
                c.disconnect();
                UI.post(new Runnable() { @Override public void run() {
                    dismissProgress();
                    install(a, f);
                }});
            } catch (final Exception e) {
                Log.w(TAG, "download failed", e);
                f.delete();
                UI.post(new Runnable() { @Override public void run() {
                    dismissProgress();
                    toast(a, TXT_FAIL);
                }});
            }
        }}).start();
    }

    private static void dismissProgress() {
        if (progress != null) { try { progress.dismiss(); } catch (Exception ignore) { } progress = null; }
    }

    // ── 安装 ──
    private static void install(Activity a, File f) {
        if (Build.VERSION.SDK_INT >= 26 && !a.getPackageManager().canRequestPackageInstalls()) {
            pendingInstallPath = f.getAbsolutePath();
            try {
                a.startActivity(new Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,
                        Uri.parse("package:" + a.getPackageName())));
            } catch (Exception e) {
                Log.w(TAG, "cannot open unknown-app settings", e);
            }
            return;
        }
        if (Build.VERSION.SDK_INT >= 24) sessionInstall(a, f); else legacyInstall(a, f);
    }

    private static void sessionInstall(Activity a, File f) {
        PackageInstaller.Session session = null;
        try {
            PackageManager pm = a.getPackageManager();
            PackageInstaller pi = pm.getPackageInstaller();
            PackageInstaller.SessionParams sp =
                    new PackageInstaller.SessionParams(PackageInstaller.SessionParams.MODE_FULL_INSTALL);
            int id = pi.createSession(sp);
            session = pi.openSession(id);
            InputStream in = new FileInputStream(f);
            OutputStream out = session.openWrite("PhoneClassUpdate", 0, f.length());
            byte[] buf = new byte[1 << 15];
            int n;
            while ((n = in.read(buf)) > 0) out.write(buf, 0, n);
            session.fsync(out);
            out.close();
            in.close();
            Intent status = new Intent(a, UpdateStatusReceiver.class);
            int flags = PendingIntent.FLAG_UPDATE_CURRENT;
            if (Build.VERSION.SDK_INT >= 23) flags |= PendingIntent.FLAG_IMMUTABLE;
            session.commit(PendingIntent.getBroadcast(a, id, status, flags).getIntentSender());
            session.close();
        } catch (Exception e) {
            Log.w(TAG, "session install failed", e);
            if (session != null) { try { session.abandon(); } catch (Exception ignore) { } }
            toast(a, TXT_INST_FAIL);
        }
    }

    private static void legacyInstall(Activity a, File f) {
        try {
            Intent i = new Intent(Intent.ACTION_VIEW);
            i.setDataAndType(Uri.fromFile(f), "application/vnd.android.package-archive");
            i.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_GRANT_READ_URI_PERMISSION);
            a.startActivity(i);
        } catch (Exception e) {
            Log.w(TAG, "legacy install failed", e);
            toast(a, TXT_INST_FAIL);
        }
    }

    private static void toast(Activity a, String s) {
        Toast.makeText(a, s, Toast.LENGTH_LONG).show();
    }
}
"""

UPDATE_STATUS = """package com.classtechstar.phoneclass;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInstaller;
import android.widget.Toast;

/** PackageInstaller 会话状态回调：中转系统确认框，失败时提示。 */
public class UpdateStatusReceiver extends BroadcastReceiver {
    @Override public void onReceive(Context c, Intent i) {
        int status = i.getIntExtra(PackageInstaller.EXTRA_STATUS, PackageInstaller.STATUS_FAILURE);
        if (status == PackageInstaller.STATUS_PENDING_USER_ACTION) {
            Intent confirm = i.getParcelableExtra(Intent.EXTRA_INTENT);
            if (confirm != null) {
                confirm.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                try { c.startActivity(confirm); } catch (Exception ignore) { }
            }
        } else if (status != PackageInstaller.STATUS_SUCCESS) {
            String msg = i.getStringExtra(PackageInstaller.EXTRA_STATUS_MESSAGE);
            Toast.makeText(c, UpdateManager.TXT_INST_FAIL + (msg == null ? "" : " (" + msg + ")"),
                    Toast.LENGTH_LONG).show();
        }
    }
}
"""

MANIFEST = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.classtechstar.phoneclass.{pkg}"
    android:versionCode="{vc}" android:versionName="{vn}">
  <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="34"/>
  <uses-permission android:name="android.permission.INTERNET"/>
  <uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES"/>
  <application android:label="{label}" android:icon="@mipmap/ic_launcher"
      android:supportsRtl="true" android:usesCleartextTraffic="true"
      android:theme="@android:style/Theme.Material.Light.NoActionBar">
    <activity android:name="com.classtechstar.phoneclass.MainActivity" android:exported="true"
        android:configChanges="orientation|screenSize|keyboardHidden">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>
    <receiver android:name="com.classtechstar.phoneclass.UpdateStatusReceiver" android:exported="false"/>
  </application>
</manifest>
"""

# 图标五档密度（从 icons/icon-512.png 缩放）
from PIL import Image
src = Image.open(ROOT / 'icons' / 'icon-512.png').convert('RGBA')
for dpi, px in [('mdpi', 48), ('hdpi', 72), ('xhdpi', 96), ('xxhdpi', 144), ('xxxhdpi', 192)]:
    d = WORK / 'res' / f'mipmap-{dpi}'
    d.mkdir(parents=True, exist_ok=True)
    src.resize((px, px), Image.LANCZOS).save(d / 'ic_launcher.png')

# ── 2. 逐语言构建 ──
ann = ROOT / 'announcements.json'
OUT.mkdir(parents=True, exist_ok=True)
SRC = WORK / 'src' / 'com' / 'classtechstar' / 'phoneclass'
for lang in LANGS:
    pkg = PKG.get(lang, lang)
    label, found, install, later, dl, latest, fail, instfail = UPD[lang]
    tag = f'MissingPhoneClass-1.8-{lang}'
    print(f'… {lang}', flush=True)
    mfile = WORK / f'AndroidManifest-{lang}.xml'
    mfile.write_text(MANIFEST.format(pkg=pkg, label=LABEL, vc=VC, vn=VN), encoding='utf-8')

    def wsrc(name, body, **toks):
        s = body
        for k, v in toks.items():
            s = s.replace('@' + k + '@', v)
        p = SRC / name
        p.write_text(s, encoding='utf-8')
        return p

    f1 = wsrc('MainActivity.java', MAIN_ACTIVITY, LANG=lang, LABEL=label)
    f2 = wsrc('UpdateManager.java', UPDATE_MANAGER, LANG=lang, API=UPD_API, LABEL=label, FOUND=found,
              INSTALL=install, LATER=later, DL=dl, LATEST=latest, FAIL=fail, INSTFAIL=instfail)
    f3 = wsrc('UpdateStatusReceiver.java', UPDATE_STATUS)

    # aapt2 compile + link
    run([str(BT / 'aapt2.exe'), 'compile', '--dir', str(WORK / 'res'), '-o', str(WORK / 'res.zip')])
    run([str(BT / 'aapt2.exe'), 'link', '-o', str(WORK / 'base.apk'),
         '-I', str(AJAR), '--manifest', str(mfile),
         '--java', str(WORK / 'gen'), str(WORK / 'res.zip')])

    # javac + d8（Java 源码含各语言 UI 文案，必须显式 UTF-8）
    run([str(JDK / 'javac.exe'), '--release', '11', '-encoding', 'UTF-8', '-cp', str(AJAR),
         '-d', str(WORK / 'cls'),
         str(f1), str(f2), str(f3),
         str(WORK / 'gen' / 'com' / 'classtechstar' / 'phoneclass' / pkg / 'R.java')])
    run([str(BT / 'd8.bat'), '--release', '--lib', str(AJAR),
         '--output', str(WORK), *map(str, (WORK / 'cls').rglob('*.class'))])

    # 组装：base.apk + assets + dex
    unsigned = WORK / f'{tag}.unsigned.apk'
    shutil.copyfile(WORK / 'base.apk', unsigned)
    with zipfile.ZipFile(unsigned, 'a', zipfile.ZIP_DEFLATED) as z:
        z.write(ROOT / 'v1.8' / f'{lang}.html', 'assets/index.html')
        if ann.exists():
            z.write(ann, 'assets/announcements.json')
        z.write(WORK / 'classes.dex', 'classes.dex')

    # zipalign + 签名
    aligned = WORK / f'{tag}.aligned.apk'
    run([str(BT / 'zipalign.exe'), '-f', '-P', '16', '4', str(unsigned), str(aligned)])
    final = OUT / f'{tag}.apk'
    run([str(BT / 'apksigner.bat'), 'sign', '--ks', str(KS),
         '--ks-pass', f'pass:{KS_PASS}', '--key-pass', f'pass:{KS_PASS}',
         '--out', str(final), str(aligned)])
    run([str(BT / 'apksigner.bat'), 'verify', str(final)])

print('全部完成 →', OUT)
for f in sorted(OUT.glob('*.apk')):
    print(f' {f.name}  {f.stat().st_size//1024} KB')
