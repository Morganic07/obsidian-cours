---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]], dans [[Cours/Informatique/Data mining/_index|Data mining]].

## Idée générale

Le [[Fouille de données|data mining]] ne consiste pas seulement à collecter et ordonner des chiffres, mais aussi à extraire des structures cachées, des corrélations non évidentes et des tendances exploitables de grandes masses de données, en combinant algorithmes, statistiques et [[Intelligence artificielle|intelligence artificielle]]. Le chapitre couvre la classification (k plus proches voisins, validation), le regroupement (k-means, hiérarchique), les arbres de décision (ID3, C4.5, CART) et les combinaisons de modèles (bagging, boosting, forêts aléatoires). Les diapositives sont en anglais, les exemples ajoutés (spam, validation croisée) et la partie « combinaison de modèles » en français.

## 1. Introduction

### Exemple de modèle : un arbre de décision (jeu météo)

| NUM | Outlook | TEMP. | HUMI. | Wind | CLASS |
|---|---|---|---|---|---|
| 1 | sunny | high | strong | no | N |
| 2 | sunny | high | strong | yes | N |
| 3 | overcast | high | strong | no | P |
| 4 | rainy | mild | strong | no | P |
| 5 | rainy | low | normal | no | P |
| 6 | rainy | low | normal | yes | N |
| 7 | overcast | low | normal | yes | P |
| 8 | sunny | mild | strong | no | N |
| 9 | sunny | low | normal | no | P |
| 10 | rainy | mild | normale | no | P |
| 11 | sunny | mild | normal | yes | P |
| 12 | overcast | mild | strong | yes | P |
| 13 | overcast | high | normal | no | P |
| 14 | rainy | mild | strong | yes | N |

![[Chp1 - intro to data mining - image52.png]]
*Figure : le tableau des 14 exemples et l'[[Arbre de décision]] obtenu — racine outlook ; sunny → humidity (high : no, normal : yes) ; overcast → yes ; rainy → windy (false : yes, true : no).*

Un arbre de décision se lit comme un ensemble de règles :
- IF OUTLOOK = sunny & HUMI = strong THEN CLASS = N
- IF OUTLOOK = sunny & HUMI = normal THEN CLASS = P
- IF OUTLOOK = overcast THEN CLASS = P
- IF OUTLOOK = rainy & WIND = yes THEN CLASS = N
- IF OUTLOOK = rainy & WIND = no THEN CLASS = P

### Tâches du data mining et du machine learning

- **Prédictives** : classification, régression, analyse de [[Série temporelle|séries temporelles]] (*time series analysis*), prédiction.
- **Descriptives** : [[Clustering]], résumé (*summarization*), [[Règle d'association|règles d'association]], découverte de séquences (*sequence discovery*).

![[Chp1 - intro to data mining - image38.png]]
*Figure : arbre des tâches, « Data mining » se divisant en « Predictive » et « Descriptive ».*

Les tâches prédictives relèvent de l'[[Apprentissage supervisé|apprentissage supervisé]] : chaque exemple d'apprentissage porte la valeur à prédire (sa classe, la [[Variable cible et variable explicative|variable cible]]). Les tâches descriptives relèvent de l'[[Apprentissage non supervisé|apprentissage non supervisé]] : les exemples n'ont pas d'étiquette et l'on cherche une structure dans les données. La classification prédit une valeur **discrète** (une classe), la régression une valeur **continue** (un prix, une température). [[Complément hors du cours|ⓘ]]

La fouille proprement dite n'est qu'une étape du processus d'**extraction de connaissances à partir des données** (ECD, en anglais *KDD, Knowledge Discovery in Databases*) : sélection des données, [[Prétraitement des données|prétraitement]] (nettoyage, valeurs manquantes), transformation (discrétisation, normalisation, réduction de dimension), fouille, puis interprétation et évaluation des résultats. Le prétraitement occupe en pratique une grande part du travail. [[Complément hors du cours|ⓘ]]

## 2. Classification

