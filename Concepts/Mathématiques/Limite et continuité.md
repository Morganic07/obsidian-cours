---
type: concept
tags: [year1, year2, year3]
aliases: [limite, limites, continuité, application continue, applications continues, fonction continue, fonctions continues, discontinue, limite à gauche, limite à droite, continuité à gauche, continuité à droite, méthode des chemins, limite d'une fonction en un point, opérations sur les limites]
matieres: [Analyse dans Rn, Analyse Maths, Analyse, Séries]
sources: ["[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[0 - Revision chapter|Chp0 - Revision chapter]]"]
maj: 2026-11-07
---

**Limite** : $f$ tend vers $l$ en $a$ si $\forall \epsilon > 0, \exists \eta > 0, \forall x \in A, \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$. La limite est unique, ne change pas entre normes équivalentes, et se calcule composante par composante. Les règles de somme, de produit et de quotient restent valables.

**Continuité** : $f$ est continue en $a \in A$ si elle y admet une limite, et continue sur $A$ si elle l'est en tout point. Cela revient à obtenir la même valeur par tous les chemins qui approchent $a$.

**Méthode pour $\mathbb{R}^2 \to \mathbb{R}$** :

1. Calculer $f(x_0, y_0)$ : sans forme indéterminée ($0 \times \infty$, $\infty/\infty$, $0/0$, $\infty - \infty$…), le cours conclut que la limite vaut $f(x_0, y_0)$ (ce qui suppose $f$ continue en ce point, voir « Erreurs du cours ») ; sinon, continuer.
2. Passer en [[Coordonnées polaires|polaires]], ou comparer des chemins. Deux valeurs différentes prouvent qu'il n'y a pas de limite.
3. Si tous les essais donnent $l_c$, montrer que $|f(x, y) - l_c| \to 0$, par exemple par une majoration.

Exemple du cours : $xy/(x^2 + y^2)$ n'a pas de limite en $(0, 0)$.

> [!warning] Écart dans le cours
> [[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]] dit qu'un résultat en polaires indépendant de $\theta$ donne la limite. Ce n'est pas suffisant : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé, mais vaut $1/2$ sur $y = x^2$. Il faut une majoration indépendante de $\theta$ (complément).

**En une variable** (polycopié d'Analyse I) : limite en $a$ ou en $\pm\infty$, finie ou infinie, par quantificateurs et par voisinages ; $f \to \ell \iff |f - \ell| \to 0$ ; unicité ; limites à gauche et à droite. $f$ est continue en $a$ si elle a en $a$ une limite finie égale à $f(a)$ ; la continuité sur un intervalle ($\mathcal{C}^0(I, \mathbb{R})$) est stable par somme, produit, quotient (si le dénominateur ne s'annule pas sur $I$) et composée. Le polycopié donne aussi la [[Caractérisation séquentielle de la limite]], le [[Prolongement par continuité]], le [[Théorème des valeurs intermédiaires]], l'image d'un segment et le [[Théorème de la bijection]]. Une fonction continue sur un intervalle est injective si et seulement si elle est strictement monotone. Le TD3 montre que $\mathbf{1}_{\mathbb{Q}}$ est discontinue partout ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

**En Séries** (chapitre de révision) : opérations sur les limites (somme, produit, quotient si la limite du dénominateur est non nulle, puissance) et limite d'une suite par une fonction. Une limite uniforme de fonctions continues est continue ([[Convergence uniforme]]).

Liens : [[Norme]], [[Boule et voisinage]], [[Application lipschitzienne]], [[Dérivée partielle]], [[Différentielle]], [[Suite numérique]], [[Borne supérieure]]

## Erreurs du cours

- [[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]] (« Méthodologies », étape 1) écrit « On calcule $f(x_0, y_0)$ et si on n'obtient pas une forme indéterminée […], alors $\lim f(x,y) = f(x_0, y_0)$ » ; il faut savoir d'abord que $f$ est continue en $(x_0, y_0)$ (par exemple par les théorèmes d'opérations), sinon la conclusion ne vaut pas. Vérifié sur l'image.
- Même chapitre, étape 2 : « Si le résultat ne dépend pas de $\theta$ alors la fonction $f$ admet une limite » ; ce test seul ne suffit pas, il faut une majoration indépendante de $\theta$ (voir l'encadré ci-dessus).

Résumés : [[3 - Limite et continuité d’applications]], [[0 - rappels pdf]], [[0 - Revision chapter]], [[3 - Sequence of function]]
