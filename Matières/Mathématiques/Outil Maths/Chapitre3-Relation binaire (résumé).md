---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du support du professeur Chapitre 3 - Relation binaire (PDF) ([[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]) (28 diapositives, Outils Mathématiques, semestre 1, novembre 2023), dans [[Outil Maths (matière)]]. Version du professeur du cours déjà résumé dans [[Chapitre 3 - Relation binaire (résumé)]]. Notions : [[Relation binaire]], [[Relation d'équivalence]], [[Relation d'ordre]]. La page de titre porte « Chapitre 3-Ensemble Binaire » (coquille pour « Relation binaire »).

## 1. Motivation : des équivalences partout (diapositive 2)

« Sans le savoir vous vivez dans un monde d'équivalences ! »

1. **Heures** : 18:45 ∼ 6:45 PM ∼ 7 h moins le quart.
2. **Rationnels** : $3/2,\ 6/4,\ 9/6$ sont équivalents, de même que $1/2,\ 2/4,\ 3/6$ (voir [[Nombre rationnel]]).
3. **Ensembles** : la définition des ensembles repose sur une équivalence qui dit que $\{1,2\}$, $\{2,1\}$, $\{1,1,1,1,2\}$ et $\{1,2,1,2\}$ sont le même ensemble (voir [[Ensemble (mathématiques)]]).
4. **Sacs d'aspirateur** : un même sac convient à plusieurs marques. Hoover 500 ∼ Miele Boost ∼ Rowenta Plus ; Dyson ∼ Air pulse II ∼ Philips Clean (« qui n'ont pas de sacs… ») ; mais Hoover 500 ≁ Dyson.

## 2. Relations binaires

### Définition (diapositive 3)

Soient deux ensembles $A$ et $B$. Une **relation binaire** entre $A$ et $B$ est un sous-ensemble $R$ de $A \times B$ (voir [[Produit cartésien]]). Si $(a, b) \in R$, on dit que $a$ est relié à $b$ par $R$ et on écrit $aRb$. $R$ est une relation binaire **sur** $A$ si c'est une relation entre $A$ et $A$.

