---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Глава 42: Панорама больших моделей и практика API
toc: default
kind: chapter
---

### Глава 42: Панорама больших моделей и практика работы с API

{class="chapter-intro mb-4"}
В предыдущих главах говорилось о том, «как сотрудничать с AI». Эта глава отвечает на более базовый вопрос: «Каким AI пользоваться? Как именно?» К августу 2026 года ландшафт больших моделей стал чрезвычайно богатым: на международной арене соперничают три лидера — GPT, Claude и Gemini, а в Китае пышным цветом расцвели DeepSeek, Tongyi Qianwen, GLM, Kimi и Doubao. У каждой модели свой характер и свои сильные стороны: удачный выбор удваивает результат при тех же усилиях, неудачный — наоборот. В этой главе вы не только познакомитесь с этими моделями, но и научитесь подключать их к своим приложениям через API, а также подбирать подходящий пакет лимитов (Token Plan) под свои задачи.

#### 1. Ведущие международные модели: расстановка трёх лидеров

К августу 2026 года на международном рынке больших моделей сложился «триумвират»: OpenAI (серия GPT), Anthropic (серия Claude) и Google (серия Gemini). У каждой компании яркий собственный почерк — познакомимся с ними по очереди.

##### 1. Серия OpenAI GPT-5.6: универсальный «шестигранный боец»

