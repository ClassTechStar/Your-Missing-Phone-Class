#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 18 语术语表（manifest/glossary/<lang>.json）。

历史教训（th 语 1992 处机翻损坏）表明：SoC/NPU/Passkey/eSIM 这类术语
一旦逐词漂移，译文即损坏。术语表把每语言的译法锁定为单一事实源，
供机翻提示词、Weblate 术语检查与人工审校共同引用。

术语表 schema：{"lang": <code>, "terms": {"<中文术语>": "<该语言译法>", ...}}
用法：python scripts/gen_glossary.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 中文术语 → 18 语译法（缩写词保留原文并附本地注解；译法一经锁定不再漂移）
TERMS = {
    "SoC（系统级芯片）": {
        "zh-TW": "SoC（系統單晶片）", "yue": "SoC（系統級晶片）", "lzh": "SoC（片上系統）",
        "ja": "SoC（システムオンチップ）", "ko": "SoC(시스템 온 칩)", "en": "SoC (system-on-chip)",
        "ru": "SoC (система на кристалле)", "it": "SoC (system-on-chip)", "pt": "SoC (system-on-chip)",
        "es": "SoC (system-on-chip)", "fr": "SoC (system-on-chip)", "de": "SoC (System-on-a-Chip)",
        "ar": "SoC (نظام على رقاقة)", "he": "SoC (מערכת על שבב)", "th": "SoC (ระบบบนชิป)",
        "id": "SoC (system-on-chip)", "ms": "SoC (system-on-chip)", "el": "SoC (σύστημα σε τσιπ)",
    },
    "NPU（神经网络处理器）": {
        "zh-TW": "NPU（神經網路處理器）", "yue": "NPU（神經網絡處理器）", "lzh": "NPU（神經處理之器）",
        "ja": "NPU（ニューラルネットワーク処理装置）", "ko": "NPU(신경망 처리 장치)",
        "en": "NPU (neural processing unit)", "ru": "NPU (нейронный процессор)",
        "it": "NPU (unità di elaborazione neurale)", "pt": "NPU (unidade de processamento neural)",
        "es": "NPU (unidad de procesamiento neuronal)", "fr": "NPU (unité de traitement neuronal)",
        "de": "NPU (Neural Processing Unit)", "ar": "NPU (وحدة معالجة عصبية)",
        "he": "NPU (יחידת עיבוד עצבי)", "th": "NPU (หน่วยประมวลผลประสาท)",
        "id": "NPU (unit pemroses neural)", "ms": "NPU (unit pemprosesan neural)",
        "el": "NPU (μονάδα νευρωνικής επεξεργασίας)",
    },
    "GPU（图形处理器）": {
        "zh-TW": "GPU（圖形處理器）", "yue": "GPU（圖形處理器）", "lzh": "GPU（圖繪之器）",
        "ja": "GPU（グラフィックス処理装置）", "ko": "GPU(그래픽 처리 장치)", "en": "GPU (graphics processor)",
        "ru": "GPU (графический процессор)", "it": "GPU (processore grafico)", "pt": "GPU (processador gráfico)",
        "es": "GPU (procesador gráfico)", "fr": "GPU (processeur graphique)", "de": "GPU (Grafikprozessor)",
        "ar": "GPU (معالج الرسوميات)", "he": "GPU (מעבד גרפי)", "th": "GPU (หน่วยประมวลผลกราฟิก)",
        "id": "GPU (prosesor grafis)", "ms": "GPU (pemproses grafik)", "el": "GPU (επεξεργαστής γραφικών)",
    },
    "eSIM（嵌入式SIM卡）": {
        "zh-TW": "eSIM（嵌入式 SIM 卡）", "yue": "eSIM（嵌入式 SIM 卡）", "lzh": "eSIM（內嵌之 SIM）",
        "ja": "eSIM（組み込みSIM）", "ko": "eSIM(내장형 SIM)", "en": "eSIM (embedded SIM)",
        "ru": "eSIM (встроенная SIM)", "it": "eSIM (SIM integrata)", "pt": "eSIM (SIM embarcado)",
        "es": "eSIM (SIM integrada)", "fr": "eSIM (SIM intégrée)", "de": "eSIM (eingebettete SIM)",
        "ar": "eSIM (شريحة مدمجة)", "he": "eSIM (SIM מוטבע)", "th": "eSIM (ซิมฝังใน)",
        "id": "eSIM (SIM tertanam)", "ms": "eSIM (SIM terbenam)", "el": "eSIM (ενσωματωμένη SIM)",
    },
    "Passkey（通行密钥）": {
        "zh-TW": "Passkey（通行金鑰）", "yue": "Passkey（通行密鑰）", "lzh": "Passkey（通行之鑰）",
        "ja": "パスキー（Passkey）", "ko": "패스키(Passkey)", "en": "Passkey",
        "ru": "Passkey (пароль-ключ)", "it": "Passkey (chiave di accesso)", "pt": "Passkey (chave de acesso)",
        "es": "Passkey (clave de acceso)", "fr": "Passkey (clé d'accès)", "de": "Passkey (Zugriffsschlüssel)",
        "ar": "Passkey (مفتاح المرور)", "he": "Passkey (מפתח גישה)", "th": "Passkey (คีย์ผ่าน)",
        "id": "Passkey (kunci akses)", "ms": "Passkey (kunci akses)", "el": "Passkey (κλειδί πρόσβασης)",
    },
    "双因素认证": {
        "zh-TW": "雙重驗證", "yue": "雙重認證", "lzh": "二重驗證",
        "ja": "二要素認証", "ko": "2단계 인증", "en": "two-factor authentication (2FA)",
        "ru": "двухфакторная аутентификация", "it": "autenticazione a due fattori",
        "pt": "autenticação de dois fatores", "es": "autenticación de dos factores",
        "fr": "authentification à deux facteurs", "de": "Zwei-Faktor-Authentifizierung",
        "ar": "المصادقة الثنائية", "he": "אימות דו-שלבי", "th": "การยืนยันตัวตนสองชั้น",
        "id": "autentikasi dua faktor", "ms": "pengesahan dua faktor",
        "el": "ταυτοποίηση δύο παραγόντων",
    },
    "云备份": {
        "zh-TW": "雲端備份", "yue": "雲備份", "lzh": "雲中之備",
        "ja": "クラウドバックアップ", "ko": "클라우드 백업", "en": "cloud backup",
        "ru": "облачная резервная копия", "it": "backup su cloud", "pt": "backup na nuvem",
        "es": "copia de seguridad en la nube", "fr": "sauvegarde dans le cloud",
        "de": "Cloud-Backup", "ar": "النسخ الاحتياطي السحابي", "he": "גיבוי בענן",
        "th": "การสำรองข้อมูลบนคลาวด์", "id": "pencadangan cloud", "ms": " sandaran awan",
        "el": "διαδικτυακό αντίγραφο ασφαλείας",
    },
    "权限管理": {
        "zh-TW": "權限管理", "yue": "權限管理", "lzh": "權柄之治",
        "ja": "権限管理", "ko": "권한 관리", "en": "permission management",
        "ru": "управление разрешениями", "it": "gestione dei permessi", "pt": "gerenciamento de permissões",
        "es": "gestión de permisos", "fr": "gestion des autorisations", "de": "Berechtigungsverwaltung",
        "ar": "إدارة الأذونات", "he": "ניהול הרשאות", "th": "การจัดการสิทธิ์",
        "id": "manajemen izin", "ms": "pengurusan kebenaran", "el": "διαχείριση αδειών",
    },
    "侧载": {
        "zh-TW": "側載", "yue": "側載", "lzh": "旁裝",
        "ja": "サイドロード", "ko": "사이드로딩", "en": "sideloading",
        "ru": "сайдлоадинг (установка вне магазина)", "it": "sideloading", "pt": "sideloading",
        "es": "sideloading", "fr": "sideloading", "de": "Sideloaden",
        "ar": "التحميل الجانبي", "he": "טעינה צדדית", "th": "การติดตั้งแอปนอกสโตร์",
        "id": "sideloading", "ms": "sideloading", "el": "sideloading",
    },
    "刷机": {
        "zh-TW": "刷機", "yue": "刷機", "lzh": "刷機",
        "ja": "端末のフラッシュ", "ko": "펌웨어 플래싱", "en": "firmware flashing",
        "ru": "прошивка устройства", "it": "flash del firmware", "pt": "flash de firmware",
        "es": "flasheo de firmware", "fr": "flashage du firmware", "de": "Firmware-Flashen",
        "ar": "تثبيت البرنامج الثابت", "he": "הבהוב קושחה", "th": "การแฟลชเฟิร์มแวร์",
        "id": "flashing firmware", "ms": "menyalin firmware", "el": "φλασάρισμα firmware",
    },
    "恢复出厂设置": {
        "zh-TW": "回復原廠設定", "yue": "恢復出廠設置", "lzh": "復原廠設",
        "ja": "初期化（工場出荷状態に戻す）", "ko": "공장 초기화", "en": "factory reset",
        "ru": "сброс к заводским настройкам", "it": "ripristino delle impostazioni di fabbrica",
        "pt": "restauração de fábrica", "es": "restablecimiento de fábrica",
        "fr": "réinitialisation d'usine", "de": "Werksreset", "ar": "إعادة ضبط المصنع",
        "he": "איפוס להגדרות יצרן", "th": "การรีเซ็ตเป็นค่าจากโรงงาน",
        "id": "reset pabrik", "ms": "tetapan semula kilang", "el": "επαναφορά εργοστασίου",
    },
    "钓鱼（网络诈骗）": {
        "zh-TW": "釣魚（網路詐騙）", "yue": "釣魚（網絡詐騙）", "lzh": "釣魚之詐",
        "ja": "フィッシング詐欺", "ko": "피싱 사기", "en": "phishing",
        "ru": "фишинг", "it": "phishing", "pt": "phishing", "es": "phishing", "fr": "hameçonnage (phishing)",
        "de": "Phishing", "ar": "التصيّد الاحتيالي", "he": "דיוג (פישינג)", "th": "การฟิชชิง",
        "id": "phishing", "ms": "pengancing data (phishing)", "el": "phishing",
    },
    "勒索软件": {
        "zh-TW": "勒索軟體", "yue": "勒索軟件", "lzh": "勒贖之軟件",
        "ja": "ランサムウェア", "ko": "랜섬웨어", "en": "ransomware", "ru": "программа-вымогатель",
        "it": "ransomware", "pt": "ransomware", "es": "ransomware", "fr": "rançongiciel",
        "de": "Ransomware", "ar": "برامج الفدية", "he": "כופרה", "th": "แรนซัมแวร์",
        "id": "ransomware", "ms": "perisian tebusan", "el": "ransomware",
    },
    "广告追踪": {
        "zh-TW": "廣告追蹤", "yue": "廣告追蹤", "lzh": "廣吿之追",
        "ja": "広告トラッキング", "ko": "광고 추적", "en": "ad tracking", "ru": "рекламное отслеживание",
        "it": "tracciamento pubblicitario", "pt": "rastreamento de anúncios", "es": "seguimiento publicitario",
        "fr": "suivi publicitaire", "de": "Werbe-Tracking", "ar": "تتبع الإعلانات",
        "he": "מעקב פרסומות", "th": "การติดตามโฆษณา", "id": "pelacakan iklan",
        "ms": "penjejakan iklan", "el": "παρακολούθηση διαφημίσεων",
    },
    "刷新率": {
        "zh-TW": "更新率", "yue": "刷新率", "lzh": "刷屏之率",
        "ja": "リフレッシュレート", "ko": "주사율", "en": "refresh rate", "ru": "частота обновления",
        "it": "frequenza di aggiornamento", "pt": "taxa de atualização", "es": "frecuencia de actualización",
        "fr": "taux de rafraîchissement", "de": "Bildwiederholrate", "ar": "معدل التحديث",
        "he": "קצב רענון", "th": "อัตราการรีเฟรช", "id": "tingkat penyegaran",
        "ms": "kadar penyegaran", "el": "ρυθμός ανανέωσης",
    },
    "分辨率": {
        "zh-TW": "解析度", "yue": "分辨率", "lzh": "解像之度",
        "ja": "解像度", "ko": "해상도", "en": "resolution", "ru": "разрешение", "it": "risoluzione",
        "pt": "resolução", "es": "resolución", "fr": "résolution", "de": "Auflösung",
        "ar": "الدقة", "he": "רזולוציה", "th": "ความละเอียด", "id": "resolusi",
        "ms": "resolusi", "el": "ανάλυση",
    },
    "快充": {
        "zh-TW": "快速充電", "yue": "快充", "lzh": "速充",
        "ja": "急速充電", "ko": "고속 충전", "en": "fast charging", "ru": "быстрая зарядка",
        "it": "ricarica rapida", "pt": "carga rápida", "es": "carga rápida", "fr": "charge rapide",
        "de": "Schnellladen", "ar": "الشحن السريع", "he": "טעינה מהירה", "th": "ชาร์จเร็ว",
        "id": "pengisian cepat", "ms": "pengecasan pantas", "el": "γρήγορη φόρτιση",
    },
    "无线充电": {
        "zh-TW": "無線充電", "yue": "無線充電", "lzh": "無線之充",
        "ja": "ワイヤレス充電", "ko": "무선 충전", "en": "wireless charging", "ru": "беспроводная зарядка",
        "it": "ricarica wireless", "pt": "carregamento sem fio", "es": "carga inalámbrica",
        "fr": "charge sans fil", "de": "kabelloses Laden", "ar": "الشحن اللاسلكي",
        "he": "טעינה אלחוטית", "th": "ชาร์จไร้สาย", "id": "pengisian nirkabel",
        "ms": "pengecasan tanpa wayar", "el": "ασύρματη φόρτιση",
    },
    "口令短语": {
        "zh-TW": "口令短語", "yue": "口令短語", "lzh": "口令之句",
        "ja": "パスフレーズ", "ko": "패스프레이즈", "en": "passphrase", "ru": "парольная фраза",
        "it": "passphrase", "pt": "frase-senha", "es": "frase de contraseña", "fr": "phrase secrète",
        "de": "Passphrase", "ar": "عبارة مرور", "he": "סיסמת ביטוי", "th": "รหัสผ่านวลี",
        "id": "frasa sandi", "ms": "frasa laluan", "el": "φράση συνθηματικού",
    },
    "密码管理器": {
        "zh-TW": "密碼管理器", "yue": "密碼管理器", "lzh": "密碼之筦",
        "ja": "パスワードマネージャー", "ko": "비밀번호 관리자", "en": "password manager",
        "ru": "менеджер паролей", "it": "gestore di password", "pt": "gerenciador de senhas",
        "es": "gestor de contraseñas", "fr": "gestnaire de mots de passe", "de": "Passwort-Manager",
        "ar": "مدير كلمات المرور", "he": "מנהל סיסמאות", "th": "ตัวจัดการรหัสผ่าน",
        "id": "pengelola kata sandi", "ms": "pengurus kata laluan", "el": "διαχειριστής κωδικών",
    },
    "系统更新": {
        "zh-TW": "系統更新", "yue": "系統更新", "lzh": "系統之新",
        "ja": "システムアップデート", "ko": "시스템 업데이트", "en": "system update",
        "ru": "обновление системы", "it": "aggiornamento di sistema", "pt": "atualização do sistema",
        "es": "actualización del sistema", "fr": "mise à jour du système", "de": "Systemupdate",
        "ar": "تحديث النظام", "he": "עדכון מערכת", "th": "อัปเดตระบบ",
        "id": "pembaruan sistem", "ms": "kemas kini sistem", "el": "ενημέρωση συστήματος",
    },
    "Root 权限": {
        "zh-TW": "Root 權限", "yue": "Root 權限", "lzh": "Root 之權",
        "ja": "Root権限", "ko": "루트 권한", "en": "root access", "ru": "root-доступ",
        "it": "accesso root", "pt": "acesso root", "es": "acceso root", "fr": "accès root",
        "de": "Root-Zugriff", "ar": "صلاحيات الروت", "he": "הרשאות root", "th": "สิทธิ์ root",
        "id": "akses root", "ms": "akses root", "el": "πρόσβαση root",
    },
    "开发者模式": {
        "zh-TW": "開發人員選項", "yue": "開發者模式", "lzh": "開發之式",
        "ja": "開発者向けオプション", "ko": "개발자 모드", "en": "developer mode",
        "ru": "режим разработчика", "it": "modalità sviluppatore", "pt": "modo desenvolvedor",
        "es": "modo de desarrollador", "fr": "mode développeur", "de": "Entwicklermodus",
        "ar": "وضع المطور", "he": "מצב מפתחים", "th": "โหมดนักพัฒนา",
        "id": "mode pengembang", "ms": "mod pembangun", "el": "λειτουργία προγραμματιστή",
    },
}

LANGS = ['zh-TW', 'yue', 'lzh', 'ja', 'ko', 'en', 'ru', 'it', 'pt', 'es',
         'fr', 'de', 'ar', 'he', 'th', 'id', 'ms', 'el']


def main():
    out_dir = ROOT / 'manifest' / 'glossary'
    out_dir.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        terms = {}
        for zh, tr in TERMS.items():
            v = tr.get(lang)
            if not v:
                raise SystemExit(f'术语缺译文：{zh} / {lang}')
            terms[zh] = v.strip()
        (out_dir / f'{lang}.json').write_text(
            json.dumps({'lang': lang, 'terms': terms}, ensure_ascii=False, indent=1) + '\n',
            encoding='utf-8', newline='\n')
    print(f'已生成 {len(LANGS)} 个术语表 → manifest/glossary/（每表 {len(TERMS)} 条）')


if __name__ == '__main__':
    main()