- Le **domaine** de $R$ est l'ensemble de toutes les premières coordonnées des couples de $R$ ; le **rang** de $R$ est l'ensemble de toutes les deuxièmes coordonnées (voir [[Domaine et rang d'une relation]]).
- Exemple : sur l'ensemble $A$ des droites du plan, la perpendicularité est une relation binaire.

### Exemples (diapositive 4)

Soient $A = \{a, b, c, d, e\}$ l'ensemble des élèves et $B = \{\text{Math}, \text{Info}, \text{Ang}, \text{Phys}\}$ l'ensemble des cours.

- $G$ décrit si un étudiant suit un cours régulièrement :
  $G = \{(a, \text{Math}), (a, \text{Phys}), (b, \text{Info}), (c, \text{Ang}), (d, \text{Ang}), (e, \text{Math}), (e, \text{Ang})\}$.
- $S$ décrit si un étudiant a acheté un cadeau à un autre étudiant :
  $G_S = \{(b, a), (a, a), (c, a), (a, d), (d, c)\}$.

### Modes de représentation (diapositive 5)

Voir [[Représentation d'une relation binaire]].

- **Diagramme cartésien et matrice de la relation** : un tableau avec les éléments de départ en lignes, ceux d'arrivée en colonnes, et un V dans la case $(x, y)$ si $xRy$.
- **Diagramme sagittal** : une flèche de $x$ vers $y$ si $xRy$ ; pour une relation sur un seul ensemble, les éléments sont des sommets, et $xRx$ est une boucle.

Matrice de $G$ (élèves et cours) telle que donnée :

| $G$ | Math | Phys | Ang | Info |
|---|---|---|---|---|
| a | V | V | | |
| b | | | | V |
| c | | | V | |
| d | | | V | |
| e | V | | V | |

![[Chapitre3-Relation binaire - p5.jpg]]
*Figure : matrices des relations $G$ (élèves et cours) et $S$ (cadeaux), puis leurs diagrammes sagittaux (diapositive 5).*

### Relation fonctionnelle (diapositive 6)

Une fonction $f : E \to F$ associe à chaque élément de $E$ au plus un élément de $F$. On lui associe la relation $R_f$ définie par le graphe
$$G_f = \{(x, f(x)) : x \in E\} \subseteq E \times F.$$
Réciproquement, si pour tout $x \in E$ il y a au plus un $y \in F$ tel que $xRy$, on peut associer à $R$ une fonction $f$ telle que $f(x) = y \iff xRy$. On dit que $R$ est une **[[Relation fonctionnelle]]** (voir [[Graphe d'une fonction]], [[Chapitre4-Fonctions (1) (résumé)]]).

## 3. Propriétés d'une relation sur un ensemble

Exemple filé (diapositives 7, 9, 11) : sur $\mathbb{R}^2$, $(x, y)\,R\,(x', y') \iff x = x'$.

### Réflexivité (diapositives 7 et 8)

**Définition.** $R$ sur $E$ est **réflexive** si $\forall a \in E,\ aRa$ (voir [[Relation réflexive]]).

- Exemple filé : $(x, y)R(x, y)$ car $x = x$.
- Diagramme cartésien : la diagonale doit être cochée. Diagramme sagittal : chaque sommet a une boucle.
- Exemples : quel que soit l'ensemble, l'égalité $=$ est réflexive. Sur $\mathbb{N}$, $\le$ est réflexive, $<$ ne l'est pas.

![[Chapitre3-Relation binaire - p8.jpg]]
*Figure : relation réflexive sur $\{1, 2, 3\}$, diagramme sagittal (une boucle par sommet) et matrice à diagonale pleine (diapositive 8).*

### Symétrie et antisymétrie (diapositives 9 et 10)

**Définitions** (voir [[Relation symétrique]], [[Relation antisymétrique]]).

- $R$ est **symétrique** si $\forall a, b \in E,\ aRb \Rightarrow bRa$.
- $R$ est **antisymétrique** si $\forall a, b \in E,\ (a \neq b \wedge aRb) \Rightarrow \neg(bRa)$.
- Caractérisation équivalente : $R$ est antisymétrique si et seulement si $\forall a, b \in E,\ (aRb \wedge bRa) \Rightarrow a = b$.

Exemple filé, symétrie : si $(x, y)R(x', y')$, alors $x = x'$, ce qui s'écrit aussi $x' = x$, c'est-à-dire $(x', y')R(x, y)$.

Lecture graphique de la symétrie : le diagramme cartésien est symétrique par rapport à la diagonale ; dans le diagramme sagittal, toute flèche de $a$ vers $b$ a sa flèche retour de $b$ vers $a$. Exemples : l'égalité est symétrique quel que soit l'ensemble ; $\le$ sur $\mathbb{N}$ ne l'est pas.

![[Chapitre3-Relation binaire - p10.jpg]]
*Figure : relation symétrique sur $\{1, 2, 3\}$ et sa matrice symétrique par rapport à la diagonale (diapositive 10).*

### Antisymétrie, lecture graphique (diapositive 12)

Une relation est antisymétrique si pour tous $x, y \in E$ vérifiant $xRy$ et $yRx$ on a $x = y$. Exemple : sur $\mathbb{N}$, $\le$ est antisymétrique. Le support donne aussi un contre-exemple dont le symbole est illisible (voir « Points à vérifier »).

![[Chapitre3-Relation binaire - p12.jpg]]
*Figure : relation antisymétrique sur $\{1, 2, 3, 4\}$ : aucune paire de flèches aller-retour entre deux sommets distincts (diapositive 12).*

### Transitivité (diapositives 11 et 13)

**Définition.** $R$ est **transitive** si $(aRb \wedge bRc) \Rightarrow aRc$ (voir [[Relation transitive]]).

- Exemple filé : si $(x, y)R(x', y')$ et $(x', y')R(x'', y'')$, alors $x = x'$ et $x' = x''$, donc $x = x''$, c'est-à-dire $(x, y)R(x'', y'')$.
- Diagramme sagittal : tout chemin qui part d'un sommet $s$ et va à un sommet $s'$ en suivant les flèches admet un **raccourci**, c'est-à-dire un chemin de longueur un de $s$ à $s'$.
- Exemples : l'égalité est transitive quel que soit l'ensemble ; $\le$ sur $\mathbb{N}$ est transitive.

![[Chapitre3-Relation binaire - p13.jpg]]
*Figure : relation transitive sur $\{1, 2, 3, 4\}$ et sa matrice (diapositive 13).*

## 4. Relations d'équivalence

### Définition et classes (diapositive 14)

Soient $E$ un ensemble non vide et $R$ une relation binaire sur $E$. $R$ est une **[[Relation d'équivalence]]** si elle est réflexive, symétrique et transitive.

Pour $a \in E$, la **classe d'équivalence** de $a$ est
$$[a] = \{x \in E \mid aRx\}.$$
Tout $x \in [a]$ est un **représentant** de la classe.

**Théorème.** L'ensemble des classes d'équivalence de $R$ forme une partition de $E$. Réciproquement, toute partition de $E$ définit une relation d'équivalence sur $E$ (voir [[Partition d'un ensemble]]).

### Ensemble quotient (diapositives 15 et 20)

**Définition.** L'ensemble des classes d'équivalence de $R$ sur $E$ est l'**ensemble quotient** de $E$ par $R$, noté $E/R$ :
$$E/R = \{[a] \mid a \in E\}.$$

Notation alternative : $\mathrm{Cl}(a) = \{x \in A \mid x \sim a\}$.

Exemples (sacs d'aspirateur) : $\mathrm{Cl}(\text{Hoover 500}) = \{\text{Hoover 500}, \text{Miele Boost}, \text{Rowenta Plus}\}$, et $\mathrm{Cl}(\text{Hoover 500}) = \mathrm{Cl}(\text{Miele Boost}) = \mathrm{Cl}(\text{Rowenta Plus})$ puisque ces trois références sont équivalentes.

**Théorème** (diapositive 20). Pour une relation d'équivalence sur $E$, l'application
$$f : E \to E/R,\quad x \mapsto \mathrm{Cl}(x)$$
est surjective (voir [[Injectivité et surjectivité]]).

### Exemple détaillé (diapositive 16)

Sur $\mathbb{R}$ : $xRy \iff x^2 - y^2 = x - y$.

1. On remarque que $xRy \iff x^2 - x = y^2 - y$. Avec cette formulation ($xRy \iff g(x) = g(y)$ pour $g(t) = t^2 - t$), il est facile de vérifier que $R$ est réflexive, symétrique et transitive.
2. Classe de $x$ : $\mathrm{Cl}(x) = \{y \in \mathbb{R} \mid xRy\}$. $y = x$ est solution (réflexivité). Pour $y \neq x$ : $x^2 - y^2 = (x - y)(x + y)$, donc l'équation devient $(x - y)(x + y) = x - y$, d'où $x + y = 1$ en divisant par $x - y \neq 0$, soit $y = 1 - x$. Conclusion :
$$\mathrm{Cl}(x) = \{x,\ 1 - x\}.$$

### Partition (diapositive 19)

**Définition** (telle que donnée). Une famille d'ensembles $(A_i)_{i \in I}$ est une **partition** de $E$ si :
- $E = \bigcup_{i \in I} A_i$ ;
- deux éléments distincts de la famille sont disjoints : si $i \neq j$ alors $A_i \cap A_j = \emptyset$ (voir [[Ensembles disjoints]]).

**Théorème.** Étant donnée une relation d'équivalence sur un ensemble, les classes d'équivalence forment une partition.

## 5. Relations d'ordre

### Définitions (diapositives 17 et 22)

- $R$ est un **ordre partiel** sur $E$ si elle est réflexive, antisymétrique et transitive ; $(E, R)$ est alors un **ensemble partiellement ordonné**.
- $R$ est un **ordre total** si de plus, pour tous $x, y \in E$, $xRy$ ou $yRx$ ; $(E, R)$ est un **ensemble totalement ordonné**.

Formulation avec $\preceq$ (diapositive 22) : $\preceq$ est une [[Relation d'ordre]] sur $E$ si
- réflexive : $x \preceq x$ pour tout $x \in E$ ;
- transitive : $x \preceq y$ et $y \preceq z \Rightarrow x \preceq z$ ;
- antisymétrique : $x \preceq y$ et $y \preceq x \Rightarrow x = y$.

L'ordre est **total** si pour tous $x, y$ on a $x \preceq y$ ou $y \preceq x$ ; il est dit **partiel** pour souligner qu'on n'a pas forcément cette propriété.

### Exercice (diapositive 18)

Donner les propriétés des relations suivantes :
1. $\le$ sur $\mathbb{Z}$ ;
2. $<$ sur $\mathbb{Z}$ ;
3. l'inclusion $\subseteq$ sur un ensemble $E$ d'ensembles ;
4. $\perp$ (perpendiculaire) sur l'ensemble $L$ des droites du plan ;
5. $\parallel$ (parallèle) sur $L$.

Le support ne donne pas la correction. Éléments présents ailleurs dans le cours : $\le$ est un ordre total, $<$ n'est pas réflexif donc pas un ordre, $\subseteq$ est un ordre non total (diapositives 23-24).

### Exemples d'ordres sur les nombres (diapositive 23)

- $\le$ et $\ge$ sont des ordres totaux sur $\mathbb{N}$, qui s'étendent à $\mathbb{Z}$ et $\mathbb{R}$.
- $<$ et $>$ ne sont pas des relations d'ordre sur $\mathbb{N}$.
- Sur $\mathbb{N}^*$, la **divisibilité** $a \mid b$ (il existe $k \in \mathbb{N}^*$ tel que $b = ak$) est un ordre non total (voir [[Divisibilité]]) :
  - réflexive : $x \mid x$ pour tout $x \in \mathbb{N}^*$ ;
  - transitive : si $y = kx$ et $z = k'y$, alors $z = k'y = (kk')x$, donc $x \mid z$ ;
  - antisymétrique : si $x \mid y$ et $y \mid x$ alors $x = y$.

### Inclusion sur les parties d'un ensemble (diapositive 24)

L'inclusion $\subseteq$ est une relation d'ordre sur $\mathcal{P}(E)$, non totale (voir [[Inclusion (ensembles)]]) :
- réflexive : $A \subseteq A$ ;
- transitive : $A \subseteq B$ et $B \subseteq C \Rightarrow A \subseteq C$ ;
- antisymétrique : $A \subseteq B$ et $B \subseteq A \Rightarrow A = B$ (voir [[Double inclusion]]).

### Fonctions croissantes et décroissantes (diapositive 25)

Soient $(A, \preceq_A)$ et $(B, \preceq_B)$ deux ensembles ordonnés et $f : A \to B$ une application (voir [[Application monotone]]).

- $f$ est **croissante** si $x \preceq_A y \Rightarrow f(x) \preceq_B f(y)$.
- $f$ est **décroissante** si $x \preceq_A y \Rightarrow f(y) \preceq_B f(x)$.
- $f$ est **strictement croissante** si $x \preceq_A y$ et $x \neq y$ $\Rightarrow$ $f(x) \preceq_B f(y)$ et $f(x) \neq f(y)$.
- $f$ est **strictement décroissante** si $x \preceq_A y$ et $x \neq y$ $\Rightarrow$ $f(y) \preceq_B f(x)$ et $f(x) \neq f(y)$.

**Proposition.** Une application strictement croissante ou strictement décroissante dont l'ensemble de départ est muni d'un ordre total est injective.

### Élément minimal, minorant, borne inférieure (diapositive 26)

Soient $(E, \preceq)$ un ensemble ordonné et $A \subseteq E$.

- $x \in A$ est **minimal** dans $A$ s'il n'y a pas d'élément plus petit que lui dans $A$.
- $x \in E$ est un **minorant** de $A$ si $\forall y \in A,\ x \preceq y$ (voir [[Majorant et minorant]]).
- $A$ admet au plus un minorant appartenant à $A$ (par antisymétrie) : c'est le **plus petit élément** de $A$, noté $\min(A)$ s'il existe.
- Le plus grand des minorants est la **borne inférieure**, notée $\inf(A)$ :
$$\forall y \in A,\ \inf(A) \preceq y \quad\text{et}\quad \forall z \text{ minorant de } A,\ z \preceq \inf(A).$$

### Élément maximal, majorant, borne supérieure (diapositive 27)

- $x \in A$ est **maximal** dans $A$ s'il n'y a pas d'élément plus grand que lui dans $A$ (voir [[Élément maximal]]).
- $x \in E$ est un **majorant** de $A$ si $\forall y \in A,\ y \preceq x$.
- $A$ admet au plus un majorant appartenant à $A$ : c'est le **plus grand élément**, noté $\max(A)$ (voir [[Plus grand élément]]).
- Le plus petit des majorants est la **[[Borne supérieure]]**, notée $\sup(A)$ :
$$\forall y \in A,\ y \preceq \sup(A) \quad\text{et}\quad \forall z \text{ majorant de } A,\ \sup(A) \preceq z.$$

### Exemples (diapositive 28)

Dans $(\mathbb{R}, \le)$ :

| Partie | Majorants (exemples) | Minorants (exemples) | Maximum | Minimum |
|---|---|---|---|---|
| $[0, 1]$ | 3, 2, 1 | −2, −1, 0 | 1 | 0 |
| $]0, 1]$ | 3, 2, 1 | −2, −1, 0 | 1 | aucun |
| $]0, 1[$ | 3, 2, 1 | −2, −1, 0 | aucun | aucun |

- Dans $(\mathcal{P}(E), \subset)$ : $\emptyset$ est le minimum de $\mathcal{P}(E)$ et $E$ son maximum.
- Pour la divisibilité sur $\mathbb{N}$ : 0 est le maximum et 1 le minimum ; la partie $\{2, 3\}$ n'admet ni maximum ni minimum.
- Dans $(\mathbb{R}, \le)$ : $]1, +\infty[$ admet 1 pour borne inférieure mais n'admet pas de borne supérieure.

## Points à vérifier

- **Partition** (diapositive 19) : la définition donnée omet la condition « parties non vides », présente au [[Chapitre2-Ensemble (4) (résumé)|chapitre 2]]. Sans elle, le théorème « les classes forment une partition » reste vrai, mais la définition est incomplète (complément).
- **Divisibilité** (diapositive 28) : « 0 est le maximum (...) » pour la divisibilité sur $\mathbb{N}$. Cela vaut sur $\mathbb{N}$ entier (tout entier divise 0), alors que l'ordre a été défini sur $\mathbb{N}^*$ ; et la fin de la phrase est tronquée (« ni maximum ni minimum 3 », renvoi de note perdu). Le support est ambigu à cet endroit.
- **Minorant** : « A admet au plus un seul minorant dans A » veut dire : au plus un minorant appartenant à $A$.
- **Matrice de $S$** (diapositive 5) : la matrice dessinée (lignes a : d ; b : a, b ; c : a, b ; d : d) ne correspond pas à l'ensemble $G_S = \{(b,a), (a,a), (c,a), (a,d), (d,c)\}$ de la diapositive 4 (il y manque $(a,a)$ et $(d,c)$, et elle ajoute $(b,b)$, $(c,b)$, $(d,d)$). L'une des deux est fausse ; à comparer à l'image.
- **Contre-exemple d'antisymétrie** (diapositive 12) : « La relation ≡ sur ℤ* n'est pas antisymétrique » ; le symbole de la relation et l'ensemble sont mal rendus dans le PDF (un symbole surmonté d'un « l », puis « sur * »). Il s'agit probablement d'une congruence, sans certitude.
- **Antisymétrie de la divisibilité** (diapositive 23) : le support énonce la propriété sans la démontrer (si $y = kx$ et $x = k'y$, alors $kk' = 1$ dans $\mathbb{N}^*$, donc $k = k' = 1$ : complément).
- **Coquilles** : définition de la transitivité « alors nécessairement on a $xz$ » (lire $xRz$) ; titre « Chapitre 3-Ensemble Binaire ».
