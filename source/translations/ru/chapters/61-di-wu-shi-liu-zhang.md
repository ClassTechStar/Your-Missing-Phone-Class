---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Глава 56: Шлифовка и публикация — выпуск в Google Play
toc: default
kind: chapter
---

### Глава 56. Шлифовка и публикация — тесты, отладка и выход в Google Play

{class="chapter-intro mb-4"}
Приложение готово. Что дальше? В этой главе — три дела на пути «от работает» к «можно передавать»: как быстро отлаживать и находить баги, как писать тесты против поломок и как выложить приложение в Google Play, чтобы его качал весь мир. Публикация — не просто красивый ритуал: это водораздел между «самоделкой» и «продуктом».

#### 1. Три кита отладки: Logcat, точки останова, инспектор UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Инструмент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Для чего</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Как пользоваться</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Смотреть системные и свои журналы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">В коде Log.d("TAG","значение=$x"), в панели ищите по TAG, чтобы отфильтровать</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Точки останова</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Останавливают программу на нужной строке, чтобы посмотреть значения переменных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Кликните рядом с номером строки — появится красная точка; запустите в режиме Debug и идите по шагам</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Смотреть структуру работающего интерфейса</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Меню Tools → Layout Inspector: дерево компонентов в реальном времени</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Три кита отладки

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: как читать сообщение об ошибке?

{class="mt-1"}
После падения в Logcat останется красный стек (Stacktrace). Идите снизу вверх и найдите первую строку, начинающуюся с имени вашего пакета (например, com.example.yourapp), — это и есть место преступления. Сначала гляньте «тип Exception» (нулевой указатель? ошибка приведения типа?), потом строку «at ... ваш_файл:строка». Этот приём закрывает 80% падений.
:::

#### 2. Тесты: страховка для кода

Ручной проверке верить нельзя: починил одну функцию — тихо сломалась соседняя. Тесты — сразу и «таблетка от сожалений», и «бронежилет». Тестирование в Android трёх уровней; новичку сперва нужно освоить первый:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Уровень</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что проверяет</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Где лежит</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Скорость</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Модульные тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Чистая логика (вычисления, проверки)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Секунды</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Инструментальные тесты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Поведение интерфейса на настоящем устройстве</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Минуты</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ручное тестирование</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Впечатления живого человека</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нужно всегда</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Три уровня тестов

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Пример модульного теста</span><span class="dots">···</span>
:::

