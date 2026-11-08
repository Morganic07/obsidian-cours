---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]] (« Chapitre 3 : Limite et continuité d'applications »), dans [[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]].
## Idée générale

La limite s'étend aux applications entre espaces normés. La différence avec $\mathbb{R}$ : on peut approcher un point par une infinité de chemins, et la limite doit être la même sur tous.

## 1. Limite

On généralise la [[Limite et continuité|limite]] des fonctions de $\mathbb R$ dans $\mathbb R$ aux fonctions d'un EVN ([[Norme|espace vectoriel normé]]) dans un autre.

> **Définition 1 (limite en un point)** : soit $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux EVN, $A \subset E$, $f : A \to F$, $a \in \overline A$ ([[Intérieur et adhérence|adhérence]] de $A$) et $l \in F$. $f$ admet la limite $l$ quand $x$ tend vers $a$ si et seulement si l'une des propriétés équivalentes suivantes est vérifiée :
> 1. $\forall \epsilon > 0,\ \exists \eta > 0,\ \forall x \in A,\ \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$ ;
> 2. $\forall \epsilon > 0,\ \exists \eta > 0,\ \forall x \in A,\ x \in B_E(a, \eta) \Rightarrow f(x) \in B_F(l, \epsilon)$ ;
> 3. $\forall V_F \in \mathcal V(l),\ \exists V_E \in \mathcal V_E(a),\ \forall x \in A,\ (x \in V_E \Rightarrow f(x) \in V_F)$ ;
> 4. $\forall V_F \in \mathcal V(l),\ \exists V_E \in \mathcal V_E(a),\ f(V_E \cap A) \subset V_F$.

(Voir [[Boule et voisinage]].)

Pourquoi $a \in \overline A$ : c'est exactement la condition pour que chaque boule $B_E(a, \eta)$ contienne des points de $A$, donc pour que la définition ne soit pas vide. $a$ n'a pas à être dans $A$ : c'est le cas courant d'une fonction définie sur $\mathbb R^2 \setminus \{(0,0)\}$ qu'on étudie en $(0,0)$, comme dans les exemples ci-dessous. [[Complément hors du cours|ⓘ]]

**Remarques** : $\epsilon$ est la précision avec laquelle on connaît la valeur de $f(x)$. On fixe $\epsilon$ ; il existe alors $\eta$ tel que tout $x$ à [[Distance|distance]] inférieure à $\eta$ de $a$ a une image à distance de $l$ inférieure à $\epsilon$. Si $\epsilon$ tend vers 0, $\eta$ doit tendre vers 0.

![[Chp 3 - Limite et continuité d’applications - image3.png]]
*Figure : dans $A$, un disque de rayon $\eta$ centré en $a$ contenant $x$ ; $f$ envoie $x$ sur $f(x)$, dans le disque de rayon $\epsilon$ centré en $l$ dans $F$.*

- **Propriété 1 (unicité de la limite)** : si $f$ admet une limite $l \in F$ en $a \in \overline A$, elle est unique ; on la note $\lim_{x \to a} f(x) = l$.
- L'unicité repose sur le fait qu'un EVN est [[Espace séparé|séparé]] (chapitre 2) : si $l \neq l'$ étaient deux limites, on prendrait $\epsilon = \|l - l'\|_F / 2$ ; pour $x \in A$ assez proche de $a$ (il en existe, car $a \in \overline A$), $\|l - l'\|_F \le \|l - f(x)\|_F + \|f(x) - l'\|_F < 2\epsilon = \|l - l'\|_F$, ce qui est absurde. [[Complément hors du cours|ⓘ]]
- **Propriété 2** : remplacer $\|\cdot\|_E$ et $\|\cdot\|_F$ par des normes équivalentes ne change ni l'existence de la limite, ni sa valeur.
- **Propriété 3 (linéarité)** : si $\lim_{x \to a} f(x) = l_1$ et $\lim_{x \to a} g(x) = l_2$ ($f, g : A \to F$), alors pour tout $\lambda \in \mathbb R$,
$$\lim_{x \to a} \big(f(x) + \lambda g(x)\big) = l_1 + \lambda l_2.$$
- **Propriété 4 (produit, quotient)** : pour $f, g : A \to \mathbb R$, de limites $l_1, l_2 \in \mathbb R$ en $a$ :
  1. $\lim_{x \to a} f(x)g(x) = l_1 l_2$ ;
  2. si $l_2 \neq 0$, $\lim_{x \to a} f(x)/g(x) = l_1/l_2$.

> **Propriété 5 (composantes)** : soit $E = \mathbb R^n$, $F = \mathbb R^p$. $f : E \to F$ admet $l = (l_1, \ldots, l_p)$ pour limite en $a$ si et seulement si, pour tout $i \in [\![1, p]\!]$, la $i$-ème application composante $f_i : E \to \mathbb R$ admet $l_i$ pour limite en $a$.
>
> Autrement dit, la limite se calcule composante par composante.

- **Composition des limites** : si $\lim_{x \to a} f(x) = b$ et $\lim_{y \to b} g(y) = l$ (avec $g$ définie sur une partie contenant $f(A)$), alors $\lim_{x \to a} g(f(x)) = l$ ([[Composition de fonctions]]). C'est ce qui permet, par exemple, de traiter $\sin(x^2 + y^2)$ ou $e^{xy}$ en $(0,0)$ à partir des limites d'une variable. [[Complément hors du cours|ⓘ]]
- **Caractérisation séquentielle** (utilisée par le cours dans la méthode, sans énoncé) : $\lim_{x \to a} f(x) = l$ si et seulement si, pour toute suite $(x_n)$ d'éléments de $A$ qui converge vers $a$, la suite $f(x_n)$ converge vers $l$ ([[Caractérisation séquentielle de la limite]]). Pour montrer qu'il n'y a pas de limite, deux suites suffisent ; pour montrer qu'il y en a une, il faudrait toutes les suites, d'où le recours à une majoration. [[Complément hors du cours|ⓘ]]

## 2. Continuité

> **Définition 2 (application continue)** : soit $A \subset E$, $f : A \to F$ et $a \in A$. $f$ est **continue en $a$** si et seulement si $f$ admet une limite en $a$. Elle est **discontinue** en $a$ sinon. Elle est continue sur $A$ si elle est continue en tout point de $A$. On note $\mathcal C(A, F)$ l'ensemble des fonctions continues de $A$ dans $F$.

La continuité en $a$ revient à étudier si, **quel que soit le chemin** par lequel on s'approche de $a$, la fonction tend vers la même valeur. C'est aussi la définition dans le cas de $\mathbb R \to \mathbb R$ (la phrase suivante du cours s'arrête au milieu, sur « on »).

Comme $a \in A$, la seule limite possible en $a$ est $f(a)$ : en prenant $x = a$ dans la définition 1, $\|f(a) - l\|_F < \epsilon$ pour tout $\epsilon > 0$, donc $l = f(a)$. La définition se lit donc, comme en première année, $f$ continue en $a \iff \lim_{x \to a} f(x) = f(a)$, soit $\forall \epsilon > 0,\ \exists \eta > 0,\ \forall x \in A,\ \|x - a\|_E < \eta \Rightarrow \|f(x) - f(a)\|_F < \epsilon$. [[Complément hors du cours|ⓘ]]

**Opérations sur les fonctions continues** : d'après les propriétés 3 à 5 et la composition des limites, les sommes, produits, quotients (dénominateur non nul), composées de fonctions continues sont continues, et $f$ à valeurs dans $\mathbb R^p$ est continue si et seulement si ses composantes le sont. Les projections $(x_1, \ldots, x_n) \mapsto x_i$ sont continues (1-lipschitziennes), donc toute fonction polynomiale en $x_1, \ldots, x_n$, et toute fonction construite à partir d'elles avec les fonctions usuelles ($\exp$, $\sin$, $\ln$, $\sqrt{\cdot}$…), est continue là où elle est définie. C'est ce qui justifie l'étape 1 de la méthode ci-dessous. [[Complément hors du cours|ⓘ]]

**Continuité séparée ≠ continuité** : être continue en chaque variable séparément (les autres étant fixées) ne suffit pas. La fonction $f_1$ de l'exemple 1, prolongée par $f_1(0,0) = 0$, vérifie $f_1(x, 0) = 0$ et $f_1(0, y) = 0$ : ses deux applications partielles sont continues en 0, mais $f_1$ n'est pas continue en $(0,0)$. [[Complément hors du cours|ⓘ]]

**Caractérisation par les images réciproques** : $f : E \to F$ est continue sur $E$ si et seulement si l'[[Image et image réciproque|image réciproque]] de tout ouvert de $F$ est un ouvert de $E$ (de même avec les fermés). Méthode pratique pour le chapitre 2 : $\{(x, y) \mid x^2 + y^2 < 1\} = g^{-1}(]-\infty, 1[)$ avec $g(x,y) = x^2 + y^2$ continue, donc c'est un ouvert ; $\{(x, y) \mid xy \ge 1\}$ est de même un fermé. Inégalité stricte : ouvert ; inégalité large ou égalité : fermé. [[Complément hors du cours|ⓘ]]

**Continuité sur un compact** : si $K \subset \mathbb R^n$ est une [[Partie compacte|partie compacte]] (fermée et bornée) non vide et $f : K \to \mathbb R$ continue, alors $f$ est bornée et **atteint ses bornes** : il existe $x_m, x_M \in K$ avec $f(x_m) = \min_K f$ et $f(x_M) = \max_K f$. C'est la généralisation du [[Théorème des bornes atteintes]] de première année, et l'outil de base pour justifier l'existence d'un extremum. [[Complément hors du cours|ⓘ]]

## 3. Applications lipschitziennes

> Soit $f : E \to F$, $A \subset E$. $f$ est **$k$-lipschitzienne** sur $A$ ([[Application lipschitzienne]]) si et seulement si
> $$\forall \mathbf x, \mathbf y \in A,\quad \|f(\mathbf x) - f(\mathbf y)\| \le k\,\|\mathbf x - \mathbf y\|_E.$$
> La première norme est celle de $F$ : le cours ne lui met pas d'indice.
> Si $f : \mathbb R \to \mathbb R$ : $|f(x) - f(y)| \le k\,|x - y|$.

$f$ $k$-lipschitzienne $\Rightarrow$ $f$ [[Continuité uniforme|uniformément continue]] ; la réciproque est fausse : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue sans être lipschitzienne. [[Erreurs du cours#^e-3-limite-et-continuite-dapplications|✎]]

> **Continuité uniforme** : $f : E \to F$ entre espaces métriques est uniformément continue si, pour toute précision fixée, on trouve une « marge de manœuvre » $\delta$ qui marche **partout** :
> $$\forall \epsilon > 0,\ \exists \delta > 0,\ \forall x, y \in E,\ d_E(x, y) < \delta \Rightarrow d_F(f(x), f(y)) < \epsilon.$$
> - Continuité classique : $\delta$ peut dépendre du point $x$ (local).
> - Continuité uniforme : $\delta$ est le même partout (global).

**Preuve de « lipschitzienne ⇒ uniformément continue »** : si $f$ est $k$-lipschitzienne avec $k > 0$, pour $\epsilon > 0$ on prend $\delta = \epsilon / k$ ; alors $\|x - y\|_E < \delta \Rightarrow \|f(x) - f(y)\| \le k\|x - y\|_E < \epsilon$, et ce $\delta$ ne dépend ni de $x$ ni de $y$. On a donc la chaîne lipschitzienne $\Rightarrow$ uniformément continue $\Rightarrow$ continue, sans réciproques. [[Complément hors du cours|ⓘ]]

Contre-exemple à « continue ⇒ uniformément continue » : $x \mapsto x^2$ sur $\mathbb R$. Avec $x = n + \frac1n$ et $y = n$, $|x - y| = \frac1n \to 0$ mais $|x^2 - y^2| = 2 + \frac{1}{n^2} \ge 2$ : aucun $\delta$ ne convient pour $\epsilon = 2$. Le problème vient de ce que $\mathbb R$ n'est pas borné : sur un compact, toute fonction continue est uniformément continue (**théorème de Heine**). [[Complément hors du cours|ⓘ]]

Exemples d'applications lipschitziennes : une norme (1-lipschitzienne par la seconde inégalité triangulaire), les projections $x \mapsto x_i$, toute application linéaire de $\mathbb R^n$ dans $\mathbb R^p$, et, en une variable, toute fonction dérivable de dérivée bornée par $k$ sur un intervalle (par l'[[Inégalité des accroissements finis]]). [[Complément hors du cours|ⓘ]]

## 4. Méthode : limite d'une fonction de $\mathbb R^2$ dans $\mathbb R$ en $a = (x_0, y_0)$

On cherche $\lim_{(x,y) \to (x_0, y_0)} f(x, y)$.

**Étape 1** : calculer $f(x_0, y_0)$. Si l'on n'obtient pas de [[Forme indéterminée|forme indéterminée]] ($0 \times \infty$, $\infty/\infty$, $0/0$, $\infty - \infty$, …) et que $f$ est continue en $(x_0, y_0)$ (par exemple par les théorèmes d'opérations sur les fonctions continues), alors $\lim f(x, y) = f(x_0, y_0)$. [[Erreurs du cours#^e-3-limite-et-continuite-dapplications|✎]] Sinon, il faut lever l'indétermination : étape 2.

**Étape 2** : montrer soit (i) que tous les chemins vers $a$ donnent la même valeur (et $f$ est continue en $a$ et prend cette valeur), soit (ii) qu'au moins deux chemins vers $a$ donnent des valeurs différentes (et $f$ n'a pas de limite en $a$).
1. **[[Coordonnées polaires]]**, surtout si le dénominateur s'y prête (par exemple $(x - x_0)^2 + (y - y_0)^2$) : on pose
$$x = x_0 + \rho\cos\theta, \qquad y = y_0 + \rho\sin\theta,$$
ce qui définit $\tilde f(\rho, \theta) = f(x, y)$, et
$$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = \lim_{(\rho,\theta) \to (0,\theta)} \tilde f(\rho, \theta).$$
Si le résultat dépend de $\theta$, $f$ n'a pas de limite en $a$. S'il ne dépend pas de $\theta$, ce n'est pas suffisant : $f$ admet la limite $l$ si l'on majore $|\tilde f(\rho, \theta) - l|$ par une quantité indépendante de $\theta$ qui tend vers 0 avec $\rho$, comme dans l'exemple 2. Contre-exemple : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé, mais vaut $1/2$ sur le chemin $y = x^2$. [[Erreurs du cours#^e-3-limite-et-continuite-dapplications|✎]]
2. **Chemins cartésiens**, si la fonction ne se prête pas aux polaires : on calcule $f$ le long de différents chemins $(x, \alpha(x))$, avec $\alpha : \mathbb R \to \mathbb R$. Si deux chemins donnent des valeurs différentes, pas de limite. Si tous donnent la même valeur $l_c$, c'est un bon candidat : étape 3.
3. Calculer $|f(x, y) - l_c|$ : si cette quantité tend vers 0 quand $(x, y) \to (x_0, y_0)$, alors $\lim f(x, y) = l_c$ ; sinon, $f$ n'a pas de limite en $(x_0, y_0)$.

Majorations utiles en $(0,0)$, avec $r = \sqrt{x^2 + y^2}$ : $|x| \le r$, $|y| \le r$, $|xy| \le \frac{x^2 + y^2}{2}$ (car $(|x| - |y|)^2 \ge 0$), et $\frac{x^2}{x^2 + y^2} \le 1$. On cherche à majorer $|f(x,y) - l_c|$ par une expression en $r$ seul qui tend vers 0 ; en polaires, c'est une majoration $|\tilde f(\rho, \theta) - l_c| \le g(\rho)$ avec $g(\rho) \to 0$, indépendante de $\theta$. Exemple : $\left|\frac{x^2 y}{x^2 + y^2}\right| \le |y| \to 0$. [[Complément hors du cours|ⓘ]]

On peut aussi utiliser la [[Caractérisation séquentielle de la limite|caractérisation séquentielle]] : comparer $f(u_n)$ et $f(v_n)$ pour deux suites $u_n, v_n \to a$.

## 5. Exemples

### Exemple 1 : $f_1(x, y) = \dfrac{xy}{x^2 + y^2}$ en $(0,0)$

$f_1(0,0) = 0/0$ : forme indéterminée.

| Coordonnées polaires | Caractérisation séquentielle | Caractérisation cartésienne |
|---|---|---|
| $x = \rho\cos\theta$, $y = \rho\sin\theta$ donnent $\tilde f_1(\rho, \theta) = \cos\theta\sin\theta$. Si $\theta = \pi/4$, la limite vaut $1/2$ ; si $\theta = \pi/2$, elle vaut $0$. | $u_n = (1/n, 1/n)$ et $v_n = (0, 1/n)$ tendent vers $(0,0)$, mais $f_1(u_n) \to 1/2$ et $f_1(v_n) \to 0$. | Chemin $(x, x)$ : $f_1(x,x) = 1/2$. Chemin $(0, y)$ : $f_1(0, y) = 0$. |

Conclusion : deux chemins donnent des valeurs différentes, donc **$f_1$ n'a pas de limite en $(0,0)$**.

![[Chp 3 - Limite et continuité d’applications - image10.png]]
*Figure : exemple 1, les trois méthodes et les deux chemins vers l'origine (diagonale $\theta = \pi/4$ et axe vertical $\theta = \pi/2$).*

### Exemple 2 : $f_2(x, y) = 1 + \dfrac{x^3}{x^2 + y^2}$ en $(0,0)$

$f_2(0,0)$ donne $0/0$ : forme indéterminée.

| Coordonnées polaires | Caractérisation séquentielle | Caractérisation cartésienne |
|---|---|---|
| $\tilde f_2(\rho, \theta) = \rho\cos^3\theta + 1 \to 1$ quand $\rho \to 0$ : « la fonction est continue ». | $u_n = (1/n, 1/n)$, $v_n = (1/n, 0)$ : $f_2(u_n) \to 1$ et $f_2(v_n) \to 1$. **On ne peut pas conclure.** | Chemins $(x, x)$ et $(x, 0)$ : limite 1 dans les deux cas. **On ne peut pas conclure.** |

Deux chemins qui donnent 1 ne prouvent pas la continuité. On étudie $|f(x, y) - l_c|$ avec $l_c = 1$ :
$$|f_2(x, y) - 1| = \left|\frac{x^3}{x^2 + y^2}\right| = \frac{x^2}{x^2 + y^2}\,|x| \le |x| \underset{(x,y) \to (0,0)}{\longrightarrow} 0.$$
Avec les trois méthodes, **$\lim_{(x,y) \to (0,0)} f_2(x, y) = 1$**.

$f_2$ n'est pas définie en $(0,0)$, mais comme elle y a une limite finie, elle se [[Prolongement par continuité|prolonge par continuité]] en posant $f_2(0,0) = 1$ ; le prolongement est alors continu sur tout $\mathbb R^2$. $f_1$, sans limite en $(0,0)$, ne se prolonge par continuité par aucune valeur. [[Complément hors du cours|ⓘ]]

![[Chp 3 - Limite et continuité d’applications - image14.png]]
*Figure : exemple 2, les trois méthodes, les chemins $u_n$ (diagonale) et $v_n$ (axe horizontal), et la majoration finale.*
