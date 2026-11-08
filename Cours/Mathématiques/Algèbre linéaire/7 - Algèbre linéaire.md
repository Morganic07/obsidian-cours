---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 7, éléments propres d'un [[Morphisme|endomorphisme]].
## Valeur propre, vecteur propre et sous-espace propre

**Définition** : soit $f \in L(E)$. S'il existe $v$ **non nul** et $\lambda$ tels que
$$f(v) = \lambda v,$$
$\lambda$ est une [[Valeur propre|valeur propre]] et $v$ un [[Vecteur propre|vecteur propre]] associé (dessin du cours, disposition perdue).

Géométriquement, un vecteur propre indique une **direction conservée** par $f$ : $f(v)$ reste sur la droite $\text{Vect}(v)$, étiré d'un facteur $\lambda$ (retourné si $\lambda < 0$, écrasé sur $0$ si $\lambda = 0$). Exemple : pour la projection $p$ de $\mathbb{R}^2$ sur l'axe des abscisses parallèlement à l'axe des ordonnées, $p(x, y) = (x, 0)$ ; les vecteurs $(x, 0)$ non nuls sont propres pour $1$, les vecteurs $(0, y)$ non nuls sont propres pour $0$, et $\text{Sp}(p) = \{0, 1\}$. [[Complément hors du cours|ⓘ]]

- L'ensemble des valeurs propres de $f$ s'appelle le [[Spectre (algèbre linéaire)|spectre]] de $f$, noté $\text{Sp}(f)$.
- Un vecteur propre n'est jamais nul, mais une valeur propre peut être nulle : si $\text{Ker} f \neq \{0\}$ ([[Espace nul]]), il existe $u \in \text{Ker} f$ non nul avec $f(u) = 0 = 0 \times u$. [[Erreurs du cours#^e-7-algebre-lineaire|✎]]

**Propriété** : soit $f \in L(E)$, $\lambda \in \mathbb{R}$, et $E_\lambda = \{ x \in E \mid f(x) = \lambda x \}$. Alors $E_\lambda$ est un [[Espace vectoriel|espace vectoriel]].

Démonstration du cours : si $f(x) = \lambda x$, alors $f(x) - \lambda x = 0$. Avec $\text{Id}(x) = x$, $f(x) - \lambda \text{Id}(x) = 0 \iff [f - \lambda \text{Id}](x) = 0$, donc $x \in \text{Ker}(f - \lambda \text{Id})$. Ainsi
$$E_\lambda = \text{Ker}(f - \lambda \text{Id})$$
est l'[[Espace propre|espace propre]] associé à la valeur propre $\lambda$.

C'est un sous-espace vectoriel parce que c'est le noyau de l'application linéaire $f - \lambda \text{Id}$, et tout noyau en est un. $E_\lambda$ contient $0$ et tous les vecteurs propres associés à $\lambda$ ; il est **stable** par $f$ : si $x \in E_\lambda$, alors $f(x) = \lambda x \in E_\lambda$, et $f$ agit sur $E_\lambda$ comme l'[[Homothétie|homothétie]] de rapport $\lambda$. [[Complément hors du cours|ⓘ]]

**Propriété** : $\lambda$ est valeur propre de $f$ $\iff E_\lambda \neq \{0\}$, c'est-à-dire
$$\lambda \in \text{Sp}(f) \iff E_\lambda \neq \{0\} \iff f - \lambda \text{Id} \text{ non injective.}$$

En dimension finie, une application linéaire de $E$ dans $E$ est injective si et seulement si elle est bijective ([[Théorème du rang]]) : $\lambda \in \text{Sp}(f)$ revient donc aussi à dire que $f - \lambda \text{Id}$ n'est pas bijective. En particulier, $0 \in \text{Sp}(f)$ si et seulement si $f$ n'est pas bijective. [[Complément hors du cours|ⓘ]]

**Propriété** : soit $e_1$ un vecteur propre associé à la valeur propre $\lambda_1$ et $e_2$ un vecteur propre associé à $\lambda_2$. Si $\lambda_1 \neq \lambda_2$, alors $\{e_1, e_2\}$ est libre.

