---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp1 - Intro to statistics.docx|Chp1 - Intro to statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp1 - Intro to statistics.docx|Chp1 - Intro to statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : vocabulaire de la statistique, types de variables, méthodes d'[[Échantillonnage]] (*sampling*) et pièges à repérer dans une étude.
## Définitions

- **Population** : tous les membres d'un groupe ou d'une catégorie d'intérêt, l'ensemble des sujets étudiés. Voir [[Population et échantillon]].
- **Échantillon** (*sample*) : partie de la population que l'on teste pour en tirer des statistiques.
- **Paramètre** (*parameter*) : valeur réelle sur la population **entière** (exemple du cours : la dépense moyenne en \$ de toute la population), estimée par une statistique. Voir [[Paramètre et statistique]].
- **Statistique** (*statistic*) : la même grandeur calculée sur l'**échantillon** (dépense moyenne de l'échantillon).
- **Variable** : la caractéristique mesurée sur chaque individu, ici la dépense en \$ d'un individu de l'échantillon. [[Erreurs du cours#^e-1-intro-to-statistics|✎]]
- **Données** (*data*) : résultats de l'échantillonnage d'une population.
- **[[Statistique descriptive]]** (*descriptive statistics*) : collecter, présenter et caractériser les données.
- **[[Statistique inférentielle]]** (*inferential statistics*) : estimation, [[Test d'hypothèse|tests d'hypothèse]]… L'humain intervient dans l'interprétation des données.

La statistique descriptive ne parle que des données recueillies ; la statistique inférentielle généralise de l'échantillon à la population, et cette généralisation comporte toujours un risque d'erreur. C'est le hasard du tirage (l'échantillonnage aléatoire, plus bas) qui permet de mesurer ce risque avec les probabilités : marge d'erreur d'un [[Intervalle de confiance|intervalle de confiance]], risque d'un test. Ainsi un paramètre est une constante, en général inconnue, tandis qu'une statistique varie d'un échantillon à l'autre. [[Complément hors du cours|ⓘ]]

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
- **Nominale ou ordinale** : une variable ordinale a des modalités ordonnées (niveau de satisfaction, mention à un examen), une variable nominale n'en a pas (couleur des yeux, pays). Un nombre qui code une catégorie (code postal, numéro de maillot) reste qualitatif : sa moyenne n'a pas de sens. [[Complément hors du cours|ⓘ]]
- **Discrète ou continue** : une variable discrète prend des valeurs isolées que l'on peut compter (nombre d'enfants, de clients par heure) ; une variable continue peut prendre toute valeur d'un intervalle, sa précision n'étant limitée que par l'instrument (taille, durée, masse). [[Complément hors du cours|ⓘ]]
- On classe aussi les variables par **niveau de mesure** (voir [[Type de variable statistique]]) : nominal, ordinal, puis, pour les variables quantitatives, **d'intervalle** (les écarts ont un sens mais le zéro est arbitraire : la température en °C, où 20 °C n'est pas « deux fois plus chaud » que 10 °C) et **de ratio** (zéro absolu, les rapports ont un sens : taille, revenu, température en kelvins). [[Complément hors du cours|ⓘ]]

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

**Strates ou grappes.** Les strates sont faites pour être homogènes à l'intérieur et différentes entre elles : tirer dans chacune garantit que chaque groupe est représenté et rend l'estimation plus précise qu'un tirage simple de même taille. Les grappes, au contraire, doivent ressembler chacune à une petite population (hétérogènes à l'intérieur) ; on les choisit pour des raisons pratiques et de coût (interroger toutes les classes de quelques écoles plutôt que des élèves dispersés), au prix d'une précision moindre si les grappes se ressemblent peu. [[Complément hors du cours|ⓘ]]

Le tirage aléatoire simple et le tirage systématique supposent une **base de sondage** (*sampling frame*) : la liste complète des membres de la population. Le tirage systématique devient biaisé si la liste suit une périodicité qui coïncide avec le pas (un relevé tous les 7 jours tombe toujours le même jour de la semaine). [[Complément hors du cours|ⓘ]]

Les instituts de sondage utilisent souvent la **méthode des quotas**, qui n'est pas aléatoire : l'enquêteur choisit les personnes interrogées de sorte que l'échantillon reproduise la structure de la population sur quelques critères connus (sexe, âge, catégorie socioprofessionnelle, région). Elle est peu coûteuse, mais le calcul probabiliste de la marge d'erreur ne s'y applique pas en toute rigueur. [[Complément hors du cours|ⓘ]]

## Tirage avec ou sans remise

([[Tirage avec et sans remise]])

