---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Chapitre 63 : Vues, états et navigation
toc: default
kind: chapter
---

### Chapitre 63 : Vues, états et navigation

{class="chapter-intro mb-4"}
Tu sais déjà fabriquer le jouet à une seule page. Ce chapitre résout deux problèmes de « croissance » : comment sauter de page en page (la navigation) et comment les données circulent d'une page à l'autre (la gestion d'état). Au terme du chapitre, tu sauras bâtir le squelette classique d'une App multi-pages : « liste → détail → édition ».

#### 1. Le panorama du flux de données pour la gestion d'état

SwiftUI ne se limite pas à @State pour gérer l'état. Regarde d'abord ce panorama pour comprendre « lequel employer, et quand » :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Outil</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qu'il gère</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Portée</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cas typiques</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">État temporaire privé de la page</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La vue courante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compteur, texte d'un champ de saisie</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Emprunter l'état d'un autre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Une vue fille modifie la vue mère</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Composant personnalisé</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logique partagée entre les pages</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Modèle de vue (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chargement de données, logique métier</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">État partagé à l'échelle globale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toute l'App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Session de l'utilisateur, réglages du thème</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panorama des outils d'état de SwiftUI (en 2026, @Observable est devenu la norme)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Le standard 2026 : view models avec @Observable</span><span class="dots">···</span>
:::

```
// la façon moderne d'iOS 17+ : la macro @Observable (recommandée pour les nouveaux projets)
import Observation

@Observable
class CounterModel {                 // le view model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // détient le modèle

    var body: some View {
        VStack {
            Text("Tu as cliqué \(model.count) fois")
            Button("Appuie ici") { model.increment() }
        }
    }
}
```
:::

Conseil brutal pour débutant : @State pour ce qui reste privé à une page, une classe @Observable pour ce qui traverse les pages ou porte de la logique. Le @StateObject/@ObservableObject des anciens tutos, c'est la génération d'avant : sache simplement le lire, et écris le nouveau code comme indiqué ci-dessus.

#### 2. NavigationStack : la « pile » des sauts de page

Depuis iOS 16, la navigation multi-pages passe par NavigationStack — comme une pile d'assiettes : on en pousse une après l'autre, et au retour on les dépile une à une :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigation avec NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Le registre de Léa") {
                    DetailView(name: "Le registre de Léa")   // page cible
                }
                NavigationLink("Le registre d'Emma") {
                    DetailView(name: "Le registre d'Emma")
                }
            }
            .navigationTitle("Liste des registres")   // grand titre en haut
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Détails de \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink, c'est le « lien de navigation cliquable » ; navigationTitle fabrique tout seul le titre de la barre de navigation et le bouton retour. Pour naviguer par le code (par exemple revenir en arrière automatiquement après un « Enregistrer »), emploie @Environment(\.dismiss) pour fermer la page courante — avec ces deux tours, 90 % des besoins de navigation sont couverts.

#### 3. Fenêtres modales et onglets : sheet et TabView

En dehors de « pousser une page », il existe deux interactions classiques :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Dialogues sheet + onglets avec TabView</span><span class="dots">···</span>
:::

```
// 1. feuille qui monte du bas, demi-écran ou plein écran (la chouchou des formulaires)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Ajouter une dépense") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // l'écran de saisie qui s'ouvre
            }
    }
}

// 2. barre d'onglets en bas (le "squelette" de l'app)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Registre", systemImage: "book") }
            StatsView()
                .tabItem { Label("Stats", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Réglages", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : laquelle choisir, et quand ?

{class="mt-1"}
Règle d'expérience : NavigationStack pour pousser les pages du parcours principal (liste → détail), sheet pour les fenêtres temporaires (ajout, édition, confirmation), TabView pour les grandes sections de même rang (onglets en bas). Combinés, les trois forment le squelette de l'immense majorité des Apps.
:::

#### 4. List : la liste incontournable d'iOS

Sur iOS, le composant le plus employé et le plus « pomme » qui soit, c'est List — il apporte d'origine séparateurs, suppression par glissement et surbrillance au tap :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Listes avec List + suppression par glissement</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Déjeuner 25.5", "Métro 6.0", "Salaire +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // glisse vers la gauche pour supprimer
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Liste + NavigationLink + sheet + TabView — combine ces quatre ingrédients et tu peux déjà monter le squelette complet d'une App : « liste du carnet → ouvrir le détail → taper + pour faire apparaître la saisie ». C'est exactement ainsi que sera monté le projet carnet de comptes du chapitre suivant.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : construis un « squelette à trois pages »

#### 5. Cycle de vie de l'App : premier plan et arrière-plan

Comme le cycle de vie des Activity sur Android, une App iOS traverse les états « naissance, premier plan, arrière-plan, mort ». En SwiftUI, observe-les avec la valeur d'environnement scenePhase :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Observer le passage premier/arrière-plan</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("retour au premier plan : reprendre le rafraîchissement")
            case .inactive:  print("en transition (appel ou instant de passage en arrière-plan)")
            case .background: print("passe en arrière-plan : enregistrer le brouillon")
            @unknown default: break
            }
        }
    }
}
```
:::

Usages typiques : rafraîchir les données au retour au premier plan, enregistrer le brouillon en passant en arrière-plan. iOS encadre très strictement l'exécution en arrière-plan — une App ordinaire est vite suspendue (gelée) après y être passée ; n'espère pas y trimer en cachette. Pour une vraie tâche programmée, passe par les notifications locales du chapitre 68 plutôt que par la « résidence permanente en arrière-plan ».

{class="mt-1"}
Réalise la version à fausses données du squelette du carnet de comptes : TabView à trois onglets (Carnet / Stats / Réglages) → la page Carnet affiche des fausses données dans une List, un tap sur une ligne ouvre le détail (NavigationStack) → le bouton « + » en haut à droite fait surgir la saisie en sheet. Aucune sauvegarde, aucun réseau : on ne fait que muscler le squelette — une fois celui-ci au point, remplir de vraies données au chapitre 65 coulera de source.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Quatre outils d'état : @State (privé à la page), @Binding (emprunt), @Observable (logique), .environment (global)
- Pour un nouveau projet, écris les view models avec la macro @Observable ; l'ancien @ObservableObject des vieux tutos, sache juste le lire
- NavigationStack pousse les pages ; @Environment(\.dismiss) revient en arrière par le code
- Parcours principal en pages poussées, actions temporaires en sheet, grandes sections de même rang en TabView
- List est la liste incontournable : séparateurs et suppression par glissement prêts à l'emploi
:::
