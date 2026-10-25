---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav: Anexo: Guía de introducción a GitHub
toc: sub
kind: chapter
---

### Anexo del Capítulo 23: Guia de inicio de GitHub

{class="chapter-intro mb-4"}
En el capítulo anterior hablamos del "pensamiento computacional", pero para llevarlo a la practica y colaborar con otros en proyectos, hay un nombre inevitable: GitHub. Tanto si eres estudiante de informática participando en competencias, si quieres guardar tus proyectos de código, o simplemente quieres ver que estan desarrollando los programadores de todo el mundo, GitHub es una plataforma que debes conocer. En esta sección empezamos desde los conceptos más básicos para ayudarte a construir una comprensión clara.

#### I. ¿Qué es GitHub exactamente?

Dicho simplemente, GitHub es una <strong>plataforma de alojamiento y colaboración de código basada en Git</strong>. Se lanzó en 2008, fue adquirida por Microsoft en 2018 y sigue siendo la plataforma de alojamiento de código abierto más grande del mundo, albergando cientos de millones de repositorios que cubren casi todos los lenguajes de programación principales.

Para entenderlo con una analogía:<strong>Git es tu diario en el ordenador, GitHub es una plataforma de blog pública</strong>— puedes publicar tus propios trabajos, seguir proyectos de otros, participar en discusiones y colaboraciones. No es solo un "almacén trasero para programadores", sino más bien una "ciudad tecnológica" construida conjuntamente por desarrolladores de todo el mundo — los proyectos nacen aquí, se iteran, se discuten y se reútilizan.

Para la gente común, GitHub tampoco está fuera de alcance. Muchos no programadores lo usan para alojar notas, libros electrónicos, blogs personales e incluso para respaldar archivos de configuración. Mientras tengas aunque sea un poco de necesidad de "organizar tus cosas y compartirlas", GitHub merece que lo conozcas.

#### II. Diferencia entre Git y GitHub (concepto clave)