Démonstration : supposons $a e_1 + b e_2 = 0$ (1). En appliquant $f$, $a \lambda_1 e_1 + b \lambda_2 e_2 = 0$ (2). En faisant (2) $- \lambda_2 \times$ (1), on obtient $a(\lambda_1 - \lambda_2) e_1 = 0$ ; comme $\lambda_1 \neq \lambda_2$ et $e_1 \neq 0$, $a = 0$, puis $b e_2 = 0$ donne $b = 0$. Le cas général se démontre de la même façon, par [[Récurrence|récurrence]] sur le nombre de vecteurs. [[Complément hors du cours|ⓘ]]

Plus généralement : une famille de vecteurs propres associés à des valeurs propres distinctes est toujours [[Indépendance linéaire|libre]].

Conséquence : une famille libre de $E$ ayant au plus $\dim E$ vecteurs, un endomorphisme d'un espace de dimension $n$ a **au plus $n$ valeurs propres distinctes**. [[Complément hors du cours|ⓘ]]

## Somme directe d'espaces vectoriels

**Théorème** : soient $E_1$ et $E_2$ deux sev de $E$.
$$E_1, E_2 \text{ supplémentaires} \iff \forall x \in E,\ \exists!\, (x_1, x_2) \in E_1 \times E_2,\ x = x_1 + x_2$$
$$\iff \dim E = \dim E_1 + \dim E_2 \text{ et } E_1 \cap E_2 = \{0\}$$

Tout élément $x$ de $E$ est la somme d'un élément de $E_1$ et d'un élément de $E_2$. On note $E_1 \oplus E_2$ et on dit qu'ils sont en [[Somme directe|somme directe]].

Exemple : dans $\mathbb{R}^2$, deux droites vectorielles distinctes $D_1$ et $D_2$ sont supplémentaires : $D_1 \cap D_2 = \{0\}$ et $1 + 1 = 2$. Un supplémentaire n'est pas unique : l'axe des abscisses a pour supplémentaire n'importe quelle droite qui n'est pas lui-même. [[Complément hors du cours|ⓘ]]

Attention, l'union $E_1 \cup E_2$ n'est en général pas un sev ; c'est la **somme** $E_1 + E_2 = \{x_1 + x_2 \mid x_1 \in E_1, x_2 \in E_2\}$ qui en est un, et la somme est directe quand la décomposition y est unique. En général, $\dim(E_1 + E_2) = \dim E_1 + \dim E_2 - \dim(E_1 \cap E_2)$ (formule de Grassmann). [[Complément hors du cours|ⓘ]]

**Théorème** : soit $f \in L(E)$ et $\lambda_1, \dots, \lambda_p$ ses valeurs propres distinctes. Alors $E_{\lambda_1}, \dots, E_{\lambda_p}$ sont en somme directe, c'est-à-dire : [[Erreurs du cours#^e-7-algebre-lineaire|✎]]
$$\forall (x_1, \dots, x_p) \in E_{\lambda_1} \times \dots \times E_{\lambda_p},\quad x_1 + \dots + x_p = 0 \Rightarrow x_1 = \dots = x_p = 0.$$

Il en découle $\dim E_{\lambda_1} + \dots + \dim E_{\lambda_p} \leq \dim E$. Quand il y a égalité, c'est-à-dire $E = E_{\lambda_1} \oplus \dots \oplus E_{\lambda_p}$, on obtient une base de $E$ formée de vecteurs propres en réunissant des bases des espaces propres : $f$ est alors **[[Diagonalisation|diagonalisable]]**, sa matrice dans cette base étant [[Matrice diagonale|diagonale]], avec les valeurs propres sur la diagonale. C'est l'usage principal de ce théorème. [[Complément hors du cours|ⓘ]]

Exemple : pour la projection $p$ vue plus haut, $E_1$ (axe des abscisses) et $E_0$ (axe des ordonnées) vérifient $\mathbb{R}^2 = E_0 \oplus E_1$ ; dans la base $\big((1,0),(0,1)\big)$, la matrice de $p$ est $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Condition suffisante classique : si $f$ a $n = \dim E$ valeurs propres distinctes, chaque $E_{\lambda_i}$ est de dimension au moins $1$, la somme vaut $n$ et $f$ est diagonalisable. [[Complément hors du cours|ⓘ]]

## Éléments propres d'une matrice carrée

