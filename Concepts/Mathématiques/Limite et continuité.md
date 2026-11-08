---
type: concept
tags: [year1, year2, year3]
aliases: [limite, limites, continuité, application continue, applications continues, fonction continue, fonctions continues, discontinue, limite à gauche, limite à droite, continuité à gauche, continuité à droite, méthode des chemins, limite d'une fonction en un point, opérations sur les limites]
matieres: [Analyse dans Rn, Analyse Maths, Analyse, Séries]
sources: ["[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[0 - Revision chapter|Chp0 - Revision chapter]]"]
maj: 2026-11-08
---

**Limite** : $f$ tend vers $l$ en $a$ si $\forall \epsilon > 0, \exists \eta > 0, \forall x \in A, \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$. La limite est unique, ne change pas entre normes équivalentes, et se calcule composante par composante. Les règles de somme, de produit et de quotient restent valables.

**Continuité** : $f$ est continue en $a \in A$ si elle y admet une limite, et continue sur $A$ si elle l'est en tout point. Cela revient à obtenir la même valeur par tous les chemins qui approchent $a$.

Précisions (complément, hors du cours) :

- Pour $a \in A$, la seule limite possible en $a$ est $f(a)$ (prendre $x = a$ dans la définition). Ainsi $f$ est continue en $a$ si et seulement si $\lim_{x \to a} f(x) = f(a)$.
- La composée de limites, et de fonctions continues, se comporte comme en une variable. Les fonctions polynomiales en $x_1, \dots, x_n$, et celles construites à partir des fonctions usuelles par somme, produit, quotient et composition, sont continues sur leur domaine de définition : c'est ce qui justifie l'étape 1 de la méthode ci-dessous.
- **Continuité séparée ≠ continuité** : $f(x, y) = xy/(x^2 + y^2)$ prolongée par $f(0, 0) = 0$ a des applications partielles $x \mapsto f(x, 0) = 0$ et $y \mapsto f(0, y) = 0$ continues en 0, mais n'est pas continue en $(0, 0)$, puisqu'elle vaut $1/2$ sur la droite $y = x$.
- **Caractérisation topologique** : $f$ est continue sur $A$ si et seulement si l'image réciproque de tout [[Ouvert et fermé|ouvert]] est un ouvert (relatif à $A$), ou de manière équivalente l'image réciproque de tout fermé est un fermé ([[Image et image réciproque]]).
- **Majorations utiles en $(0, 0)$**, avec $r = \sqrt{x^2 + y^2}$ : $|x| \le r$, $|y| \le r$ et $|xy| \le \frac{x^2 + y^2}{2} = \frac{r^2}{2}$. Par exemple $\left|\frac{x^3}{x^2 + y^2}\right| \le \frac{r^3}{r^2} = r \to 0$ : c'est une majoration indépendante de $\theta$, comme l'étape 3 le demande.

**Méthode pour $\mathbb{R}^2 \to \mathbb{R}$** :

1. Calculer $f(x_0, y_0)$ : sans forme indéterminée ($0 \times \infty$, $\infty/\infty$, $0/0$, $\infty - \infty$…) et si $f$ est continue en ce point (par exemple par les théorèmes d'opérations), la limite vaut $f(x_0, y_0)$ ; sinon, continuer. [[Erreurs du cours#^e-limite-et-continuite|✎]]
2. Passer en [[Coordonnées polaires|polaires]], ou comparer des chemins. Deux valeurs différentes prouvent qu'il n'y a pas de limite. Un résultat en polaires indépendant de $\theta$ ne suffit pas à conclure : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé, mais vaut $1/2$ sur $y = x^2$. [[Erreurs du cours#^e-limite-et-continuite|✎]]
3. Si tous les essais donnent $l_c$, montrer que $|f(x, y) - l_c| \to 0$, par exemple par une majoration.

Exemple du cours : $xy/(x^2 + y^2)$ n'a pas de limite en $(0, 0)$.

**En une variable** (polycopié d'Analyse I) : limite en $a$ ou en $\pm\infty$, finie ou infinie, par quantificateurs et par voisinages ; $f \to \ell \iff |f - \ell| \to 0$ ; unicité ; limites à gauche et à droite. $f$ est continue en $a$ si elle a en $a$ une limite finie égale à $f(a)$ ; la continuité sur un intervalle ($\mathcal{C}^0(I, \mathbb{R})$) est stable par somme, produit, quotient (si le dénominateur ne s'annule pas sur $I$) et composée. Le polycopié donne aussi la [[Caractérisation séquentielle de la limite]], le [[Prolongement par continuité]], le [[Théorème des valeurs intermédiaires]], l'image d'un segment et le [[Théorème de la bijection]]. Une fonction continue sur un intervalle est injective si et seulement si elle est strictement monotone. Le TD3 montre que $\mathbf{1}_{\mathbb{Q}}$ est discontinue partout ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

**En Séries** (chapitre de révision) : opérations sur les limites (somme, produit, quotient si la limite du dénominateur est non nulle, puissance) et limite d'une suite par une fonction. Une limite uniforme de fonctions continues est continue ([[Convergence uniforme]]).

Liens : [[Norme]], [[Boule et voisinage]], [[Application lipschitzienne]], [[Dérivée partielle]], [[Différentielle]], [[Suite numérique]], [[Borne supérieure]], [[Ouvert et fermé]], [[Image et image réciproque]], [[Coordonnées polaires]]

Résumés : [[3 - Limite et continuité d’applications]], [[0 - rappels pdf]], [[0 - Revision chapter]], [[3 - Sequence of function]]
