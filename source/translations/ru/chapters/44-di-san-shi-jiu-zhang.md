---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Глава 39: Инженерия контекста — помогаем ИИ понять ваш замысел
toc: default
kind: chapter
---

### Глава 39. Инженерия контекста — помогите ИИ понять ваши намерения

{class="chapter-intro mb-4"}
Знакомо ли вам это: открыли новое окно диалога, и ИИ будто амнезию получил — забыл всё о вашем проекте? Это не ИИ вас нарочно дразнит, просто ему от природы свойственна «забывчивость». Эта глава научит ставить ИИ «систему долговременной памяти» и заодно познакомит с одной из самых горячих парадигм разработки 2026 года — разработкой по спецификациям.

#### 1. Файл памяти проекта: «долговременная память» ИИ

У ИИ-моделей есть фундаментальное ограничение: их память «краткосрочна». В начале каждого диалога ИИ знает о вашем проекте ровно ноль. Вам приходится раз за разом сообщать ему «у нас React», «бэкенд на Node.js», «база данных PostgreSQL», «строки в коде берём в двойные кавычки». Это не только неэффективно, но и чревато упущениями — как заново проводить онбординг новому коллеге каждое утро.

Решение — «файл памяти проекта»: текстовый файл в корне проекта, который ИИ-инструменты автоматически читают в начале каждого диалога. У разных инструментов свои соглашения об именах:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Инструмент</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Имя файла</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Универсальный вариант</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Соглашения об именах файлов памяти проекта в разных инструментах

Имена разные, но принцип один: записывайте в этот файл то, что ИИ должен «помнить всегда». Хороший файл памяти проекта должен содержать: обзор проекта (что это за проект), техстек (какие технологии используются), стандарты кода (имена, отступы, стиль комментариев), структуру каталогов (как организован код), соглашения разработки (стратегия веток, правила коммитов, требования к тестам). CLAUDE.md у Karpathy — всего 70 строк, но покрывает всю ключевую информацию: лаконично и полно.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Проект: личное приложение для учёта финансов
## Обзор
Полностековое приложение для личных финансов: помогает записывать ежедневные доходы и расходы.
## Технологии
- Фронтенд: React + TypeScript + Tailwind CSS
- Бэкенд: Node.js + Express + TypeScript
- База данных: SQLite (разработка) / PostgreSQL (прод)
- Тесты: Vitest
## Стиль кода
- Используем двойные кавычки
- Отступ в 2 пробела
- Имена функций в camelCase
- Типы в PascalCase
- У каждой функции — комментарий JSDoc
## Структура каталогов
/src
  /frontend  - код фронтенда
  /backend   - код бэкенда
  /shared    - общие типы фронта и бэка
  /tests     - файлы тестов
