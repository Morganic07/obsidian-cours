---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 6 : Joint probability distributions.docx|Chp 6 - Joint probability distributions]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Probability/Chp 6 : Joint probability distributions.docx|Chp 6 - Joint probability distributions]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les énoncés donnés en images sont recopiés ; seule la figure des nuages de points est intégrée (l'icône d'avertissement est décorative).

## Idée générale

Étudier plusieurs variables à la fois : loi conjointe, lois marginales, indépendance, covariance, corrélation, combinaisons linéaires et loi d'une somme.

## Loi conjointe de deux variables (*joint pmf & pdf*)

**Définition (cas discret).** Soit $X$ et $Y$ deux variables discrètes définies sur l'[[Espace probabilisé|espace d'échantillonnage]] $S$ d'une expérience. La **fonction de masse conjointe** (*joint [[Variable aléatoire|probability mass function]]*) est définie pour tout couple $(x, y)$ par
$$p(x, y) = P(X = x \text{ et } Y = y)$$

Une fonction $p(x, y)$ peut servir de *pmf* conjointe ([[Loi conjointe]]) si :
1. $p(x, y) \ge 0$ pour tous $x$ et $y$ ;
2. $\sum_{x,y} p(x, y) = 1$.

Si $p$ est la pmf du couple $(X, Y)$ et $A$ un événement de « $S \times S$ » (sic), alors
$$P((X, Y) \in A) = \sum_{(x,y) \in A}\sum p(x, y)$$

**Définition (cas continu).** Soit $X$ et $Y$ continues. $f(x, y)$ est la **densité conjointe** (*joint probability density function*) de $X$ et $Y$ si, pour tout ensemble $A$ du plan,
$$P((X, Y) \in A) = \iint_A f(x, y)\,dx\,dy$$
En particulier, si $A$ est le rectangle $\{(x, y) : a \le x \le b,\ c \le y \le d\}$ :
$$P((X, Y) \in A) = P(a \le X \le b,\ c \le Y \le d) = \int_a^b \int_c^d f(x, y)\,dy\,dx$$
(voir [[Intégrale multiple]]).

## Loi conjointe de plus de deux variables

**Définition.** Si $X_1, \dots, X_n$ sont discrètes, leur **pmf conjointe** est
$$p(x_1, x_2, \dots, x_n) = P(X_1 = x_1 \cap X_2 = x_2 \cap \dots \cap X_n = x_n)$$
Si elles sont continues, leur **densité conjointe** est la fonction $f(x_1, \dots, x_n)$ telle que, pour tous intervalles $[a_1, b_1], \dots, [a_n, b_n]$ :
$$P(a_1 \le X_1 \le b_1, \dots, a_n \le X_n \le b_n) = \int_{a_1}^{b_1} \cdots \int_{a_n}^{b_n} f(x_1, \dots, x_n)\,dx_n \dots dx_1$$

## Lois marginales : de deux variables à une seule

**Définition (discret).** Les **fonctions de masse marginales** (*marginal pmfs*) de $X$ et de $Y$ sont
$$p_X(x) = \sum_y p(x, y), \qquad p_Y(y) = \sum_x p(x, y)$$
Elles permettent de retrouver la pmf d'une seule variable à partir de la pmf conjointe.

**Définition (continu).** Les **densités marginales** (*marginal pdfs*) sont
$$f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,dy \quad (-\infty < x < \infty), \qquad f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\,dx \quad (-\infty < y < \infty)$$

## Indépendance de deux variables

**Définition.** $X$ et $Y$ sont **indépendantes** ([[Indépendance de variables aléatoires]]) si, pour tout couple $(x, y)$ :
$$p(x, y) = p_X(x) \cdot p_Y(y) \text{ (discret)} \qquad \text{ou} \qquad f(x, y) = f_X(x) \cdot f_Y(y) \text{ (continu)} \quad (1)$$
Si (1) n'est pas vraie pour tous les $(x, y)$, $X$ et $Y$ sont **dépendantes**.

## Espérance pour deux variables

**Proposition.** Soit $X$ et $Y$ de pmf conjointe $p$ ou de densité conjointe $f$. L'[[Espérance et variance|espérance]] d'une fonction $h(X, Y)$, notée $E[h(X, Y)]$ ou $\mu_{h(X,Y)}$, est
$$E[h(X, Y)] = \begin{cases} \displaystyle\sum_x \sum_y h(x, y)\, p(x, y) & \text{discret} \\ \displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} h(x, y)\, f(x, y)\,dx\,dy & \text{continu} \end{cases}$$

