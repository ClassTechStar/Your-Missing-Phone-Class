---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Usa el emisor infrarrojo como mando a distancia
toc: sub
kind: supplement
---

### Anexo del Capítulo 20: Termux, un entorno de terminal Linux portátil en dispositivos Android

{class="chapter-intro mb-4"}
Si crees que el modo desarrollador no es suficientemente "hardcore" y quieres experimentar con una linea de comandos Linux completa en tu móvil, Termux es para ti. No necesita permisos Root y puede convertir un Android común en una estacion de trabajo Linux portátil; es una herramienta poderosa para usuarios intermedios que exploran desarrollo y operaciones móviles.

#### I. Que es Termux

Termux es un emulador de terminal y entorno Linux de código abierto disenado para Android. No necesita permisos Root para ofrecer una experiencia completa de shell Linux en el móvil. Como App ligera (unos 30 MB), Termux soporta un rico ecosistema de software via gestor de paquetes APT, permitiendo ejecutar Python, Node.js, Git, SSH e incluso montar servidores o hacer pruebas de penetracion.

La ventaja principal de Termux es su ligereza y alta escalabilidad, adecuada para desarrollo, aprendizaje y administración de sistemas. Combina paquetes estándar con emulación de terminal precisa en una solución de código abierto.

#### II. Funciones principales y carácterísticas

##### Entorno Linux completo

Termux <strong>Solo Bash integrado</strong> Este tipo de Shell. Si quieres usar Zsh, fish u otros Shells, necesitas instalarlos manualmente mediante un gestor de paquetes, por ejemplo:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> o<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Además, Termux soporta editores como Vim, Nano, Emacs, ofreciendo una experiencia de línea de comandos casi nativa. Los usuarios pueden instalar más de 2000 paquetes de software mediante "pkg install", incluyendo herramientas de desarrollo y seguridad como GCC, OpenSSH, SQLMap.

##### Gestor de paquetes potente

Usa el gestor de paquetes APT (similar a Debian/Ubuntu) para instalar miles de paquetes Linux: herramientas de desarrollo, red, etc. Soporta Python, Ruby, Node.js, Go, Rust, Swift y más.

##### 🔒 Funciones de seguridad y red

- <strong>Conexión SSH remota</strong>: Soporta funciones de cliente y servidor SSH; puede conectarse a otros equipos en remoto o convertir el móvil en un host SSH.
- <strong>Herramientas de cifrado</strong>: proporciona herramientas como OpenSSL; soporta cifrado de datos y comunicaciones seguras.
- <strong>Configuración de servidores</strong>: puedes configurar Nginx o Apache para montar servidores web estáticos.

##### Integración del sistema y extensiones

- Accede a los permisos de almacenamiento del móvil para gestionar archivos locales.
- Llamar a sensores, cámara y otras funciones hardware de Android mediante el plugin Termux:API.
- Soporta teclados Bluetooth y pantallas externas, con soporte completo de ratón.

#### III. Ecosistema de plugins

La App principal de Termux se puede ampliar con varias Apps de plugins opcionales, que aportan funciones e integraciones extra:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nombre del plugin</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descripcion de función</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Expone funciones de API de Android a programas de linea de comandos</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permite ejecutar scripts al iniciar el dispositivo</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: Proporciona una ventana de terminal flotante.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Habilita esquemas de color y personalizacion de fuentes para la terminal</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integra scripts de Termux con la App de automatización Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permite ejecutar scripts desde widgets de la pantalla principal</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Nota importante

{class="mt-1"}
Termux y sus plugins deben instalarse desde la misma fuente porque comparten el mismo sharedUserId. Mezclar fuentes (F-Droid y GitHub) causará errores de instalación.
:::

#### IV. Guia de instalación y configuración

##### Pasos de instalación

1. <strong>Descargar App</strong>: Descarga e instala Termux desde canales oficiales (F-Droid o GitHub), sin permisos de root.
2. <strong>Inicializar el sistema</strong>: Tras el primer arranque, espera a que termine «Installing bootstrap packages».
3. <strong>Conseguir el permiso de almacenamiento</strong>: ejecuta<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> para obtener acceso al sistema de archivos del móvil.
4. <strong>Actualizar los repositorios de software</strong>: ejecuta<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> para actualizar la lista de paquetes.

##### Optimizacion básica

- <strong>Cambiar repositorio espejo</strong>:usa el comando<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> para cambiar el repositorio espejo mediante interfaz gráfica (recomendado: mirror de Universidad de Tsinghua).
- <strong>Configuracion de atajos de teclado</strong>: volumen - simula Ctrl, volumen + simula Esc; mejora la eficiencia de entrada.
- <strong>Embellecer interfaz</strong>: instala Zsh + Oh My Zsh, configura temas y plugins.

#### V. Escenarios de uso típicos

##### Desarrollo y pruebas móviles

Construye en el móvil un entorno de desarrollo completo: escribe y ejecuta scripts de Python, compila programas C con GCC, gestiona tus repositorios con Git y sincroniza con servidores remotos por SSH.

##### Administracion de servidores

Gestíona servidores remotamente por SSH: mantenimiento, análisis de logs, etc.; resuelve problemas de servidor desde cualquier lugar.

##### Aprender operaciones Linux

Proporciona un entorno Linux real; plataforma ideal para aprender línea de comandos y administración de sistemas: scripts Shell, permisos de archivos, etc. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> establecer permisos rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> modificar el propietario del archivo,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> ver los tres grupos de nueve bits de permisos owner/group/other) y otros comandos básicos. Ten en cuenta que este es el clásico modelo de permisos "tres grupos, nueve bits" de Unix/Linux (propietario / grupo / otros × leer / escribir / ejecutar), que es un sistema completamente diferente de las listas de control de acceso (ACL) de Windows NTFS.

##### Pruebas de seguridad en red

Instala Nmap, SQLMap, Hydra, Metasploit y otras herramientas de seguridad para escaneo de red y pruebas de penetración.

#### VI. Versiones y compatibilidad

La última versión estable de Termux es v0.118.2, para dispositivos Android &gt;= 7. Nota: Termux puede ser inestable en Android 12+; consulta el registro oficial de cambios para información de compatibilidad.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Resumen

{class="mt-1"}
Termux lleva la potente experiencia de terminal Linux a dispositivos Android, convirtiendo el móvil en una herramienta portátil de desarrollo y aprendizaje. Tanto desarrolladores como administradores o entusiastas pueden disfrutar de una experiencia completa de linea de comandos en dispositivos móviles, realizando la visión de "Linux en el bolsillo".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica: ejecuta tu primer comando Linux en el móvil

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Descarga e instala Termux desde F-Droid; espera la inicializacion al primer inicio.
2. Ejecuta<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> para actualizar los paquetes.
3. Instala Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Escribe<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code> y disfruta ejecutar código en tu móvil.
:::