## Правила разработки
- Сообщения коммитов на русском
- Для новых функций сначала пишем тесты
- API всегда возвращает { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Внимание: не превращайте его во «второй документ требований»

{class="mt-1"}
Следите за длиной этого файла — не пишите из него многотомный документ требований на десятки страниц. Задача файла памяти — «дать ИИ быстрый фон», а не «детально описать каждую функцию». Держите его кратким, структурированным, только то, «что ИИ должен знать».
:::

#### 2. Разработка по спецификациям (SDD)

Spec-Driven Development (SDD, разработка по спецификациям) — парадигма разработки, взрослеющая с 2026 года. Её суть в одном предложении: сначала спецификация, потом код. В отличие от классического TDD (разработки через тестирование), «спецификация» в SDD — это не только тест-кейсы, но и описание требований, определения интерфейсов, модели данных и т. д. ИИ генерирует код по этим спецификациям, а обязанность человека — писать и поддерживать спецификации.

Рабочий процесс SDD состоит из пяти шагов:

1. Опишите требования на естественном языке (в файле .md);
2. Определите интерфейсы и структуры данных (в файле спецификации);
3. Поручите ИИ сгенерировать реализацию кода по спецификации;
4. Запустите тесты, чтобы проверить соответствие результата спецификации;
5. Если не соответствует — правьте спецификацию или пусть ИИ правит код.

В этом процессе файл спецификации — «единственный источник истины»: код можно перегенерировать, но спецификация сначала должна быть верной.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Написать файл спецификации</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Достаточна ли спецификация?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Достаточна</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> ИИ генерирует код по спецификации</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Прогнать тесты и проверить результат</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Недостаточна / тесты не проходят</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Проблема в коде → правим код; проблема в спецификации → правим спецификацию</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Снова к проверке</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Всё пройдено → сдаём</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Рисунок 3: рабочий процесс разработки по спецификациям (SDD)
:::

Сила SDD в том, что файл спецификации стабильнее кода. Когда меняется модель или инструмент, ваш файл спецификации остаётся в силе — достаточно поручить новому ИИ-инструменту перегенерировать код. Именно поэтому книга подчёркивает «методология важнее инструментов»: файл спецификации — конкретный носитель вашей методологии.

#### 3. Управление окном контекста

Даже с файлом памяти проекта вы всё равно столкнётесь в диалогах с проблемой «контекста не хватает». Окно контекста ИИ-модели (объём информации, обрабатываемой одновременно) ограничено. Когда диалог слишком длинный или файлов упомянуто слишком много, ИИ «забывает» раннюю информацию, и качество результата падает — как у друга, с которым вы проговорили шесть часов и который давно не помнит, о чём вы сказали в самом начале.

Ключевая стратегия управления окном контекста — «послойные ссылки»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Слой контекста</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Содержимое</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Способ управления</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Слой 1: память проекта</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Техстек, стандарты, структура каталогов</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Записывается в CLAUDE.md и подобные файлы, загружается автоматически, повторять не нужно</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Слой 2: ссылки на файлы</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Файлы кода, затронутые текущей задачей</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ссылайтесь точно через символ @, не вставляйте файл целиком в диалог</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Слой 3: контекст диалога</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">История диалога по текущей задаче</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Завершив задачу, открывайте новый диалог — контекст не должен разбухать</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Слой 4: текущая инструкция</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Конкретные требования текущего шага</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ясно, кратко, по делу — без длинных описаний</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Послойная стратегия управления окном контекста

#### 4. Практические приёмы инженерии контекста

Инженерия контекста — не разовая настройка, а процесс постоянной оптимизации. Вот несколько приёмов, многократно проверенных практикой:

1. Обновляйте файл памяти вместе с эволюцией проекта. Появилась новая технология или изменилась архитектура — обновите файл памяти сразу, а не объясняйте «на ходу» в диалоге.
2. Пользуйтесь ссылками @ вместо вставки целого текста. Большинство ИИ-инструментов поддерживают синтаксис @file или @folder: содержимое подставляется в контекст ИИ в фоне — эффективнее, чем вставлять вручную, и не засоряет диалог.
3. Держите диалоги «короткими и ёмкими». Один диалог — одна задача или одна функциональная точка. Закончили — открывайте новый диалог для следующей. Длинные диалоги не только съедают окно контекста, но и «рассеивают внимание» ИИ.
4. Давайте ИИ «увидеть» результат, а не «услышать описание». Наткнулись на баг — прикладывайте лог ошибки через ссылку @, а не пересказывайте своими словами «там вроде какая-то ошибка». ИИ полезнее видеть исходную информацию, чем ваш пересказ.
5. Регулярно чистите и архивируйте. Завершённые диалоги и временные файлы занимают рабочее пространство. Периодическая уборка лишнего и порядок в каталоге проекта помогают ИИ эффективнее понимать структуру проекта.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Практика: напишите для своего проекта 70-строчный файл памяти

{class="mt-1"}
Возьмите проект, которым занимаетесь (или собираетесь), и напишите CLAUDE.md: обзор проекта (2–3 предложения), техстек (перечислите), стандарты кода (3–5 пунктов), структура каталогов (нарисуйте дерево), соглашения разработки (2–3 пункта). Уложитесь в 70 строк — закончив, вы заметите, что и сами стали понимать проект заметно яснее.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Краткие итоги главы

- Память ИИ «краткосрочна»: в каждом новом диалоге он знает о проекте ноль
- Файл памяти проекта (CLAUDE.md и др.) — «долговременная память» ИИ, загружается автоматически в начале каждого диалога
- Хороший файл памяти = обзор + техстек + стандарты + структура каталогов + соглашения; 70 строк вполне достаточно
- SDD — разработка по спецификациям: сначала спецификация, потом код; спецификация — «единственный источник истины», она стабильнее кода
- Контекст управляется четырьмя слоями: память проекта → ссылки @файлы → история диалога → текущая инструкция
- Пять практических приёмов: синхронно обновлять, ссылаться через @, короткие диалоги, давать исходные данные, регулярно чистить
:::
