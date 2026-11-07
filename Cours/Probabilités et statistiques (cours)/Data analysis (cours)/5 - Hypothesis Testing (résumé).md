---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 5 : Hypothesis Testing .docx|Cours 5 - Hypothesis Testing]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 5 : Hypothesis Testing .docx|Cours 5 - Hypothesis Testing]], dans [[Data analysis (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un test d'hypothèse décide, à partir d'un échantillon, si une affirmation sur un paramètre est crédible. Le cours donne le principe, les erreurs possibles, la procédure en six étapes et la façon de poser $H_0$ et $H_1$.

## Le test d'hypothèse

Le [[Test d'hypothèse]] est une démarche statistique qui permet de prendre une décision sur une population à partir d'un échantillon.

- Si une **affirmation** (*claim*) est faite sur un paramètre, on fait un **test d'hypothèse**.
- Si **aucune affirmation** n'est faite et qu'une entreprise veut utiliser l'échantillon pour **estimer** un paramètre (par exemple pour savoir quelles affirmations elle pourra faire plus tard), on construit un **[[Intervalle de confiance|intervalle de confiance]]**.

### 1. Le principe de décision

- On émet une hypothèse sur la valeur d'un paramètre (moyenne, proportion…).
- On la compare aux faits fournis par l'échantillon (la statistique).
- Question clé : l'écart entre la valeur observée et l'hypothèse est-il dû au **hasard** ou est-il **significatif** ?
  - écart significatif → on **rejette** l'hypothèse ;
  - sinon → on **ne peut pas rejeter** l'hypothèse.

### 2. Les deux types d'hypothèses

| Hypothèse | Nom | Rôle |
|---|---|---|
| $H_0$ | Hypothèse nulle | Contient la valeur du paramètre testée. C'est le point de référence. |
| $H_1$ | Hypothèse alternative | N'est « acceptée » que si l'on prouve que $H_0$ est fausse. |

### 3. La nuance technique importante

**On n'accepte jamais $H_0$.** Si le test ne permet pas de la rejeter, on dit qu'on « n'a pas de preuves suffisantes pour la rejeter ». Comme dans un procès : un accusé déclaré « non coupable » faute de preuves n'est pas pour autant prouvé innocent.

## Les deux types d'erreurs

Voir [[Erreur de type I et de type II]].

| Décision \\ État de la nature | $H_0$ vraie | $H_0$ fausse |
|---|---|---|
| Ne pas rejeter $H_0$ | correct | erreur $\beta$ (type II) |
| Rejeter $H_0$ | erreur $\alpha$ (type I) | correct |

### Le compromis (*trade-off*)

- **Si on diminue $\alpha$** : on devient très prudent avant de rejeter $H_0$, donc on risque davantage de « garder » $H_0$ alors qu'elle est fausse : **$\beta$ augmente**.
- **Si on diminue $\beta$** : on veut ne pas rater une $H_0$ fausse, on devient plus sévère, ce qui augmente le risque de rejeter $H_0$ à tort : **$\alpha$ augmente**.

Quand une erreur diminue, l'autre augmente nécessairement.

### Analogie avec les intervalles de confiance

On voudrait idéalement un intervalle très étroit avec une confiance très élevée. C'est impossible : pour augmenter la confiance, il faut élargir l'intervalle. Il faut toujours choisir un compromis acceptable selon la situation.

## Procédure du test d'hypothèse

1. **Formuler $H_0$ et $H_1$** : par exemple $H_0 : \mu = 12{,}7$ ans, $H_1 : \mu \neq 12{,}7$ ans (le signe est perdu dans la note, voir Points à vérifier).
2. **Fixer le [[Seuil de signification|seuil de signification]] $\alpha$** : la probabilité de rejeter $H_0$ alors qu'elle est vraie, en général **0,05** ou **0,01**.
3. **Choisir la [[Statistique de test|statistique de test]]** : la loi $Z$ ([[Test Z]]), ou la loi $t$ pour les petits échantillons ([[Test t]]).
4. **Établir la [[Valeur critique|valeur critique]]** : le seuil à partir duquel on rejette $H_0$. Conseil : **toujours dessiner la courbe** pour visualiser les zones de rejet.
5. **Calculer la valeur réelle** de la statistique à partir des données de l'échantillon.
6. **Décider** : rejeter $H_0$, ou ne pas la rejeter.

## Test unilatéral ou bilatéral (*one tail / two tail*)

En formulant $H_0$ et $H_1$, il faut choisir un test unilatéral ou bilatéral ([[Test unilatéral et bilatéral]]).

- **Bilatéral** (*two-tail*) : $\alpha$ est partagé en deux et placé dans les deux queues ; $H_1$ contient deux possibilités ($\mu > \#$ ou $\mu < \#$, c'est-à-dire $\mu \neq \#$). La région de rejet est donc divisée en deux queues.
- La **région de rejet correspond toujours à $H_1$**.
- **Unilatéral** (*one-tail*) : $\alpha$ est entièrement dans une des queues.

**Exemples** :

- Une entreprise affirme qu'un produit contient **exactement** 1 mg d'aspirine : test **bilatéral**. Des mots comme « exactement » suggèrent un test bilatéral : trop ou trop peu d'aspirine pose problème.
- Une entreprise affirme qu'une boîte de céréales contient **au moins** 100 raisins : test **unilatéral**. Si la [[Moyenne empirique|moyenne d'échantillon]] dépasse 100, tout va bien ; le problème n'apparaît que si elle est inférieure à 100.

## Poser $H_0$ et $H_1$

- Principe fondamental : il est beaucoup plus facile de prouver qu'une chose est fausse que de prouver qu'elle est vraie.
- But du test : savoir si les données de l'échantillon apportent des preuves solides **contre** $H_0$.

### A. Prouver son affirmation

Une entreprise qui veut prouver sa propre affirmation (conformité, publicité, pureté du produit) la place dans **$H_1$**.

- Pourquoi ? Le coût d'une erreur est élevé : on veut des preuves solides avant d'affirmer que le produit est conforme.
- Conséquence : si les résultats ne sont pas statistiquement significatifs, on ne peut pas rejeter $H_0$ et les données sont jugées non concluantes.

### B. Contredire un concurrent

Si le test est fait par un organisme de contrôle ou un concurrent pour contester une affirmation, celle-ci est placée dans **$H_0$**. Si $H_0$ est rejetée, l'affirmation est réputée réfutée.

## Les outils du test

- **Statistique de test** : variable aléatoire calculée à partir de l'échantillon pour décider du rejet de $H_0$ ; elle compare les données à ce qui est attendu sous $H_0$.
- **[[P-value]]** : probabilité d'obtenir les résultats observés (ou plus extrêmes) si $H_0$ est vraie.

| Type de test | Statistique de test |
|---|---|
| [[Test Z\|z-test]] | statistique z |
| [[Test t\|t-test]] | statistique t |
| [[ANOVA]] | [[Statistique F\|statistique F]] |
| [[Test du χ²\|test du khi-deux]] | statistique χ² |

## Vraisemblance (*likelihood*) et probabilité

| Concept | Direction de l'analyse | Ce qui est fixe |
|---|---|---|
| Probabilité | des paramètres vers les données | le paramètre (ex. : $\mu = 8$ \$) |
| [[Vraisemblance]] | des données vers les paramètres | les données observées (ex. : $\bar{X} = 7{,}6$ \$) |

Dans un test, on utilise la probabilité (la p-value) pour juger de la **vraisemblance** de $H_0$ : si la probabilité est minuscule, l'hypothèse n'est plus vraisemblable et on la rejette.

- **La probabilité** : « si je connais la règle, que va-t-il se passer ? » Elle regarde vers l'avenir : on suppose connue la vérité sur la population, et on calcule la chance des données à partir d'un paramètre connu.
- **La vraisemblance** : « si j'ai ce résultat, quelle était la règle ? » Elle regarde vers le passé : on a le résultat de l'échantillon et on évalue la crédibilité du paramètre (l'affirmation) à partir des données.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les deux images (arbre de décision et tableau des erreurs) n'ont pas été ouvertes.

1. **Symboles manquants** : la note écrit « $H_1$ : $\mu = 12{,}7$ » et, pour le bilatéral, « $\mu = \#$ ou $\mu \ne \#$ ». Le texte converti a perdu les signes : il faut lire $H_1 : \mu \ne 12{,}7$, et $\mu > \#$ ou $\mu < \#$ (complément).
2. **Exemple unilatéral des raisins** : seule une moyenne d'échantillon inférieure à 100 pose problème, donc $H_1 : \mu < 100$ et la zone de rejet est à gauche. Le cours ne l'écrit pas ainsi (complément).
