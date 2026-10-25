---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: 第六十一章：Swift快速上手——蘋果開發之第一語言
toc: default
kind: chapter
---

### 第六十一章：Swift 速成——蘋果開發之第一語言

{class="chapter-intro mb-4"}
此章吾儕正式學其語言。勿懼——Swift 素以「善待新手」著稱，且爾不必背語法之書：先掌握 20% 之語法，即可看懂且寫出 80% 日常之代碼。其餘者，且作項目且查之。記吾儕學習之則：看懂勝於強記，會用勝於精通。

#### 一、變量與類型：為數據起名

程序者，「數據加邏輯」也。變量者，為數據起一名而儲之也。Swift 以 let 與 var 聲明之：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 變量</span><span class="dots">···</span>
:::

```
let name = "張三"        // let：常量（宜以為默認）
var age = 18             // var：變量（後尚可改）

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var 可改
// name = "李四"         // <i class="fas fa-times-circle mr-1"></i> let 不可改，編譯報錯

let score: Int = 100     // 亦可明書其型
let pi = 3.14            // 不書亦自推之

print("汝好，\(name)")   // 字符串插值：反斜槓 + 括號
```
:::

常用類型一表記之：

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">類型</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">儲何物</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">示例</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">整數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">小數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">文字</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「你好」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">真/假</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int]（陣列）</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">一組數據</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 常用基礎類型

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
小訣：let 優先之原則

{class="mt-1"}
Swift 社區之鐵律：默認用 let，確有所須方用 var。可用 let 之處而用 var，Xcode 將以黃字警爾。此習能助爾少卻一大類「變量遭意外之改」之 bug——代碼之變愈少，推理愈易。
:::

#### 二、可選值（Optional）：Swift「防崩護身之符」

此 Swift 至要之概念，無出其右。一言以蔽之：一值或「不存」之時，Swift 強爾理之——自語言之層滅「空指針崩潰」此業中之惡夢。

::: div .code-block
:::inline div .code-head
<span>SWIFT · 可選值</span><span class="dots">···</span>
:::

```
var name: String = "張三"   // 普通之型：決不容為 nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> 編譯之誤，徑阻之

var nickname: String? = nil  // 加問號：許為 nil（可選值）
nickname = "三兒"

// 用可選值，必"解包"：
if let n = nickname {        // if let：安全解包
    print("汝好，\(n)")
} else {
    print("尚無暱稱")
}

let len = nickname?.count ?? 0   // ?? 予默認值（空合運算符）
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
注意：! 乃「高危操作」

{class="mt-1"}
代碼中書 nickname!（強制解包）猶謂編譯器曰「吾保其非 nil」——一猜而誤，App 當場即崩。新手之期其則曰：務用 if let / ??，勿用 !。Xcode 補全代碼之時偶爾順手加 !，記而易之。
:::

#### 三、函數與閉包：打包邏輯成「鈕」

函數者，一段有名之邏輯也，若遙控之鈕。閉包（Closure）者，「無名之函」也，可隨手遞於人：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 函數與閉包</span><span class="dots">···</span>
:::

```
// 函數：名字於前，參數與返回類型於後
func greet(name: String) -> String {
    return "汝好，\(name)！"
}
print(greet(name: "張三"))     // 調用時要帶參數名

// 閉包：就地定義，輕快直接
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = 當前元素
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // 篩選
// [3, 4]
```
:::

SwiftUI 之中閉包無所不在：按鈕 Button(「點我」) { ... } 之後大括號即一閉包也。map、filter、sorted 此數「集合連招」請牢記之——來日 90% 列表之處理皆其組合也。

#### 四、結構體與協議：Swift「積木」之體系

Swift 官方之好甚明：先用結構體（struct），須繼承之時方用類（class）。結構體者「值類型」也——複製之時各自為之，天然少一類之 bug：

::: div .code-block
:::inline div .code-head
<span>SWIFT · 結構體與協議</span><span class="dots">···</span>
:::

```
// 結構體：盛數據之盒
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // 結構體自帶"逐一成員構造器"：可徑建
}
let r = Record(amount: 25.5, category: "餐飲", date: Date())

// 協議：約"必具何能"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // 遵守協議 = 承諾實現其要求
```
:::

SwiftUI 之中幾乎皆 struct（View 即協議也）。此言今不解無妨，第 62 章將日日相見——Swift 之世界，先擁抱 struct 可也。

#### 五、貽零基者之語法速查卡

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">欲何為</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">寫法</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定常量/變量</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">字符串插值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">「你好，\(name)」</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定函數</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func 名(參數: 類型) -> 返回類型 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">判斷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if 條件 { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">遍歷</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in 陣列 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">安全解包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = 可選值 { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">默認值</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? 默認值</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">定結構體</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">閉包</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Swift 語法速查卡（新手版）

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
來動手：於 Playgrounds 玩 15 分鐘之 Swift

{class="mt-1"}
有 Mac 則開 Xcode → Playground；無 Mac 則用 iPad 上之 Swift Playgrounds 或網頁版之演練場。以本章每一段之代碼皆跑一遍，改其數字與文字，故意造數誤以觀 Xcode 何以提示之。此「先玩後學」之 15 分鐘，將令爾第 62 章上手之時輕鬆一倍。
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
<i class="fas fa-flag-checkered mr-1"></i>本章小結

- let 為先，var 慎用；類型自動推斷，冒號之後明言亦可
- 可選值者 Swift 之魂也：或空必理之，if let 與 ?? 乃護身之符，! 乃高危操作
- 函數之調用須帶參數之名；閉包者無名之函也，SwiftUI 之中無所不在
- 先用 struct，守協議（Protocol）；SwiftUI 之中幾乎皆 struct
- 20% 之語法為 80% 之事：先會用之，再精通之
:::
