---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]], dans [[Cours/Informatique/Data mining/_index|Data mining]]. En cas d'écart, le cours et ses images font foi.

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

### Validation d'un classifieur

![[Chp1 - intro to data mining - image15.png]]
*Figure : la base est séparée en données d'entraînement (construction du modèle) et de test ; si la précision est acceptable, le modèle est appliqué à des données inconnues pour prédire leur valeur.*

**Validation 1.**
- L'erreur $Er$ d'un classifieur est la probabilité qu'il ne prédise pas correctement la valeur cible d'une donnée. Le taux de réussite est $1 - Er$.
- L'erreur d'entraînement est mesurée sur l'[[Ensemble d'entraînement et de test|ensemble d'entraînement]] (qui sert à construire le classifieur).
- Pour estimer la qualité, il faut un ensemble d'entraînement $X_{train}$ et un ensemble de test $X_{test}$ (où la valeur cible est connue pour chaque exemple) pour estimer l'erreur.

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

**Exemple : filtre anti-spam** sur 100 e-mails (en réalité 20 spams, positifs, et 80 légitimes, négatifs) :

| | Prédit spam | Prédit non-spam | Total réel |
|---|---|---|---|
| Réellement spam | **15** (VP) | **5** (FN) | 20 spams |
| Réellement non-spam | **2** (FP) | **78** (VN) | 80 légitimes |

- Réussites (diagonale) : 15 VP, spams bien filtrés ; 78 VN, e-mails légitimes restés dans la boîte.
- Erreurs : **2 FP** (fausse alerte, [[Erreur de type I et de type II|erreur de type I]]) : 2 e-mails importants classés spams, erreur pénalisante ; **5 FN** (manqués, erreur de type II) : 5 spams arrivés dans la boîte, désagrément rarement bloquant.
- **Précision** $= \frac{15}{15+2} \approx 88{,}2\,\%$ : parmi ce que le filtre a classé spam, la part de vrais spams (on minimise les FP).
- **Rappel / sensibilité** $= \frac{15}{15+5} = 75\,\%$ : parmi tous les vrais spams, la part interceptée (on minimise les FN, vital en diagnostic médical).

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

### Travaux pratiques annoncés

- **Jeux de données** : Weather (attributs qualitatifs), IRIS (quantitatifs).
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

- **Inertie intra-classes** (*intra-cluster*), si $I_1, \dots, I_k$ sont les inerties des groupes : $I_W = \sum_{i=1}^{k} I_i$.
- **Inertie inter-classes** : $I_B = \sum_{i=1}^{k} w_i\, d^2(g_i, g)$ avec $w_i = \frac{|g_i|}{N}$.
- Décomposition : $I = I_W + I_B$.
- But : des groupes denses et si possible bien séparés : **minimiser $I_W$**.

