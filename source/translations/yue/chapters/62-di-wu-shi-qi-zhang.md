---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: 第五十七章：進階之路——權限、通知與現代架構
toc: default
kind: chapter
---

### 第五十七章：進階之路——權限、通知同現代架構

{class="chapter-intro mb-4"}
做到 App 出嚟只係開始。呢一章同你傾吓由「識做」到「做好」嘅幾道坎：點樣優雅咁申請權限、點樣發通知唔惹人嬲、點樣將架構再升高一層，仲有——喺 2026 年，點樣同 AI 拍檔寫安卓代碼。每一條都係你喺真實項目入面即刻會遇到嘅。

#### 一、運行時權限：先敲門，再入門

相機、定位、通訊錄、通知……呢啲「敏感地帶」，安卓要求 App 喺運行時向用戶申請（Android 6 起）。規矩係：先聲明（Manifest），再申請（代碼），用戶拒絕咗就要優雅降級。喺 Compose 用官方庫 Accompanist 嘅 rememberPermissionState 最省心：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 運行時權限（Compose 版）</span><span class="dots">···</span>
:::

```
// Manifest 入面先聲明：
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
    }) { Text("影相") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：畀人永久拒絕咗點算？

{class="mt-1"}
用戶㩒咗「不再詢問」之後，launchPermissionRequest 就唔會再彈窗。嗰陣應該引導用戶去系統設定度手動開啟（用 Intent 跳去應用設定頁），並且喺界面講明「呢個權限用嚟做乜嘢」。態度好啲，用戶開權限嘅意欲會高好多——申請權限嘅文案，值得認真寫。
:::

#### 二、通知：喺啱嘅時間講有用嘅嘢

通知係 App 接觸用戶嘅通道，亦都係最容易被用戶「拉黑」嘅功能。發通知三條紀律：齋發有用嘅、畀用戶關得到、唔好半夜嘈人。基礎用法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 發一條通知</span><span class="dots">···</span>
:::

```
// Android 13+ 必須先申請 POST_NOTIFICATIONS 權限（見上一節）

// 1. 建立通知渠道（Android 8+ 必須）
val channel = NotificationChannel(
    "reminder", "提醒", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. 發通知
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("記賬提醒")
    .setContentText("今日仲未記賬喎")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

定時任務（例如「每日 20:00 提醒記賬」）用 WorkManager——佢係官方推薦嘅「後台調度管家」，可以保證任務喺合適時機執行，唔使自己操心電池優化。鬧鐘類需求用佢實冇錯。

#### 三、架構進階：依賴注入同模組化

項目變大之後，兩個「甜蜜嘅煩惱」會自己搵上門：

- 物件創建亂：每個頁面都喺度自己 new 數據庫、new API——用 Hilt（依賴注入框架）統一管理，「邊個要乜嘢，開聲就有人遞」；
- 代碼堆成山：單模組項目越改越慢——拆做多模組（app / core / feature-xxx），各功能獨立開發、獨立測試。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：唔好過度設計

{class="mt-1"}
Hilt 同模組化都係好工具，但單人項目唔好咁快上。記賬本單模組 + 手動創建依賴完全夠用。等代碼量超過幾萬行、編譯開始變慢、多人協作嗰陣，先至按需引入。工具係服務目標嘅，唔係攞嚟炫耀嘅——呢個都係我哋呢本 AI 編程書入面嘅「簡單至上」原則。
:::

#### 四、2026 年嘅新玩法：AI 輔助安卓開發

2026 年，AI 已經深度嵌入咗安卓開發流程。如果你想提速，呢套組合拳好成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 點樣幫</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你嘅職責</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫代碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio 內置 Gemini/第三方 AI 插件嚟補全同生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，審查產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">將官方文檔同報錯信息掟畀 AI 解讀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵結論返去官方文檔核實</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">叫 AI 按「正常/邊界/異常」三類生成用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確認用例符合業務語義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼堆疊 + 相關代碼，AI 定位修復</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">睇明改動，行測試驗證</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 輔助安卓開發嘅四個場景

具體方法論——點樣畀 AI 下指令、點樣驗收、點樣避坑——完整嘅 11 章內容喺本書第七篇《AI編程實戰篇》（第37-47章）入面，強烈建議配住睇：安卓語法交畀呢一篇，AI 協作嘅心法交畀第七篇。

#### 五、Compose 性能優化同除錯工具

Compose 寫起上嚟好爽，但「重組過多」都會卡。三個實用技巧：

- 穩定參數：畀數據類加 @Immutable 或者用 derivedStateOf，避免無關狀態變化觸發大面積重組；
- 記得用 key：items(list, key = { it.id }) 令列表增刪嗰陣齋郁應該郁嗰啲項——唔加 key，刪一項可能成個表重畫；
- Layout Inspector 嘅 Compose 模式：實時睇每個 Composable 嘅重組次數，邊個頻密重組一目了然，照住熱點嚟優化。

另外將 Compose 編譯器報告（Metrics）打開，可以生成一份「邊啲組件唔穩定」嘅報告——進階路上，數據永遠比感覺可靠。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
嚟動手：畀記賬本加「三件套」

{class="mt-1"}
① 畀記賬本加「每日 20:00 記賬提醒」（WorkManager + 通知渠道 + Android 13 通知權限）；② 將數據庫同 API 嘅創建改成 Hilt 注入；③ 試吓用 AI 工具令「月度篩選」功能提速實現，然後按三層驗收法檢查產出。三件套做完，你個項目就有「正規軍」嘅樣喇。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 敏感權限：Manifest 聲明 + 運行時申請 + 被拒之後優雅引導
- 通知三紀律：齋發有用嘅、可以關、唔嘈人；渠道 + 權限缺一不可
- 定時任務用 WorkManager，唔好自己重新發明車轆
- Hilt 管物件、模組化管代碼——單人小項目唔好咁快上
- AI 輔助四場景：寫碼、查資料、寫測試、改 bug；方法論見第七篇（第37-47章）
:::