**Définition** : soit $A \in \mathcal{M}_n(\mathbb{R})$. $\lambda$ est valeur propre de $A$ s'il existe un vecteur (une [[Matrice|matrice]] colonne) $X$ non nul tel que $A X = \lambda X$ ; $X$ est un vecteur propre associé à $\lambda$. [[Erreurs du cours#^e-7-algebre-lineaire|✎]]

**Théorème** :
$$\lambda \text{ valeur propre de } A \iff \text{Ker}(A - \lambda \text{Id}) \neq \{0\} \iff A - \lambda \text{Id} \text{ non injective} \iff \det(A - \lambda \text{Id}) = 0$$
(les vecteurs colonnes de $A - \lambda \text{Id}$ sont liés ; voir [[Déterminant]] et [[Équation caractéristique]]).

**Polynôme caractéristique.** $\chi_A(\lambda) = \det(A - \lambda I_n)$ est un [[Polynôme|polynôme]] de degré $n$ en $\lambda$ ; les valeurs propres de $A$ sont exactement ses racines, d'où au plus $n$ valeurs propres. Pour $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ : [[Complément hors du cours|ⓘ]]
$$\chi_A(\lambda) = (a - \lambda)(d - \lambda) - bc = \lambda^2 - (a + d)\lambda + (ad - bc) = \lambda^2 - \text{tr}(A)\,\lambda + \det A.$$

Méthode, sur l'exemple $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ : [[Complément hors du cours|ⓘ]]
1. $\chi_A(\lambda) = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3)$, donc $\text{Sp}(A) = \{1, 3\}$.
2. $E_1 = \text{Ker}(A - I)$ : $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} X = 0 \iff x + y = 0$, donc $E_1 = \text{Vect}\big((1, -1)\big)$.
3. $E_3 = \text{Ker}(A - 3I)$ : $\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} X = 0 \iff x = y$, donc $E_3 = \text{Vect}\big((1, 1)\big)$.
4. Vérification : $A \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ et $A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$. Deux valeurs propres distinctes en dimension $2$ : $\mathbb{R}^2 = E_1 \oplus E_3$ et $A$ est diagonalisable.

Valeurs propres, [[Trace d'une matrice|trace]] et déterminant : en comptant les valeurs propres complexes avec leur [[Multiplicité d'une valeur propre|multiplicité]], leur somme vaut $\text{tr}(A)$ (somme des coefficients diagonaux) et leur produit vaut $\det A$. Sur l'exemple : $1 + 3 = 4 = \text{tr}(A)$ et $1 \times 3 = 3 = \det A$. Pour une [[Matrice triangulaire|matrice triangulaire]], les valeurs propres sont les coefficients diagonaux, puisque $\det(A - \lambda I_n) = \prod_i (a_{ii} - \lambda)$. [[Complément hors du cours|ⓘ]]

Une matrice réelle peut n'avoir **aucune valeur propre réelle** : la rotation d'angle $\frac{\pi}{2}$, de matrice $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, a pour polynôme caractéristique $\lambda^2 + 1$, sans racine réelle ; géométriquement, elle ne conserve aucune direction. Dans $\mathbb{C}$, ses valeurs propres sont $i$ et $-i$. [[Complément hors du cours|ⓘ]]

Lien entre $f$ et sa matrice : si $A$ est la [[Matrice d'une application linéaire|matrice de $f$]] dans une base $\mathcal{B}$, $f(v) = \lambda v$ équivaut à $AX = \lambda X$, où $X$ est la colonne des coordonnées de $v$ dans $\mathcal{B}$. Les valeurs propres ne dépendent pas de la base : après un [[Changement de base|changement de base]], $A' = P^{-1} A P$ et $\det(A' - \lambda I_n) = \det\big(P^{-1}(A - \lambda I_n)P\big) = \det(A - \lambda I_n)$. [[Complément hors du cours|ⓘ]]

Pour la culture : le [[Théorème de Cayley-Hamilton|théorème de Cayley-Hamilton]] affirme que toute matrice carrée annule son polynôme caractéristique, $\chi_A(A) = 0$. Pour $n = 2$ : $A^2 - \text{tr}(A)\,A + \det(A)\, I_2 = 0$. [[Complément hors du cours|ⓘ]]
