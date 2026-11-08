---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]] (« Chapitre 2 : éléments de topologie dans Rn »), dans [[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]].
## Idée générale

Une norme permet de mesurer des distances, donc de parler de points « proches ». Le chapitre en tire le vocabulaire utilisé ensuite pour les limites : boules, voisinages, ouverts, fermés, intérieur et adhérence.

Plan annoncé en tête de chapitre : **topologie** (norme et distance, espace vectoriel normé, boule ouverte et fermée, ouvert, fermé et compact, intérieur et adhérent) et **suites** (convergence, [[Suite extraite|suites extraites]] et valeurs d'adhérence, [[Suite de Cauchy|suite de Cauchy]], espace complet et de Banach). La note ne traite que la partie topologie, sans les compacts.

Pour la partie suites annoncée, l'essentiel tient en trois points. Une suite $(u_n)$ d'un EVN **converge** vers $l$ si $\|u_n - l\| \to 0$, c'est-à-dire $\forall \epsilon > 0,\ \exists N,\ \forall n \ge N,\ \|u_n - l\| < \epsilon$ ([[Convergence d'une suite]]) ; dans $\mathbb R^n$, cela revient à converger composante par composante, et le choix de la norme ne change rien (théorème 1 ci-dessous). Une **valeur d'adhérence** de $(u_n)$ est la limite d'une de ses [[Suite extraite|suites extraites]] ; toute suite bornée de $\mathbb R^n$ en possède au moins une ([[Théorème de Bolzano-Weierstrass]]). Enfin, $\mathbb R^n$ est **complet** : toute [[Suite de Cauchy|suite de Cauchy]] y converge, ce qui en fait un espace de Banach. [[Complément hors du cours|ⓘ]]

## 1. Normes et distances

> **Définition 1 (norme)** : soit $E$ un [[Espace vectoriel|espace vectoriel]] et $\|\cdot\|$ une application de $E$ dans $\mathbb R$. $\|\cdot\|$ est une [[Norme|norme]] sur $E$ si et seulement si :
> 1. $\forall x \in E,\ \|x\| = 0 \Rightarrow x = 0_E$ (**séparation**) ;
> 2. $\forall x \in E,\ \forall \lambda \in \mathbb R,\ \|\lambda x\| = |\lambda|\,\|x\|$ (**absolue homogénéité**) ;
> 3. $\forall x, y \in E,\ \|x + y\| \le \|x\| + \|y\|$ ([[Inégalité triangulaire|inégalité triangulaire]]).
>
> $(E, \|\cdot\|)$ est alors un **espace vectoriel normé** (EVN).

- **Remarque 1** : les deux premières propriétés donnent la réciproque $x = 0_E \Rightarrow \|x\| = 0$, car $\|0_E\| = \|0 \times 0_E\| = 0 \times \|0_E\| = 0$.
- **Remarque 2** : la norme d'un vecteur représente sa « taille », mais un même espace peut porter plusieurs normes. Dans $\mathbb R^3$, pour $\vec X = (x, y, z)$, on connaît déjà $\|\vec X\| = \sqrt{x^2 + y^2 + z^2}$.

**Exemples sur $E = \mathbb R^n$** : pour $x = (x_1, \ldots, x_n)$,
$$\|x\|_1 = \sum_{i=1}^n |x_i|, \qquad \|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}, \qquad \|x\|_\infty = \max_{1 \le i \le n} |x_i|.$$

**Preuve que $\|\cdot\|_1$ est une norme** :
1. $\|x\|_1 = 0 \Rightarrow \forall i,\ x_i = 0$, donc $x = 0_E$.
2. $\|\lambda x\|_1 = \sum |\lambda x_i| = |\lambda| \sum |x_i| = |\lambda|\,\|x\|_1$.
3. $\|x + y\|_1 = \sum |x_i + y_i| \le \sum (|x_i| + |y_i|) = \|x\|_1 + \|y\|_1$.

Pour $\|\cdot\|_\infty$, la preuve est la même : pour tout $i$, $|x_i + y_i| \le |x_i| + |y_i| \le \|x\|_\infty + \|y\|_\infty$, puis on passe au maximum sur $i$. [[Complément hors du cours|ⓘ]]

