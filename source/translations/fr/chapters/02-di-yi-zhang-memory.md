---
id: di-yi-zhang-memory
part: ji-chu-pian
nav:  Annexe : analyse de l'extension de mémoire Android
toc: sub
kind: supplement
---

### Annexe : analyse de l'extension de mémoire Android

{class="chapter-intro mb-4"}
Lors de l'achat d'un smartphone, vous voyez souvent la publicité « 12 Go + 8 Go RAM » — comme si 8 Go de RAM apparaissaient par magie. Mais cela rend-il vraiment le smartphone plus rapide ? Et ne risque-t-il pas d'abîmer le smartphone ? Dans cette section, nous allons expliquer à fond la technologie « d'extension de mémoire ».

#### I. Définition essentielle

L'« extension de mémoire » Android (aussi appelée extension de RAM, fusion de mémoire, RAM Plus, etc.)<strong>n'ajoute pas physiquement de puce de RAM</strong>, mais est une technologie logicielle au niveau système : elle convertit dynamiquement une partie du stockage interne (ROM/flash UFS) pour simuler une RAM virtuelle.

Pour ainsi dire : la RAM physique est le « plan de travail rapide », la mémoire étendue est le « débarras temporaire ». Quand le plan de travail est insuffisant, le système déplace les données inutilisées vers le débarras, et les ramène quand nécessaire. Le débarras est grand, mais l'aller-retour est forcément plus lent que de laisser sur le plan de travail.

#### II. Principe technique

Les principaux fabricants l'implémentent principalement de deux façons :

##### 1. Compression zRAM

Divise un espace de données compressées dans la RAM, compresse le code d'applications inactives, taux de compression d'environ 2:1. Les données restent dans la RAM, rapides, sans user la flash, mais le CPU participe à la compression/décompression.

##### 2. Partition swap

Divise directement un espace fixe dans la flash UFS comme mémoire virtuelle, écrit les données des processus en arrière-plan dans le stockage. Dépend de la bande passante de stockage, vitesse de lecture/écriture bien inférieure à la mémoire physique.

La publicité « 12 Go + 8 Go RAM » est généralement une combinaison de 12 Go de RAM physique + 8 Go de mémoire virtuelle flash. À noter, zRAM n'occupe pas par défaut le stockage interne ; ce n'est que lorsque zRAM est complètement rempli de données que le système crée un fichier d'échange sur le stockage, et cette situation est extrêmement rare.

#### III. L'écart de vitesse est le goulot clé

La limite fondamentale de cette technologie réside dans l'écart de vitesse. La flash UFS 4.0 actuelle a une vitesse de lecture séquentielle d'environ 4200 Mo/s, soit seulement 1/10 à 1/15 de la mémoire physique LPDDR5X. Ainsi, pendant la phase de compression zRAM à faible charge, la vitesse est proche de la RAM réelle, mais dès qu'on entre dans des scénarios de forte charge, la vitesse chute à quelques dizaines de fois moins.

#### IV. Scénarios applicables et limites des bénéfices

L'extension de mémoire n'est pas universelle, l'effet varie selon le modèle et le scénario d'utilisation :

- <strong>Cas utiles</strong>: modèles avec 6 Go de RAM physique + UFS 3.1 ou supérieur et espace libre ≥ 30 Go ; après activation d'une extension de 3 Go, le nombre d'apps maintenues en arrière-plan augmente de 3-4, le taux de rechargement baisse de 68 %, adapté aux livreurs et chauffeurs VTC, utilisateurs intensifs de multitâche.
- <strong>Scénarios quotidiens</strong>: amélioration notable pour le multi-comptes WeChat, le maintien des onglets de navigateur, la réactivité des messages de messagerie instantanée, le temps de démarrage à froid des apps en arrière-plan considérablement réduit.
- <strong>Scénarios limités</strong>: amélioration limitée pour le chargement de gros jeux, le montage vidéo 4K et autres scénarios à forte bande passante.
- <strong>Cas nuisibles</strong>: modèles avec 8 Go de RAM + UFS 2.2 et espace libre insuffisant ; après activation, les fluctuations de fréquence d'images du jeu s'aggravent, la consultation de courtes vidéos consomme plus de batterie, le basculement saccade.
- <strong>Cas inutiles</strong>: les modèles avec plus de 16 Go de RAM n'en tirent presque aucun bénéfice, maintiennent au mieux une app supplémentaire en arrière-plan, mais augmentent la charge CPU de 12 % et la chaleur de 2-3 °C. Pour les modèles avec plus de 12 Go de RAM, il est recommandé de désactiver pour éviter des calculs de compression inutiles.

#### V. Dénomination et activation par fabricant

Les marques l'appellent différemment : Xiaomi « extension de mémoire », Huawei « fusion de mémoire », Samsung « RAM Plus », vivo « Extended RAM », OnePlus « Memory Extension ». Cette fonction est une capacité native du système, sans lien direct avec la version sous-jacente d'Android.

Le chemin d'activation général : [Réglages] → [Plus de réglages] → trouver la sous-section [Mémoire] ou [Performance] → activer « extension de mémoire » et choisir le palier de capacité (généralement 2 Go-7 Go), redémarrer pour prendre effet. Après activation, le système affiche une combinaison de mémoire telle que « 8 Go + 4 Go ».

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Précautions

{class="list-disc pl-6 mt-1 space-y-1"}
- L'extension de mémoire occupe une partie du stockage interne, veillez à ce qu'il reste au moins 20-30 Go, sinon la fluidité du système peut être affectée.
- La flash utilisée comme mémoire virtuelle subit une usure de lecture/écriture ; bien que la flash UFS moderne ait une longue durée de vie, un swap intense à long terme peut accélérer le vieillissement du stockage.
- Si la RAM physique du smartphone est faible (4 Go ou moins), l'extension de mémoire ne fait que soulager une urgence, sans résoudre fondamentalement le problème de lag.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Résumé

{class="mt-1"}
L'extension de mémoire est une technologie d'optimisation au niveau système mature, qui peut améliorer les capacités de multitâche et le maintien en arrière-plan des modèles milieu et entrée de gamme sans modifier le matériel, mais elle est limitée par le fossé de vitesse entre flash et RAM physique, et n'est pas une « panacée ». L'activer ou non, et à quel niveau, dépend de la taille de la RAM physique, de la spécification de flash, de l'espace de stockage libre et des habitudes d'utilisation.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>À vous de jouer : vérifiez si votre smartphone a l'extension de mémoire

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ouvrez [Réglages], recherchez « extension de mémoire », « fusion de mémoire », « RAM Plus » ou « Extended RAM ».
2. Une fois trouvé, vérifiez si c'est activé actuellement et quel est le réglage de capacité étendue.
3. Selon cette section, évaluez : quelle est la taille de RAM physique de votre modèle ? Quelle est la spécification de flash ? L'espace de stockage libre est-il suffisant ?
4. Essayez de désactiver ou de réduire la capacité étendue, observez pendant une semaine l'évolution du maintien en arrière-plan et de la chauffe, pour trouver le réglage qui vous convient le mieux.
:::
