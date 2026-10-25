---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav:  Annexe du Chapitre 20
toc: sub
kind: supplement
---

### Chapitre 20 Annexe : Termux — environnement de terminal Linux portable sur appareils Android

{class="chapter-intro mb-4"}
Si vous trouvez le mode développeur pas assez « hardcore » et que vous voulez expérimenter une véritable ligne de commande Linux sur votre smartphone, Termux est fait pour vous. Sans nécessiter de permissions root, il transforme un smartphone Android ordinaire en une station de travail Linux portable, c'est l'outil de choix pour les utilisateurs avancés qui veulent explorer le développement et l'administration système en mobilité.

#### I. Qu'est-ce que Termux

Termux est un émulateur de terminal open source et une application d'environnement Linux conçu pour les appareils Android, qui offre une expérience complète de shell Linux sur smartphone sans nécessiter de permissions root. En tant qu'application légère (environ 30 Mo pour le package d'installation), Termux prend en charge un riche écosystème logiciel via le gestionnaire de paquets APT, permettant aux utilisateurs d'exécuter Python, Node.js, Git, SSH et d'autres outils sur appareil mobile, voire de configurer des serveurs ou de réaliser des tests d'intrusion.

L'avantage principal de Termux réside dans sa légèreté et son extensibilité, adapté à de nombreux scénarios comme le développement, l'apprentissage et l'administration système. Il combine des packages logiciels standards avec une émulation de terminal précise dans une solution open source.

#### II. Fonctions et caractéristiques principales

##### 🖥️ Environnement Linux complet

Termux <strong>Seul Bash est intégré</strong> comme shell. Si vous souhaitez utiliser d'autres shells comme Zsh ou fish, vous devez les installer manuellement via le gestionnaire de paquets, par exemple :<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> ou<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Termux prend également en charge les éditeurs tels que Vim, Nano, Emacs, offrant une expérience en ligne de commande quasi native. Les utilisateurs peuvent installer plus de 2000 paquets via « pkg install », y compris GCC, OpenSSH, SQLMap et d'autres outils de développement et de sécurité.

##### 📦 Gestion de packages puissante

Utilise le gestionnaire de packages APT (similaire à Debian et Ubuntu), peut installer des milliers de packages Linux, couvrant les outils de développement, les outils réseau, etc. Prend en charge plusieurs environnements de langages de programmation comme Python, Ruby, Node.js, Go, Rust, Swift.

##### 🔒 Fonctions de sécurité et réseau

- <strong>Connexion SSH à distance</strong>: prend en charge les fonctions client et serveur SSH, peut se connecter à distance à d'autres appareils ou transformer le téléphone en hôte SSH.
- <strong>Outils de chiffrement</strong>: fournit des outils de chiffrement comme OpenSSL, prend en charge le chiffrement des données et les communications sécurisées.
- <strong>Configuration de serveur</strong>: peut configurer Nginx ou Apache pour mettre en place un serveur web statique.

##### 🔧 Intégration et extension système

- Accès aux permissions de stockage du téléphone pour la gestion locale des fichiers.
- Appel des fonctions matérielles Android comme les capteurs, la caméra via le plugin Termux:API.
- Prise en charge des claviers Bluetooth et des écrans externes, avec support complet de la souris.

#### III. Écosystème de plugins

L'application principale de Termux peut être étendue par plusieurs applications plugins optionnelles, offrant des fonctionnalités et intégrations supplémentaires :

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nom du plugin</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Description de la fonction</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Expose les fonctions de l'API Android aux programmes en ligne de commande</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permet d'exécuter des scripts au démarrage de l'appareil</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fournit une fenêtre de terminal flottante</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Active les schémas de couleurs et la personnalisation des polices pour le terminal</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Intègre les scripts Termux avec l'application d'automatisation Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permet d'exécuter des scripts depuis un widget sur l'écran d'accueil</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Important

{class="mt-1"}
Termux et ses plugins doivent être installés depuis la même source, car ils partagent le même sharedUserId. Mélanger des installations provenant de sources différentes (comme F-Droid et GitHub) entraînera des erreurs d'installation.
:::

#### IV. Guide d'installation et de configuration

##### 📥 Étapes d'installation

1. <strong>Télécharger l'application</strong>: téléchargez et installez Termux depuis les canaux officiels (F-Droid ou GitHub), sans nécessiter de permissions root.
2. <strong>Initialiser le système</strong>: après le premier lancement, attendez que « Installing bootstrap packages » soit terminé.
3. <strong>Obtenir les permissions de stockage</strong>: exécutez<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code> pour obtenir les permissions du système de fichiers du téléphone.
4. <strong>Mettre à jour les sources logicielles</strong>: exécutez<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> pour mettre à jour la liste des packages.

##### ⚙️ Optimisations de base

- <strong>Changer de miroir</strong>: utilisez la commande<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code> pour changer de miroir via une interface graphique (miroir de l'Université Tsinghua recommandé).
- <strong>Configuration des raccourcis clavier</strong>: la touche volume bas simule Ctrl, la touche volume haut simule Esc, améliore l'efficacité de saisie.
- <strong>Embellissement de l'interface</strong>: installez Zsh + Oh My Zsh, configurez les thèmes et plugins.

#### V. Scénarios d'utilisation typiques

##### 💻 Tests de développement mobile

Configurez un environnement de développement complet sur le smartphone, écrivez et exécutez des scripts Python, compilez des programmes C avec GCC, gérez des dépôts de code avec Git, synchronisez avec des serveurs distants via SSH.

##### 🖥️ Administration de serveurs

Gérez à distance des serveurs via SSH, exécutez des tâches de maintenance système, d'analyse de journaux, traitez les problèmes de serveurs à tout moment et en tout lieu.

##### 📚 Apprentissage de Linux

Fournit un véritable environnement Linux, c'est la plateforme idéale pour apprendre la ligne de commande et l'administration système, permettant de s'exercer à la rédaction de scripts shell, à la gestion des permissions de fichiers Linux (par exemple <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> définir les bits de permission rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> modifier le propriétaire du fichier,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> consulter les trois groupes de neuf bits de permissions owner/group/other) et d'autres commandes de base. Notez qu'il s'agit du modèle de permissions classique Unix/Linux « trois groupes, neuf bits » (owner / group / other × lecture / écriture / exécution), qui est un système complètement différent des listes de contrôle d'accès (ACL) de Windows NTFS.

##### 🔐 Tests de sécurité réseau

Installez Nmap, SQLMap, Hydra, Metasploit et autres outils de sécurité, effectuez des scans réseau et des tests d'intrusion.

#### VI. Versions et compatibilité

La dernière version stable de Termux est v0.118.2, compatible avec les appareils Android ≥ 7. À noter que Termux peut présenter des instabilités sur Android 12 et versions ultérieures, il est conseillé de suivre le journal des mises à jour officiel pour obtenir les dernières informations de compatibilité.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Résumé

{class="mt-1"}
Termux apporte l'expérience puissante du terminal Linux sur les appareils Android, transformant le smartphone en un outil de développement et d'apprentissage portable. Que vous soyez développeur, administrateur système ou passionné de technologie, vous pouvez utiliser Termux pour profiter d'une expérience complète en ligne de commande sur appareil mobile, réalisant le concept de « Linux dans la poche ».
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>À faire : exécutez votre première commande Linux sur smartphone

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Téléchargez et installez Termux depuis F-Droid, attendez l'initialisation au premier lancement.
2. Exécutez<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> pour mettre à jour les packages.
3. Installez Python :<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Saisissez<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>, ressentez le plaisir d'exécuter du code sur smartphone.
:::