Pour $\|\cdot\|_2$, seule l'inégalité triangulaire demande un argument : elle découle de l'[[Inégalité de Cauchy-Schwarz]] $\sum x_i y_i \le \|x\|_2\,\|y\|_2$, car $\|x + y\|_2^2 = \|x\|_2^2 + 2\sum x_i y_i + \|y\|_2^2 \le \|x\|_2^2 + 2\|x\|_2\|y\|_2 + \|y\|_2^2 = (\|x\|_2 + \|y\|_2)^2$. C'est l'**inégalité de Minkowski**. [[Complément hors du cours|ⓘ]]

- **Remarque 3** : $\|\cdot\|_2$ est la **norme euclidienne**, généralisation à $n$ dimensions de la norme connue.
- **Remarque 4** : si $E = \mathbb R$, les trois normes coïncident : $\|x\|_1 = \|x\|_2 = \|x\|_\infty = |x|$.
- **Remarque 5** : en dimension 2, ces normes correspondent à des « tailles de vecteur » dans des situations différentes : la norme euclidienne mesure $\overrightarrow{AB}$ à vol d'oiseau, la norme 1 (**norme de Manhattan**) en suivant le quadrillage.

![[Chp 2 - éléments de topologie dans Rn - image49.png]]
*Figure : de $A(3,5)$ à $B(7,2)$, segment en pointillés rouges (norme 2) et chemin en escalier le long du quadrillage (norme 1).*