**Algorithme** (entrée : $X$, $K \in \mathbb{N}$, $I \leftarrow \infty$) :
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
- **saut moyen** : la distance entre les centroïdes est minimale ;
- **[[Méthode de Ward]]** : perte minimale d'inertie $I_W$, avec
$$S_{G_i,G_j} = \frac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j), \qquad w_i = \frac{|G_i|}{N}.$$

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
- [[Entropie (théorie de l'information)|Entropie]] d'une partition $E_1, \dots, E_k$ de $E$ ($|E| = N$, $|E_i| = n_i$, $p_i = \frac{n_i}{N}$) :
$$I(\text{partition}) = \sum_{i=1}^{k} \frac{n_i}{N}\log_2 \frac{N}{n_i} = \sum_{i=1}^{k} p_i \log_2 \frac{1}{p_i}.$$
- L'arbre est une source d'information qui émet
$$I(E) = \sum_{i=1}^{NC} p_i \log_2 \frac{1}{p_i} \qquad (2)$$
où $p_i$ est la fréquence de la classe $i$ dans $E$ et $NC$ le nombre de classes.
- Information moyenne des $k$ sous-ensembles obtenus par un test $T$ : $\sum_{l=1}^{k} W_l\, I(E_l^T)$, où $W_l$ est la proportion d'exemples dans $E_l^T$.
- **[[Gain d'information]]** : $gain(T) = I(E) - \sum_{l=1}^{k} W_l\, I(E_l^T)$.

**Cas à deux classes** ($p$ positifs, $n$ négatifs) :
$$I(p, n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n} \qquad (3)$$
$$gain(T) = I(p, n) - \sum_{i=1}^{k}\frac{p_i+n_i}{p+n}\, I(p_i, n_i).$$

**Exemple (PlayTennis).**
$$gain(OUTLOOK) = I(9,5) - \left(\tfrac{5}{14} I(2,3) + \tfrac{4}{14} I(4,0) + \tfrac{5}{14} I(3,2)\right) = 0{,}246 \text{ bits},$$
contre gain(TEMP.) $= 0{,}029$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$ bits : OUTLOOK, de gain maximal, est placé à la racine.

![[Chp1 - intro to data mining - image34.png]]
*Figure : la partition selon outlook utilisée dans le calcul du gain.*

### Algorithme C4.5

[[Algorithme C4.5]], descendant d'ID3 :
- traite les **attributs continus** par des méthodes de discrétisation ;
- **normalise le gain** :
$$SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2 \frac{|T_i|}{|T|} \qquad (4), \qquad GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}$$
  (le [[Rapport de gain]]) ;
- regroupe des valeurs d'attributs ;
- traite les **[[Valeur manquante|valeurs manquantes]]** : si la valeur de $a_i$ manque pour un exemple, on partitionne l'ensemble d'apprentissage en $n$ groupes selon les $n$ valeurs possibles de $a_i$ ; l'exemple est affecté à chaque groupe avec une probabilité égale à la fréquence du groupe ; cette probabilité est prise en compte dans le calcul du gain et propagée dans l'arbre ;
- **[[Élagage]]** (*pruning*) de l'arbre.

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

![[Chp1 - intro to data mining - image23.png]]
*Figure : le nœud windy et ses deux branches (false : 6 yes / 2 no ; true : 3 yes / 3 no).*

![[Chp1 - intro to data mining - image27.png]]
*Figure : indice de Gini pour 20 individus et 2 classes en fonction du nombre d'individus de la classe 1 : parabole nulle en 0 et 20, maximale (0,5) en 10.*

## 5. Combinaison de plusieurs modèles

[[Méthodes d'ensemble]].

![[Chp1 - intro to data mining - image25.png]]
*Figure : des échantillons tirés des exemples d'apprentissage alimentent chacun un algorithme d'apprentissage ; les classifieurs obtenus sont combinés pour prédire sur de nouvelles données.*

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

### Boosting (AdaBoost.M1)

- Les modèles diffèrent par leur capacité de généralisation ; le boosting repose sur le vote ou la moyenne.
- Les modèles sont construits **itérativement** : chacun est influencé par les précédents.
- AdaBoost.M1 : les exemples sont **pondérés** ; l'erreur est la somme des poids des exemples mal classés divisée par la somme totale des poids. La pondération permet au classifieur de *se concentrer* sur certains exemples.

**Génération des modèles.**
```
affecter le même poids w = 1/N à chaque exemple
pour chaque itération t des k itérations :
    appliquer l'algorithme d'apprentissage aux exemples pondérés
    stocker le modèle
    calculer l'erreur e_t sur l'ensemble d'apprentissage (pondérée par les w_i) et la stocker
    SI e_t = 0 ou e_t > 0.5 : terminer
    SINON
        pour chaque exemple bien classé : w_i ← w_i · e_t / (1 − e_t)
        normaliser les poids (pour que la somme soit N)
```
- Les poids des exemples bien classés (faciles) diminuent ; après normalisation (la somme restant la même), ceux des exemples mal classés (difficiles) augmentent.

**Classification (vote pondéré).**
```
affecter le poids 0 à toutes les classes
pour chaque modèle t : ajouter −log(e_t / (1 − e_t)) au poids de la classe qu'il prédit
retourner la classe de poids maximal
```
Poids du modèle $t$ : $W_t = -\log \frac{e_t}{1-e_t}$.

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

## Erreurs du cours

Les formules et l'algorithme de cette fiche sont écrits sous leur forme corrigée ; voici ce que le cours écrit.

- [[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]], inertie intra-classes (vérifié sur l'image) : écrit « Let $I_1, .., I_n$ inertias of clusters $g_1 ... g_k$ : $I_w = \sum_{i=1}^{k} I_k$ » ; il faut $I_W = \sum_{i=1}^{k} I_i$, avec $I_1, \dots, I_k$ (comme dans la puce suivante).
- Même document, algorithme des k-means (vérifié sur l'image) : écrit « For $k \in \{1..k\}$ » pour la mise à jour des centroïdes ; il faut $k \in \{1..K\}$. L'image mélange aussi $I_w$ et $I_W$. L'ordre « $I \leftarrow I_w$ » puis « Compute $I_w$ » est juste : on garde l'ancienne inertie avant de calculer la nouvelle, puis on compare les deux.
- Même document, entropie d'une partition (vérifié sur l'image) : écrit $I(\text{partition}) = \sum_{i=1}^{m} \frac{n_i}{N}\log_2 \frac{N}{n_i}$ ; il faut une somme jusqu'à $k$, nombre de sous-ensembles $E_1, \dots, E_k$ (la deuxième écriture de la diapositive va bien jusqu'à $k$).
- Même document, boosting (vérifié sur l'image) : affecte d'abord le poids $w = \frac{1}{N}$ à chaque exemple (somme 1), puis normalise les poids « pour que la sommes soit N » ; il faut une seule convention : la somme 1 avec des poids initiaux $1/N$, ou la somme $N$ avec des poids initiaux de 1. L'autre diapositive dit « pour que la somme reste la même pour toutes les itérations » (complément).
- Même document, figure « Combinaison de plusieurs modèles » (vérifié sur l'image) : étiquette les trois échantillons « Test Sample 1 » à « Test Sample 3 » ; il faut des échantillons d'**apprentissage** : ils sont tirés des « Training Examples » et servent à entraîner chaque classifieur (déduit du schéma).
