---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: Глава 58: Справочник и ресурсы
toc: default
kind: chapter
---

### Глава 58. Справочник и ресурсы

{class="chapter-intro mb-4"}
Эта глава — справочник, которым можно пользоваться и отдельно. Когда не можете вспомнить, как что-то пишется, или нужно быстро принять решение, — просто заглядывайте сюда. Советуем обращаться с ним как с «карманными карточками»: шпаргалки по часто используемому коду, частые вопросы, учебные ресурсы — ни одна страница не пропадёт.

#### 1. Шпаргалка по часто используемому коду

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что нужно сделать</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ключевой код</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запомнить изменяемое состояние</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var x by remember { mutableStateOf(начальное Значение) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Не терять состояние при повороте экрана</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable { mutableStateOf(начальное Значение) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Вертикальная/горизонтальная компоновка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Список с ленивой загрузкой</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn { items(список) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Переход между экранами</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">navController.navigate("маршрут")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Долгая работа в корутине</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Наблюдать за потоком данных</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Хранить небольшие настройки</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">context.dataStore.edit { it[KEY] = значение }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Хранить структурированные данные</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тройка Room: @Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Получать данные из сети</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Интерфейс Retrofit + suspend-функции</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отправлять уведомления</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Писать в лог</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка по разработке под Android (версия августа 2026 года)

#### 2. Частые вопросы (FAQ)

В 1: Я совсем не умею программировать. Сколько времени займёт освоение разработки под Android?

Идите по пути этой книги: недели 1–2 — установка окружения и основы Kotlin; недели 3–4 — изучение Compose и создание интерфейса; недели 5–6 — завершение проекта «учёт расходов»; недели 7–8 — завершение проекта «погода». Два месяца — от нуля до умения самостоятельно делать небольшое приложение. При условии, что вы готовы уделять 1–2 часа в день и писать код руками, а не только читать.

В 2: Нужно ли ещё учить Java?

Нет. Новые проекты, новые учебники и новые вакансии почти все ориентированы на Kotlin. Много Java вы встретите только при «поддержке проекта десятилетней давности». Если после Kotlin работа потребует Java, подтянуть его получится быстро — в основе обоих языков одна экосистема виртуальной машины.

В 3: Эмулятор или реальное устройство?

Для отладки в процессе разработки удобен эмулятор (снимки состояния, много моделей устройств), но финальная приёмка — обязательно на реальном устройстве: ощущения от касаний, производительность, настоящая сеть, датчики — эмулятор этого не заменит. Если есть возможность, купить реальное устройство среднего класса под тесты — самая выгодная инвестиция.

В 4: Легко ли найти работу в разработке под Android?

Ситуация 2026 года: на начальные позиции уровня «просто умею делать интерфейсы» конкуренция острая, но разработчики, которые «знают Kotlin + понимают архитектуру + имеют опубликованное приложение», по-прежнему нарасхват. Лучшее резюме для вас, пока вы учитесь, — это сделанное вами приложение в магазине.

В 5: Что делать, если застряли на ошибке?

Золотые три шага: ① скопируйте первую строку ошибки как есть и поищите в StackOverflow/поисковике; ② посмотрите соответствующую страницу официальной документации; ③ если не помогло, соберите «ожидаемое поведение + фактический результат + полный текст ошибки + относящийся код» и отправьте вопрос ИИ или сообществу. Подавляющее большинство проблем решается уже на первом шаге.

#### 3. Рекомендуемые учебные ресурсы

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Тип</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ресурс</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Почему стоит попробовать</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация Android: внутри и руководства по Compose/Kotlin — источник номер один</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный сайт Kotlin (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальная документация языка + онлайн-песочница</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пошаговые практические уроки «рука об руку»; пятёрка по дружелюбности к новичкам</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (метка android)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Первая остановка за помощью при ошибках</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сообщество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Juejin / раздел Android на CSDN</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Много практических статей на китайском; проверяйте свежесть (сначала смотрите дату)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Видео</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальный канал Google Developers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разборы новых технологий с ежегодных конференций разработчиков</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Из этой книги</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Часть 7 «Практика программирования с ИИ» (главы 37–47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Полная методика разработки под Android с помощью ИИ</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Список учебных ресурсов по разработке под Android (август 2026 года)

#### 4. Шпаргалка по командам Gradle

В обычной жизни достаточно нажимать кнопки, но командная строка иногда эффективнее (особенно в связке с ИИ-инструментами или CI-конвейером):

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Команда</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Назначение</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Собрать отладочный APK (в Windows уберите ./)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Собрать релизную версию (нужна настроенная подпись)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Запустить все модульные тесты</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Статический анализ: находит потенциальные баги и неаккуратный код</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Очистить результаты сборки («перезагрузка» в мире компиляции)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Показать дерево зависимостей (волшебное средство против конфликтов версий)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Шпаргалка по командам Gradle

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: если сборка барахлит, сначала clean

{class="mt-1"}
Если «вчера всё работало, а сегодня нет», то в шести-семи случаях из десяти виноват перепутанный кэш сборки. Выполните ./gradlew clean и соберите заново — это лечит большую часть «мистических» проблем. Не помогло — перезапустите Android Studio; этот приём лучше всего работает в паре с File → Invalidate Caches.
:::

#### 5. Заключение: от первого приложения до N-го

Оглядываясь назад: вы прошли путь от «не знаю, что такое Activity» до установленного окружения, освоенного Kotlin, интерфейсов, нарисованных в Compose, подключённых к приложению базы данных и сети, а дальше — тестирования, сборки пакета и публикации. Самый трудный отрезок пути «от нуля к единице» вы уже прошли.

Мир технологий меняется быстро: фреймворки обновляются, инструменты сменяют друг друга, а ИИ берёт на себя всё больше «клавиатурной» работы. Но одна вещь не устареет никогда: ваша способность превратить расплывчатую идею в чёткие шаги и шаг за шагом её воплотить. Инструменты — усилитель, образ мышления — фундамент. Усилитель можно заменить, фундамент шататься не должен.

:::inline div .quote-line
Вы больше не просто «умеющий пользоваться телефоном». Вы можете превратить идеи из головы в настоящие приложения, работающие на трёхстах миллионах Android-устройств. С сегодняшнего дня творите с клавиатурой — в этом романтика Android-разработчика.
:::

#### Список литературы

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