**Linéarité de l'espérance.** Pour toutes fonctions $h_1, h_2$ et constantes $a_1, a_2, b$ :
$$E[a_1 h_1(X, Y) + a_2 h_2(X, Y) + b] = a_1 E[h_1(X, Y)] + a_2 E[h_2(X, Y)] + b$$

**Théorème.** Si $X$ et $Y$ sont *indépendantes* et $h(X, Y) = g_1(X) \cdot g_2(Y)$, alors
$$E[h(X, Y)] = E[g_1(X) \cdot g_2(Y)] = E[g_1(X)] \cdot E[g_2(Y)]$$

## Covariance

**Définition.** La **[[Covariance et corrélation|covariance]]** de $X$ et $Y$ est
$$\mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = \begin{cases} \displaystyle\sum_x \sum_y (x - \mu_X)(y - \mu_Y)\, p(x, y) & \text{discret} \\ \displaystyle\iint (x - \mu_X)(y - \mu_Y)\, f(x, y)\,dx\,dy & \text{continu} \end{cases}$$

![[Chp 6 - Joint probability distributions - image17.png]]
*Figure : trois nuages de dix points équiprobables ($p(x, y) = 0{,}10$), découpés en quadrants par $\mu_X$ et $\mu_Y$ (produits $+$ en bas à gauche et en haut à droite, $-$ ailleurs) — (a) covariance positive, (b) covariance négative, (c) covariance proche de zéro.*

**Proposition.** Pour toutes variables $X$ et $Y$ :
1. $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$ ;
2. $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$ ;
3. **formule raccourcie** (*covariance shortcut formula*) : $\mathrm{Cov}(X, Y) = E(XY) - \mu_X \cdot \mu_Y$ ;
4. **distributivité** : pour toute variable $Z$ et constantes $a, b, c$,
$$\mathrm{Cov}(aX + bY + c, Z) = a\,\mathrm{Cov}(X, Z) + b\,\mathrm{Cov}(Y, Z)$$

## Corrélation

**Définition.** Le **coefficient de corrélation** de $X$ et $Y$, noté $\mathrm{Corr}(X, Y)$, $\rho_{X,Y}$ ou $\rho$, est
$$\rho_{X,Y} = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$

**Proposition.**
1. Si $X$ et $Y$ sont indépendantes, $\rho = 0$ ; mais $\rho = 0$ n'entraîne pas l'indépendance.
2. $\rho = 1$ ou $-1$ si et seulement si $Y = aX + b$ pour des nombres $a, b$ avec $a \ne 0$.

**[[Corrélation et causalité|Corrélation contre causalité]]** (*correlation versus causation*). Un $\rho$ proche de 1 ne signifie pas qu'augmenter $X$ *fait* augmenter $Y$ ; seulement que les grandes valeurs de $X$ sont *associées* aux grandes valeurs de $Y$. Exemple : chez les enfants, la taille du vocabulaire et le nombre de caries sont assez fortement corrélés positivement, mais les caries ne font pas grandir le vocabulaire : les deux augmentent avec une troisième variable, l'âge. À âge fixé, la corrélation est probablement très faible. Une forte corrélation n'est pas une causalité : « la corrélation mesure l'association, pas la causalité ! »

## Variables non corrélées (*uncorrelated*)

**Proposition.** Deux variables $X$ et $Y$ sont non corrélées si et seulement si $E[XY] = \mu_X \cdot \mu_Y$.

## Combinaisons linéaires de variables aléatoires

Pour des variables $X_1, \dots, X_n$ et des constantes $a_1, \dots, a_n, b$ (le cours écrit « $b = 0$ », voir Points à vérifier), la [[Combinaison linéaire|combinaison linéaire]]
$$a_1 X_1 + \dots + a_n X_n + b$$
est une nouvelle variable aléatoire, avec sa propre loi, sa moyenne et son écart-type.

Combinaison très importante : la **[[Moyenne empirique|moyenne empirique]]** (*sample mean*) $\bar{X} = \dfrac{X_1 + \dots + X_n}{n}$, obtenue avec $a_1 = \dots = a_n = \frac{1}{n}$ et $b = 0$.

On n'exige ni que les $X_i$ soient indépendantes, ni qu'elles aient la même loi : elles peuvent avoir des moyennes et des écarts-types différents.

