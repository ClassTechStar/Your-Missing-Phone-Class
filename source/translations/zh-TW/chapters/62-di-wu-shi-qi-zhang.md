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
能做出 App 只是開始。這一章聊聊從"會做"到"做好"的幾道坎：怎麼優雅地申請權限、怎麼發通知不討人厭、怎麼把架構再往上抬一層，以及——在 2026 年，怎麼和 AI 搭檔寫安卓程式碼。每一條都是你在真實專案裡馬上會遇到的。

#### 一、執行時權限：先敲門，再進門

相機、定位、通訊錄、通知……這些"敏感地帶"，安卓要求 App 執行時向使用者申請（Android 6 起）。規矩是：先宣告（Manifest），再申請（程式碼），使用者拒絕要優雅降級。Compose 裡用官方庫 Accompanist 的 rememberPermissionState 最省心：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 執行時許可權（Compose 版）</span><span class="dots">···</span>
:::

```
// Manifest 裡先宣告：
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
注意：被永久拒絕怎麼辦？

{class="mt-1"}
使用者勾了"不再詢問"後，launchPermissionRequest 不會再跳出視窗。此時應引導使用者去系統設定裡手動開啟（用 Intent 跳到應用設定頁），並在介面裡說明"這個權限用來做什麼"。態度好一點，使用者開權限的意願會高很多——申請權限的文案，值得認真寫。
:::

#### 二、通知：在正確的時間說有用的話

通知是 App 觸達使用者的通道，也是最容易被使用者"拉黑"的功能。發通知三條紀律：只發有用的、讓使用者能關、別半夜騷擾。基礎用法：

::: div .code-block
:::inline div .code-head
<span>KOTLIN · 發一條通知</span><span class="dots">···</span>
:::

```
// Android 13+ 必須先申請 POST_NOTIFICATIONS 許可權（見上一節）

// 1. 建立通知渠道（Android 8+ 必須）
val channel = NotificationChannel(
    "reminder", "提醒", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. 發通知
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("記帳提醒")
    .setContentText("今天還沒記帳哦")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

定時任務（比如"每天 20:00 提醒記帳"）用 WorkManager——它是官方推薦的"後臺排程管家"，能保證任務在合適時機執行，不用自己操心電池最佳化。鬧鐘類需求用它準沒錯。

#### 三、架構進階：依賴注入與模組化

專案變大後，兩個"甜蜜的煩惱"會找上門：

- 物件建立亂：每個頁面都在自己 new 資料庫、new API——用 Hilt（依賴注入框架）統一管理，"誰要什麼，開口就有人遞"；
- 程式碼堆成山：單模組專案越改越慢——拆成 多模組（app / core / feature-xxx），各功能獨立開發、獨立測試。

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小貼士：別過度設計

{class="mt-1"}
Hilt 和模組化都是好工具，但單人專案先別急著上。記帳本單模組 + 手動建立依賴完全夠用。等程式碼量超過幾萬行、編譯開始變慢、多人協作時，再按需引入。工具是服務目標的，不是用來炫耀的——這也是咱們 AI 程式設計書裡的"簡單至上"原則。
:::

#### 四、2026 年的新玩法：AI 輔助安卓開發

2026 年，AI 已經深度嵌入安卓開發流程。如果你想提速，這套組合拳很成熟：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">環節</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">AI 怎麼幫</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">你的職責</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫程式碼</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio 內建 Gemini/第三方 AI 外掛補全與生成</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">描述清楚需求，審查產出</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">查資料</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">把官方文件和報錯資訊丟給 AI 解讀</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">關鍵結論回官方文件核實</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">寫測試</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">讓 AI 按"正常/邊界/異常"三類生成用例</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">確認用例符合業務語義</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">改 bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">貼堆疊 + 相關程式碼，AI 定位修復</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">看懂改動，跑測試驗證</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
AI 輔助安卓開發的四個場景

具體方法論——怎麼給 AI 下指令、怎麼驗收、怎麼避坑——完整的 11 章內容在本書第七篇《AI程式設計實戰篇》（第37-47章）裡，強烈建議配合閱讀：安卓語法交給本篇，AI 協作的心法交給第七篇。

#### 五、Compose 效能最佳化與除錯工具

Compose 寫起來爽，但"重組過多"也會卡。三個實用技巧：

- 穩定引數：給資料類加 @Immutable 或使用 derivedStateOf，避免無關狀態變化觸發大面積重組；
- 記得用 key：items(list, key = { it.id }) 讓列表增刪時只動該動的項——不加 key，刪除一項可能整表重畫；
- Layout Inspector 的 Compose 模式：實時看每個 Composable 的重組次數，誰頻繁重組一目瞭然，照著熱點最佳化。

另外把 Compose 編譯器報告（Metrics）開啟，能生成一份"哪些元件不穩定"的報告——進階路上，資料永遠比感覺可靠。

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：給記帳本加"三件套"

{class="mt-1"}
① 給記帳本加"每天 20:00 記帳提醒"（WorkManager + 通知管道 + Android 13 通知權限）；② 把資料庫和 API 的建立改成 Hilt 注入；③ 試著用 AI 工具讓"月度篩選"功能提速實現，然後按三層驗收法檢查產出。三件套做完，你的專案就有"正規軍"的樣子了。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
本章小結

- 敏感權限：Manifest 宣告 + 執行時申請 + 被拒後優雅引導
- 通知三紀律：只發有用的、能關、不騷擾；管道 + 權限缺一不可
- 定時任務用 WorkManager，別自己造輪子
- Hilt 管物件、模組化管程式碼——單人小專案先別急著上
- AI 輔助四場景：寫碼、查資料、寫測試、改 bug；方法論見第七篇（第37-47章）
:::
