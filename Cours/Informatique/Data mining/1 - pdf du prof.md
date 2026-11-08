---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du PDF cours data mining du prof ([[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]) (73 diapositives beamer, « Introduction to Data Mining », daté du 30 septembre 2026, ID4 Introduction to Machine Learning), dans [[Cours/Informatique/Data mining/_index|Data mining]]. Le cours est en anglais, avec la dernière partie en français. C'est la version du cours dont [[1 - intro to data mining]] résume la note ; ce PDF ajoute des diapositives (processus, CART détaillé, exercices). Les figures ont été ouvertes et sont intégrées ci-dessous. Les passages ajoutés finissent par ⓘ.

Plan : 1. Introduction ; 2. Clustering & partitioning ; 3. Decision trees and random forest (ID3, CART) ; 4. Combinaison de plusieurs modèles (bagging, boosting, random forest).

## 1. Introduction

### Data mining et machine learning

- **[[Fouille de données|Data mining]]** : découverte de connaissances à partir des données (*knowledge discovery from data*). Il utilise l'information de données passées pour analyser l'issue d'un problème ou d'une situation [Fayyad et al., 1995]. « Comment faire parler les données ? »
- **[[Apprentissage automatique|Machine learning]]** : étant donné une expérience ou observation $E$ (un jeu de données), une tâche $T$ et une mesure de performance $M$, un système apprend de $E$ à réaliser $T$ si, après apprentissage, sa performance sur $T$ mesurée par $M$ s'améliore [Mitchell, 1997].

![[Data mining prof - p4.jpg]]
*Figure : le data mining au croisement des statistiques, de l'IA et du machine learning, et des bases de données ; à droite, les cercles emboîtés IA ⊃ machine learning ⊃ deep learning.*

### Données

- Un **exemple** est une structure, une observation (statistique), une instance (objet), un point, un vecteur.
- Un **attribut** est qualitatif, quantitatif, ou une structure.
- Une base de données est un ensemble d'exemples ; un exemple (cas, observation) est un vecteur de $p$ attributs, chacun associé à un domaine prédéfini.

**Le jeu météo** (*weather*), utilisé dans tout le cours :

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

### Le processus

![[Data mining prof - p7.jpg]]
*Figure : « DM versus ML process » — à gauche, le cycle du data mining (définir le problème, préparer et explorer les données, construire et valider les modèles, les déployer) ; à droite, la chaîne de la data science où data mining, machine learning, deep learning et IA se recouvrent.*

Le cycle de gauche rappelle la méthode **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*, fin des années 1990), standard de l'industrie en six phases qui bouclent : compréhension du métier, compréhension des données, préparation des données, modélisation, évaluation, déploiement. En pratique, la préparation des données y prend souvent la plus grande part du temps. [[Complément hors du cours|ⓘ]]

**Étapes (DM and ML process).**
1. **Analyse du problème.**
2. **Sélection et exploration des données** : évaluation de la qualité, regroupement et visualisation, détection des pathologies des données.
3. **[[Prétraitement des données|Prétraitement]]** :
   - *nettoyage* : bruit, [[Valeur manquante|valeurs manquantes]], valeurs aberrantes ;
   - *réduction* : sélection d'instances, extraction, combinaison de variables ;
   - *transformation* : discrétisation des variables continues, binarisation des variables nominales, ajout de variables.
4. L'algorithme de data mining ou de machine learning.
5. Évaluation et interprétation des résultats.

![[Data mining prof - p9.jpg]]
*Figure : la chaîne sélection → prétraitement → transformation → data mining → interprétation, jusqu'à « l'idée ».*

Cette chaîne est le schéma classique du processus **KDD** (*Knowledge Discovery in Databases*) de Fayyad et ses coauteurs : au sens strict, le data mining n'en est qu'une étape, celle où l'on applique l'algorithme ; au sens large, le mot désigne tout le processus. [[Complément hors du cours|ⓘ]]

### Nature des variables

- **Indépendantes** (prédictives, explicatives) : valeur obtenue par observation. **Dépendante** (cible) : sa valeur dépend des autres ([[Variable cible et variable explicative]]).
- **[[Apprentissage non supervisé]]** : pas de variable cible (ex. clustering). **[[Apprentissage supervisé]]** : une variable cible à prédire (ex. classification).

### Résultat du processus

La connaissance extraite prend la forme :
- d'un **modèle** : vue globale du jeu de données ;
- de **motifs** (*patterns*) : description locale de sous-ensembles des données, par exemple des règles.

**Exemple de modèle : un [[Arbre de décision]].**

![[Data mining prof - p12.jpg]]
*Figure : le jeu météo et l'arbre obtenu (racine outlook ; sunny → humidity ; overcast → yes ; rainy → windy).*

Un arbre se lit comme un ensemble de règles :
- IF OUTLOOK = sunny & HUMI = strong THEN CLASS = N
- IF OUTLOOK = sunny & HUMI = normal THEN CLASS = P
- IF OUTLOOK = overcast THEN CLASS = P
- IF OUTLOOK = rainy & WIND = yes THEN CLASS = N
- IF OUTLOOK = rainy & WIND = no THEN CLASS = P

![[Data mining prof - p13.jpg]]
*Figure : l'arbre et ses règles sur la même diapositive.*

### Tâches