**Théorème.** Soit $X_1, \dots, X_n$ de moyennes $\mu_1, \dots, \mu_n$ et d'écarts-types $\sigma_1, \dots, \sigma_n$.

1. Que les $X_i$ soient indépendantes ou non :
$$E(a_1 X_1 + \dots + a_n X_n + b) = a_1 E(X_1) + \dots + a_n E(X_n) + b = a_1\mu_1 + \dots + a_n\mu_n + b \quad (4.4)$$
$$\mathrm{Var}(a_1 X_1 + \dots + a_n X_n + b) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_i a_j\,\mathrm{Cov}(X_i, X_j) = \sum_{i=1}^{n} a_i^2 \sigma_i^2 + 2\sum_{i<j}\sum a_i a_j\,\mathrm{Cov}(X_i, X_j) \quad (4.5)$$
2. Si $X_1, \dots, X_n$ sont indépendantes :
$$\mathrm{Var}(a_1 X_1 + \dots + a_n X_n + b) = a_1^2\,\mathrm{Var}(X_1) + \dots + a_n^2\,\mathrm{Var}(X_n) = a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2 \quad (4.6)$$
$$\mathrm{SD}(a_1 X_1 + \dots + a_n X_n + b) = \sqrt{a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2}$$

**Corollaire (cas $n = 2$).** Pour toutes variables $X_1, X_2$ et constantes $a_1, a_2, b$ :
$$E(a_1 X_1 + a_2 X_2 + b) = a_1 E(X_1) + a_2 E(X_2) + b$$
$$\mathrm{Var}(a_1 X_1 + a_2 X_2 + b) = a_1^2\,\mathrm{Var}(X_1) + a_2^2\,\mathrm{Var}(X_2) + 2 a_1 a_2\,\mathrm{Cov}(X_1, X_2)$$
En particulier :
- $E(X_1 + X_2) = E(X_1) + E(X_2)$ et $E(X_1 - X_2) = E(X_1) - E(X_2)$ ;
- si $X_1$ et $X_2$ sont indépendantes, $\mathrm{Var}(X_1 + X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$ et $\mathrm{Var}(X_1 - X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$.

## Densité d'une somme de variables

En général, connaître la moyenne et l'écart-type d'une variable $W$ ne suffit pas à connaître sa loi, donc à calculer $P(W > 10)$ ou $P(W \le -2)$. Pour des [[Indépendance de variables aléatoires|variables indépendantes]], une méthode générale donne la densité de $X_1 + \dots + X_n$ à partir des densités marginales. Le cours donne le cas de deux variables.

**Théorème.** Si $X$ et $Y$ sont indépendantes, continues, de densités marginales $f_X$ et $f_Y$, la densité de $W = X + Y$ est
$$f_W(w) = \int_{-\infty}^{\infty} f_X(x)\, f_Y(w - x)\,dx$$
C'est le **produit de convolution** de $f_X$ et $f_Y$, parfois noté $f_W = f_X \star f_Y$. Les bornes d'intégration sont les $x$ pour lesquels $f_X(x) > 0$ et $f_Y(w - x) > 0$.

Le chapitre ne contient ni exemple numérique ni exercice.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« $b = 0$ » dans la combinaison linéaire** : la note écrit « constants $a_1, \dots, a_n$, $b = 0$ » alors que $b$ est une constante quelconque dans le théorème qui suit. Seule la moyenne empirique impose $b = 0$ (complément).
2. **Distributivité de la covariance** : l'énoncé donne $\mathrm{Cov}(aX + bY + c, Z) = a\mathrm{Cov}(X, Z) + b\mathrm{Cov}(Y, Z)$. C'est juste, la constante $c$ disparaissant (complément).
3. **Événement sur $S \times S$** : la phrase sur $P((X, Y) \in A)$ parle d'un événement de « $S \times S$ ». Le cadre est celui des couples de valeurs $(x, y)$, pas de l'espace $S$ lui-même. Vérifié sur l'image le 2026-11-06 : l'image écrit bien « sample space $S \times S$ ».
4. **Images tronquées** : le « $y$ » isolé après les lois marginales est le début d'un schéma coupé. Vérifié sur l'image le 2026-11-06 : l'image ne montre que ce « $y$ », le schéma ou tableau annoncé n'est pas dans la note. Rien n'en est repris.
5. **Appel de note « ¹ »** : le corollaire $n = 2$ porte un renvoi « ¹ » après $\mathrm{Var}(X_1 + X_2)$, dont la note de bas de page n'est pas dans le cours.
