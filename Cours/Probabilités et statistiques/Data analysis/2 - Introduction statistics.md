---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 2 : Introduction statistics.docx|Cours 2 - Introduction statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 2 : Introduction statistics.docx|Cours 2 - Introduction statistics]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Note courte qui pose le vocabulaire : statistiques descriptives et inférentielles, paramètre et statistique, niveaux de mesure des données.

## Statistiques descriptives et statistiques inférentielles

- **[[Statistique descriptive|Statistiques descriptives]]** (*descriptive statistics*) : les statistiques qui **résument** un **échantillon** de données numériques par des moyennes et d'autres mesures, dans un but de description, par exemple la **moyenne** et l'**[[Espérance et variance|écart-type]]** (*standard deviation*).
- **[[Statistique inférentielle|Inférence statistique]]** (*statistical inference*) : le processus qui **utilise des statistiques d'échantillon** pour **tirer des conclusions** sur des **paramètres de la population**.

La différence tient à l'incertitude : la description ne parle que des données observées, alors que l'inférence généralise à une population qu'on n'a pas observée en entier, et doit donc chiffrer le risque de se tromper. Ses trois outils principaux sont l'estimation ponctuelle ([[Estimateur]]), l'[[Intervalle de confiance]] et le [[Test d'hypothèse]], tous valables seulement si l'échantillon est représentatif, idéalement tiré au hasard ([[Échantillonnage]]). [[Complément hors du cours|ⓘ]]

### Paramètre et statistique

Voir [[Paramètre et statistique]] et [[Population et échantillon]].

- **Paramètre** ⇒ décrit la **population** (exemple : la moyenne $\mu$).
- **Statistique** ⇒ décrit l'**échantillon** (exemple : la [[Moyenne empirique|moyenne d'échantillon]] $\bar{X}$).
- Par convention, les paramètres s'écrivent en lettres grecques et les statistiques en lettres latines ou avec un chapeau : moyenne $\mu$ et $\bar{x}$, écart-type $\sigma$ et $s$, proportion $p$ et $\hat{p}$, corrélation $\rho$ et $r$. [[Complément hors du cours|ⓘ]]
- Un paramètre est un nombre fixe mais inconnu ; une statistique est connue mais **aléatoire** : elle change d'un échantillon à l'autre, et sa loi s'appelle la [[Distribution d'échantillonnage|distribution d'échantillonnage]]. Une statistique utilisée pour approcher un paramètre est un [[Estimateur|estimateur]] ($\bar{X}$ estime $\mu$). [[Complément hors du cours|ⓘ]]

## Types de données

Voir [[Type de variable statistique]].

| Famille | Niveau | Propriété clé | Statistiques appropriées |
|---|---|---|---|
| Catégoriel / qualitatif (*categorical / qualitative*) | Nominal | classification uniquement | mode, fréquences |
| Catégoriel / qualitatif | Ordinal | classification + ordre | médiane (en plus du mode) |
| Numérique / quantitatif (*numerical / quantitative*) | Intervalle | ordre + écart significatif | moyenne (en plus de la médiane) |
| Numérique / quantitatif | Ratio | écart + zéro absolu | toutes (moyenne, médiane, mode, [[Coefficient de variation|CV]]…) |

Chaque niveau hérite des statistiques du niveau précédent et en ajoute une.

Exemples pour chaque niveau : [[Complément hors du cours|ⓘ]]
- **nominal** : couleur des yeux, groupe sanguin, code postal (un nombre qui sert d'étiquette ne se moyenne pas) ;
- **ordinal** : niveau de satisfaction (« pas du tout » à « tout à fait »), mention au bac ; l'ordre a un sens, pas l'écart entre deux rangs ;
- **intervalle** : température en degrés Celsius, année du calendrier ; le zéro est conventionnel, donc les rapports n'ont pas de sens (20 °C n'est pas « deux fois plus chaud » que 10 °C) ;
- **ratio** : taille, masse, revenu, durée, température en kelvins ; le zéro signifie l'absence de la grandeur, donc « deux fois plus » a un sens.

C'est pour cela que le [[Coefficient de variation|CV]] $= s / \bar{x}$ demande une échelle de ratio : sur une échelle d'intervalle, il change quand on déplace le zéro (passer des degrés Celsius aux degrés Fahrenheit change le CV, pas la dispersion réelle). [[Complément hors du cours|ⓘ]]

Cette classification en quatre niveaux vient du psychologue Stanley Smith Stevens (article « On the Theory of Scales of Measurement », *Science*, 1946). [[Complément hors du cours|ⓘ]]

Les variables quantitatives se divisent aussi en **discrètes**, qui prennent des valeurs isolées qu'on peut compter (nombre d'enfants, de clics), et **continues**, qui peuvent prendre toute valeur d'un intervalle (taille, temps) ; ce choix commande la représentation (diagramme en bâtons ou [[Histogramme|histogramme]]) et le modèle de probabilité (loi discrète ou à densité). Une variable qualitative à deux modalités (oui/non) est dite **binaire** ou dichotomique ; on la code souvent 0/1 ([[Variable indicatrice]]). [[Complément hors du cours|ⓘ]]