OpenAI стояла у истоков волны больших моделей, и серия GPT до сих пор остаётся самой востребованной в мире. Вышедшая в июле 2026 года серия GPT-5.6 использует стратегию трёх уровней: флагман GPT-5.6 Sol рассчитан на задачи с требовательными рассуждениями, сбалансированный GPT-5.6 Terra — на повседневную разработку, а лёгкий GPT-5.6 Luna — на сценарии с высокой нагрузкой и низкой стоимостью. У всех трёх моделей контекстное окно в 1,05 млн токенов; все они поддерживают ввод изображений, вызов функций и структурированный вывод.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модель</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Позиционирование</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ввод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Вывод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Контекстное окно</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Флагманские рассуждения</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 долл. (около 36 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30,00 долл. (около 217 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сбалансированные повседневные задачи</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,50 долл. (около 18 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">15,00 долл. (около 109 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Лёгкий, дешёвый</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,00 долл. (около 7 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6,00 долл. (около 44 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 млн токенов</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Цены серии OpenAI GPT-5.6 (август 2026 г.)

Ключевое преимущество серии GPT — сбалансированность: рассуждения, программирование, письмо, мультимодальность — без заметных слабых мест. Добавьте огромную экосистему плагинов и сообщество разработчиков OpenAI — самая проработанная документация и цепочки инструментов. Когда вы «не знаете, что выбрать», GPT — ответ по умолчанию, «который не подведёт даже с закрытыми глазами». Но есть минусы: доступ из Китая требует особых сетевых средств, по-китайски модель иногда звучит с «переводным акцентом», а цены API — выше среднего.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Хорошая новость

{class="mt-1"}
В августе 2026 года OpenAI объявила, что моделью по умолчанию для бесплатных пользователей стала GPT-5.6 Luna, а текстовый чат открыт без лимитов. Это значит, что базовые возможности GPT вы можете опробовать бесплатно — платить придётся только если нужны более мощные рассуждения или вызовы API.
:::

##### 2. Серия Anthropic Claude: эталон программирования и строгости

Если GPT — универсальный игрок, то Claude — «потолок» в программировании. Серия Claude от Anthropic долго время с большим отрывом лидирует в SWE-bench (бенчмарке программной инженерии); качество генерации кода и способность доводить проекты до промышленного уровня — первые в отрасли. Что ещё ценнее, у Claude самый низкий в сети уровень галлюцинаций (вероятности выдачи ложной информации) — всего около 1%. Поэтому он особенно подходит для высокоточных сценариев: наука, юриспруденция и т. п.

Ещё один козырь Claude — сверхдлинный контекст: контекстное окно в 1 млн токенов позволяет за один раз «прочитать» контракт на сотни страниц или целую кодовую базу, ничего не упустив. В задачах вроде рефакторинга кода и анализа длинных документов он практически незаменим. Claude Code как инструмент AI-программирования в терминале к середине 2026 года достиг годовой выручки в 2,5 млрд долларов — лучшее подтверждение признания способностей Claude к программированию.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модель</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Позиционирование</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ввод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Вывод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Контекстное окно</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Флагман</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 долл. (около 72 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50,00 долл. (около 362 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Профессиональный</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 долл. (около 36 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">25,00 долл. (около 181 юаня)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Оптимум по цене и качеству</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,00 долл. (около 14 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 долл. (около 72 юаней)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Цены серии Anthropic Claude (август 2026 г.; Sonnet 5 — по льготной цене)

Слабое место Claude — цена: у Fable 5 самая высокая цена вывода среди всех моделей — 50 долларов за миллион токенов. Мультимодальные возможности (понимание изображений и видео) тоже сравнительно слабее. Для индивидуальных разработчиков с ограниченным бюджетом Sonnet 5 в льготный период даёт особенно выгодное соотношение цены и качества.

##### 3. Серия Google Gemini: король мультимодальности

Серия Gemini от Google к 2026 году доросла до версии 3.1 Pro. Главный козырь Gemini — нативная мультимодальность: точный разбор текста и изображений, безошибочное распознавание таблиц через OCR, эффективное извлечение кадров видео, плюс глубокий разбор аудио и видео. Модель глубоко интегрирована с экосистемой Google (поиск, почта, облачные сервисы) и блестяще справляется с поиском информации в реальном времени и межмодальным пониманием. Gemini также поддерживает сверхдлинный контекст ввода в 2 млн токенов — это самое большое контекстное окно среди существующих моделей.

Gemini позиционируется как «выбор номер один для научных рассуждений и мультимодальных задач». Если ваш проект связан с анализом большого числа изображений, пониманием видео или научными вычислениями, у Gemini почти нет конкурентов. Но в генерации кода по чистому тексту он немного уступает Claude, а по-китайски выражается менее естественно, чем китайские модели.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Параметр сравнения</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Общий балл</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Навыки программирования (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Средний</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Контекстное окно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 млн токенов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Мультимодальность</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сбалансированная</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Слабая</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Самая сильная</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Уровень галлюцинаций</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Низкий</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Самый низкий (около 1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Низкий</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Доступность в Китае</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Требует особой сети</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Требует особой сети</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Требует особой сети</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API-экосистема</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Самая развитая</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">В развитии</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Привязка к экосистеме Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Сравнение трёх международных моделей (август 2026 г.)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: реальные барьеры при использовании в Китае

{class="mt-1"}
Для китайских разработчиков главное препятствие для GPT, Claude и Gemini — сетевой доступ. Пользоваться ими можно опосредованно — через прокси Azure, платформы-агрегаторы API и т. п., — но стабильность и легальность нужно оценивать самостоятельно. Если ваш проект предъявляет строгие требования к безопасности данных, лучше в первую очередь рассмотреть китайские модели.
:::

#### 2. Ведущие китайские модели: богатое разнообразие

В 2026 году китайские большие модели перестали быть «догоняющими» и бегут наравне с лидерами, а в некоторых областях даже вырвались вперёд. В отличие от споров 2023 года о «моделях-обёртках», китайские флагманы 2026 года уже на равных с передовыми международными моделями в логических рассуждениях, генерации кода и понимании китайского языка — разрыв сократился до 5% и меньше. Что ещё важнее, у китайских моделей есть незаменимые преимущества в китайскоязычных сценариях, стоимости и развёртывании с соблюдением норм.

##### 1. DeepSeek V4: король цены и качества

DeepSeek — феномен среди китайских больших моделей. В начале 2025 года DeepSeek-V3 потряс рынок позицией «в десять раз дешевле GPT при равных возможностях» и получил в отрасли имя «линия уничтожения универсальных AI-моделей»: те, что дешевле, не так удобны, а те, что дороже, не дают такого объёма и щедрости. К августу 2026 года вышел официальный релиз DeepSeek V4-Pro: MoE-архитектура на 1,6 трлн параметров с активацией около 49 млрд, поддержка контекста в 1 млн токенов без потерь; соотношение цены и качества в коде считается общемировым потолком.

В DeepSeek V4 резко выросли агентные способности: бенчмарк DeepSWE подскочил с 12,8 до 62,7 (+390%), а NL2Repo — с 38,5 до 61,5. API получил поддержку сразу двух протоколов — Responses API и Anthropic API — и уже совместим с популярными инструментами программирования вроде Codex и Claude Code. Это значит, что вы можете использовать API DeepSeek вместо API Claude прямо в Claude Code: затраты падают в несколько раз, а впечатления почти идентичны.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модель</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Позиционирование</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ввод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Вывод (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Контекстное окно</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Флагманские рассуждения</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 юаня (около 0,43 долл.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 юаней (около 0,87 долл.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Лёгкий и быстрый</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 юань (около 0,14 долл.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 юаня (около 0,28 долл.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн токенов</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Цены серии DeepSeek V4 (август 2026 г., акционные)

Сравнение цен: за 1 млн токенов ввода плюс 1 млн токенов вывода DeepSeek V4 Flash стоит около 0,42 доллара, GPT-5.6 Sol — около 35 долларов, а Claude Fable 5 — около 60 долларов. Разница достигает 80–140 раз.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: DeepSeek готовится поднять цены

{class="mt-1"}
Официально DeepSeek 6 августа 2026 года объявил о «плане в ближайшее время заметно поднять цены на API» — акционные цены могут долго не продержаться. По слухам в СМИ, подорожание может достигнуть 30 раз; по состоянию на 14 августа окончательная схема цен не опубликована. Кроме того, официальный релиз DeepSeek V4 ввёл тарифы «пик–непик»: в часы пик вызовы стоят вдвое дороже. Следите за официальными объявлениями, чтобы знать актуальные цены.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: корпоративный выбор Alibaba Cloud

Серия Tongyi Qianwen (Qwen) от Alibaba Cloud, опираясь на экосистему Alibaba Cloud, имеет естественные преимущества в корпоративном развёртывании. Флагман июля 2026 года — Qwen3.7 Max: плотная модель на 235 млрд параметров с нативным контекстом 256K, расширяемым до 1 млн. Ключевые преимущества Qwen: зрелая open-source-экосистема (открыта вся линейка от 7B до 235B), точное понимание китайскоязычных сценариев и глубокая интеграция с инфраструктурой Alibaba Cloud.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модель</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Цена вывода (за 1 млн токенов)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Сценарии применения</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0,6 юаня</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Простые вопросы-ответы, классификация текста, высокая нагрузка</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,0 юаня</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Обработка сверхдлинного контекста (10 млн)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7,2 юаня</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Обычные диалоги, генерация контента</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12,0 юаня</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Мультимодальность (изображения и видео), тексты на китайском</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36,0 юаней</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Флагманские возможности для китайского языка, сложные задачи</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ступенчатые цены серии Tongyi Qianwen Qwen (август 2026 г.)

Цены Qwen выстроены ступенями — от сверхдешёвого qwen-turbo (вывод 0,6 юаня за миллион токенов) до флагмана qwen3.7-max (вывод 36 юаней за миллион токенов), покрывая все сценарии — от простых вопросов-ответов до сложных рассуждений. Для компаний, уже работающих с Alibaba Cloud, Qwen — самый удобный вариант интеграции.

##### 3. Zhipu GLM-5.1: первое место среди китайских моделей в SWE-bench

Серия GLM от Zhipu AI в 2026 году выглядела блестяще. GLM-5.1 занял первое место среди китайских моделей в SWE-bench: гибридная MoE-архитектура на 744 млрд параметров, поддержка контекста в 1 млн токенов. Его отличают точное понимание китайской семантики и поддержка легального частного развёртывания в Китае — это очень важно для финансов и госсектора, где требования к безопасности данных высоки. Цены GLM-5.1: ввод 6 юаней, вывод 24 юаня за миллион токенов — середина среди китайских моделей.

##### 4. Kimi K3: король сверхдлинных текстов

Серия Kimi от компании Moonshot AI славится обработкой сверхдлинных текстов. Вышедший в июле 2026 года Kimi K3 имеет 2,8 трлн параметров и в ряде оценок сложных задач входит в мировой первый эшелон. Главные сценарии Kimi — анализ длинных кодовых баз и расширенный поиск по длинным документам: он может обработать текст целой книги или код целого проекта и блестяще справляется с задачами поиска «иголки в стоге сена». Цены у Kimi сравнительно высокие (вывод около 12–20 юаней за миллион токенов), но по цене и качеству в сценариях с длинными текстами ему нет равных.

##### 5. Doubao: универсальный игрок ByteDance

Серия Doubao от ByteDance в 2026 году показывает стабильные результаты. Doubao Seed 2.1 Pro — флагманская модель Volcano Engine с контекстом 256K: в реальных тестах она работает стабильно, а в китайскоязычных сценариях особенно приятна. Преимущества Doubao: большие бесплатные пакеты токенов сразу после регистрации, хорошо проработанная интеграция с экосистемой Volcano Engine и одни из самых низких цен в Китае. Для новичков, которые хотят быстро попробовать AI-программирование, Doubao — вход без порога.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Параметр сравнения</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Общий балл</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Навыки программирования</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Очень сильные</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сильная</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">№1 в SWE среди китайских моделей</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сильная</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Выше среднего</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Понимание китайского языка</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отлично</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отлично</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Точно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отлично</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Отлично</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Контекстное окно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 млн</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сверхдлинное</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Цена вывода (юаней за 1 млн)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Открытый код</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Лицензия MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Вся линейка открыта</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Частично открыт</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Закрытый</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Закрытый</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Частное развёртывание</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Да</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Да</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Да</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нет</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нет</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Сравнение пяти ведущих китайских моделей (август 2026 г.)

Важный тренд: ощущение «поколенческого разрыва» между китайскими моделями и GPT/Claude исчезло. В логических рассуждениях и математических олимпиадах отрыв китайских флагманов от GPT-5 — обычно однозначные числа. В системном архитектурном мышлении и сложных инженерных рассуждениях Claude всё ещё впереди: он предлагает более «вдохновлённые» архитектурные решения, тогда как китайские модели порой выглядят «догматично». Но в китайскоязычных сценариях, контроле затрат и легальном развёртывании у китайских моделей подавляющее преимущество.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">Цена вывода (юаней/млн токенов)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Доубао</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">Цена вывода (ниже — лучше)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">Общий балл (выше — лучше)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 4: сравнение пяти моделей по цене и производительности (чем ниже цена и выше балл — тем лучше)
:::

#### 3. Каркас принятия решения при выборе модели

Узнав особенности моделей, как выбрать модель для своего проекта? Дарим вам «метод четырёх вопросов» — ответьте на четыре вопроса, и вы определите самую подходящую модель.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> Проект разворачивается в Китае или за рубежом?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Китай → выбирайте китайскую модель</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Международный → доступны зарубежные модели</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> Основная задача — программирование или что-то другое?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Программирование → Claude или DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Другое → продолжаем выбор</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> Нужен сверхдлинный контекст (&gt;500 тыс. токенов)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Да → Gemini или Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Нет → продолжаем выбор</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> Бюджет ограничен?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Да → DeepSeek или Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Нет → GPT-5.6 или Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 5: метод четырёх вопросов для выбора большой модели
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Совет: комбинированная стратегия

{class="mt-1"}
Этот метод — не догма: во многих случаях полезно комбинировать несколько моделей. Распространённая стратегия: DeepSeek или Qwen для повседневной разработки (дёшево, хорошо на китайском), Claude для ключевых архитектурных решений (сильные рассуждения, мало галлюцинаций), Gemini для мультимодального анализа (работа с изображениями и видео). Переключайте модели по необходимости, а не «используйте одну до конца».
:::

#### 4. Первые шаги с API: подключаем большую модель с нуля

Многие учебники по AI-программированию учат только работе с чат-интерфейсом, но настоящее «AI-программирование» — когда ваше приложение само вызывает большую модель — идёт через API. API (Application Programming Interface, программный интерфейс приложения) — это протокол общения между программами. Через API ваш код может задействовать возможности большой модели так же просто, как вызывает обычную функцию.

##### 1. Что такое токен

Прежде чем разбираться с API, нужно понять понятие «токен». Токен — базовая единица тарификации больших моделей; её можно назвать «единицей чтения и письма AI». Один токен примерно соответствует 0,75 английского слова (4 символам) или 0,5–1 китайскому иероглифу. Китайский текст в 1000 знаков потребляет примерно 1500–2000 токенов.

Токен — это не количество слов и не количество символов. Большая модель с помощью специального токенизатора (Tokenizer) разбивает текст на токены. Одно и то же слово в разных моделях может занимать разное число токенов: например, «искусственный интеллект» по-китайски — 3 токена в GPT и, возможно, 2 в DeepSeek. API большинства моделей возвращает фактическое число израсходованных токенов — его можно посмотреть в ответе API.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Быстрая оценка стоимости в токенах

{class="mt-1"}
1 миллион китайских знаков — это примерно 1,5 млн токенов. Обработать 1 млн знаков ввода плюс 1 млн знаков вывода с DeepSeek V4 Flash стоит около 0,42 доллара (примерно 3 юаня); с Claude Fable 5 тот же объём — около 60 долларов (примерно 434 юаня). Вот почему выбор модели напрямую влияет на стоимость вашего проекта.
:::

##### 2. Получение API-ключа

Первый шаг к работе с API больших моделей — получить API-ключ (API Key), то есть строку-ключ для подтверждения личности. У каждого провайдера моделей своя API-платформа: нужно зарегистрировать аккаунт и создать API-ключ. Ниже — входы на API-платформы основных моделей и порядок получения ключа:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Модель</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">API-платформа</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Порядок получения</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Бесплатный лимит</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → верификация личности → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатный лимит для новых пользователей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tongyi Qianwen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (платформа Bailian)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Вход с аккаунтом Alibaba Cloud → включение сервиса → создание ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатный пробный период для новых пользователей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → верификация личности → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатный лимит для новых пользователей</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → верификация личности → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ограниченный бесплатный лимит</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcano Engine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → включение Ark → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Много токенов в подарок за регистрацию</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → привязка кредитной карты → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Без бесплатного лимита (платно)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Регистрация → привязка карты → создание API-ключа</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Небольшой лимит для новых пользователей</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
API-платформы основных моделей и способы получения ключа (август 2026 г.)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Безопасность: API-ключ = пароль от кошелька

{class="mt-1"}
API-ключ равнозначен паролю от вашего кошелька: любой, кто получит ключ, сможет вызывать модели за ваш счёт. Поэтому: никогда не пишите API-ключ прямо в коде (храните его в переменных окружения); никогда не отправляйте код с ключом в публичный Git-репозиторий; никогда не публикуйте в соцсетях скриншоты с ключом. Если ключ утёк, немедленно удалите его на платформе и создайте новый.
:::

##### 3. Первый вызов API

Получив API-ключ, вы можете вызывать API больших моделей на любом языке программирования. Ниже — простейший вызов на Python: отправляем DeepSeek сообщение и получаем ответ.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Первый вызов API</span><span class="dots">···</span>
:::

```
# Установите SDK: pip install openai
# DeepSeek совместим с форматом OpenAI SDK — можно использовать напрямую
from openai import OpenAI
import os

# 1. Создаём клиент (API-ключ читается из переменной окружения)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. Отправляем запрос
response = client.chat.completions.create(
    model="deepseek-chat",  # указываем модель
    messages=[
        {"role": "system", "content": "Ты — ассистент по программированию на Python."},
        {"role": "user", "content": "Напиши функцию быстрой сортировки."}
    ]
)

# 3. Получаем ответ
print(response.choices[0].message.content)

# 4. Смотрим расход токенов
print(f"Входные токены: {response.usage.prompt_tokens}")
print(f"Выходные токены: {response.usage.completion_tokens}")
print(f"Всего токенов: {response.usage.total_tokens}")
```
:::

Ключевая логика этого кода: создаём клиент (с API-ключом и адресом модели) → формируем список сообщений (system задаёт роль, user — ввод пользователя) → отправляем запрос → получаем ответ. Этот шаблон подходит почти для всех моделей, совместимых с форматом OpenAI: чтобы сменить модель, достаточно поменять api_key и base_url. Именно поэтому многие китайские модели сделали совместимость с форматом OpenAI SDK: разработчику хватает двух строк кода, чтобы переключить модель, — затраты на мигрение минимальны.

Ниже — различия в коде при переключении на другие модели. Обратите внимание: меняются всего две строки:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Смена модели — всего две строки</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Tongyi Qianwen (платформа Bailian)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# Zhipu GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url можно оставить по умолчанию
)
# model="gpt-5.6-terra"
```
:::

##### 4. Потоковые ответы (Streaming)

В реальных приложениях обычно не хочется ждать, пока AI допишет всё до конца, чтобы показать текст одним куском, — пользователю пришлось бы ждать слишком долго. Потоковый ответ (Streaming) позволяет показывать текст слово за словом по мере генерации, заметно улучшая впечатление от работы. Как на печатной машинке: буквы выпрыгивают одна за другой — ощущения совсем другие.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Потоковый ответ</span><span class="dots">···</span>
:::

```
# Потоковый ответ: вывод по символам
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Напиши туториал по пузырьковой сортировке на Python"}
    ],
    stream=True  # включаем потоковый режим
)

# Получаем по кускам и печатаем
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# Вывод появится посимвольно, как на печатной машинке
```
:::

#### 5. Руководство по покупке Token Plan

У большинства провайдеров моделей два способа тарификации: оплата по мере использования (Pay-as-you-go) и подписочный план (Token Plan / Subscription). Понимание разницы между ними поможет заметно снизить ваши затраты.

##### 1. Оплата по использованию или подписка

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Критерий</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Оплата по использованию (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Подписка (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Способ оплаты</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Платите за фактически израсходованные токены</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Фиксированная предоплата за лимит</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Подходит для</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нестабильное потребление, редкие вызовы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Стабильное потребление, частые вызовы</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ценовое преимущество</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Стандартная цена</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">На 20–50% ниже оплаты по использованию</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Гибкость</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Доступно в любой момент, без обязательств</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Нужна предоплата; лимит может сгореть</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Превышение лимита</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Автоматический переход к оплате по использованию</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">После исчерпания лимита — оплата по использованию</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Типичные платформы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Официальные API-платформы каждой модели</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Сравнение двух способов оплаты

Новичкам советуем начинать с оплаты по использованию: без предоплаты, платите ровно за то, что потратили. Когда месячное потребление стабилизируется (например, превысит 50 юаней в месяц), подумайте о переходе на подписку ради более низкой цены за единицу.

##### 2. Обзор популярных подписок

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">План</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Цена в месяц</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Что входит</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Кому подходит</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Безлимитный текстовый чат с GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проба для новичков с нуля</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 долл./мес</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, генерация изображений, анализ данных, доступ к плагинам</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Умеренно активные пользователи</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200 долл./мес</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Безлимитный доступ ко всем моделям, приоритетный доступ к новинкам</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Профессионалы с высокой нагрузкой</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ограниченное число диалогов с Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проба для новичков с нуля</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 долл./мес</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Безлимитное использование Claude, приоритетный доступ к новым моделям</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разработчики</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатно</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ограниченное число AI-дополнений и диалогов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Проба для начинающих</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 долл./мес</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Безлимитные AI-дополнения, 500 премиум-запросов в месяц</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Разработчики на каждый день</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40 долл./мес за человека</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Командная работа, панель администратора, режим приватности</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Команды</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Подписки популярных AI-инструментов (август 2026 г.)

У китайских моделей подписочные схемы немного другие. DeepSeek работает в основном по оплате за использование — месячных подписок нет: вы пополняете счёт и платите по факту. Tongyi Qianwen на платформе Bailian предлагает предоплаченные пакеты ресурсов (покупаете определённый объём токенов со скидкой). У Doubao на Volcano Engine есть похожие предоплаченные схемы. Для китайских разработчиков самая экономная комбинация обычно такая: DeepSeek с оплатой по использованию (повседневная разработка) + бесплатные лимиты Doubao (пробы и тесты).

##### 3. Платформы-агрегаторы API

Если нужно пользоваться сразу несколькими моделями, платформа-агрегатор API — беспроблемный выбор. Агрегатор даёт один общий API-ключ, с которым доступны десятки моделей по всему миру, — регистрироваться отдельно на каждой платформе не придётся.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Платформа</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Особенности</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ценовое преимущество</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Подходит для</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Международный агрегатор: один ключ открывает модели всего мира</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Прозрачные цены, сравнение в реальном времени</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Тем, кто гибко переключается между зарубежными моделями</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Китайский агрегатор: API множества китайских моделей</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">На 20–30% ниже официальных цен</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Китайские разработчики, сравнение цен между моделями</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (прокси Microsoft)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API OpenAI через прокси Microsoft Azure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API даёт скидку 50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Корпоративные вызовы OpenAI, крупные асинхронные задачи</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Облачная AI-платформа Baidu: модели ERNIE (Wenxin) и другие</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Бесплатный лимит для новых пользователей</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пользователи экосистемы Baidu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Популярные агрегаторы API (август 2026 г.)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Осторожно: не покупайте «общие ключи»

{class="mt-1"}
Не покупайте так называемые «общие API-ключи» на Taobao, Xianyu и подобных площадках: происхождение таких ключей неизвестно, аккаунт могут заблокировать в любой момент, плюс есть риск утечки данных. Получайте API-ключи только через официальные или проверенные платформы-агрегаторы.
:::

##### 4. Стратегии экономии

Правильно выбранная модель — только первый шаг; не менее важно «пользоваться экономно». Вот несколько проверенных на практике стратегий снижения затрат:

1. Используйте попадания в кэш. У многих моделей есть «кэширование»: если в запросе есть уже обработанное ранее содержимое (например, системный промпт), эта часть тарифицируется по очень низкой цене. У DeepSeek попадание в кэш стоит всего 1/60 обычной цены. Ставьте фиксированный системный промпт в начало списка сообщений — так вы максимизируете попадания в кэш.
2. Многоуровневая маршрутизация: простые задачи — дешёвой модели, сложные — дорогой. Например, DeepSeek V4 Flash для классификации текстов (вывод 2 юаня за миллион токенов), а Claude — для архитектурного проектирования (вывод 181 юань за миллион токенов). В проекте около 80% вызовов можно отдать дешёвой модели.
3. Ограничивайте длину вывода. API тарифицируется по токенам вывода: чем длиннее вывод, тем дороже. Если пространные рассуждения не нужны, задайте параметр max_tokens, чтобы ограничить длину ответа и не дать AI «лить воду».
4. Используйте Batch API для задач без реального времени. Если у вас много задач, не требующих мгновенного ответа (массовая разметка данных, сводки документов и т. п.), Batch API даёт скидку 50%. Эту функцию предлагают и OpenAI, и Azure.
5. Следите за расходом токенов. Большинство API-платформ предлагают панели статистики. Регулярно смотрите распределение расходов, находите самые «токенозатратные» вызовы и точечно их оптимизируйте. Маленькая правка промпта (например, заменить «объясните подробно» на «объясните в трёх предложениях») может сэкономить до 50% токенов.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Стратегия оптимизации</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Экономия</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Сложность внедрения</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Пояснение</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Попадания в кэш</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">До 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Низкая</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Фиксированное содержимое — в начало сообщений</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Многоуровневая маршрутизация</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Средняя</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Простые задачи — дешёвой модели</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ограничение длины вывода</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Низкая</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Задайте параметр max_tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Низкая</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Пакетная обработка отложенных задач</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Оптимизация промптов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Средняя</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Сокращайте промпты, убирайте избыточность</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Стратегии экономии и их эффект (август 2026 г.)

#### 6. Практика: подключаем API большой модели в проекте

Завершим главу полноценной практикой — создадим «генератор резюме на AI»: пользователь вводит длинный текст, а мы вызываем API большой модели и получаем выжимку. Эта практика покажет полный цикл работы с API: настройку окружения, вызов API, обработку ошибок и контроль затрат.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - ИИ-суммаризатор
import os
from openai import OpenAI

# 1. Настройка (API-ключ читается из переменной окружения — никогда не вшивайте его в код)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Суммаризация текста

    Args:
        text: исходный текст для суммаризации
        max_length: максимальная длина резюме (в токенах)

    Returns:
        dict: резюме и сведения о расходе токенов
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Ты — генератор резюме."
                               "Кратко резюмируй предоставленный пользователем текст."
                               "Резюме — не длиннее 3 предложений."
                },
                {
                    "role": "user",
                    "content": f"Суммаризируй следующий текст:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # ограничиваем длину вывода
            temperature=0.3  # низкая температура = стабильнее
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. Пример использования
if __name__ == "__main__":
    long_text = """
    (вставьте сюда длинный текст…)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Резюме: {result['summary']}")
        print(f"Потрачено токенов: {result['total_tokens']}")
        # оцениваем стоимость: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # ≈0,4 фэня за 1 000 токенов
        print(f"Ожидаемая стоимость: {cost:.4f} юаня")
    else:
        print(f"Ошибка: {result['error']}")
```
:::

Этот код воплощает несколько лучших практик работы с API: API-ключ читается из переменных окружения и никогда не зашивается в код; у функции понятная документация и подсказки типов; параметр max_tokens ограничивает длину вывода; temperature задан низким (0.3) для более стабильного вывода; есть полноценная обработка ошибок; возвращается информация о расходе токенов для контроля затрат. Когда поручите этот код AI, просто перечислите ему эти требования — он вполне способен их реализовать.

:::inline div .quote-line
Главный итог главы: модели — это «боеприпасы», методология — «тактика». Правильные боеприпасы облегчают бой, но без хорошей тактики даже лучшие патроны войну не выиграют. Теперь вы знаете особенности моделей и умеете работать с API — ваш «арсенал» полон, но как вести этот бой, решают методы мышления из предыдущих глав.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Попробуйте сами: добейтесь первого успешного вызова API

{class="mt-1"}
Зарегистрируйтесь на платформе китайской модели (рекомендуем DeepSeek или Zhipu — оба дарят лимиты новым пользователям), создайте API-ключ, запишите его в переменные окружения системы (не в код!), затем запустите код из раздела «Первый вызов API». В тот момент, когда вы увидите напечатанный ответ AI, вы перейдёте границу между «пользоваться AI» и «создавать AI-приложения».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Итоги главы

- Международная тройка лидеров: GPT-5.6 (сбалансированный универсал), Claude (эталон программирования + всего 1% галлюцинаций), Gemini (король мультимодальности + контекст 2 млн)
- Китайская пятёрка: DeepSeek V4 (король цены и качества; следите за анонсом повышения цен), Qwen3.7 (корпоративный уровень), GLM-5.1 (№1 в SWE среди китайских моделей), Kimi K3 (сверхдлинные тексты), Doubao (бесплатный старт)
- Метод четырёх вопросов: где развёртывание? программирование или другое? нужен сверхдлинный контекст? важен бюджет?
- Токен — единица тарификации: 1 китайский знак — примерно 1,5–2 токена; 1 млн знаков — примерно 1,5 млн токенов
- API-ключ = пароль от кошелька: храните в переменных окружения, никогда не зашивайте в код и не отправляйте в Git
- Китайские модели обычно совместимы с OpenAI SDK: для смены модели достаточно поменять две строки — api_key и base_url
- Пять приёмов экономии: попадания в кэш, многоуровневая маршрутизация, ограничение вывода, Batch API, контроль расхода
:::
