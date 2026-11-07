---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp1 - Intro to statistics.docx|Chp1 - Intro to statistics]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Statistics/Chp1 - Intro to statistics.docx|Chp1 - Intro to statistics]], dans [[Statistics (index)]] : vocabulaire de la statistique, types de variables, méthodes d'[[Échantillonnage]] (*sampling*) et pièges à repérer dans une étude. En cas d'écart, le cours et ses images font foi.

## Définitions

- **Population** : tous les membres d'un groupe ou d'une catégorie d'intérêt, l'ensemble des sujets étudiés. Voir [[Population et échantillon]].
- **Échantillon** (*sample*) : partie de la population que l'on teste pour en tirer des statistiques.
- **Paramètre** (*parameter*) : valeur réelle sur la population **entière** (exemple du cours : la dépense moyenne en \$ de toute la population), estimée par une statistique. Voir [[Paramètre et statistique]].
- **Statistique** (*statistic*) : la même grandeur calculée sur l'**échantillon** (dépense moyenne de l'échantillon).
- **Variable** : selon la note, « la dépense d'un individu de l'échantillon » (voir les points à vérifier).
- **Données** (*data*) : résultats de l'échantillonnage d'une population.
- **[[Statistique descriptive]]** (*descriptive statistics*) : collecter, présenter et caractériser les données.
- **[[Statistique inférentielle]]** (*inferential statistics*) : estimation, [[Test d'hypothèse|tests d'hypothèse]]… L'humain intervient dans l'interprétation des données.

## Variables

- **Univariée** (*univariate data set*) : observations d'une seule variable $(x_1, x_2, x_3, \dots)$.
- **Bivariée** (*bivariate data*) : observations de deux variables $(x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)$.
- **Multivariée** (*multivariate data*) : plus de deux variables $(x_1, y_1, z_1, \dots), (x_2, y_2, z_2, \dots)$.

### Types de variables

![[Chp1 - Intro to statistics - image7.png]]

*Figure : arbre « Types of variables » : qualitative (nominale ou ordinale) et quantitative (continue ou discrète).*

([[Type de variable statistique]])

| Catégorielle ou nominale (*qualitative information*) | Numérique (*quantitative information*, résultat d'une mesure) |
|---|---|
| Nominale (non ordonnée) ou ordinale | Continue ou discrète |
| On ne peut **pas** leur appliquer d'opérations arithmétiques : une moyenne n'a pas de sens | On peut leur appliquer des **opérations arithmétiques** : additionner, soustraire, faire la moyenne… |

- Les **data** sont les valeurs effectives de la variable : nombres ou mots. Un **datum** est une seule valeur.

## Échantillonnage

Un échantillon doit avoir les mêmes caractéristiques que la population qu'il représente.

**Échantillonnage aléatoire** (*random sampling*) : chaque membre de la population a au départ la même chance d'être choisi. Cela introduit les probabilités dans le cadre d'étude.

| Méthode | Principe |
|---|---|
| Aléatoire simple (*simple random sampling*) | Tout échantillon de même taille a la même chance d'être choisi |
| Stratifié (*stratified sampling*) | On divise la population en groupes, les **strates**, et on prend dans chacune un nombre **proportionnel** d'individus (tirage aléatoire simple dans chaque strate) |
| Par grappes (*cluster sampling*) | On divise la population en grappes et on tire au hasard quelques grappes ; tous leurs membres forment l'échantillon |
| Systématique (*systematic* ou *interval sampling*) | Point de départ aléatoire, puis un élément sur $n$ dans une liste de la population ; souvent choisi pour sa simplicité |
| De convenance (*convenience sampling*) | On prend l'échantillon qui nous arrange : il est **biaisé** |

![[Chp1 - Intro to statistics - image1.png]]

*Figure : stratifié contre grappes : deux strates homogènes (hommes, femmes) où l'on tire des individus selon la distribution de la population, contre six grappes hétérogènes dont on tire des grappes entières.*

## Tirage avec ou sans remise

([[Tirage avec et sans remise]])

- Le vrai tirage aléatoire se fait **avec remise** (*with replacement*) : un membre tiré retourne dans la population et peut être choisi plusieurs fois.
- En pratique, le tirage aléatoire simple se fait le plus souvent **sans remise** (*without replacement*) : un membre ne peut être choisi qu'une fois.
- Quand l'échantillon est petit devant la population, les deux reviennent presque au même, car la probabilité de tirer deux fois le même individu avec remise est très faible.
- La différence ne devient un problème mathématique que si la **population est petite**.

## Erreurs d'échantillonnage

([[Erreur d'échantillonnage]])

- **Erreur d'échantillonnage** (*sampling error*) : causée par le processus d'échantillonnage lui-même, par exemple un échantillon trop petit.
- **Erreur hors échantillonnage** (*nonsampling error*) : due à des facteurs sans lien avec l'échantillonnage. Exemple : un compteur défectueux.
- **Biais d'échantillonnage** (*sampling bias*) : certains membres de la population ont moins de chances d'être choisis que d'autres. Il peut conduire à des conclusions fausses sur la population.

## Évaluation critique

([[Évaluation critique d'une étude statistique]])

Il faut évaluer les études statistiques de façon critique avant d'accepter leurs résultats. Problèmes courants (texte relu sur l'image) :

- **Problems with samples** : un échantillon doit être représentatif ; sinon il est biaisé, et ses résultats sont inexacts et non valides.
- **Self-selected samples** : les réponses des seules personnes qui choisissent de répondre (sondages par appel, *call-in surveys*) sont souvent peu fiables.
- **Sample size issues** : un échantillon trop petit peut être peu fiable ; plus grand vaut mieux si possible. Parfois un petit échantillon est inévitable et reste utilisable : crash tests de voitures, essais médicaux sur des maladies rares.
- **Undue influence** : recueillir les données ou poser les questions d'une manière qui influence la réponse.
- **Non-response or refusal of subject to participate** : les réponses peuvent ne plus être représentatives ; souvent, seules les personnes aux opinions très positives ou très négatives répondent.
- **Causality** : une relation entre deux variables ne veut pas dire que l'une cause l'autre ; elles peuvent être corrélées à cause d'une autre variable. Voir [[Corrélation et causalité]].
- **Self-funded or self-interest studies** : étude menée pour appuyer sa propre thèse. Est-elle impartiale ? La lire attentivement, ne la présumer ni bonne ni mauvaise, la juger sur ses mérites.
- **Misleading use of data** : graphiques mal présentés, données incomplètes, manque de contexte.
- **Confounding** : les effets de plusieurs facteurs sur une réponse ne peuvent pas être séparés, ce qui rend difficile ou impossible de conclure sur chacun.

La dernière ligne de l'image est coupée : « Determine if the following samples are representative » ; l'exercice qui suit n'est pas dans la note.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition de « variable »** : la note écrit « variable = average of \$ spent per one individual in the sample », ce qui décrit une valeur individuelle, pas une moyenne. Une variable est la caractéristique mesurée, et ses valeurs sont les data (complément).
2. **Encadré « Critical Evaluation »** : sa transcription est un résumé, non le texte complet, et sa dernière ligne est coupée (« Determine if the following samples are representative »). Image non ouverte, le détail est à vérifier sur l'image.
   Mise à jour du 2026-11-06 : l'image a été ouverte pour cette fiche, et la liste détaillée de la section « Évaluation critique » vient de l'image elle-même.
3. **Début d'image coupé** : le mot « population. » tronqué en haut du schéma des types de variables n'enlève rien au sens.