- Le vrai tirage aléatoire se fait **avec remise** (*with replacement*) : un membre tiré retourne dans la population et peut être choisi plusieurs fois.
- En pratique, le tirage aléatoire simple se fait le plus souvent **sans remise** (*without replacement*) : un membre ne peut être choisi qu'une fois.
- Quand l'échantillon est petit devant la population, les deux reviennent presque au même, car la probabilité de tirer deux fois le même individu avec remise est très faible.
- La différence ne devient un problème mathématique que si la **population est petite**.
- Règle d'usage : on traite un tirage sans remise comme un tirage avec remise (observations indépendantes) tant que l'échantillon représente au plus 5 % de la population, $n/N \le 0{,}05$. Au-delà, l'écart-type de la moyenne d'échantillon se multiplie par le **facteur de correction pour population finie** $\sqrt{(N-n)/(N-1)}$, inférieur à 1 (voir [[Distribution d'échantillonnage]]). [[Complément hors du cours|ⓘ]]
- Nombre d'échantillons possibles de taille $n$ dans une population de taille $N$ : $N^n$ suites ordonnées avec remise, $\binom{N}{n}$ échantillons sans remise et sans ordre ([[Combinaison (dénombrement)]]). Dans un tirage aléatoire simple sans remise, chacun de ces $\binom{N}{n}$ échantillons a la probabilité $1/\binom{N}{n}$. [[Complément hors du cours|ⓘ]]

## Erreurs d'échantillonnage

([[Erreur d'échantillonnage]])

- **Erreur d'échantillonnage** (*sampling error*) : causée par le processus d'échantillonnage lui-même, par exemple un échantillon trop petit.
- **Erreur hors échantillonnage** (*nonsampling error*) : due à des facteurs sans lien avec l'échantillonnage. Exemple : un compteur défectueux.
- **Biais d'échantillonnage** (*sampling bias*) : certains membres de la population ont moins de chances d'être choisis que d'autres. Il peut conduire à des conclusions fausses sur la population.
- L'erreur d'échantillonnage diminue quand la taille de l'échantillon augmente : l'écart-type de la moyenne d'échantillon vaut $\sigma/\sqrt{n}$, si bien qu'il faut quadrupler $n$ pour diviser cette erreur par deux. Un biais, lui, ne diminue pas avec $n$ : un grand échantillon biaisé donne une estimation précise d'une mauvaise valeur. [[Complément hors du cours|ⓘ]]
- Exemple classique : en 1936, le magazine américain *Literary Digest* a recueilli environ 2,4 millions de réponses et prédit la défaite de Roosevelt, réélu largement. Ses listes (abonnés, annuaires téléphoniques, propriétaires de voitures) sur-représentaient les foyers aisés, et seule une partie des personnes sollicitées avait répondu : biais de sélection et de non-réponse, que la taille de l'échantillon n'a pas corrigés. [[Complément hors du cours|ⓘ]]
- Autres erreurs hors échantillonnage fréquentes : erreurs de mesure ou de saisie, questions mal comprises, réponses volontairement inexactes sur des sujets sensibles, non-réponse. [[Complément hors du cours|ⓘ]]

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

**Étude observationnelle ou expérience.** Dans une **étude observationnelle**, on mesure les individus sans intervenir (enquête, suivi d'une cohorte) : elle peut montrer une association, mais un facteur de confusion peut toujours l'expliquer. Dans une **expérience**, on attribue soi-même le traitement ; si l'attribution est tirée au hasard (**randomisation**), les facteurs de confusion, connus ou non, se répartissent en moyenne également entre les groupes, et une différence nette de résultat peut alors s'interpréter comme un effet causal. Voir [[Étude observationnelle et expérience randomisée]]. [[Complément hors du cours|ⓘ]]

Les essais cliniques ajoutent un **groupe témoin** (qui reçoit un placebo ou le traitement de référence) et le **double aveugle** (ni le patient ni le médecin ne savent qui reçoit quoi), pour neutraliser l'effet placebo et l'influence de l'expérimentateur, deux formes de l'*undue influence* ci-dessus. [[Complément hors du cours|ⓘ]]

Deux procédés courants de *misleading use of data* : un axe vertical qui ne part pas de zéro, qui fait paraître énorme une petite différence, et le choix d'une période ou d'un sous-groupe favorable à la conclusion voulue. Le [[Paradoxe de Simpson]] montre aussi qu'une tendance vraie dans chaque groupe peut s'inverser une fois les groupes réunis. [[Complément hors du cours|ⓘ]]

La dernière ligne de l'image est coupée : « Determine if the following samples are representative » ; l'exercice qui suit n'est pas dans la note.