- **Supervisées** : chaque instance = $p$ variables prédictives + 1 variable cible.
  - *Classification* : cible discrète (ex. diagnostic de maladie) ;
  - *Régression* : cible continue (ex. estimation d'un prix).
- **Non supervisées** :
  - *segmentation* ([[Clustering]]) : ex. détection de profils d'utilisateurs ;
  - *association* ([[Règle d'association|règles d'association]]) : ex. analyse des logs d'un serveur web.

![[Data mining prof - p15.jpg]]
*Figure : tâches prédictives (classification, régression, séries temporelles, prédiction) et descriptives (clustering, résumé, règles d'association, découverte de séquences).*

![[Data mining prof - p16.jpg]]
*Figure : autour d'une table de données, quatre tâches — clustering, modélisation prédictive (arbre), règles d'association (lait → couches), détection d'anomalies.*

![[Data mining prof - p17.jpg]]
*Figure : processus supervisé — entraînement (données brutes → feature engineering → ensembles d'entraînement, de validation pour régler les hyperparamètres, et de test pour l'évaluation → modèle), puis prédiction sur de nouvelles données.*

### Classification

**Types de [[Classifieur|classifieurs]].**
1. Construction d'un modèle (un arbre de décision par exemple) pour prédire la classe cible.
2. Estimation directe de la classe cible en fonction des exemples.
3. Construction d'un modèle paramétrable ([[Réseau de neurones|réseaux de neurones]], [[Machine à vecteurs de support|SVM]]).

**[[K plus proches voisins]]** : jeu à deux attributs numériques $(X_1, X_2)$ et deux classes (A, B).

![[Data mining prof - p19.jpg]]
*Figure : le point à classer (étoile) ; avec $k = 3$, majorité violette (B) ; avec $k = 6$, majorité jaune (A).*

**Principe.** Pour classer un nouveau point $x$ : calculer sa [[Distance|distance]] à chaque exemple d'apprentissage, garder les $k$ plus proches, et lui attribuer la classe majoritaire parmi eux (en régression, la moyenne de leurs valeurs cibles). C'est l'« estimation directe » du type 2 ci-dessus : il n'y a pas de phase d'apprentissage, tout le calcul a lieu au moment de la prédiction, d'où un coût proportionnel à la taille de la base pour chaque point à classer. [[Complément hors du cours|ⓘ]]

**Réglages.** Un $k$ petit suit le bruit des données, un $k$ grand lisse trop (avec $k = N$, on prédit toujours la classe majoritaire) ; on choisit $k$ par [[Validation d'un classifieur|validation croisée]], et on le prend impair à deux classes pour éviter les égalités. Comme la distance mélange les attributs, il faut les mettre à la même échelle (normalisation min-max dans $[0,1]$ ou centrage-réduction), sinon l'attribut aux plus grandes valeurs décide seul. [[Complément hors du cours|ⓘ]]

### Validation d'un classifieur

[[Validation d'un classifieur]].

**Validation 1.**
- L'erreur $Er$ est la probabilité que le classifieur ne prédise pas correctement la valeur cible d'une donnée ; taux de réussite $1 - Er$.
- L'erreur d'entraînement est mesurée sur l'[[Ensemble d'entraînement et de test|ensemble d'entraînement]].
- Il faut un ensemble d'entraînement $X_{train}$ et un ensemble de test $X_{test}$ (valeur cible connue) pour estimer l'erreur.
- L'erreur d'entraînement est optimiste : un modèle assez souple peut « apprendre par cœur » les exemples (erreur d'entraînement nulle) et mal prédire les nouveaux, c'est le [[Surapprentissage|surapprentissage]] (*overfitting*). Seule l'erreur sur des données non vues estime la capacité de **généralisation** ; un écart grand entre les deux erreurs est le signe du surapprentissage. [[Complément hors du cours|ⓘ]]

![[Data mining prof - p21.jpg]]
*Figure : base → données d'entraînement (construction du modèle) et de test (précision acceptable ?) → si oui, prédiction sur des données inconnues.*

**Validation 2 : matrice de confusion**, pour chaque valeur cible. TP / TN : nombre d'exemples positifs / négatifs bien prédits ; FP / FN : nombre d'exemples négatifs / positifs prédits positifs / négatifs.

| | + Pred | − Pred |
|---|---|---|
| Real + | TP | FN |
| Real − | FP | TN |

**Validation 3 : quatre mesures.**
- Précision positive $\dfrac{TP}{TP+FP}$ et négative $\dfrac{TN}{TN+FN}$ : proportion d'exemples vraiment positifs parmi ceux classés positifs.
- Rappel positif $\dfrac{TP}{TP+FN}$ et négatif $\dfrac{TN}{TN+FP}$ : proportion des positifs retrouvés parmi tous les positifs.
- Le taux de réussite global (*accuracy*, exactitude) se lit aussi sur la matrice : $\dfrac{TP+TN}{TP+TN+FP+FN} = 1 - Er$. Il trompe quand les classes sont déséquilibrées : avec 99 % de négatifs, un classifieur qui répond toujours « négatif » a 99 % de réussite et un rappel positif nul. [[Complément hors du cours|ⓘ]]
- La [[F-mesure]] citée en TP résume précision $P$ et rappel $R$ positifs par leur moyenne harmonique, $F_1 = \dfrac{2PR}{P+R}$ : elle n'est élevée que si les deux le sont. Précision et rappel varient en sens inverse quand on rend le classifieur plus ou moins prudent. [[Complément hors du cours|ⓘ]]

**Validation 4 : validation croisée.** Couper le jeu en $n$ sous-ensembles disjoints de même taille, chaque valeur cible apparaissant dans chacun. Avec A, B, C : $CL_{A\cup B}$ est le classifieur construit sur $A \cup B$, $Er_C$ son erreur sur C ; trois tests $(CL_{A\cup B}, Er_C)$, $(CL_{C\cup A}, Er_B)$, $(CL_{C\cup B}, Er_A)$ ; erreur globale
$$Er = \frac{Er_A + Er_B + Er_C}{3}.$$

![[Data mining prof - p25.jpg]]
*Figure : validation croisée à $k = 4$ plis, le bloc de test se déplace à chaque itération.*

Exiger que chaque valeur cible apparaisse dans chaque sous-ensemble, en respectant ses proportions, s'appelle la validation croisée **stratifiée**. On prend souvent $n = 5$ ou $10$ plis ; le cas extrême $n = N$ (un seul exemple de test à chaque fois) est le *leave-one-out*, coûteux mais utile sur de petits jeux. Chaque exemple sert une fois en test et $n-1$ fois en entraînement, ce qui donne une estimation plus stable qu'un seul découpage entraînement / test. [[Complément hors du cours|ⓘ]]

**Travaux pratiques annoncés.** Jeux Weather (qualitatif) et IRIS (quantitatif) ; exploration et visualisation ; méthodes : k plus proches voisins, arbres de décision ; validation : ensembles d'entraînement et de test, validation croisée ; mesures : matrice de confusion, erreur, précision, rappel, [[F-mesure|F-score]] ; logiciels Weka, R, Python.

## 2. Clustering & partitioning

Étant donné un jeu d'exemples non étiquetés $X$, trouver une partition de $X$ en $k$ groupes telle que :
1. les données d'un même groupe $G_i$ ($i \in 1..k$) sont semblables ;
2. deux exemples de groupes différents ne sont pas semblables.

Exemple : analyse des logs d'un site de commerce en ligne, détection de profils d'utilisateurs.

![[Data mining prof - p27.jpg]]
*Figure : nuage de points réparti en trois groupes.*

**Définitions et notations.**
- $X$ : ensemble des exemples, $|X| = N$ ; $K$ : nombre de groupes (paramètre).
- Le **[[Centroïde|centroïde]]** $g$ de $X$ (exemples à $P$ attributs) est l'exemple synthétique $g = \{\bar{a}_1, \dots, \bar{a}_P\}$, $\bar{a}_i$ moyenne des $a_i$ sur $X$.
- But : trouver $K$ groupes représentés par leurs centroïdes $g_i$, par une approche non hiérarchique (k-means) ou hiérarchique.

### Méthode des k-moyennes

[[K-moyennes]], [[Inertie (clustering)]].
- Inertie de $X$ : $I = \frac{1}{N}\sum_{i=1}^{N} d^2(x_i, g)$, avec $d$ une [[Distance|distance]] : euclidienne $\sqrt{\sum (x_i - y_i)^2}$, Manhattan $\sum |x_i - y_i|$, Hamming, etc.
- La distance de Hamming compte les positions où deux vecteurs diffèrent : $d_H(x, y) = \#\{i : x_i \neq y_i\}$. Elle convient aux attributs qualitatifs ou binaires, comme ceux du jeu météo (entre les exemples 1 et 2, qui ne diffèrent que par Wind, $d_H = 1$). [[Complément hors du cours|ⓘ]]
- Inertie intra-classes $I_W = \sum_{i=1}^{k} w_i I_i$, où $I_i$ est l'inertie du groupe $G_i$ (calculée sur ses $|G_i|$ exemples) ; inter-classes $I_B = \sum_{i=1}^{k} w_i\, d^2(g_i, g)$, $w_i = \frac{|g_i|}{N}$ ; $I = I_W + I_B$. [[Erreurs du cours#^e-1-pdf-du-prof|✎]]
- La décomposition $I = I_W + I_B$ est le **théorème de Huygens** (avec la distance euclidienne ; $I_W = \frac{1}{N}\sum_{i=1}^{k}\sum_{x \in G_i} d^2(x, g_i)$, ce que donne aussi la somme sans poids $\sum I_i$ si chaque $I_i$ est divisée par l'effectif total $N$). L'inertie totale $I$ ne dépend pas de la partition : minimiser $I_W$ revient donc à maximiser $I_B$, les deux buts « denses » et « bien séparés » n'en font qu'un. Le rapport $I_B / I$, entre 0 et 1, mesure la part d'inertie expliquée par la partition. [[Complément hors du cours|ⓘ]]
- But : des groupes denses et bien séparés, **minimiser $I_W$**.

**Algorithme.**
```
Entrée : X, K ∈ ℕ ; I ← ∞
Choisir au hasard K centroïdes C_k ∈ X
RÉPÉTER
    pour k ∈ 1..K : G_k ← ∅
    pour i ∈ 1..N :
        k* ← argmin_{k ∈ 1..K} d(x_i, C_k)
        G_k* ← G_k* ∪ {x_i}
    pour k ∈ 1..K : C_k ← centroïde de G_k
    I ← I_W
    calculer I_W
JUSQU'À |I − I_W| < ε
```

![[Data mining prof - p31.jpg]]
*Figure : itérations de K-means avec $K = 2$ (choix des centres, affectation, mise à jour des moyennes, réaffectation).*

**Convergence.** Chaque étape fait baisser (ou laisse égale) $I_W$ : réaffecter un point au centroïde le plus proche ne peut que diminuer sa contribution, et le centroïde (la moyenne) est le point qui minimise la somme des carrés des distances au groupe. Comme il y a un nombre fini de partitions, l'algorithme s'arrête en un nombre fini d'itérations, mais sur un **minimum local** : le résultat dépend des centroïdes de départ (l'exercice ci-dessous le montre). On relance donc l'algorithme avec plusieurs initialisations et on garde la partition de plus petite $I_W$ ; la variante *k-means++* choisit des centres initiaux éloignés les uns des autres. [[Complément hors du cours|ⓘ]]

**Choix de $K$.** $I_W$ diminue toujours quand $K$ augmente (elle vaut 0 pour $K = N$) : on ne peut pas choisir $K$ en minimisant $I_W$. On trace $I_W$ en fonction de $K$ et on retient le « coude » de la courbe, au-delà duquel ajouter un groupe n'apporte plus grand-chose (méthode du coude) ; le score de silhouette est une autre méthode courante. [[Complément hors du cours|ⓘ]]

### Classification hiérarchique

[[Classification hiérarchique ascendante]] : approche ascendante qui regroupe progressivement les exemples ($N-1$ groupes, $N-2$, …, 1). On obtient un arbre dont les feuilles sont les exemples et la racine $X$ ; une coupe horizontale donne $K$ groupes.

![[Data mining prof - p32.jpg]]
*Figure : regroupements emboîtés des points 1 à 5 et dendrogramme correspondant.*

**Algorithme.**
```
Entrée : N exemples ; N groupes G_i ← {x_i}, étiquetés
pour d de 1 à N−1 :
    choisir G_i, G_j étiquetés
    G_d ← G_i ∪ G_j
    désétiqueter G_i, G_j ; étiqueter G_d
```

![[Data mining prof - p33.jpg]]
*Figure : le même dendrogramme, coupé par une ligne horizontale.*

**Choix des groupes à fusionner**, quatre approches :
- saut minimal : la plus petite distance entre groupes est minimale ;
- saut maximal : la plus grande distance est minimale ;
- méthode des centroïdes : la distance entre centroïdes est minimale (le **saut moyen**, *average linkage*, minimise, lui, la moyenne des distances entre toutes les paires d'exemples des deux groupes) ; [[Erreurs du cours#^e-1-pdf-du-prof|✎]]
- **[[Méthode de Ward]]** : perte minimale de $I_W$, $S_{G_i,G_j} = \dfrac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j)$, avec $w_i = \frac{|G_i|}{N}$, $w_j = \frac{|G_j|}{N}$.

![[Data mining prof - p34.jpg]]
*Figure : la diapositive des critères de fusion, avec le dendrogramme.*

Dans les logiciels, ces critères s'appellent *single linkage* (saut minimal), *complete linkage* (saut maximal), *average linkage* (saut moyen), *centroid* (méthode des centroïdes) et *ward*. Le saut minimal produit des groupes allongés en « chaîne » (deux groupes se rejoignent dès qu'un seul couple de points est proche) ; le saut maximal et Ward donnent des groupes plus compacts. [[Complément hors du cours|ⓘ]]

Le critère de Ward découle de l'[[Inertie (clustering)|inertie]] : $S_{G_i,G_j}$ est exactement l'augmentation de $I_W$ (donc la perte de $I_B$) quand on fusionne $G_i$ et $G_j$. Fusionner à chaque étape la paire de plus petit $S$ revient à perdre le moins d'inertie inter-classes possible, ce qui rend Ward cohérent avec le critère des k-moyennes. [[Complément hors du cours|ⓘ]]

### Exercice (clustering)

Points de $\mathbb{R}$ : $x_1 = 1$, $x_2 = 2$, $x_3 = 9$, $x_4 = 12$, $x_5 = 20$.
1. Appliquer k-means avec :
   1. $k = 2$, $g_1 = 1$ et $g_2 = 20$ ;
   2. $k = 2$, $g_1 = 2$ et $g_2 = 9$ ;
   3. $k = 3$, $g_1 = 1$, $g_2 = 9$ et $g_3 = 12$.
2. Appliquer la classification hiérarchique ascendante avec le saut minimal.

Pas de correction dans le document.

Correction proposée, avec la distance $|x - y|$ et $I_W = \frac{1}{N}\sum_k \sum_{x \in G_k} (x - g_k)^2$, $N = 5$ (inertie totale $I = 48{,}56$, centre $g = 8{,}8$) : [[Complément hors du cours|ⓘ]]
- **1.1** ($g_1 = 1$, $g_2 = 20$) : 9 est plus près de 1 (8) que de 20 (11), 12 plus près de 20 ; groupes $\{1, 2, 9\}$ et $\{12, 20\}$, centroïdes 4 et 16. Réaffectation : 9 reste avec 4 (5 contre 7), rien ne bouge. $I_W = (38 + 32)/5 = 14$. [[Complément hors du cours|ⓘ]]
- **1.2** ($g_1 = 2$, $g_2 = 9$) : groupes $\{1, 2\}$ et $\{9, 12, 20\}$, centroïdes 1,5 et $41/3 \approx 13{,}67$ ; 9 reste dans le second (4,67 contre 7,5), stable. $I_W \approx (0{,}5 + 64{,}67)/5 \approx 13{,}03$ : meilleure que 1.1, alors que $K$ est le même. Deux départs différents donnent deux partitions différentes : k-means ne trouve qu'un minimum local. [[Complément hors du cours|ⓘ]]
- **1.3** ($g_1 = 1$, $g_2 = 9$, $g_3 = 12$) : premier tour $\{1, 2\}$, $\{9\}$, $\{12, 20\}$, centroïdes 1,5, 9 et 16 ; au deuxième tour, 12 passe au groupe de 9 (distance 3 contre 4) ; groupes $\{1, 2\}$, $\{9, 12\}$, $\{20\}$, centroïdes 1,5, 10,5 et 20, stable. $I_W = (0{,}5 + 4{,}5 + 0)/5 = 1$. [[Complément hors du cours|ⓘ]]
- **2** (saut minimal) : distances entre voisins 1 (1–2), 7 (2–9), 3 (9–12), 8 (12–20). Fusions : $\{1, 2\}$ à la hauteur 1, $\{9, 12\}$ à 3, $\{1, 2, 9, 12\}$ à 7, puis tout l'ensemble avec 20 à 8. Une coupe entre 3 et 7 donne les trois groupes de 1.3 ; une coupe entre 7 et 8 isole 20. [[Complément hors du cours|ⓘ]]

## 3. Arbres de décision et forêts

**Approches inductives** : découverte de connaissances par arbres de décision.
- Une **feuille** indique une valeur de classe ; un **nœud** représente un test sur un attribut ; une **arête** correspond à une valeur du domaine de l'attribut.
- L'ensemble d'apprentissage doit couvrir le domaine des données (même les exemples inhabituels doivent être représentés).

![[Data mining prof - p38.jpg]]
*Figure : « A decision tree ?! » — un arbre beaucoup plus profond, construit avec TEMP. à la racine puis CIEL, VENT, HUMI (libellés en français) : un mauvais choix de racine donne un arbre complexe.*

![[Data mining prof - p39.jpg]]
*Figure : l'arbre obtenu par ID3, en français (CIEL → HUMI / P / VENT) et en anglais (outlook → humidity / yes / windy).*

![[Data mining prof - p40.jpg]]
*Figure : recherche de la racine — répartition yes / no selon outlook (2/3, 4/0, 3/2), windy (6/2, 3/3), humidity (3/4, 6/1) et temperature (2/2, 4/2, 3/1).*

![[Data mining prof - p41.jpg]]
*Figure : l'arbre découvert à partir du jeu météo.*

**Interpréter l'arbre** : règles « IF OUTLOOK = sunny & HUMI = strong THEN PLAY = N », etc. (mêmes règles que plus haut, avec PLAY au lieu de CLASS). La classe Play = P est décrite par : [[Erreurs du cours#^e-1-pdf-du-prof|✎]]
$$(OUTLOOK = sunny \wedge HUMI = normal) \vee (OUTLOOK = overcast) \vee (OUTLOOK = rainy \wedge WIND = no)$$

### L'algorithme ID3

[[Algorithme ID3]].
- $E = \{e_i\}$ : ensemble d'apprentissage ; chaque exemple est un vecteur d'attributs et sa classe $c_i$.
- À chaque attribut $j$ est associé un test $T_j : E \to V_j = \{V_{ji}\}$ ; ex. $T_1 : E \to \{sunny, overcast, rainy\}$ pour OUTLOOK.

```
FONCTION construct-tree(E : exemples, {T_1..T_m} : tests) : arbre
    SI tous les exemples sont de la même classe
        construct-tree ← feuille étiquetée par la classe
    SINON
        T_j ← Info-choose({T_1..T_m})
        {E_j1..E_jk} ← partition de E selon T_j
        construct-tree ← arbre de racine T_j
        l ← 1
        TANT QUE l ≤ k :
            sous-arbre_l ← construct-tree(E_jl, {T_1..T_m} \ T_j)
            l ← l + 1
```

ID3 (*Iterative Dichotomiser 3*) a été proposé par J. R. Quinlan (1986). C'est un algorithme **glouton** : à chaque nœud, il choisit le meilleur test du moment et ne revient jamais sur ce choix, ce qui ne garantit pas l'arbre le plus petit possible (trouver celui-ci est un problème NP-complet). Si les tests sont épuisés sans que le nœud soit pur, la feuille reçoit la classe majoritaire. [[Complément hors du cours|ⓘ]]

**Info-choose : la quantité d'information.**
- Information d'un sous-ensemble de cardinal $n$ tiré de $N$ événements : $Q = \log_2 \frac{N}{n}$ (1).
- [[Entropie (théorie de l'information)|Entropie]] d'une partition $E_1, \dots, E_k$ ($|E_i| = n_i$, $p_i = \frac{n_i}{N}$) : $I(\text{partition}) = \sum_{i=1}^{k} \frac{n_i}{N}\log_2 \frac{N}{n_i} = \sum_{i=1}^{k} p_i\log_2 \frac{1}{p_i}$.
- Information émise par l'arbre : $I(E) = \sum_{i=1}^{NC} p_i\log_2\frac{1}{p_i}$ (2), $p_i$ fréquence de la classe $i$, $NC$ nombre de classes.
- Information moyenne après un test $T$ : $\sum_{l=1}^{k} W_l\, I(E_l^T)$, $W_l$ proportion d'exemples dans $E_l^T$.
- L'entropie vaut 0 pour un ensemble pur (une seule classe) et atteint son maximum $\log_2 NC$ quand les classes sont équiprobables (1 bit pour deux classes moitié-moitié) : elle mesure le désordre, l'incertitude sur la classe d'un exemple tiré au hasard. [[Complément hors du cours|ⓘ]]
- **[[Gain d'information]]** : $gain(T) = I(E) - \sum_{l=1}^{k} W_l\, I(E_l^T)$.
- Le gain est la baisse d'entropie apportée par le test ; il est toujours positif ou nul, et on place au nœud le test de gain maximal, c'est-à-dire celui qui laisse les fils les plus purs. [[Complément hors du cours|ⓘ]]
- Deux classes ($p$ positifs, $n$ négatifs) :
$$I(p,n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n} \quad (3), \qquad gain(T) = I(p,n) - \sum_{i=1}^{k}\frac{p_i+n_i}{p+n}\, I(p_i, n_i).$$

**Exemple (PlayTennis).**
$$gain(OUTLOOK) = I(9,5) - \left(\tfrac{5}{14}I(2,3) + \tfrac{4}{14}I(4,0) + \tfrac{5}{14}I(3,2)\right) = 0{,}246 \text{ bits},$$
contre gain(TEMP.) $= 0{,}029$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$ bits : OUTLOOK à la racine.

Détail du calcul, avec la formule (3) : [[Complément hors du cours|ⓘ]]
$$I(9,5) = \tfrac{9}{14}\log_2\tfrac{14}{9} + \tfrac{5}{14}\log_2\tfrac{14}{5} \approx 0{,}643 \times 0{,}637 + 0{,}357 \times 1{,}485 \approx 0{,}940,$$
$$I(2,3) = I(3,2) = \tfrac{2}{5}\log_2\tfrac{5}{2} + \tfrac{3}{5}\log_2\tfrac{5}{3} \approx 0{,}971, \qquad I(4,0) = 0 \text{ (nœud pur)},$$
$$gain(OUTLOOK) \approx 0{,}940 - \tfrac{10}{14} \times 0{,}971 \approx 0{,}940 - 0{,}694 = 0{,}246.$$

![[Data mining prof - p48.jpg]]
*Figure : le calcul du gain d'outlook et la partition correspondante.*

### L'algorithme C4.5

[[Algorithme C4.5]], descendant d'ID3 :
- attributs continus traités par discrétisation ;
- pour un attribut continu, on trie ses valeurs, on essaie comme seuil chaque milieu entre deux valeurs consécutives (test binaire $a \le s$ / $a > s$) et on garde le seuil de meilleur critère. [[Complément hors du cours|ⓘ]]
- normalisation du gain : $SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2\frac{|T_i|}{|T|}$ (4), $GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}$ ([[Rapport de gain]]) ;
- pourquoi normaliser : le gain favorise les attributs à beaucoup de valeurs. Un identifiant (NUM dans le jeu météo) découpe la base en 14 feuilles pures et obtient le gain maximal $I(E)$, sans rien apprendre de généralisable. $SplitInfo$ est l'entropie de la partition elle-même : elle grandit avec le nombre de branches ($\log_2 14 \approx 3{,}81$ pour NUM) et pénalise ces tests. [[Complément hors du cours|ⓘ]]
- regroupement de valeurs d'attributs ;
- valeurs manquantes : si $a_i$ manque pour un exemple, on partitionne l'ensemble selon les $n$ valeurs de $a_i$, l'exemple est affecté à chaque groupe avec une probabilité égale à la fréquence du groupe, prise en compte dans le gain et propagée dans l'arbre ;
- [[Élagage]] de l'arbre.

### L'algorithme CART

[[Algorithme CART]] (*Classification and Regression Tree*), 1984, L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone : arbre **binaire** (deux fils par nœud), tous types de variables, séparation par l'**[[Indice de Gini]]** :
$$IG(No) = 1 - \sum_{i=1}^{NC} p_i^2 \qquad (5)$$
($No$ : nœud, $NC$ : nombre de classes, $p_i$ : fréquence de la classe $i$ dans le nœud). Plus l'indice est petit, plus le nœud est pur. On cherche la variable qui maximise le gain de pureté
$$IG(\text{avant}) - [W_1\, IG(\text{fils}_1) + W_2\, IG(\text{fils}_2)],$$
$W_i$ proportion d'exemples du fils $i$.

**Exemple (windy).**
$$IG(windy) = 1 - \left[\left(\tfrac{9}{14}\right)^2 + \left(\tfrac{5}{14}\right)^2\right], \quad IG(fils_1) = 1 - \left[\left(\tfrac{2}{8}\right)^2 + \left(\tfrac{6}{8}\right)^2\right], \quad IG(fils_2) = 1 - \left[\left(\tfrac{3}{6}\right)^2 + \left(\tfrac{3}{6}\right)^2\right],$$
$$Gain(windy) = IG(windy) - \left[\tfrac{8}{14}\, IG(fils_1) + \tfrac{6}{14}\, IG(fils_2)\right].$$

Valeurs numériques : $IG(windy) = 1 - \frac{81 + 25}{196} = \frac{90}{196} \approx 0{,}459$, $IG(fils_1) = 1 - \frac{4 + 36}{64} = 0{,}375$, $IG(fils_2) = 0{,}5$ (le maximum, classes à égalité), d'où $Gain(windy) = \frac{90}{196} - \left(\frac{3}{14} + \frac{3}{14}\right) = \frac{6}{196} \approx 0{,}031$ : windy sépare mal, comme avec l'entropie. [[Complément hors du cours|ⓘ]]

L'indice de Gini est la probabilité de se tromper en étiquetant un exemple du nœud au hasard selon les fréquences des classes ; il vaut 0 pour un nœud pur et au plus $1 - \frac{1}{NC}$ (0,5 pour deux classes, comme sur la figure suivante). Gini et entropie classent presque toujours les coupes dans le même ordre ; Gini, sans logarithme, est plus rapide à calculer. [[Complément hors du cours|ⓘ]]

![[Data mining prof - p53.jpg]]
*Figure : le nœud windy (false : 6 yes / 2 no ; true : 3 yes / 3 no) et le calcul de Gini.*

![[Data mining prof - p54.jpg]]
*Figure : indice de Gini pour 20 individus et 2 classes, parabole de maximum 0,5 à 10 individus.*

**Construction de l'arbre** (on maximise le gain de Gini, pas l'indice de Gini lui-même) : [[Erreurs du cours#^e-1-pdf-du-prof|✎]]
```
Tant que les conditions d'arrêt ne sont pas vérifiées :
    1. trouver la variable X et les conditions positive / négative qui donnent la meilleure séparation (gain de Gini maximal)
    2. séparer les données en deux sous-ensembles selon X
    3. construire un nœud X avec un fils gauche et un fils droit
    4. recommencer pour chaque fils (étape 1)
Élaguer l'arbre (optionnel)
```
**Conditions d'arrêt** : profondeur de l'arbre (liée au nombre de variables utilisées) ; nombre de feuilles limité ; effectif d'un fils limité ; performance suffisante (erreur d'entraînement faible) ; plus d'amélioration de la performance.

**Élagage.** Construire l'arbre complet ; l'élaguer successivement (en supprimant deux feuilles qui sont les fils d'un même nœud) ; garder l'arbre élagué de meilleure performance (plus petite erreur sur l'ensemble de test).

L'élagage lutte contre le [[Surapprentissage|surapprentissage]] : un arbre poussé jusqu'au bout a des feuilles presque pures, donc une erreur d'entraînement quasi nulle, mais ses dernières coupes suivent le bruit de quelques exemples. Les conditions d'arrêt ci-dessus sont un **pré-élagage** (on s'arrête avant), l'élagage de l'arbre complet un **post-élagage**, en général plus sûr car une coupe peu utile peut en préparer une très utile. Un ensemble qui sert à choisir l'arbre ne mesure plus honnêtement son erreur : c'est le rôle de l'ensemble de validation de la figure du processus supervisé, l'ensemble de test étant gardé pour l'évaluation finale. [[Complément hors du cours|ⓘ]]

**Affectation des classes.** Pour chaque feuille, et chaque classe $c_i$, $P_{c_i}$ est la proportion d'exemples de la feuille dans $c_i$ ; on affecte à la feuille la classe $c_k$ de $P_{c_k}$ maximal.

**Exemple (nœud windy).**
- Fils 1 [wind = false] comme feuille : P(6), N(2) ; $P_P = \frac{6}{8}$, $P_N = \frac{2}{8}$ ; classe affectée P ; taux d'erreur $\frac{2}{8}$.
- Fils 2 [wind = true] comme feuille : P(3), N(3) ; $P_P = \frac{3}{6}$, $P_N = \frac{3}{6}$ ; classe affectée « P ?? » (égalité) ; taux d'erreur $\frac{3}{6}$.
- Taux d'erreur global = somme pondérée des erreurs des feuilles.

![[Data mining prof - p57.jpg]]
*Figure : les deux feuilles du nœud windy et leurs classes affectées.*

## 4. Combinaison de plusieurs modèles

[[Méthodes d'ensemble]].

![[Data mining prof - p58.jpg]]
*Figure : des échantillons tirés des exemples d'apprentissage (étiquetés « Test Sample ») passent chacun par un algorithme d'apprentissage ; les classifieurs sont combinés pour prédire sur de nouvelles données.*

**Décision de plusieurs modèles.** Transformer les sorties en une seule prédiction par un vote ou un vote pondéré. [[Bagging]] : modèles de même poids ; [[Boosting]] : poids différents selon leur succès.

### Bagging

- À partir de $k$ ensembles d'apprentissage de même taille, d'exemples tirés au hasard, on apprend un modèle par ensemble (ex. un arbre).
- Les $k$ modèles ne prédisent pas tous pareil un exemple de test : solution « démocratique », le vote.

```
Génération (N = nombre d'exemples d'apprentissage) :
    pour chacune des k itérations :
        choisir N exemples par tirage aléatoire avec remise
        appliquer l'algorithme d'apprentissage à cet échantillon
        stocker le modèle
Classification :
    pour chacun des k modèles : prédire la classe de l'exemple
    retourner la classe majoritaire
```

**Discussion.** Pour des méthodes instables vis-à-vis des changements de données : le bagging (*Bootstrap Aggregating*) essaie de neutraliser cette instabilité. Les $k$ ensembles ne sont pas disjoints deux à deux. En numérique, on fait la moyenne au lieu du vote.

Le tirage avec remise de $N$ exemples parmi $N$ est un **échantillon bootstrap** : un exemple donné n'y figure pas avec la probabilité $\left(1 - \frac{1}{N}\right)^N \to e^{-1} \approx 0{,}368$, si bien que chaque échantillon contient environ 63,2 % d'exemples distincts, certains en plusieurs exemplaires. Les exemples non tirés (*out-of-bag*) servent d'ensemble de test gratuit pour le modèle correspondant. [[Complément hors du cours|ⓘ]]

Ce qui rend le bagging utile : un modèle instable, comme un arbre profond, a une erreur due surtout à sa **variance** (il change beaucoup d'un échantillon à l'autre). Moyenner des modèles dont les erreurs ne sont pas toutes les mêmes réduit cette variance sans augmenter le biais ; sur un modèle stable (k plus proches voisins avec $k$ grand, régression linéaire), le gain est faible. [[Complément hors du cours|ⓘ]]

### Boosting

- Les modèles diffèrent par leur capacité de généralisation ; vote ou moyenne.
- Construction itérative : chaque modèle est influencé par les précédents.
- AdaBoost.M1 : exemples pondérés ; l'erreur est la somme des poids des exemples mal classés divisée par la somme totale des poids ; la pondération permet de *se concentrer* sur certains exemples.
- Les poids initiaux valent $1/N$ (somme 1) et sont renormalisés à chaque itération pour que leur somme reste 1. [[Erreurs du cours#^e-1-pdf-du-prof|✎]]

```
Génération :
    affecter à chaque exemple le poids w = 1/N
    pour chaque itération t des k itérations :
        appliquer l'algorithme aux exemples pondérés ; stocker le modèle
        calculer l'erreur e_t (pondérée par les w_i) et la stocker
        SI e_t = 0 ou e_t > 0.5 : terminer
        SINON
            pour chaque exemple bien classé : w_i ← w_i · e_t / (1 − e_t)
            normaliser les poids (pour que la somme reste 1)
Classification :
    affecter le poids 0 à toutes les classes
    pour chaque modèle t : ajouter −log(e_t / (1 − e_t)) au poids de la classe prédite
    retourner la classe de poids maximal
```

**Discussion.** Après chaque itération, les exemples bien classés ont leur poids multiplié par $\frac{e_t}{1-e_t}$, puis on normalise (la somme reste la même) : les poids des exemples faciles (bien classés) baissent, ceux des exemples difficiles (mal classés) montent. Vote pondéré avec $W_t = -\log\frac{e_t}{1-e_t}$ ; on somme les poids par classe et on choisit la classe de poids maximal.

Lecture des formules : $W_t = \log\frac{1-e_t}{e_t}$ est positif tant que $e_t < 0{,}5$, d'autant plus grand que le modèle est bon, et nul pour $e_t = 0{,}5$. D'où l'arrêt quand $e_t > 0{,}5$ : à deux classes, un tel modèle fait pire que le hasard. Le boosting n'attend de chaque modèle que d'être un peu meilleur que le hasard (*apprenant faible*, souvent un arbre à un seul nœud, le *decision stump*) et en combine beaucoup pour obtenir un classifieur fort. [[Complément hors du cours|ⓘ]]

AdaBoost (*Adaptive Boosting*) est dû à Y. Freund et R. Schapire (1995-1997). Là où le bagging réduit surtout la variance, le boosting réduit aussi le biais ; en contrepartie, il est séquentiel (pas de calcul en parallèle) et sensible au bruit, puisque les exemples mal étiquetés, toujours mal classés, voient leur poids grimper. Le *gradient boosting* (XGBoost, LightGBM) en est la forme moderne, très utilisée sur les données tabulaires. [[Complément hors du cours|ⓘ]]

### Forêt aléatoire

[[Forêt aléatoire]] : application du bagging au cas d'un algorithme qui construit des arbres. Le but est de rendre les arbres plus **indépendants** entre eux, ce qui rend le vote des « experts » plus efficace. Approche très fructueuse en grande dimension.

![[Data mining prof - p69.jpg]]
*Figure : toutes les données → sous-ensembles aléatoires → un arbre chacun ; à chaque nœud, on tire un petit sous-ensemble de variables et on choisit la meilleure coupe.*

**Algorithme.**
- $z = \{(x_1, y_1), \dots, (x_n, y_n)\}$ : échantillon d'apprentissage, $x_i$ décrit par $p$ variables explicatives.
- Pour $t = 1, \dots, K$ ($K$ arbres) : tirer $z_t$ avec remise dans $z$ ; estimer un arbre sur $z_t$ en tirant uniformément, à chaque nœud, $q$ variables parmi $p$.
- On obtient $K$ arbres qu'on moyenne (régression) ou fait voter (classification).
- Les forêts aléatoires sont dues à L. Breiman (2001), l'un des auteurs de CART. Les valeurs de $q$ recommandées par défaut sont $q \approx \sqrt{p}$ en classification et $q \approx p/3$ en régression ; les arbres sont en général poussés au bout sans élagage, le vote corrigeant leur surapprentissage. Plus $q$ est petit, plus les arbres sont différents (moins corrélés), mais chacun est moins bon. [[Complément hors du cours|ⓘ]]
- Une forêt fournit aussi l'erreur *out-of-bag* (chaque exemple est prédit par les arbres qui ne l'ont pas vu) et une **importance des variables** (baisse moyenne de l'impureté qu'elles apportent, ou perte de performance quand on mélange leurs valeurs) : elle compense en partie la perte de lisibilité par rapport à un arbre seul, qu'on lit comme un ensemble de règles. [[Complément hors du cours|ⓘ]]

## 5. Exercices

Le document ne donne aucune correction.

### Exercice 1 — arbres de formules booléennes
Trouver des arbres de décision pour :
1. $A \wedge \neg B$ ;
2. $A \vee (B \wedge C)$ ;
3. $A \text{ XOR } B$ ;
4. $(A \wedge B) \vee (C \wedge D)$.

Appliquer ID3 (via Weka) à ces exemples et commenter.

Correction proposée (V = vrai, F = faux) : [[Complément hors du cours|ⓘ]]
1. Racine A ; A = F → F ; A = V → test B (B = V → F, B = F → V). [[Complément hors du cours|ⓘ]]
2. Racine A ; A = V → V ; A = F → test B ; B = F → F ; B = V → test C (C = V → V, C = F → F). [[Complément hors du cours|ⓘ]]
3. Racine A, puis B sous chaque branche, quatre feuilles : aucun arbre plus petit ne convient, car la valeur de A seule ne dit rien de la sortie. Sur la table de vérité complète (2 V, 2 F), chaque fils de A ou de B garde un V et un F : le gain des deux attributs à la racine est nul, et ID3 choisit au hasard. C'est la limite d'un critère glouton, qui ne voit qu'un attribut à la fois. [[Complément hors du cours|ⓘ]]
4. Racine A ; A = V → B ; B = V → V ; B = F → sous-arbre de $C \wedge D$ ; A = F → le même sous-arbre de $C \wedge D$ (C puis D). Le sous-arbre apparaît deux fois : un arbre représente mal une disjonction de conjonctions sans variable commune (problème de **réplication**), alors que la formule tient en deux règles. [[Complément hors du cours|ⓘ]]

### Exercice 2 — entropie et gain

| Instance | Classe | a1 | a2 |
|---|---|---|---|
| 1 | + | T | T |
| 2 | + | T | T |
| 3 | − | T | F |
| 4 | + | F | F |
| 5 | − | F | T |
| 6 | − | F | T |

1. Calculer l'entropie de l'ensemble selon la classe.
2. Calculer le gain de l'attribut a2.

Correction proposée : 3 + et 3 −, donc $I(3,3) = 1$ bit. Pour a2 : T → instances 1, 2, 5, 6 (2 +, 2 −), F → instances 3, 4 (1 +, 1 −), deux fils d'entropie 1, d'où $gain(a2) = 1 - \left(\frac{4}{6} \times 1 + \frac{2}{6} \times 1\right) = 0$. Pour comparer, a1 donne T → (2 +, 1 −) et F → (1 +, 2 −), $I(2,1) \approx 0{,}918$, $gain(a1) \approx 1 - 0{,}918 = 0{,}082$ : a1 serait choisi. [[Complément hors du cours|ⓘ]]

### Exercice 3
Appliquer ID3 au jeu météo pour trouver l'arbre de décision.

Correction proposée : OUTLOOK à la racine (gains calculés plus haut). Branche overcast : 4 P, feuille P. Branche sunny (exemples 1, 2, 8, 9, 11 : 2 P, 3 N, $I = 0{,}971$) : gain(HUMI.) $= 0{,}971$ (strong → 3 N, normal → 2 P, fils purs), gain(TEMP.) $\approx 0{,}571$, gain(WIND) $\approx 0{,}020$ ; on teste HUMI. Branche rainy (exemples 4, 5, 6, 10, 14 : 3 P, 2 N) : gain(WIND) $= 0{,}971$ (no → 3 P, yes → 2 N), gain(TEMP.) et gain(HUMI.) $\approx 0{,}020$ ; on teste WIND. Toutes les feuilles sont pures : c'est l'arbre de la figure, avec les cinq règles du début. [[Complément hors du cours|ⓘ]]