**Propriétés des normes**
- **Propriété 1 (positivité)** : $\forall x,\ \|x\| \ge 0$.
- **Propriété 2** : pour la norme euclidienne, $\|x + y\| = \|x\| + \|y\| \iff y = 0$ ou $x = \lambda y$ avec $\lambda \ge 0$ (pour $y = -x$ non nul, $0 \neq 2\|x\|$). [[Erreurs du cours#^e-2-elements-de-topologie-dans-rn|✎]]
- **Propriété 3 (seconde inégalité triangulaire)** : $\forall x, y$, $\|x - y\| \ge \big|\,\|x\| - \|y\|\,\big|$.
- Preuve de la propriété 3 : $\|x\| = \|(x - y) + y\| \le \|x - y\| + \|y\|$ donne $\|x\| - \|y\| \le \|x - y\|$ ; en échangeant $x$ et $y$, $\|y\| - \|x\| \le \|y - x\| = \|x - y\|$. Les deux ensemble donnent la valeur absolue. Conséquence : la norme est 1-[[Application lipschitzienne|lipschitzienne]], donc continue (chapitre 3). [[Complément hors du cours|ⓘ]]

> **Définition 2 (normes équivalentes)** : deux normes $\|\cdot\|_a$ et $\|\cdot\|_b$ sur $E$ sont équivalentes si et seulement s'il existe $\alpha, \beta > 0$ tels que
> $$\forall x \in E,\quad \alpha\|x\|_a \le \|x\|_b \le \beta\|x\|_a.$$

> **Théorème 1 (équivalence des normes)** : si $E$ est de dimension finie, toutes les normes sur $E$ sont équivalentes.

Pour les trois normes de $\mathbb R^n$, les constantes sont explicites : pour tout $x \in \mathbb R^n$, [[Complément hors du cours|ⓘ]]
$$\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt n\,\|x\|_2 \le n\,\|x\|_\infty.$$
On les obtient en majorant chaque $|x_i|$ par $\|x\|_\infty$, et par Cauchy-Schwarz pour $\|x\|_1 = \sum 1 \cdot |x_i| \le \sqrt n\,\|x\|_2$. [[Complément hors du cours|ⓘ]]

En dimension infinie, le théorème tombe. Sur l'espace des fonctions continues sur $[0,1]$, avec $\|f\|_\infty = \max |f|$ et $\|f\|_1 = \int_0^1 |f|$, la suite $f_n(x) = x^n$ vérifie $\|f_n\|_\infty = 1$ et $\|f_n\|_1 = \frac{1}{n+1} \to 0$ : aucune constante $\beta$ ne peut donner $\|f\|_\infty \le \beta\|f\|_1$. C'est pourquoi le cours précise « en dimension finie » dans les propriétés 8 et 14. [[Complément hors du cours|ⓘ]]

> **Définition 3 (distance)** : soit $X$ un ensemble quelconque. $d : X \times X \to \mathbb R^+$ est une [[Distance|distance]] sur $X$ si et seulement si :
> 1. $d(X, Y) = 0 \iff X = Y$ ;
> 2. $d(X, Y) = d(Y, X)$ ;
> 3. $d(X, Y) \le d(X, Z) + d(Z, Y)$.

- **Propriété 4 (positivité)** : $d(X, Y) \ge 0$.
- **Propriété 5 (distance associée à une norme)** : dans un EVN $(E, \|\cdot\|)$, $d(X, Y) = \|X - Y\|$ définit une distance $E \times E \to \mathbb R^+$.
- **Propriété 6** : cette distance vérifie $d(\lambda X, \lambda Y) = |\lambda|\,d(X, Y)$.

**Exemples de distances** :
- dans $(\mathbb R^2, \|\cdot\|_2)$ : $d(X, Y) = \|X - Y\|_2 = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$ ;
- sur un espace vectoriel quelconque, la **distance discrète** $d_0(X, Y) = 0$ si $X = Y$, $1$ si $X \neq Y$.

La distance discrète ne vient d'aucune norme : elle viole la propriété 6, puisque pour $X \neq Y$, $d_0(2X, 2Y) = 1 \neq 2 = 2\,d_0(X, Y)$. Toute distance n'est donc pas de la forme $\|X - Y\|$. Pour elle, la boule $B(a, 1)$ se réduit à $\{a\}$ : toute partie est ouverte. [[Complément hors du cours|ⓘ]]

## 2. Boule ouverte, boule fermée et sphère

> **Définition 4** : dans un EVN $(E, \|\cdot\|)$, pour $a \in E$ et $r > 0$ ([[Boule et voisinage]]) :
> 1. **boule ouverte** : $B(a, r) = \{x \in E \mid \|x - a\| < r\}$ ;
> 2. **boule fermée** : $\overline B(a, r) = \{x \in E \mid \|x - a\| \le r\}$ ;
> 3. **sphère** : $S(a, r) = \{x \in E \mid \|x - a\| = r\}$.
>
> On a $\overline B(a, r) = B(a, r) \cup S(a, r)$.

- **Propriété 7** : $\forall r, r' > 0$, $r \le r' \iff B(a, r) \subset B(a, r')$ et $r \le r' \iff \overline B(a, r) \subset \overline B(a, r')$. [[Erreurs du cours#^e-2-elements-de-topologie-dans-rn|✎]]

**La forme des boules dépend de l'espace et de la norme :**

a) Dans $(\mathbb R, |\cdot|)$ : $|x - a| \le r \iff x \in [a - r, a + r]$ (boule fermée) et $|x - a| < r \iff x \in\, ]a - r, a + r[$ (boule ouverte). La boule ouverte est l'[[Intervalle réel|intervalle]] ouvert centré en $a$ de longueur $2r$, la boule fermée le même intervalle fermé.

b) Dans $\mathbb R^2$, boule fermée de centre $(0,0)$ et de rayon 1 :

1. **Norme 1** : $\|X\|_1 = |x| + |y|$. On cherche la sphère $|x| + |y| = 1$ par quadrants :
   - $x > 0, y > 0$ : $x + y = 1 \iff y = 1 - x$ ;
   - $x > 0, y < 0$ : $x - y = 1 \iff y = x - 1$ ;
   - $x < 0, y > 0$ : $-x + y = 1 \iff y = 1 + x$ ;
   - $x < 0, y < 0$ : $-x - y = 1 \iff y = -1 - x$.

   La sphère est un **losange** centré en 0.

![[Chp 2 - éléments de topologie dans Rn - image48.png]]
*Figure : boule fermée de la norme 1, losange plein de sommets $(\pm1, 0)$, $(0, \pm1)$, avec l'équation de chaque côté par quadrant ; le côté du quadrant $x < 0,\ y > 0$ a pour équation $y = 1 + x$ (l'étiquette $y = x - 1$ de l'image est fausse).* [[Erreurs du cours#^e-2-elements-de-topologie-dans-rn|✎]]

2. **Norme 2** : $\|X\|_2 = \sqrt{x^2 + y^2} = 1$ est un cercle de rayon 1 ; la boule fermée est un **disque**.

![[Chp 2 - éléments de topologie dans Rn - image13.png]]
*Figure : boule fermée de la norme 2, disque plein de rayon 1 centré à l'origine.*

3. **Norme $\infty$** (à vérifier en exercice) : la boule fermée est un **carré** de côtés allant de $-1$ à $1$.

![[Chp 2 - éléments de topologie dans Rn - image21.png]]
*Figure : boule fermée de la norme $\infty$, carré plein $[-1,1]^2$.*

Vérification : $\|X\|_\infty = \max(|x|, |y|) \le 1 \iff |x| \le 1$ et $|y| \le 1 \iff (x, y) \in [-1, 1]^2$. [[Complément hors du cours|ⓘ]]

Les inégalités $\|X\|_\infty \le \|X\|_2 \le \|X\|_1$ se lisent sur les dessins : le losange (norme 1) est inscrit dans le disque (norme 2), lui-même inscrit dans le carré (norme $\infty$). Une norme plus grande donne une boule plus petite. [[Complément hors du cours|ⓘ]]

## 3. Voisinage

> **Définition 5 (voisinage)** : soit $a \in E$ et $V \subset E$. $V$ est un **voisinage** de $a$ si et seulement si $V$ contient au moins une boule ouverte centrée en $a$ de rayon $r > 0$ :
> $$V \in \mathcal V(a) \iff \exists r > 0,\ B(a, r) \subset V.$$
> $\mathcal V(a)$ désigne l'ensemble des voisinages de $a$.

- **Propriété 8** : en dimension finie, être un voisinage de $a$ ne dépend pas de la norme choisie.
- **Propriété 9** : $a$ appartient à tous ses voisinages.
- **Propriété 10** : toute boule ouverte ou fermée de centre $a$ et de rayon $r$ est un voisinage de $a$.
- **Propriété 11** : toute réunion de voisinages de $a$ est un voisinage de $a$.
- **Propriété 12** : toute intersection **finie** de voisinages de $a$ est un voisinage de $a$.

> **Remarque (WARNING)** : une intersection **infinie** de voisinages n'en est pas forcément un. Dans $(\mathbb R, |\cdot|)$, $V_n = \left]-\frac1n, \frac1n\right[$ sont des voisinages de 0, mais $\bigcap_{n=1}^{\infty} V_n = \{0\}$ ne contient aucune boule ouverte : ce n'est pas un voisinage de 0.

> **Définition 6 ([[Espace séparé]])** : $E$ est séparé si et seulement si pour tous $a \neq b$, il existe $V_a \in \mathcal V(a)$ et $V_b \in \mathcal V(b)$ tels que $V_a \cap V_b = \emptyset$.

- **Propriété 13** : tout EVN est séparé.

## 4. Ouverts et fermés

> **Définition 7 (ouvert)** : $U \subset E$ est un **ouvert** si et seulement si chaque point de $U$ a un voisinage contenu dans $U$ ; autrement dit, $U$ est voisinage de chacun de ses points ([[Ouvert et fermé]]) :
> $$U \text{ ouvert} \iff \forall x \in U,\ \exists r > 0,\ B(x, r) \subset U.$$

**Remarque importante** : $r$ dépend de $x$ ; plus on s'approche du bord de $U$, plus $r$ doit être petit.

![[Chp 2 - éléments de topologie dans Rn - image8.png]]
*Figure : un ouvert $U$ (carré en pointillés), une grande boule autour d'un point central et une toute petite boule autour d'un point proche du bord.*

- **Propriété 14** : en dimension finie, être ouvert ne dépend pas de la norme.
- **Propriété 15** : $\emptyset$ et $E$ sont des ouverts.
- **Propriété 16** : une boule ouverte est un ouvert.
- Preuve de la propriété 16 : soit $x \in B(a, r)$ et $\rho = r - \|x - a\| > 0$. Pour $y \in B(x, \rho)$, l'inégalité triangulaire donne $\|y - a\| \le \|y - x\| + \|x - a\| < \rho + \|x - a\| = r$, donc $B(x, \rho) \subset B(a, r)$. C'est exactement la remarque ci-dessus : le rayon $\rho$ rétrécit quand $x$ s'approche du bord. [[Complément hors du cours|ⓘ]]
- **Propriété 17** : une union quelconque d'ouverts est un ouvert.
- **Propriété 18** : toute intersection finie d'ouverts est un ouvert.
- **Corollaire** : pour $a < b$, $]-\infty, b[$, $]a, b[$ et $]a, +\infty[$ sont des ouverts de $\mathbb R$.

> **Définition 8 (fermé)** : $F \subset E$ est un **fermé** si et seulement si son complémentaire $C_E F$ est un ouvert ([[Complémentaire d'un ensemble]]).

- **Propriété 19** : $\emptyset$ et $E$ sont des fermés ; ils sont donc à la fois ouverts et fermés.
- **Propriété 20** : une boule fermée est un fermé.
- **Propriété 21** : toute intersection de fermés est un fermé.
- **Propriété 22** : toute union finie de fermés est un fermé.
- **Corollaire** : pour $a < b$, $]-\infty, b]$, $[a, b]$ et $[a, +\infty[$ sont des fermés de $\mathbb R$.

Les restrictions « finie » des propriétés 18 et 22 sont nécessaires, comme pour les voisinages : $\bigcap_{n \ge 1} \left]-\frac1n, \frac1n\right[ = \{0\}$ n'est pas ouvert, et $\bigcup_{n \ge 1} \left[\frac1n, 1\right] = \,]0, 1]$ n'est pas fermé. [[Complément hors du cours|ⓘ]]

« Fermé » n'est pas le contraire d'« ouvert » : $[a, b[$ n'est ni ouvert (aucune boule centrée en $a$ n'y est contenue) ni fermé (son complémentaire n'est pas voisinage de $b$), et $\emptyset$, $E$ sont les deux à la fois. Dans $\mathbb R^n$, ce sont d'ailleurs les seules parties à la fois ouvertes et fermées. [[Complément hors du cours|ⓘ]]

**Caractérisation séquentielle des fermés** : $F$ est fermé si et seulement si la limite de toute suite convergente d'éléments de $F$ est dans $F$. C'est souvent la façon la plus rapide de montrer qu'un ensemble est fermé ; par exemple, $]0, 1]$ n'est pas fermé car $\frac1n \to 0 \notin\, ]0, 1]$. [[Complément hors du cours|ⓘ]]

**Parties bornées et compacts** (annoncés dans le plan, absents de la note). $A$ est **bornée** si elle est contenue dans une boule : $\exists M > 0,\ \forall x \in A,\ \|x\| \le M$ ; en dimension finie, cela ne dépend pas de la norme. $K$ est **compacte** si toute suite d'éléments de $K$ admet une suite extraite qui converge dans $K$ ([[Partie compacte]]). Dans $\mathbb R^n$, les compacts sont exactement les parties **fermées et bornées** : $[a, b]$, les boules fermées, les sphères, les pavés $[a_1, b_1] \times \cdots \times [a_n, b_n]$ ; en revanche $\mathbb R$ (non borné) et $]0, 1]$ (non fermé) ne sont pas compacts. Leur intérêt apparaît au chapitre 3 : une fonction continue sur un compact y atteint son minimum et son maximum. [[Complément hors du cours|ⓘ]]

## 5. Intérieur et adhérent

> **Définition 9 (intérieur)** : $a$ est **intérieur** à $A$ si et seulement si $A$ est un voisinage de $a$. L'**intérieur** $\mathring A$ est l'ensemble des points intérieurs à $A$ ([[Intérieur et adhérence]]) :
> $$x \in \mathring A \iff \exists r > 0,\ B(x, r) \subset A.$$

Intuitivement, $x \in \mathring A$ s'il y a de l'espace entre $x$ et le bord de $A$ : $\mathring A$ s'obtient en enlevant les bords de $A$.

- **Propriété 23** : $\mathring A \subset A$.
- **Propriété 24** : $\mathring A$ est le plus grand ouvert contenu dans $A$.
- **Propriété 25** : (1) $A$ ouvert $\iff \mathring A = A$ ; (2) $\mathring{\mathring A} = \mathring A$ ; (3) $A \subset B \Rightarrow \mathring A \subset \mathring B$.

**Exemples** : dans $\mathbb R$, l'intérieur de $]a,b[$, $[a,b[$, $]a,b]$ et $[a,b]$ est $]a,b[$. Dans $\mathbb R^n$, l'intérieur de $\overline B(a, r)$ est $B(a, r)$, et l'intérieur de $B(a, r)$ est $B(a, r)$.

> **Définition 10 (adhérent)** : $a$ est **adhérent** à $A$ si et seulement si tout voisinage de $a$ rencontre $A$. L'**adhérence** (« l'adhérent ») $\overline A$ est l'ensemble des points adhérents à $A$ :
> $$x \in \overline A \iff \forall r > 0,\ B(x, r) \cap A \neq \emptyset.$$

- **Propriété 26** : $A \subset \overline A$.
- **Propriété 27** : $\overline A$ est un fermé.
- **Propriété 28** : $\overline A$ est le plus petit fermé contenant $A$.
- **Propriété 29** : (1) $A$ fermé $\iff \overline A = A$ ; (2) $\overline{\overline A} = \overline A$ ; (3) $A \subset B \Rightarrow \overline A \subset \overline B$.

**Caractérisation séquentielle de l'adhérence** : $x \in \overline A$ si et seulement s'il existe une suite d'éléments de $A$ qui converge vers $x$. Dans un sens, on prend $u_n \in B(x, \frac1n) \cap A$ ; dans l'autre, une telle suite finit par entrer dans toute boule centrée en $x$. C'est la forme qu'on utilise au chapitre 3, où $a \in \overline A$ garantit qu'on peut s'approcher de $a$ en restant dans $A$. [[Complément hors du cours|ⓘ]]

**Lien entre intérieur et adhérence par le complémentaire** : le complémentaire de l'adhérence est l'intérieur du complémentaire, $C_E \overline A = (C_E A)^\circ$, et $C_E \mathring A = \overline{C_E A}$. Ce sont les propriétés 24 et 28 traduites l'une dans l'autre, comme ouverts et fermés se répondent par la définition 8. [[Complément hors du cours|ⓘ]]

**Exemples** : dans $\mathbb R$, l'adhérence de $]a,b[$, $[a,b[$, $]a,b]$ et $[a,b]$ est $[a,b]$ ; dans un EVN, l'adhérence de $B(a, r)$ est $\overline B(a, r)$. Cas extrême : comme $\mathbb Q$ et les irrationnels rencontrent tous deux tout intervalle ouvert non vide ([[Densité de ℚ dans ℝ]]), $\overline{\mathbb Q} = \mathbb R$ et $\mathring{\mathbb Q} = \emptyset$. On dit qu'une partie $A$ est **dense** dans $E$ quand $\overline A = E$. [[Complément hors du cours|ⓘ]]

> **Définition 11 (frontière)** : la **frontière** de $A$, notée $Fr(A)$ ou $\partial A$, est
> $$\partial A = \overline A \setminus \mathring A.$$

- **Propriété 30** : (1) $\overline A = A \cup \partial A$ ; (2) $\mathring A = A \setminus \partial A$.

Exemples de frontières : $\partial [a, b[\, = \{a, b\}$ dans $\mathbb R$, $\partial B(a, r) = \partial \overline B(a, r) = S(a, r)$ dans un EVN, et $\partial \mathbb Q = \mathbb R$ puisque $\overline{\mathbb Q} = \mathbb R$ et $\mathring{\mathbb Q} = \emptyset$. La frontière est toujours un fermé, et $x \in \partial A$ signifie que toute boule centrée en $x$ rencontre à la fois $A$ et son complémentaire. [[Complément hors du cours|ⓘ]]

Un dessin du cours (non extractible) représente une partie $A$ : en bleu l'intérieur, en noir la frontière, et noir + bleu l'adhérence.

## 6. Méthodes

**Montrer qu'un ensemble $A$ n'est pas ouvert** : trouver au moins un point (sur la frontière de $A$) tel que, quelle que soit la taille de la boule ouverte centrée en ce point, une partie de la boule sorte de $A$.

**Montrer qu'un ensemble $A$ n'est pas fermé** : montrer que son complémentaire n'est pas ouvert, en appliquant la méthode précédente au complémentaire.

**Trouver l'adhérence $\overline A$** (démonstration dans le TD3) : on choisit un candidat $B$ (intuition : le plus petit fermé contenant $A$).
1. Vérifier que $B$ est fermé.
2. Vérifier que $A \subset B$.

   Alors pour tout $x \in C_E B$, il existe $r > 0$ tel que $B(x, r) \cap A = \emptyset$ : aucun point extérieur à $B$ n'est dans $\overline A$, donc $\overline A \subset B$ ($B$ n'est pas trop petit).
3. Vérifier que $B$ n'est pas trop grand : pour tout $x \in B \setminus A$, $\forall r > 0,\ B(x, r) \cap A \neq \emptyset$. Alors $\overline A = B$ ; sinon, retirer les points qui ne vérifient pas cette condition.

**Trouver l'intérieur $\mathring A$** (démonstration dans le TD3) : on choisit un candidat $B$ (intuition : le plus grand ouvert contenu dans $A$).
1. Vérifier que $B$ est ouvert.
2. Vérifier que $B \subset A$.

   Alors pour tout $x \in B$, il existe $r > 0$ tel que $B(x, r) \subset A$ : $B \subset \mathring A$ ($B$ n'est pas trop grand).
3. Vérifier que $B$ n'est pas trop petit ($\mathring A \subset B$) : pour tout $x \in A \setminus B$, $\forall r > 0,\ B(x, r) \not\subset A$. Si c'est le cas, $\mathring A = B$ ; sinon, $B$ est trop petit.