Un **[[Classifieur|classifieur]]** est une fonction mathématique ou un algorithme qui prend des caractéristiques en entrée (*features*) et attribue automatiquement une étiquette discrète (une classe) en sortie. C'est lui qui produit les prédictions que l'on évalue ensuite avec la matrice de confusion ([[Validation d'un classifieur]]).

**Types de classifieurs :**
1. construction d'un modèle (un arbre de décision, par exemple) pour prédire la classe cible ;
2. estimation directe de la classe cible en fonction des exemples (k plus proches voisins) ;
3. construction d'un modèle paramétrable ([[Réseau de neurones|réseaux de neurones]], [[Machine à vecteurs de support|machines à vecteurs de support]]).

### K plus proches voisins (*K-Nearest Neighbours*)

Jeu de données à deux attributs numériques $(X_1, X_2)$ et deux classes (A, B). Le point à classer reçoit la classe majoritaire parmi ses $k$ plus proches voisins ([[K plus proches voisins]]).

![[Chp1 - intro to data mining - image33.png]]
*Figure : l'étoile rouge est le point à classer ; avec $k = 3$, 1 point jaune (A) et 2 violets (B) ; avec $k = 6$, 4 jaunes et 2 violets. Le résultat dépend de $k$.*

Le voisinage se mesure avec une [[Distance|distance]], le plus souvent euclidienne. Les k-NN ne construisent aucun modèle (apprentissage dit « paresseux », *lazy learning*) : tout le calcul a lieu au moment de classer, en comparant le point à tous les exemples, ce qui devient coûteux sur de grandes bases. [[Complément hors du cours|ⓘ]]

- **Choix de $k$** : un $k$ petit rend la décision sensible au bruit (un seul voisin mal étiqueté suffit à se tromper) ; un $k$ grand lisse la frontière jusqu'à favoriser la classe majoritaire de toute la base. Avec deux classes, un $k$ impair évite les égalités ; en pratique, on choisit $k$ par validation croisée. [[Complément hors du cours|ⓘ]]
- **Mise à l'échelle** : un attribut aux valeurs grandes (un revenu en euros) écrase dans la distance un attribut aux valeurs petites (un âge) ; on ramène donc les attributs à une même échelle, par [[Centrage et réduction|centrage-réduction]] ou en les ramenant entre 0 et 1. [[Complément hors du cours|ⓘ]]

### Validation d'un classifieur

![[Chp1 - intro to data mining - image15.png]]
*Figure : la base est séparée en données d'entraînement (construction du modèle) et de test ; si la précision est acceptable, le modèle est appliqué à des données inconnues pour prédire leur valeur.*

**Validation 1.**
- L'erreur $Er$ d'un classifieur est la probabilité qu'il ne prédise pas correctement la valeur cible d'une donnée. Le taux de réussite est $1 - Er$.
- L'erreur d'entraînement est mesurée sur l'[[Ensemble d'entraînement et de test|ensemble d'entraînement]] (qui sert à construire le classifieur).
- Pour estimer la qualité, il faut un ensemble d'entraînement $X_{train}$ et un ensemble de test $X_{test}$ (où la valeur cible est connue pour chaque exemple) pour estimer l'erreur.
- L'erreur d'entraînement est optimiste : un modèle assez complexe peut apprendre par cœur ses exemples (erreur d'entraînement nulle) et mal prédire de nouvelles données, c'est le [[Surapprentissage|surapprentissage]] (*overfitting*). Seule l'erreur sur des exemples non vus pendant l'apprentissage estime la capacité de **généralisation**, d'où l'ensemble de test, qui ne doit jamais servir à construire ni à régler le modèle. [[Complément hors du cours|ⓘ]]

**Validation 2 : matrice de confusion.** Pour chaque valeur cible :
- **TP / TN** (vrais positifs / négatifs) : nombre d'exemples positifs / négatifs correctement prédits ;
- **FP / FN** (faux positifs / négatifs) : nombre d'exemples négatifs / positifs prédits positifs / négatifs.

| | + Pred | − Pred |
|---|---|---|
| Real + | TP | FN |
| Real − | FP | TN |

**Validation 3 : quatre mesures**, pour chaque valeur cible :
- **précision** positive $\dfrac{TP}{TP+FP}$ et négative $\dfrac{TN}{TN+FN}$ : proportion de vrais positifs parmi les exemples classés positifs ;
- **rappel** (*recall*) positif $\dfrac{TP}{TP+FN}$ et négatif $\dfrac{TN}{TN+FP}$ : proportion des positifs retrouvés parmi tous les positifs.
- **exactitude** (*accuracy*), ou taux de réussite global : $\dfrac{TP+TN}{TP+TN+FP+FN}$, soit $1 - Er$ ; c'est la diagonale de la matrice rapportée au total. [[Complément hors du cours|ⓘ]]
- **[[F-mesure]]** (*F-score*, $F_1$), citée dans les TP : moyenne harmonique de la précision $P$ et du rappel $R$, $F_1 = \dfrac{2PR}{P+R} = \dfrac{2\,TP}{2\,TP+FP+FN}$. Elle n'est élevée que si les deux le sont : un filtre qui classe tout en spam a un rappel de 100 % mais une précision faible, donc une F-mesure faible. [[Complément hors du cours|ⓘ]]
- Le rappel positif s'appelle aussi **sensibilité**, le rappel négatif **spécificité** (vocabulaire du diagnostic médical). [[Complément hors du cours|ⓘ]]

**Exemple : filtre anti-spam** sur 100 e-mails (en réalité 20 spams, positifs, et 80 légitimes, négatifs) :

| | Prédit spam | Prédit non-spam | Total réel |
|---|---|---|---|
| Réellement spam | **15** (VP) | **5** (FN) | 20 spams |
| Réellement non-spam | **2** (FP) | **78** (VN) | 80 légitimes |

- Réussites (diagonale) : 15 VP, spams bien filtrés ; 78 VN, e-mails légitimes restés dans la boîte.
- Erreurs : **2 FP** (fausse alerte, [[Erreur de type I et de type II|erreur de type I]]) : 2 e-mails importants classés spams, erreur pénalisante ; **5 FN** (manqués, erreur de type II) : 5 spams arrivés dans la boîte, désagrément rarement bloquant.
- **Précision** $= \frac{15}{15+2} \approx 88{,}2\,\%$ : parmi ce que le filtre a classé spam, la part de vrais spams (on minimise les FP).
- **Rappel / sensibilité** $= \frac{15}{15+5} = 75\,\%$ : parmi tous les vrais spams, la part interceptée (on minimise les FN, vital en diagnostic médical).
- **Exactitude** $= \frac{15+78}{100} = 93\,\%$, soit $Er = 7\,\%$ ; **F-mesure** $= \frac{2 \times 15}{2 \times 15 + 2 + 5} = \frac{30}{37} \approx 81{,}1\,\%$. [[Complément hors du cours|ⓘ]]
- L'exactitude trompe quand les classes sont **déséquilibrées** : un filtre qui ne classe jamais rien en spam obtient ici 80 % d'exactitude (les 80 légitimes) avec un rappel nul. C'est pourquoi on regarde précision, rappel et F-mesure par classe. [[Complément hors du cours|ⓘ]]

**Validation 4 : validation croisée** (*cross validation*).
- Couper le jeu de données en $n$ sous-ensembles disjoints de même taille ; chaque valeur cible doit apparaître dans les $n$ sous-ensembles (**stratification**).
- Avec 3 sous-ensembles A, B, C : le classifieur construit sur $A \cup B$ est $CL_{A\cup B}$, son erreur de test sur C est $Er_C$. Trois tests : $(CL_{A\cup B}, Er_C)$, $(CL_{C\cup A}, Er_B)$, $(CL_{C\cup B}, Er_A)$.
- Erreur globale : $Er = \dfrac{Er_A + Er_B + Er_C}{3}$.

**Exemple : 300 e-mails, $n = 3$.**
1. Trois blocs A, B, C de 100 e-mails, chacun avec la même proportion de spams (20 spams, 80 légitimes) pour éviter un bloc sans spam.
2. Tour 1 : entraînement sur $A \cup B$ (200 e-mails), test sur C ; 7 erreurs (ex. 2 FP + 5 FN), $Er_C = 7\,\%$. Tour 2 : entraînement sur $C \cup A$, test sur B, 9 erreurs, $Er_B = 9\,\%$. Tour 3 : entraînement sur $C \cup B$, test sur A, 5 erreurs, $Er_A = 5\,\%$.
3. Plutôt que de se fier à une évaluation peut-être chanceuse : $Er = \frac{5 + 9 + 7}{3} = 7\,\%$.

![[Chp1 - intro to data mining - image10.png]]
*Figure : validation croisée à $k = 4$ plis ; à chaque itération, un bloc différent sert de test et les autres d'entraînement.*

En pratique, on prend souvent 5 ou 10 plis. Le cas extrême où chaque pli contient un seul exemple ($n = N$) est le *leave-one-out* : $N$ apprentissages, chacun testé sur l'exemple laissé de côté, utile pour les petites bases. Le modèle finalement livré est en général réappris sur toutes les données : la validation croisée sert à estimer son erreur ou à choisir un réglage (comme le $k$ des k-NN), pas à produire le modèle. [[Complément hors du cours|ⓘ]]

### Travaux pratiques annoncés

- **Jeux de données** : Weather (attributs qualitatifs), IRIS (quantitatifs).
  - IRIS est le jeu de données classique publié par le statisticien R. A. Fisher en 1936 : 150 fleurs d'iris, 50 de chacune des trois espèces (*setosa*, *versicolor*, *virginica*), décrites par 4 mesures en centimètres (longueur et largeur du sépale et du pétale). *Setosa* se sépare facilement des deux autres, qui se chevauchent un peu. [[Complément hors du cours|ⓘ]]
- Exploration et visualisation des données.
- **Méthodes** : k plus proches voisins, arbres de décision.
- **Validation** : stratégies (ensemble d'entraînement, de test, validation croisée) ; mesures (matrice de confusion, erreur, précision, rappel, [[F-mesure|F-score]]).
- **Logiciels** : Weka, R, Python.

## 3. Clustering et partitionnement

Étant donné un jeu d'exemples **non étiquetés** $X$, trouver une partition de $X$ en $k$ groupes (*clusters*) telle que :
1. les données d'un même groupe $G_i$ ($i \in 1..k$) sont semblables ;
2. deux exemples de groupes différents ne sont pas semblables.

Exemple : analyse des journaux (*logs*) d'un site de commerce en ligne pour détecter des profils d'utilisateurs.

![[Chp1 - intro to data mining - image2.png]]
*Figure : « K-means clustering », trois groupes de points sur les deux premières composantes (qui expliquent 55,61 % de la variabilité).*

Les « composantes » de la figure sont celles d'une [[Analyse en composantes principales]] : les données ont plus de deux attributs, et l'ACP les projette sur le plan qui conserve le plus de variabilité pour pouvoir dessiner les groupes. Ici, 44,39 % de la variabilité n'est pas visible sur le dessin : deux groupes qui se chevauchent sur le plan peuvent être séparés dans l'espace d'origine. [[Complément hors du cours|ⓘ]]

### Définitions et notations

- $X$ : ensemble des exemples, $|X| = N$ ; $K$ : nombre de groupes (paramètre de l'algorithme).
- Si chaque exemple est décrit par $P$ attributs, le **[[Centroïde|centroïde]]** $g$ de $X$ est un *exemple synthétique* $g = \{\bar{a}_1, \dots, \bar{a}_P\}$, où $\bar{a}_i$ est la moyenne des valeurs de $a_i$ dans $X$.
- But : trouver $K$ groupes, chacun représenté par son centroïde $g_i$. Deux familles : approches non hiérarchiques (k-means) et hiérarchiques.

### Méthode des k-moyennes (*K-means*)

[[K-moyennes]] et [[Inertie (clustering)]].
- **Inertie** d'un ensemble $X$ de $N$ exemples, de centroïde $g$ :
$$I = \frac{1}{N}\sum_{i=1}^{N} d^2(x_i, g),$$
avec $d$ une [[Distance|distance]] :

| Distance | Formule |
|---|---|
| euclidienne | $\sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}$ |
| de Manhattan | $\sum_{i=1}^{n} \lvert x_i - y_i \rvert$ |
| de Hamming | (non détaillée) |

La **distance de Hamming** entre deux vecteurs de même longueur est le nombre de positions où ils diffèrent : $d_H(x, y) = \operatorname{card}\{i : x_i \neq y_i\}$. Elle convient aux attributs qualitatifs ou binaires, où une différence de valeurs n'a pas de sens : entre (sunny, high, strong, no) et (sunny, mild, strong, yes), $d_H = 2$. [[Complément hors du cours|ⓘ]]

- **Inertie intra-classes** (*intra-cluster*), si $I_1, \dots, I_k$ sont les inerties des groupes $G_1, \dots, G_k$ (chacune calculée sur son groupe) : $I_W = \sum_{i=1}^{k} w_i I_i$, avec $w_i = \frac{|G_i|}{N}$. [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]
- **Inertie inter-classes** : $I_B = \sum_{i=1}^{k} w_i\, d^2(g_i, g)$ avec $w_i = \frac{|g_i|}{N}$.
- Décomposition : $I = I_W + I_B$.
- Cette décomposition est le **théorème de Huygens** (ou de König-Huygens). Avec $I_i = \frac{1}{|G_i|}\sum_{x \in G_i} d^2(x, g_i)$, on a $I_W = \frac{1}{N}\sum_{i=1}^{k}\sum_{x \in G_i} d^2(x, g_i)$ ; la somme sans poids $\sum I_i$ ne vaut $I_W$ que si chaque $I_i$ est divisée par $N$, l'effectif total. L'inertie totale $I$ ne dépend pas de la partition, donc minimiser $I_W$ revient à **maximiser $I_B$** : rendre les groupes compacts, c'est aussi les éloigner. [[Complément hors du cours|ⓘ]]
- But : des groupes denses et si possible bien séparés : **minimiser $I_W$**.

**Algorithme** (entrée : $X$, $K \in \mathbb{N}$, $I \leftarrow \infty$ ; les groupes sont indexés de 1 à $K$) : [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]
```
Choisir au hasard K centroïdes C_k dans X
RÉPÉTER
    pour k de 1 à K : G_k ← ∅
    pour i de 1 à N :
        k* ← argmin_{k ∈ 1..K} d(x_i, C_k)
        G_k* ← G_k* ∪ {x_i}
    pour k de 1 à K : C_k ← centroïde de G_k
    I ← I_W
    calculer I_W
JUSQU'À |I − I_W| < ε
```

![[Chp1 - intro to data mining - image28.png]]
*Figure : itérations de K-means avec $K = 2$ — choisir deux centres, affecter chaque objet au centre le plus proche, mettre à jour les moyennes, réaffecter, jusqu'à stabilisation.*

- **Convergence** : avec la distance euclidienne, chaque étape (réaffectation, puis recalcul des centroïdes) ne peut que faire baisser $I_W$, et il n'y a qu'un nombre fini de partitions : l'algorithme s'arrête toujours. Mais il atteint un **minimum local**, qui dépend des centroïdes tirés au départ ; on le relance donc plusieurs fois et l'on garde la partition de plus petite $I_W$. La variante *k-means++* choisit des centres initiaux éloignés les uns des autres pour limiter ce problème. [[Complément hors du cours|ⓘ]]
- **Choix de $K$** : $I_W$ diminue toujours quand $K$ augmente (elle vaut 0 pour $K = N$, un groupe par exemple), on ne peut donc pas choisir $K$ en minimisant $I_W$. La **méthode du coude** trace $I_W$ en fonction de $K$ et retient la valeur après laquelle la baisse devient faible. [[Complément hors du cours|ⓘ]]
- **Limites** : la moyenne est sensible aux valeurs aberrantes, et la méthode trouve surtout des groupes compacts, de forme à peu près sphérique et de tailles comparables. [[Complément hors du cours|ⓘ]]

### Classification hiérarchique

[[Classification hiérarchique ascendante]] : approche ascendante (*down-top*) qui regroupe progressivement les exemples : $N - 1$ groupes, $N - 2$ groupes, …, 1 groupe. On obtient un arbre (**dendrogramme**) dont les feuilles sont les exemples et la racine représente $X$. Une coupe horizontale de l'arbre donne $K$ groupes.

![[Chp1 - intro to data mining - image60.png]]
*Figure : les points 1 à 5 regroupés en ensembles emboîtés, et le dendrogramme correspondant (6 = 1+2, 7 = 4+5, 8 = 6+3, 9 = racine), coupé par une ligne horizontale.*

**Algorithme.**
```
Entrée : N exemples
N groupes G_i ← {x_i} ; étiqueter les G_i
pour d de 1 à N−1 :
    choisir deux groupes étiquetés G_i, G_j
    les fusionner : G_d ← G_i ∪ G_j
    désétiqueter G_i, G_j ; étiqueter G_d
```

![[Chp1 - intro to data mining - image59.png]]
*Figure : le même exemple, avec la coupe du dendrogramme au niveau des nœuds 8 et 7 (deux groupes).*

**Choix des groupes à fusionner**, quatre approches :
- **saut minimal** : la plus petite distance entre les groupes est minimale ;
- **saut maximal** : la plus grande distance est minimale ;
- **méthode des centroïdes** : la distance entre les centroïdes est minimale (à ne pas confondre avec le **saut moyen**, *average linkage*, où c'est la moyenne des distances entre toutes les paires d'exemples des deux groupes qui est minimale) ; [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]
- **[[Méthode de Ward]]** : perte minimale d'inertie $I_W$, avec
$$S_{G_i,G_j} = \frac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j), \qquad w_i = \frac{|G_i|}{N}.$$

En anglais, le saut minimal est le *single linkage*, le saut maximal le *complete linkage*, la méthode des centroïdes le *centroid linkage* (par exemple `METHOD=CENTROID` dans la procédure CLUSTER de SAS, `METHOD=AVERAGE` pour le saut moyen). [[Complément hors du cours|ⓘ]]

Le saut minimal produit souvent un **effet de chaîne** : des groupes allongés, reliés de proche en proche par des points intermédiaires. Le saut maximal et Ward donnent des groupes plus compacts. $S_{G_i,G_j}$ est exactement l'augmentation de $I_W$ (la baisse de $I_B$) causée par la fusion : Ward est donc l'analogue hiérarchique des k-means. [[Complément hors du cours|ⓘ]]

Pour choisir où couper le dendrogramme, on regarde la hauteur des fusions (la distance ou la perte d'inertie au moment de fusionner) : on coupe juste avant un grand saut, qui signale la fusion de deux groupes bien distincts. La méthode doit garder en mémoire les distances entre toutes les paires, soit de l'ordre de $N^2$ valeurs : sur de très grandes bases, on applique souvent d'abord les k-means puis la classification hiérarchique sur les centroïdes obtenus. [[Complément hors du cours|ⓘ]]

## 4. Arbres de décision

On reprend le jeu météo (tableau de la partie 1). Pour chaque attribut, la répartition des classes :

![[Chp1 - intro to data mining - image14.png]]
*Figure : quatre arbres à un niveau — outlook (sunny : 2 yes / 3 no ; overcast : 4 yes ; rainy : 3 yes / 2 no), windy (false : 6 / 2 ; true : 3 / 3), humidity (high : 3 / 4 ; normal : 6 / 1), temperature (hot : 2 / 2 ; mild : 4 / 2 ; cool : 3 / 1).*

![[Chp1 - intro to data mining - image35.png]]
*Figure : l'arbre final, racine outlook, puis humidity sous sunny et windy sous rainy.*

### Algorithme ID3

[[Algorithme ID3]].
- Soit $E = \{e_i\}$ un ensemble d'apprentissage ; chaque exemple est un vecteur d'attributs avec sa classe $c_i$.
- À chaque attribut $j$ est associé un test $T_j : E \to V_j = \{V_{ji}\}$. Exemple : le test de OUTLOOK est $T_1 : E \to \{sunny, overcast, rainy\}$.

**Construction récursive.**
```
FONCTION construct-tree(E : exemples, {T_1..T_m} : tests) : arbre
    SI tous les exemples sont de la même classe
        retourner une feuille étiquetée par cette classe
    SINON
        T_j ← Info-choose({T_1..T_m})
        {E_j1..E_jk} ← partition de E selon T_j
        arbre de racine T_j
        pour l de 1 à k :
            sous-arbre_l ← construct-tree(E_jl, {T_1..T_m} \ T_j)
```

![[Chp1 - intro to data mining - image1.png]]
*Figure : partition des exemples selon outlook (sunny : 2 yes / 3 no ; overcast : 4 yes ; rainy : 3 yes / 2 no), à côté de l'algorithme.*

**Choix du test : la quantité d'information.**
- Quantité d'information d'un sous-ensemble de cardinal $n$ tiré d'un ensemble de $N$ événements :
$$Q = \log_2 \frac{N}{n} \qquad (1)$$
- [[Entropie (théorie de l'information)|Entropie]] d'une partition $E_1, \dots, E_k$ de $E$ ($|E| = N$, $|E_i| = n_i$, $p_i = \frac{n_i}{N}$), somme sur les $k$ sous-ensembles : [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]
$$I(\text{partition}) = \sum_{i=1}^{k} \frac{n_i}{N}\log_2 \frac{N}{n_i} = \sum_{i=1}^{k} p_i \log_2 \frac{1}{p_i}.$$
- L'arbre est une source d'information qui émet
$$I(E) = \sum_{i=1}^{NC} p_i \log_2 \frac{1}{p_i} \qquad (2)$$
où $p_i$ est la fréquence de la classe $i$ dans $E$ et $NC$ le nombre de classes.
- Information moyenne des $k$ sous-ensembles obtenus par un test $T$ : $\sum_{l=1}^{k} W_l\, I(E_l^T)$, où $W_l$ est la proportion d'exemples dans $E_l^T$.
- **[[Gain d'information]]** : $gain(T) = I(E) - \sum_{l=1}^{k} W_l\, I(E_l^T)$.
- L'entropie mesure le **désordre** d'un ensemble du point de vue des classes : elle vaut 0 quand tous les exemples sont de la même classe (ensemble pur, une feuille), et elle est maximale, égale à $\log_2 NC$, quand les classes sont équiréparties (1 bit pour deux classes à 50 %). Le gain est donc la baisse de désordre obtenue en posant le test : on choisit le test qui rend les sous-ensembles les plus purs. Par convention, $0 \log_2 \frac{1}{0} = 0$. [[Complément hors du cours|ⓘ]]

**Cas à deux classes** ($p$ positifs, $n$ négatifs) :
$$I(p, n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n} \qquad (3)$$
$$gain(T) = I(p, n) - \sum_{i=1}^{k}\frac{p_i+n_i}{p+n}\, I(p_i, n_i).$$

**Exemple (PlayTennis).**
$$gain(OUTLOOK) = I(9,5) - \left(\tfrac{5}{14} I(2,3) + \tfrac{4}{14} I(4,0) + \tfrac{5}{14} I(3,2)\right) = 0{,}246 \text{ bits},$$
contre gain(TEMP.) $= 0{,}029$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$ bits : OUTLOOK, de gain maximal, est placé à la racine.

Détail du calcul (9 P et 5 N au total) : [[Complément hors du cours|ⓘ]]
$$I(9,5) = \tfrac{9}{14}\log_2\tfrac{14}{9} + \tfrac{5}{14}\log_2\tfrac{14}{5} \approx 0{,}643 \times 0{,}637 + 0{,}357 \times 1{,}485 \approx 0{,}940 \text{ bit},$$
$$I(2,3) = I(3,2) = \tfrac{2}{5}\log_2\tfrac{5}{2} + \tfrac{3}{5}\log_2\tfrac{5}{3} \approx 0{,}971, \qquad I(4,0) = 0 \text{ (overcast est pur)},$$
$$gain(OUTLOOK) \approx 0{,}940 - \tfrac{10}{14} \times 0{,}971 \approx 0{,}940 - 0{,}694 = 0{,}246.$$

On recommence ensuite dans chaque branche impure avec les attributs restants : sous *sunny* (2 P, 3 N), l'humidité sépare parfaitement les exemples (gain égal à toute l'entropie, 0,971), sous *rainy*, c'est le vent. On obtient l'arbre de la partie 1. [[Complément hors du cours|ⓘ]]

![[Chp1 - intro to data mining - image34.png]]
*Figure : la partition selon outlook utilisée dans le calcul du gain.*

### Algorithme C4.5

[[Algorithme C4.5]], descendant d'ID3 :
- traite les **attributs continus** par des méthodes de discrétisation ;
- **normalise le gain** :
$$SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2 \frac{|T_i|}{|T|} \qquad (4), \qquad GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}$$
  (le [[Rapport de gain]]) ;
- pourquoi normaliser : le gain favorise les attributs à **nombreuses valeurs**. Un identifiant (NUM, 14 valeurs) découpe la base en 14 sous-ensembles d'un exemple, tous purs : son gain est maximal (0,940 bit) alors qu'il ne permet aucune prédiction sur un nouvel exemple. $SplitInfo$, l'entropie de la partition elle-même, est d'autant plus grand que le test a de branches ($\log_2 14 \approx 3{,}81$ pour NUM) et pénalise ce découpage. [[Complément hors du cours|ⓘ]]
- regroupe des valeurs d'attributs ;
- traite les **[[Valeur manquante|valeurs manquantes]]** : si la valeur de $a_i$ manque pour un exemple, on partitionne l'ensemble d'apprentissage en $n$ groupes selon les $n$ valeurs possibles de $a_i$ ; l'exemple est affecté à chaque groupe avec une probabilité égale à la fréquence du groupe ; cette probabilité est prise en compte dans le calcul du gain et propagée dans l'arbre ;
- **[[Élagage]]** (*pruning*) de l'arbre.
  - Un arbre développé jusqu'à des feuilles pures colle aux exemples d'apprentissage, bruit compris ([[Surapprentissage|surapprentissage]]). On distingue le **pré-élagage**, qui arrête la croissance (profondeur maximale, effectif minimal par feuille, gain trop faible), et le **post-élagage**, qui construit l'arbre entier puis remplace par des feuilles les sous-arbres qui n'améliorent pas l'erreur estimée. C4.5 pratique le post-élagage. [[Complément hors du cours|ⓘ]]

### Algorithme CART

[[Algorithme CART]] (*Classification and Regression Tree*), 1984, L. Breiman, J.H. Friedman, R.A. Olshen et C.J. Stone :
- binaire : deux nœuds fils pour chaque nœud parent ;
- accepte tous les types de variables ;
- séparation par l'**[[Indice de Gini]]** :
$$IG(No) = 1 - \sum_{i=1}^{NC} p_i^2 \qquad (5)$$
où $No$ est un nœud (un sous-ensemble des données), $NC$ le nombre de classes, $p_i$ la fréquence de la classe $i$ dans le nœud.
- Plus l'indice de Gini est petit, plus le nœud est pur. Pour couper un nœud en deux, on cherche la variable qui maximise le gain de pureté :
$$IG(\text{avant}) - [W_1\, IG(\text{fils}_1) + W_2\, IG(\text{fils}_2)],$$
où $W_i$ est la proportion d'exemples du fils $i$.

**Exemple (météo, attribut windy).** Windy = false : 8 exemples (6 yes, 2 no) ; windy = true : 6 exemples (3 yes, 3 no).
$$IG(windy) = 1 - \left[\left(\tfrac{9}{14}\right)^2 + \left(\tfrac{5}{14}\right)^2\right], \quad IG(fils_1) = 1 - \left[\left(\tfrac{2}{8}\right)^2 + \left(\tfrac{6}{8}\right)^2\right], \quad IG(fils_2) = 1 - \left[\left(\tfrac{3}{6}\right)^2 + \left(\tfrac{3}{6}\right)^2\right],$$
$$Gain(windy) = IG(windy) - \left[\tfrac{8}{14}\, IG(fils_1) + \tfrac{6}{14}\, IG(fils_2)\right].$$

Valeurs numériques : $IG(windy) = 1 - \frac{81 + 25}{196} = \frac{90}{196} \approx 0{,}459$, $IG(fils_1) = 1 - \frac{4 + 36}{64} = 0{,}375$, $IG(fils_2) = 0{,}5$ (nœud le plus impur possible à deux classes), d'où $Gain(windy) \approx 0{,}459 - (0{,}214 + 0{,}214) \approx 0{,}031$ : un gain faible, comme le gain d'information de WIND. [[Complément hors du cours|ⓘ]]

L'indice de Gini est la probabilité que deux exemples tirés au hasard (avec remise) dans le nœud soient de classes différentes ; il vaut au plus $1 - \frac{1}{NC}$ (0,5 à deux classes). Pour un attribut à plus de deux valeurs, CART, étant binaire, essaie les regroupements des valeurs en deux paquets (outlook : {sunny} contre {overcast, rainy}, etc.) ; pour une variable continue, les seuils $x \le s$. En régression, la pureté se mesure par la variance de la variable cible dans le nœud, et la feuille prédit la moyenne. [[Complément hors du cours|ⓘ]]

![[Chp1 - intro to data mining - image23.png]]
*Figure : le nœud windy et ses deux branches (false : 6 yes / 2 no ; true : 3 yes / 3 no).*

![[Chp1 - intro to data mining - image27.png]]
*Figure : indice de Gini pour 20 individus et 2 classes en fonction du nombre d'individus de la classe 1 : parabole nulle en 0 et 20, maximale (0,5) en 10.*

## 5. Combinaison de plusieurs modèles

[[Méthodes d'ensemble]].

![[Chp1 - intro to data mining - image25.png]]
*Figure : des échantillons d'apprentissage tirés des exemples d'apprentissage alimentent chacun un algorithme d'apprentissage ; les classifieurs obtenus sont combinés pour prédire sur de nouvelles données.* [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]

- On transforme les sorties des modèles en une seule prédiction par un **vote** ou un **vote pondéré**.
- [[Bagging]] : modèles de même poids ; [[Boosting]] : modèles de poids différents selon leur succès.

### Bagging (*Bootstrap Aggregating*)

- À partir de $k$ ensembles d'apprentissage de même taille, dont les exemples sont tirés au hasard, on apprend un modèle par ensemble (ex. un arbre de décision).
- Les $k$ modèles ne prédisent pas tous de la même façon un exemple de test : solution « démocratique », le vote.
- Pour les méthodes instables vis-à-vis des changements de données : le bagging essaie de neutraliser cette instabilité.
- Les $k$ ensembles ne sont pas disjoints deux à deux.
- En numérique, on calcule la moyenne au lieu de voter.

**Algorithme.**
```
Génération du modèle (N = nombre d'exemples d'apprentissage) :
    pour chacune des k itérations :
        tirer N exemples avec remise dans l'ensemble d'apprentissage
        appliquer l'algorithme d'apprentissage à cet échantillon
        stocker le modèle
Classification :
    pour chacun des k modèles : prédire la classe de l'exemple
    retourner la classe majoritaire
```
(Tirage [[Tirage avec et sans remise|avec remise]].)

Un tel échantillon, de même taille $N$ que la base, s'appelle un **échantillon bootstrap**. Un exemple donné n'y figure pas avec la probabilité $\left(1 - \frac{1}{N}\right)^N$, qui tend vers $e^{-1} \approx 0{,}368$ : chaque échantillon contient donc environ 63,2 % des exemples distincts, certains en plusieurs exemplaires. Les 36,8 % restants, dits *out-of-bag*, n'ont pas servi à ce modèle et permettent d'estimer son erreur sans ensemble de test séparé. [[Complément hors du cours|ⓘ]]

Le vote réduit la **variance** des prédictions (leur sensibilité à l'échantillon d'apprentissage), pas leur biais. Il est donc utile pour les méthodes instables, comme les arbres de décision, où un petit changement des données change beaucoup l'arbre ; il n'apporte presque rien aux méthodes stables, comme les k plus proches voisins avec un grand $k$. [[Complément hors du cours|ⓘ]]

### Boosting (AdaBoost.M1)

- Les modèles diffèrent par leur capacité de généralisation ; le boosting repose sur le vote ou la moyenne.
- Les modèles sont construits **itérativement** : chacun est influencé par les précédents.
- AdaBoost.M1 : les exemples sont **pondérés** ; l'erreur est la somme des poids des exemples mal classés divisée par la somme totale des poids. La pondération permet au classifieur de *se concentrer* sur certains exemples.

**Génération des modèles** (poids initiaux $1/N$, de somme 1, et normalisés pour que la somme reste 1) : [[Erreurs du cours#^e-1-intro-to-data-mining|✎]]
```
affecter le même poids w = 1/N à chaque exemple
pour chaque itération t des k itérations :
    appliquer l'algorithme d'apprentissage aux exemples pondérés
    stocker le modèle
    calculer l'erreur e_t sur l'ensemble d'apprentissage (pondérée par les w_i) et la stocker
    SI e_t = 0 ou e_t > 0.5 : terminer
    SINON
        pour chaque exemple bien classé : w_i ← w_i · e_t / (1 − e_t)
        normaliser les poids (pour que la somme reste 1)
```
- Les poids des exemples bien classés (faciles) diminuent ; après normalisation (la somme restant la même), ceux des exemples mal classés (difficiles) augmentent.

**Classification (vote pondéré).**
```
affecter le poids 0 à toutes les classes
pour chaque modèle t : ajouter −log(e_t / (1 − e_t)) au poids de la classe qu'il prédit
retourner la classe de poids maximal
```
Poids du modèle $t$ : $W_t = -\log \frac{e_t}{1-e_t}$.

Ce poids s'écrit aussi $W_t = \log \frac{1-e_t}{e_t}$ : il est positif tant que $e_t < 0{,}5$, d'autant plus grand que le modèle se trompe peu, et nul pour $e_t = 0{,}5$. C'est la raison de l'arrêt quand $e_t > 0{,}5$ : à deux classes, un tel modèle fait pire que le hasard. L'arrêt pour $e_t = 0$ évite une division par zéro (poids infini) : le modèle classe déjà tout parfaitement. [[Complément hors du cours|ⓘ]]

Le facteur $\frac{e_t}{1-e_t}$ est inférieur à 1 dès que $e_t < 0{,}5$ : multiplier les poids des exemples bien classés par ce facteur puis renormaliser revient à augmenter la part des exemples mal classés. Après cette mise à jour, le modèle $t$ a une erreur pondérée de exactement 50 % : le modèle suivant est obligé d'apprendre autre chose. [[Complément hors du cours|ⓘ]]

Là où le bagging réduit surtout la variance, le boosting réduit surtout le **biais** : il combine des modèles faibles (par exemple des arbres à un seul niveau, dits *stumps*, comme ceux de la partie 4) en un modèle fort. Comme il insiste sur les exemples difficiles, il est sensible au bruit et aux exemples mal étiquetés. AdaBoost a été proposé par Y. Freund et R. Schapire au milieu des années 1990. [[Complément hors du cours|ⓘ]]

### Forêt aléatoire (*Random Forest*)

[[Forêt aléatoire]].

![[Chp1 - intro to data mining - image30.png]]
*Figure : toutes les données sont tirées en sous-échantillons aléatoires, chacun donne un arbre ; à chaque nœud, on choisit au hasard un petit sous-ensemble de variables et la variable (et la valeur) qui optimise la coupe.*

**Algorithme.**
- $z = \{(x_1, y_1), \dots, (x_n, y_n)\}$ : échantillon d'apprentissage, chaque $x_i$ décrit par $p$ variables explicatives.
- Pour $t = 1, \dots, K$ ($K$ = nombre d'arbres) :
  - tirer un échantillon aléatoire $z_t$ avec remise dans $z$ ;
  - estimer un arbre sur $z_t$ avec randomisation des variables : pour chaque nœud, tirer uniformément $q$ variables parmi $p$ pour former la décision.
- On obtient $K$ arbres, que l'on moyenne (régression) ou fait voter (classification).

La forêt aléatoire est un bagging d'arbres auquel s'ajoute le tirage des variables à chaque nœud. Ce second hasard **décorrèle** les arbres : sans lui, une variable très prédictive serait choisie à la racine de presque tous les arbres, qui se ressembleraient, et le vote de modèles semblables réduit peu la variance. Valeurs usuelles : $q \approx \sqrt{p}$ en classification, $q \approx p/3$ en régression ; les arbres sont développés en profondeur, sans élagage, le vote compensant leur surapprentissage. La méthode a été formalisée par L. Breiman en 2001. [[Complément hors du cours|ⓘ]]

La forêt fournit aussi une **erreur *out-of-bag*** (chaque exemple est prédit par les seuls arbres qui ne l'ont pas vu) et une mesure d'**importance des variables** (baisse de pureté ou hausse d'erreur quand on perturbe une variable), utile pour interpréter un modèle qui, avec des centaines d'arbres, ne se lit plus comme un arbre seul. [[Complément hors du cours|ⓘ]]