Mucha gente confunde estos dos términos al contacto por primera vez; aquí te ayudo a aclararlo:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento de comparación</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Naturaleza</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Herramienta de control de versiones (software)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataforma de alojamiento de código (sitio web)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ubicación de ejecución</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En ordenador local</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En la nube (acceso por navegador)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Responsabilidad principal</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registra cada cambio de archivo (qué cambió, quién lo cambió, cuándo)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pone repositorios Git en la nube para facilitar almacenamiento, visualización y colaboración</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Requiere internet?</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No, funciona sin conexión</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere conexión a internet</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pertenencia</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Software de código abierto, creado por Linus Torvalds (padre de Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Producto de Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Competidores similares</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

En resumen:<strong>Git gestióna "como registrar cambios", GitHub gestióna "donde guardar los cambios y como colaborar"</strong>. Git es una herramienta que funciona localmente; GitHub es una plataforma que pone repositorios Git en la nube para facilitar colaboracion y visualización. Puedes usar Git sin GitHub (por ejemplo para gestionar versiones de tu propio código), pero si usas GitHub debes usar obligatoriamente Git (porque GitHub se basa en Git).

#### III. Conceptos y funciones principales de GitHub

##### 📁 Conceptos básicos

Antes de empezar, conoce algúnos terminos frecuentes; de lo contrario la interfaz de GitHub te parecera confusa:

- <strong>Repositorío (Repository, abreviado Repo)</strong>: cada proyecto corresponde a un repositorio que contiene todos los archivos de código, versiones históricas y documentos del proyecto. Puedes entenderlo como una "carpeta de proyecto".
- <strong>Commit</strong>: un registro de modificación del código. Cada commit incluye un mensaje descriptivo que registra "que se cambio y por que". Esta es la base de la "viaje en el tiempo" de Git/GitHub.
- <strong>Rama (Branch)</strong>: una linea de desarrollo independiente que se separa de la rama principal. Por ejemplo, si quieres anadir una nueva función, puedes crear una rama para desarrollarla por separado y luego fusionarla de vuelta a la rama principal sin afectar a otros.
- <strong>Clonar (Clone)</strong>: copiar completamente un repositorio de la nube a tu ordenador local para poder modificar el código localmente.
- <strong>Push / Pull</strong>: Push sube código local a GitHub; Pull descarga el último código de GitHub a tu ordenador local. Son las dos acciones básicas para sincronizar código en colaboracion de equipo.
- <strong>Pull Request (PR)</strong>: cuando terminas de modificar código en una rama y quieres fusionarlo con la rama principal, inicias un PR para que los miembros del equipo revisen el código antes de fusionar. Este es el mecanismo central de colaboracion en GitHub.
- <strong>Issue</strong>: se usa para registrar bugs, solicitudes de funciones y temas de discusion. Cada Issue es como un hilo de discussion donde se puede asignar un responsable y etiquetar.
- <strong>Fork</strong>: copiar el repositorio de otra persona a tu propia cuenta. Puedes modificar libremente tu copia sin afectar el repositorio original. Cuando hayas terminado, puedes enviar un PR al autor original solicitando fusionar tus mejoras.

##### 🛠️ Funciones principales

GitHub ofrece no solo almacenamiento de código, sino también:

- <strong>Control de versiones</strong>: registra el historial de cada cambio en el código; si algo sale mal, puedes volver a cualquier versión anterior normal.
- <strong>Colaboracion en equipo</strong>: soporta desarrollo paralelo multip usuario en un mismo proyecto; multiples personas pueden desarrollar simultaneamente sin sobrescribir ni crear conflictos.
- <strong>Seguimiento de problemas</strong>: usa Issues para registrar bugs y solicitudes de funciones, facilitando el seguimiento del equipo.
- <strong>Gestíon de proyectos</strong>: integra tareas, tableros de proyecto (Projects) y otras herramientas de gestión; equivalente a tener un Trello ligero integrado.
- <strong>Automatización</strong>: mediante <strong>GitHub Actions</strong>, compila, prueba, empaqueta e despliega automáticamente tras cada envío de código. Es la herramienta central de "CI/CD (integracion/despliegue continuo)" moderno.
- <strong>Gestíon de documentación</strong>: README presenta el proyecto, Wiki almacena arquitectura detallada y normas de desarrollo, Pages incluso puede alojar sitios web estaticos.
- <strong>Alojamiento y presentación de código</strong>: cada repositorio tiene una hermosa pagina web con resaltado de sintaxis; es la "carta de presentación" de tu obra técnica.
- <strong>Comunidad open source</strong>: puedes Star (Guardar) proyectos que te gusten, Watch (seguir) la actividad de proyectos, Follow (seguir) desarrolladores, participando en la colaboracion open source global.

#### IV. Registro e inicio: Crea tu primer repositorio en 5 minutos

##### 📝 Registrar cuenta

1. Visita<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>y haz clic en "Sign up".
2. Introduce tu correo electrónico, establece una contrasena y un nombre de usuario (aparecera en la URL de tu perfil; se recomienda usar inglés, ej.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/tunombre</code>).
3. Completa la verificación de correo y el captcha.
4. Elige el plan gratuito (Free); es completamente suficiente para usuarios individuales.

##### 📁 Crear tu primer repositorio

1. Tras iniciar sesion, haz clic en "+" en la esquina superior derecha y selecciona "New repository".
2. Introduce el nombre del repositorio (Repository name), por ejemplo<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Escribe una breve descripción (Descriptíon) para que otros sepan de que trata este repositorio.
4. Elige Publico (Public) o Privado (Private). Los repositorios publicos son visibles para todos; los privados solo para ti y tus colaboradores. La cuenta gratuita soporta repositorios privados ilimitados.
5. Marca "Add a README file" — README es el "manual de instrucciones" del proyecto; se recomienda en cada repositorio.
6. Haz clic en "Create repository" y tu primer repositorio GitHub nacera!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Mini-dato: que es README

{class="mt-1"}
README.md es un archivo en formato Markdown, lo primero que ven otros al abrir tu repositorio. Un buen README suele contener: descripción del proyecto, método de instalación, ejemplos de uso, licencia, contacto. Escribir un buen README es una competencia básica de programador y la primera barrera para que otros usen tu proyecto.
:::

#### V. Flujo de trabajo básico: de local a la nube

Para entender el flujo de trabajo de GitHub, recuerda este ciclo:<strong>modificación local -&gt; area de preparación (stage) -&gt; commit -&gt; push -&gt; actualización en la nube</strong>. A continuacion explico cada paso con palabras sencillas:

1. <strong>Modificar archivos</strong>: escribe código o edita documentos en tu editor local.
2. <strong>git add</strong>: anade los archivos modificados al "area de preparación (staging)", equivalente a decirle a Git "estos cambios estoy listo para registrarlos".
3. <strong>git commit</strong>: registra oficialmente los cambios del staging como un "commit", acompanado de un mensaje descriptivo como "corregir bug de inicio de sesion". Este paso se completa solo localmente.
4. <strong>git push</strong>: sube tus commits locales a GitHub en la nube para que otros puedan verlos.
5. <strong>git pull</strong>: antes de empezar a trabajar, descarga el último código desde la nube para mantener tu local sincronizado con el resto del equipo.

Para principiantes, recuerda esta fórmula:<strong>"primero pull, luego modificas, al terminar haces add, commit con descripción, finalmente push"</strong>. Adopta este hábito y la colaboracion en equipo sera ordenada.

#### VI. Flujo de colaboración en equipo: cómo funciona Pull Request

Lo más poderoso de GitHub es su mecanismo de colaboracion. Un flujo tipico de colaboracion en equipo es el siguiente:

1. <strong>Crear rama</strong>: desde la rama principal (generalmente llamada main o máster) crea una nueva rama, por ejemplo<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, y desarrolla la nueva función en ella.
2. <strong>Desarrollar y hacer commits</strong>: escribe código en la nueva rama, haciendo multiples commits para registrar el progreso.
3. <strong>Push a GitHub</strong>: sube la rama al repositorio en la nube.
4. <strong>Iniciar Pull Request</strong>: en la web de GitHub inicia un PR solicitando fusionar tu rama con la principal. Explica claramente que cambios hace este PR y por que.
5. <strong>Revisión de código (Code Review)</strong>: los miembros del equipo revisan tu código, dan opiniones o sugieren modificaciones. Puedes seguir haciendo commits según los comentarios; el PR se actualiza automáticamente.
6. <strong>Fusionar (Merge)</strong>: tras aprobar la revisión, haz clic en "Merge" para fusionar el código con la rama principal. Tu contribucion entra oficialmente en el proyecto!

Este flujo garantiza que <strong>todo código que entra en la rama principal pasa por revisión</strong>, reduciendo enormemente la probabilidad de errores. Los proyectos open source también usan este mecanismo para aceptar contribuciones de extraños de todo el mundo — puedes enviar un PR a cualquier proyecto open source conocido y, si se acepta, te conviertes en colaborador de ese proyecto.

#### VII. Escenarios típicos de uso de GitHub

##### 🎓 Estudíantes: competencias y proyectos academicos

Los estudiantes de informática que participan en ACM, hackathons o trabajos de fin de carrera casi siempre usan GitHub. Sirve tanto como plataforma de colaboracion en equipo como como ventana de exhibicion de trabajos — los jueces pueden ver directamente tu repositorio para evaluar la calidad del código y el proceso de colaboracion. Muchas empresas piden el enlace a tu perfil de GitHub como prueba de capacidad técnica al contratar.

##### 📚 Base de conocimiento personal y alojamiento de notas

Los no programadores también pueden usar GitHub. Muchos lo usan para alojar notas de estudio, blogs técnicos (con GitHub Pages se puede crear un sitio web gratis), libros electrónicos. Escritura en Markdown + control de versiones con Git + respaldo en la nube, tres en uno.

##### 🌐 Participar en proyectos open source

GitHub es la fortaleza central del movimiento open source global. Puedes Forkar proyectos que te gusten, modificarlos y enviar PRs para devolver mejoras a la comunidad; o simplemente StarGuardar buenos proyectos para seguir sus actualizaciones. Participar en open source es una via excelente para mejorar tus habilidades técnicas y acumular reputacion.

##### 🤖 Despliegue automatizado y CI/CD

Con GitHub Actions puedes implementar un flujo totalmente automático de "código push -&gt; prueba automática + despliegue al servidor". Muchos blogs personales y sitios de documentación funcionan asi: escribes un artículo, haces push y el sitio se actualiza automáticamente.

##### 💾 Respaldo de código y sincronización multidispositivo

Usa los repositorios como nube; al cambiar de ordenador o trabajar con multiples dispositivos, un git pull te da el último código sin necesidad de copiar con USB.

#### VIII. Consejos para principiantes

- <strong>Escribe mensajes de commit claros</strong>: no uses mensajes inútiles como "update". Un buen commit message seria "corregir problema de redireccion tras inicio de sesion"; seis meses después seguiras sabiendo que hiciste.
- <strong>Comitea frecuentemente, avanza a pasos pequenos</strong>: haz un commit cada vez que completes una función pequena, en vez de una sola vez al final del día. Asi es más fácil localizar problemas.
- <strong>Desarrolla en ramas, no modifiques directamente la rama principal</strong>: incluso en proyectos personales, acostumbra a crear ramas; cuando colabores en equipo no estaras perdido.
- <strong>Usa bien .gitignore</strong>: este archivo le dice a Git que archivos no incluir en el control de versiones (configuraciones de contraseñas, compilados, carpetas de dependencias), evitando subir archivos basura.
- <strong>Estudía proyectos open source excelentes</strong>: navega por GitHub Trending, observa la estructura de código, la redacción del README y el flujo de colaboracion de los proyectos con más estrellas; es la forma más rápida y gratuita de mejorar.
- <strong>Solicitar el paquete estudíantil de GitHub</strong>: tras verificar tu condición de estudiante, puedes obtener gratis créditos de númerosas herramientas y servicios de pago (Copilot, dominios, servicios en la nube, etc.), valor de miles de dólares.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Recordatorío de seguridad

{class="list-disc pl-6 mt-1 space-y-1"}
- Nunca subas contraseñas, claves API, cadenas de conexión a bases de datos u otra información sensible a GitHub, especialmente en repositorios públicos — una vez filtrada, los rastreadores la capturarán al instante con graves consecuencias.
- Si por error subiste información sensible, no basta con borrar el archivo (todavía está en el historial); usa<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> o herramientas profesionales para limpiar el historial y cambia inmediatamente las claves filtradas.
- Los repositorios privados tampoco son absolutamente seguros; lo mejor es gestionar la información sensible con variables de entorno, sin incluirla en el repositorio de código.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Notas importantes: acceso a GitHub desde China

{class="mt-1"}
El acceso a GitHub desde China a veces es inestable; puede que no se abra o que el clonado sea lento. Puedes intentar: ① Usar sitios mirror nacionales (como GitClone, ghproxy) para acelerar el clonado; ② Configurar Hosts o usar proxy; ③ Si colaboras principalmente dentro de China, también puedes considerar la alternativa nacional <strong>Gitee</strong>, con funciones similares y acceso rápido. Muchos equipos alojan simultáneamente en GitHub y Gitee, equilibrando internacionalización y velocidad doméstica.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Nivel intermedio: crea tu blog personal gratis con GitHub Pages

{class="mt-1"}
GitHub Pages te permite alojar gratis un sitio estático; combinado con generadores de sitios estáticos como Jekyll, Hexo o Hugo, puedes crear fácilmente un blog personal. Escribe artículos en Markdown, haz push al repositorio y el blog se actualiza automáticamente, con HTTPS y dominio personalizado incluidos. Innumerables blogs de tecnólogos están construidos así: costo cero, sin anuncios, con control de versiones.
:::

#### IX. Resumen: por qué todos deberían conocer GitHub

GitHub hace tiempo que dejó de ser solo "una herramienta de programadores"; es más bien una <strong>forma de trabajar en la era digital</strong>: el control de versiones hace todo rastreable, los mecanismos de colaboración hacen que los equipos funciónen eficientemente, y el espíritu open source deja fluir libremente el conocimiento. Aunque no escribas código, entender conceptos como "commit, branch, merge" te ayudará a gestionar mejor cualquier contenido que necesite "modificaciones repetidas + colaboración entre varias personas" — desde tesis y documentos hasta notas y propuestas.

Para los estudiantes de informática, GitHub es una hábilidad indispensable: es tu portafolio, plataforma de colaboración, repositorio de recursos de aprendizaje, y también el "currículum" más convincente cuando busques empleo en el futuro. Regístrate pronto, sube tus tareas de curso y pequeños proyectos, acumula poco a poco, y en unos años tendrás un historial técnico que deslumbrará a los entrevistadores.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Práctica: completa tu primera experiencia con GitHub

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Regístrate en una cuenta de GitHub, completa tu perfil (avatar, biografía, áreas tecnológicas de interés).
2. Crea un repositorio público llamado<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>, marcando "Add a README file".
3. Entra al repositorio, haz clic en el botón de edición de README.md (icono de lápiz), escribe una presentación personal en Markdown y confirma los cambios.
4. Busca en la barra de búsqueda de GitHub una palabra clave que te interése (por ejemplo<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutoríal</code>) y dale Star a dos proyectos que te gusten.
5. (Intermedio) Instala Git en tu ordenador, clona el repositorio localmente, modifica el README y haz push de vuelta a la nube, completando un flujo de trabajo completo "local → nube".
:::
