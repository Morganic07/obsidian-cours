---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF cours data mining du prof ([[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]) (73 diapositives beamer, « Introduction to Data Mining », daté du 30 septembre 2026, ID4 Introduction to Machine Learning), dans [[Data mining (index)]]. Le cours est en anglais, avec la dernière partie en français. C'est la version du cours dont [[1 - intro to data mining (résumé)]] résume la note ; ce PDF ajoute des diapositives (processus, CART détaillé, exercices). Les figures ont été ouvertes et sont intégrées ci-dessous.

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

### Validation d'un classifieur

[[Validation d'un classifieur]].

**Validation 1.**
- L'erreur $Er$ est la probabilité que le classifieur ne prédise pas correctement la valeur cible d'une donnée ; taux de réussite $1 - Er$.
- L'erreur d'entraînement est mesurée sur l'[[Ensemble d'entraînement et de test|ensemble d'entraînement]].
- Il faut un ensemble d'entraînement $X_{train}$ et un ensemble de test $X_{test}$ (valeur cible connue) pour estimer l'erreur.

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

**Validation 4 : validation croisée.** Couper le jeu en $n$ sous-ensembles disjoints de même taille, chaque valeur cible apparaissant dans chacun. Avec A, B, C : $CL_{A\cup B}$ est le classifieur construit sur $A \cup B$, $Er_C$ son erreur sur C ; trois tests $(CL_{A\cup B}, Er_C)$, $(CL_{C\cup A}, Er_B)$, $(CL_{C\cup B}, Er_A)$ ; erreur globale
$$Er = \frac{Er_A + Er_B + Er_C}{3}.$$

![[Data mining prof - p25.jpg]]
*Figure : validation croisée à $k = 4$ plis, le bloc de test se déplace à chaque itération.*

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
- Inertie intra-classes $I_W = \sum_{i=1}^{k} I_i$ ; inter-classes $I_B = \sum_{i=1}^{k} w_i\, d^2(g_i, g)$, $w_i = \frac{|g_i|}{N}$ ; $I = I_W + I_B$.
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
- saut moyen : la distance entre centroïdes est minimale ;
- **[[Méthode de Ward]]** : perte minimale de $I_W$, $S_{G_i,G_j} = \dfrac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j)$, avec $w_i = \frac{|G_i|}{N}$, $w_j = \frac{|G_j|}{N}$.

![[Data mining prof - p34.jpg]]
*Figure : la diapositive des critères de fusion, avec le dendrogramme.*

### Exercice (clustering)

Points de $\mathbb{R}$ : $x_1 = 1$, $x_2 = 2$, $x_3 = 9$, $x_4 = 12$, $x_5 = 20$.
1. Appliquer k-means avec :
   1. $k = 2$, $g_1 = 1$ et $g_2 = 20$ ;
   2. $k = 2$, $g_1 = 2$ et $g_2 = 9$ ;
   3. $k = 3$, $g_1 = 1$, $g_2 = 9$ et $g_3 = 12$.
2. Appliquer la classification hiérarchique ascendante avec le saut minimal.

Pas de correction dans le document.

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

**Interpréter l'arbre** : règles « IF OUTLOOK = sunny & HUMI = strong THEN PLAY = N », etc. (mêmes règles que plus haut, avec PLAY au lieu de CLASS). La classe Play = P est décrite par :
$$(OUTLOOK = overcast \wedge HUMI = normal) \vee (OUTLOOK = overcast) \vee (OUTLOOK = rainy \wedge WIND = no)$$
(tel quel dans le cours ; voir les points à vérifier).

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

**Info-choose : la quantité d'information.**
- Information d'un sous-ensemble de cardinal $n$ tiré de $N$ événements : $Q = \log_2 \frac{N}{n}$ (1).
- [[Entropie (théorie de l'information)|Entropie]] d'une partition $E_1, \dots, E_k$ ($|E_i| = n_i$, $p_i = \frac{n_i}{N}$) : $I(\text{partition}) = \sum_{i=1}^{k} \frac{n_i}{N}\log_2 \frac{N}{n_i} = \sum_{i=1}^{k} p_i\log_2 \frac{1}{p_i}$.
- Information émise par l'arbre : $I(E) = \sum_{i=1}^{NC} p_i\log_2\frac{1}{p_i}$ (2), $p_i$ fréquence de la classe $i$, $NC$ nombre de classes.
- Information moyenne après un test $T$ : $\sum_{l=1}^{k} W_l\, I(E_l^T)$, $W_l$ proportion d'exemples dans $E_l^T$.
- **[[Gain d'information]]** : $gain(T) = I(E) - \sum_{l=1}^{k} W_l\, I(E_l^T)$.
- Deux classes ($p$ positifs, $n$ négatifs) :
$$I(p,n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n} \quad (3), \qquad gain(T) = I(p,n) - \sum_{i=1}^{k}\frac{p_i+n_i}{p+n}\, I(p_i, n_i).$$

**Exemple (PlayTennis).**
$$gain(OUTLOOK) = I(9,5) - \left(\tfrac{5}{14}I(2,3) + \tfrac{4}{14}I(4,0) + \tfrac{5}{14}I(3,2)\right) = 0{,}246 \text{ bits},$$
contre gain(TEMP.) $= 0{,}029$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$ bits : OUTLOOK à la racine.

![[Data mining prof - p48.jpg]]
*Figure : le calcul du gain d'outlook et la partition correspondante.*

### L'algorithme C4.5

[[Algorithme C4.5]], descendant d'ID3 :
- attributs continus traités par discrétisation ;
- normalisation du gain : $SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2\frac{|T_i|}{|T|}$ (4), $GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}$ ([[Rapport de gain]]) ;
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

![[Data mining prof - p53.jpg]]
*Figure : le nœud windy (false : 6 yes / 2 no ; true : 3 yes / 3 no) et le calcul de Gini.*

![[Data mining prof - p54.jpg]]
*Figure : indice de Gini pour 20 individus et 2 classes, parabole de maximum 0,5 à 10 individus.*

**Construction de l'arbre.**
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

### Boosting

- Les modèles diffèrent par leur capacité de généralisation ; vote ou moyenne.
- Construction itérative : chaque modèle est influencé par les précédents.
- AdaBoost.M1 : exemples pondérés ; l'erreur est la somme des poids des exemples mal classés divisée par la somme totale des poids ; la pondération permet de *se concentrer* sur certains exemples.

```
Génération :
    affecter à chaque exemple le poids w = 1/N
    pour chaque itération t des k itérations :
        appliquer l'algorithme aux exemples pondérés ; stocker le modèle
        calculer l'erreur e_t (pondérée par les w_i) et la stocker
        SI e_t = 0 ou e_t > 0.5 : terminer
        SINON
            pour chaque exemple bien classé : w_i ← w_i · e_t / (1 − e_t)
            normaliser les poids (pour que la somme soit N)
Classification :
    affecter le poids 0 à toutes les classes
    pour chaque modèle t : ajouter −log(e_t / (1 − e_t)) au poids de la classe prédite
    retourner la classe de poids maximal
```

**Discussion.** Après chaque itération, les exemples bien classés ont leur poids multiplié par $\frac{e_t}{1-e_t}$, puis on normalise (la somme reste la même) : les poids des exemples faciles (bien classés) baissent, ceux des exemples difficiles (mal classés) montent. Vote pondéré avec $W_t = -\log\frac{e_t}{1-e_t}$ ; on somme les poids par classe et on choisit la classe de poids maximal.

### Forêt aléatoire

[[Forêt aléatoire]] : application du bagging au cas d'un algorithme qui construit des arbres. Le but est de rendre les arbres plus **indépendants** entre eux, ce qui rend le vote des « experts » plus efficace. Approche très fructueuse en grande dimension.

![[Data mining prof - p69.jpg]]
*Figure : toutes les données → sous-ensembles aléatoires → un arbre chacun ; à chaque nœud, on tire un petit sous-ensemble de variables et on choisit la meilleure coupe.*

**Algorithme.**
- $z = \{(x_1, y_1), \dots, (x_n, y_n)\}$ : échantillon d'apprentissage, $x_i$ décrit par $p$ variables explicatives.
- Pour $t = 1, \dots, K$ ($K$ arbres) : tirer $z_t$ avec remise dans $z$ ; estimer un arbre sur $z_t$ en tirant uniformément, à chaque nœud, $q$ variables parmi $p$.
- On obtient $K$ arbres qu'on moyenne (régression) ou fait voter (classification).

## 5. Exercices

Le document ne donne aucune correction.

### Exercice 1 — arbres de formules booléennes
Trouver des arbres de décision pour :
1. $A \wedge \neg B$ ;
2. $A \vee (B \wedge C)$ ;
3. $A \text{ XOR } B$ ;
4. $(A \wedge B) \vee (C \wedge D)$.

Appliquer ID3 (via Weka) à ces exemples et commenter.

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

### Exercice 3
Appliquer ID3 au jeu météo pour trouver l'arbre de décision.

## Points à vérifier

1. **Poids du boosting** : le poids initial est $1/N$ mais l'étape de normalisation vise une somme égale à $N$ (déjà signalé dans [[1 - intro to data mining (résumé)]]).
2. **Description de la classe P** : la formule $(\text{OUTLOOK} = \text{overcast} \wedge \text{HUMI} = \text{normal}) \vee (\text{OUTLOOK} = \text{overcast}) \vee (\text{OUTLOOK} = \text{rainy} \wedge \text{WIND} = \text{no})$ ne correspond pas aux règles de l'arbre : elle oublie la branche `sunny ET HUMI = normal` et répète `overcast` (complément : comparaison avec les règles données juste au-dessus).
3. **Formule de la validation croisée** : le texte de la diapositive 24 se lit « $Er = \frac{Er_A + Er_B + Er_C}{3}$ », mais l'extraction du PDF a mêlé le 3 au milieu (« ErA + Er3B + ErC ») ; la forme ci-dessus est la seule cohérente.
4. **Coquilles du support** : « normale » à la ligne 10 du jeu météo ; « CLASSE = P » dans les règles ; « Hiererachical », « labaled », « Chose », « estimante », « loose » (pour *loss*) ; la règle « IF OUTLOOK = overcast THEN CLASSE = P » reste écrite avec CLASSE quand les autres règles passent à PLAY.
5. **Libellés du jeu météo** : le tableau utilise TEMP. high / mild / low, HUMI. strong / normal, Wind yes / no, tandis que les figures d'ID3 utilisent hot / mild / cool, high / normal, false / true, ou des libellés français (CIEL, VENT, Haute / Normale).
6. **Affectation de classe, fils 2** : égalité P(3) / N(3) ; le cours affecte « P ?? » sans donner de règle pour départager.
