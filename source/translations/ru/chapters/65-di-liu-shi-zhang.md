---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Глава 60: Настройка окружения — Xcode и первый проект
toc: default
kind: chapter
---

### Глава 60. Настраиваем среду разработки — Xcode и первый проект

{class="chapter-intro mb-4"}
Чтобы дело спорилось, сначала нужно наточить инструменты. В этой главе мы обустроим «кухню»: установим Xcode, запустим симулятор, создадим первый в жизни проект iOS и разберём структуру проекта по косточкам. Когда среда будет готова, вы впервые увидите, как написанный вами код превращается в кнопку, которую можно нажать, — этот момент многие запоминают на всю жизнь.

#### 1. Готовим Mac

Сначала о барьере: разработка под iOS возможна только на macOS. Если у вас нет Mac, есть три варианта: купить (подойдёт даже б/у Mac mini или MacBook Air), на короткий срок арендовать облачный Mac или сначала прочитать часть 8 «Практика разработки под Android» (там хватит и Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Параметр</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Минимум</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Комфортный уровень (рекомендуется)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Чип</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (от M1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 и новее</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Память</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Диск</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запас от 40 ГБ+ (сам Xcode весьма «упитанный»)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">от 256 ГБ</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Система</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">новейшая macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">держать автообновление включённым</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ориентировочная конфигурация Mac для разработки (август 2026 года)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: без Mac язык тоже можно начать учить

{class="mt-1"}
Бесплатное приложение Swift Playgrounds на iPad поможет освоить основы Swift (Mac не нужен); оно ставится даже на iPhone. Освойте в Playgrounds языковой материал главы 61, а когда появится Mac — сразу взлетите. Недаром говорят: хорошо наточенный топор дров не портит.
:::

#### 2. Устанавливаем Xcode

Xcode — официальная интегрированная среда разработки Apple, бесплатная. Установка в три шага:

1. Откройте на Mac App Store, найдите «Xcode» и нажмите «Установить» — учтите, он весит несколько гигабайт, выберите время с хорошей скоростью сети;
2. При первом запуске после установки примите лицензионное соглашение и дождитесь установки компонентов (происходит автоматически);
3. В меню Xcode → Settings → Locations убедитесь, что выбран Command Line Tools — инструменты командной строки нужны многим скриптам и сторонним инструментам.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: «игра в соответствие» версий и системы

{class="mt-1"}
Новый Xcode обычно требует новейшую macOS, а старый Mac может застрять на старой версии. При публикации в App Store Apple требует собирать приложение более свежим Xcode (обычно давая отсрочку). Поэтому не затягивайте с обновлением системы — iOS-разработчики самые усердные «охотники за новыми версиями».
:::

#### 3. Создаём ваш первый проект

Откройте Xcode → Create New Project → выберите iOS → шаблон App, затем заполните:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Параметр</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что вводить</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Пояснение</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Название приложения</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ваш Apple ID (бесплатно)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">нужен для подписи, личного аккаунта достаточно</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">вместе с Product Name образует идентификатор пакета</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">основной фреймворк этой книги</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">без комментариев</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Пять вещей, которые заполняются при создании проекта

После нажатия Create Xcode сгенерирует проект, который можно запустить сразу. В левом верхнем углу выберите симулятор (например, iPhone 17) и нажмите ▶ — через несколько секунд на экране симулятора появится окно с надписью «Hello, world!». Ваше первое приложение iOS родилось.

#### 4. Разбираем структуру проекта: зачем нужен каждый файл

Слева находится навигатор проекта; новичку достаточно знать лишь несколько пунктов:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ — корень проекта</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (папка кода)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← точка входа приложения</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← главный экран</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← иконки, картинки, цвета</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(все новые файлы кладём в эту папку)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Вкладка Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Декларации приложения: имя, разрешения, настройки</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Другие важные места</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← материалы превью</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Настройки таргета (синяя иконка проекта)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— номер версии, минимальная система, подпись — всё здесь</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← модульные тесты</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← тесты интерфейса</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(шаблоны тестов уже созданы; используются в главе 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 2. Структура проекта Xcode, которую обязан понять новичок
:::

- MyFirstAppApp.swift: точка входа программы; в SwiftUI она занимает всего несколько строк — «запусти, затем покажи главный экран»;
- ContentView.swift: главное представление экрана; всё, что вы сейчас видите, находится здесь;
- Assets.xcassets: хранилище ресурсов — сюда кладут иконки, картинки и цвета;
- Настройки Target: нажмите на синий значок проекта слева — внутри номер версии, минимальная версия iOS и подпись. Здесь же настраиваются отображаемое имя и иконка приложения.

#### 5. Приёмы эффективности в Xcode: пять «читов» с горячими клавишами для новичка

Освоив эти приёмы, вы будете выглядеть «очень профессионально»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Действие</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Горячая клавиша</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Назначение</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запуск</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Скомпилировать и запустить</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Открыть/переключить предпросмотр на холсте</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Переключатель «что видишь, то и получаешь»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Форматирование отступов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Автоматически выровнять отступы выделенного кода</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Быстрое открытие файла</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Введите имя файла — откроется мгновенно (самое ходовое!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Закомментировать/раскомментировать</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Быстро включать/выключать код во время отладки</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Частые горячие клавиши Xcode (пятёрка новичка)

Ещё два скрытых бонуса: несколько симуляторов сразу (запустить iPhone и iPad одновременно и сравнить компоновку) и библиотека фрагментов кода (перетащите часто используемые строки в панель Snippets справа — в следующий раз вставите одним нажатием). Начните пользоваться инструментами эффективности — и ловкость придёт сама.

#### 6. Отладка на реальном устройстве: устанавливаем приложение на ваш iPhone

Симулятор хорош, но финиш — на реальном устройстве. Отлаживать на нём можно и с бесплатным Apple ID:

1. Соедините iPhone кабелем (или отлаживайте по Wi-Fi в одной сети);
2. В списке устройств вверху Xcode выберите свой телефон; при первом подключении появится предложение войти в Apple ID, и подпись настроится автоматически;
3. На iPhone: [Настройки] → [Основные] → [VPN и управление устройствами] → доверьтесь сертификату вашего разработчика;
4. Нажмите ▶ — приложение установится на реальное устройство.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: «семидневное ограничение» бесплатного аккаунта

{class="mt-1"}
Приложение, подписанное бесплатным Apple ID, перестанет работать через 7 дней (чтобы продлить, просто запустите его ещё раз). Это защитный механизм Apple; на этапе обучения его вполне хватает, а у платного аккаунта разработчика (99 долларов в год) такого ограничения нет — подробнее в главе 67.
:::

#### 7. Первые пробы + скорая помощь при частых ошибках

Откройте ContentView.swift, замените текст в Text("Hello, world!") на своё имя и нажмите ⌘R для повторного запуска — через несколько секунд на симуляторе появится ваше имя. Поздравляем: вы прошли свой первый полный цикл «изменил код → скомпилировал → установил → запустил».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Симптом ошибки</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Частая причина</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Лекарство</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ошибка Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">не выбран Team, истёк срок сертификата</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">в Target → Signing отметьте свой аккаунт; с бесплатным аккаунтом запустите ещё раз</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Симулятор с чёрным экраном / не запускается</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">повреждённый образ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">меню Device → Erase All Content; либо удалите симулятор и создайте заново</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode медленно скачивается / не устанавливается</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">скачки сети в App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">попробуйте в другое время; или скачайте офлайн-пакет .xip с сайта разработчиков Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Таблица скорой помощи при ошибках окружения у новичков

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: пройдите свой «обряд посвящения» в разработчики

{class="mt-1"}
① установите Xcode и запустите симулятор; ② запустите своё приложение на реальном устройстве и сделайте памятный скриншот; ③ замените текст Hello на своё имя; ④ в настройках Target смените отображаемое имя приложения на «Моё первое приложение». Сделав эти четыре шага, вы становитесь автором собственного приложения.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Жёсткий барьер: Mac + Xcode; нет Mac — начните учить язык в Swift Playgrounds на iPad
- Xcode ставится из App Store; новая версия требует новую систему — не затягивайте с обновлениями
- Пять элементов нового проекта: имя, Team, идентификатор организации, SwiftUI, Swift
- Мантра проекта: весь код — в каталоге MyFirstApp/; настройки Target отвечают за версию и подпись
- При отладке на устройстве с бесплатным Apple ID подпись действует 7 дней; у платного аккаунта этого ограничения нет
- Быт разработчика = изменить код → ⌘R → посмотреть результат, и так по кругу
:::