```
// Выносим логику вроде «строка суммы -> число» в чистую функцию
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Тестируем (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

Проверку сумм и статистические расчёты в учётной книге обязаны прикрывать модульные тесты. Запуск: правый клик по папке test → Run. Зелёный — всё прошло, меняйте код спокойно.

#### 3. Подпись и сборка: ставим на приложение «печать»

Android требует подписи для всех устанавливаемых пакетов — как печать на документе: она подтверждает, что «пакет выпущен мной и не подделан». При отладке Android Studio автоматически подписывает debug-подписью; для выпуска нужна собственная release-подпись. Порядок:

1. меню Build → Generate Signed Bundle / APK;
2. создайте файл keystore (хранилище ключей) — задайте пароль и храните бережно;
3. выберите release и формат AAB — сборка готова.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: потеряли keystore — потеряли приложение

{class="mt-1"}
После публикации обновления подписываются тем же ключом, иначе магазин отклонит обновление. Потеряли файл keystore и пароль — останется лишь выпустить приложение заново как новое, и старые пользователи останутся ни с чем. Обязательно сделайте резервную копию keystore и пароля в надёжном месте (зашифрованное облако + блокнот) — это один из самых дорогих уроков Android-разработчика.
:::

#### 4. Публикация в Google Play: весь путь

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Зарегистрировать аккаунт разработчика</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Подготовить материалы для магазина</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Загрузить AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Заполнить форму безопасности данных</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Проверка (от часов до дней)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Публикация</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 6. Шесть шагов публикации в Google Play
:::

- Регистрация: разовый регистрационный взнос 25 долларов; нужен работающий Google-аккаунт;
- Материалы: значок приложения (512×512), скриншоты (минимум 2), описание функций, ссылка на политику конфиденциальности (обязательна, если собираете данные);
- Форма безопасности данных: честно перечислите, что собираете, — учётная книга без сети может указать «сбор отсутствует»;
- Проверка: первую публикацию нового аккаунта часто смотрит живой модератор — от нескольких часов до нескольких дней; вернули — правьте по замечаниям.

Пользователям из Китая: для Google Play нужен особый сетевой доступ, а в материковом Китае распространение обычно идёт через местные магазины (Huawei, Xiaomi, Yingyongbao и др.). Процедура в местных магазинах похожа, но у каждого свои вкусы проверки — один и тот же AAB/APK можно разослать в несколько магазинов. Для тренировки достаточно пройти хоть один.

#### 5. Материалы для магазина: первое впечатление — это и есть загрузки

Страница в магазине — витрина, которую смотрит «зашедший» пользователь. Первое впечатление делают три материала:

- Значок: 512×512; не отделывайтесь скриншотом. Нет дизайнерских навыков — сгенерируйте лаконичную геометрическую фигуру ИИ-инструментом; зачёт, только если значок узнаётся с одного взгляда даже уменьшенным на рабочем столе телефона;
- Скриншоты: минимум 2, лучше 4–6 — показывайте самые главные сценарии; к каждому добавьте одну простую человеческую фразу («записать трату за секунду» в десять раз лучше «эффективного решения для учёта финансов»);
- Описание: первая фраза должна ясно отвечать «что это и для кого»; не лепите горой «самое профессиональное, самое мощное» — поисковый вес в магазине зависит в основном от ключевых слов и конверсии в загрузки, искренность действеннее преувеличений.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: сравните себя с соседями по полке

{class="mt-1"}
До публикации прогуляйтесь по первой десятке похожих приложений в магазине и сравните скриншоты: какой у них стиль значка? какой довод вынесен на скриншоты? как написаны заголовки? Подражать — не значит красть: переймите ход, вложите своё содержание. Это самый быстрый урок холодного старта для любого продукта.
:::

#### 6. Мини-чек-лист: производительность и отчёты о сбоях

Перед публикацией приложения на эти два дела стоит потратить по полчаса:

##### 1. Четыре пункта проверки производительности

1. Списки — через LazyColumn: длинные списки ни в коем случае не собирайте жёстким Column — ленивая загрузка это первый урок производительности Android;
2. Не пихайте картинки в оригинальном размере: библиотека Coil сама уменьшит и закэширует; один оригинал на 5 МБ способен задушить слабый телефон;
3. Не гоняйте тяжёлую работу в главном потоке: база данных, сеть, большие файлы — всё в корутинах;
4. Измеряйте через Profiler: встроенный в Android Studio анализатор производительности показывает память, CPU и расход батареи — сначала измерьте, потом оптимизируйте, на ощущения не надейтесь.

##### 2. Отчёты о сбоях

То, что у вас при тестах не падало, не значит, что не упадёт у пользователя. До публикации подключите Firebase Crashlytics (официальный сервис Google, бесплатный): несколько строк настроек — и при падении стек сам прилетит в консоль: увидите «какая модель, какая версия, на какой строке рухнуло». Публиковать без мониторинга сбоев — всё равно что ездить с закрытыми глазами.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: «сдайте» учётную книгу в эксплуатацию

{class="mt-1"}
① Добавьте 3 модульных теста к логике вроде parseAmount; ② через Logcat своими руками поймайте специально подстроенное падение и почините его; ③ соберите APK с release-подписью и отправьте другу на установку (вот она, церемония «произведения»); ④ если есть силы — зарегистрируйте аккаунт разработчика и действительно отправьте учётную книгу на публикацию. Первые три пункта по силам уже сегодня вечером.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Коротко о главном

- Три кита отладки: Logcat — журналы, точки останова — переменные, Layout Inspector — интерфейс
- Читать падение: в стеке снизу вверх ищите первую строку с именем своего пакета
- Три уровня тестов: модульные (секунды, осваиваем первыми) / инструментальные / ручные
- Выпуск — только с подписью: держите резервные копии keystore и пароля; потеряете — приложение «сменит хозяина»
- Шесть шагов публикации: регистрация → материалы → загрузка AAB → форма безопасности данных → проверка → публикация
:::
