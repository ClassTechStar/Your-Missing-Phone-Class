---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: 第五十七章：進階之路——權限、通知與現代架構
toc: default
kind: chapter
---

### 第五十七章：進階之路——權限、通知與現代架構

{class="chapter-intro mb-4"}
能作 App 者，僅其始也。此章論自「會作」至「作善」之數關：何以雅然請權限、何以發通知而不擾人、何以再抬架構一層，以及——於 2026 年，何以與 AI 相伴而作安卓之碼。凡此諸條，皆爾於真實項目中頃刻將遇者也。

#### 一、運行時權限：先敲門，再進門

相機、定位、通訊錄、通知……此皆「敏感之地」，安卓令 App 於運行之時請於用戶（自 Android 6 始）。其規：先聲明（Manifest），再申請（代碼），用戶拒之則宜雅然降級。Compose 之中以官方庫 Accompanist 之 rememberPermissionState 為最省心：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 運行時權限（Compose 版）</span><span class="dots">···</span>
:::

```
// Manifest 中先聲明：
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("拍照") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：遭永拒則奈何？

{class="mt-1"}
用戶既勾「不再詢問」，則 launchPermissionRequest 不復彈窗。此時當引用戶往系統設定手動啟之（以 Intent 跳至應用設定之頁），且於界面明言「此權限何所用也」。態度稍善，則用戶啟權限之意必高——申請權限之文案，宜認真書之。
:::

#### 二、通知：於正確之時說有用之言

通知者，App 達用戶之途也，亦最易為用戶所「拒」之功能也。發通知有三戒：惟發有用者、令用戶能關之、勿半夜擾之。其基礎之法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 發一條通知</span><span class="dots">···</span>
:::

```
// Android 13+ 必須先申請 POST_NOTIFICATIONS 權限（見上一節）

// 1. 建通知渠道（Android 8+ 必須）
val channel = NotificationChannel(
    "reminder", "提醒", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. 發通知
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("記賬提醒")
    .setContentText("今日尚未記賬也")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

定時之務（如「每日 20:00 提點記帳」）當用 WorkManager——此官方所薦「後台調度之管家」也，能保任務於合宜之時而行，不必自慮電池之優化。鬧鐘之屬用之必無誤。

#### 三、架構進階：依賴注入與模塊化

項目既大，二「甘美之擾」將至：

- 對象之造紊亂：每一頁皆自 new 數據庫、new API——當用 Hilt（依賴注入之框架）統而管之，「誰欲何物，啟口即有人奉之」；
- 代碼積之如山：單模塊之項目愈改愈緩——當拆為多模塊（app / core / feature-xxx），諸功能各自開發、各自測試。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：勿過度設計

{class="mt-1"}
Hilt 與模塊化皆良器也，然獨人之項目勿遽用之。記帳本單模塊加手創依賴，綽綽有餘。待代碼逾數萬行、編譯始緩、多人共作之時，再因需引入。器者所以達的也，非以誇示也——此亦吾儕 AI 編程之書「簡單至上」之旨也。
:::

#### 四、2026 年之新玩法：AI 輔助安卓開發

2026 年，AI 已深嵌安卓開發之流程。爾若欲提速，此組合之法甚成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 何以助</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">爾之責</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">作代碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio 內置 Gemini 及第三方 AI 之插件以補全與生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明述需求，審其產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">以官方文檔與報錯之訊付 AI 解之</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵之結論，復核於官方文檔</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">作測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">令 AI 依「正常/邊界/異常」三類生用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確用例合乎業務之義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼堆棧與相關代碼，AI 定位而修之</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">明其改動，行測試以驗之</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 佐安卓開發之四場景

其具體之法——何以令 AI、何以驗收、何以避坑——凡十一章全備於本書第七篇《AI編程實戰篇》（第37-47章），力薦並讀之：安卓之語法付諸本篇，AI 協作之心法付諸第七篇。

#### 五、Compose 性能優化與調試工具

Compose 書之甚暢，然「重組過多」亦滯。三實用之技：

- 穩其參數：數據之類加 @Immutable，或用 derivedStateOf，以免無關狀態之變觸發廣域之重組；
- 切記用 key：items(list, key = { it.id }) 令列表增刪之時惟動當動之項——不加 key，刪一項或致全表重繪；
- Layout Inspector 之 Compose 模式：實時觀每 Composable 重組之次數，孰頻繁重組，一覽了然，循其熱點而優之。

又當開 Compose 編譯器之報告（Metrics），可生「何組件不穩」之報——進階之路，數據終較感覺可靠。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給記帳本加「三件套」

{class="mt-1"}
① 給記帳本加「每日 20:00 記帳之提點」（WorkManager 加通知之渠道加 Android 13 通知之權限）；② 以 Hilt 注入改數據庫與 API 之創建；③ 試以 AI 之器令「月度篩選」之功速成，而後依三層驗收之法察其產出。三件既畢，爾之項目遂有「正規軍」之貌矣。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 敏感權限：Manifest 聲明加運行時申請加被拒之後雅然引導
- 通知三戒：惟發有用者、能關、不擾；渠道與權限缺一不可
- 定時之務用 WorkManager，勿自造輪
- Hilt 管對象、模塊化管代碼——獨人小項目勿遽用之
- AI 佐助四場景：作碼、查資料、作測試、改 bug；其法見第七篇（第37-47章）
:::
