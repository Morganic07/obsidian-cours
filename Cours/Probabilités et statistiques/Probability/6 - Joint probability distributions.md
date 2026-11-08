---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 6 : Joint probability distributions.docx|Chp 6 - Joint probability distributions]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 6 : Joint probability distributions.docx|Chp 6 - Joint probability distributions]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les énoncés donnés en images sont recopiés ; seule la figure des nuages de points est intégrée (l'icône d'avertissement est décorative). Les passages ajoutés finissent par ⓘ.

## Idée générale

Étudier plusieurs variables à la fois : loi conjointe, lois marginales, indépendance, covariance, corrélation, combinaisons linéaires et loi d'une somme.

## Loi conjointe de deux variables (*joint pmf & pdf*)

**Définition (cas discret).** Soit $X$ et $Y$ deux variables discrètes définies sur l'[[Espace probabilisé|espace d'échantillonnage]] $S$ d'une expérience. La **fonction de masse conjointe** (*joint [[Variable aléatoire|probability mass function]]*) est définie pour tout couple $(x, y)$ par
$$p(x, y) = P(X = x \text{ et } Y = y)$$

Une fonction $p(x, y)$ peut servir de *pmf* conjointe ([[Loi conjointe]]) si :
1. $p(x, y) \ge 0$ pour tous $x$ et $y$ ;
2. $\sum_{x,y} p(x, y) = 1$.

Si $p$ est la pmf du couple $(X, Y)$ et $A$ un ensemble de couples $(x, y)$ (une partie de $\mathbb{R}^2$), alors [[Erreurs du cours#^e-6-joint-probability-distributions|✎]]
$$P((X, Y) \in A) = \sum_{(x,y) \in A}\sum p(x, y)$$

En pratique, la pmf conjointe de deux variables à peu de valeurs se donne sous forme de tableau à double entrée, comme un [[Tableau de contingence|tableau de contingence]] dont les cases contiennent des probabilités. Exemple qui sert de fil rouge plus bas : [[Complément hors du cours|ⓘ]]

| $p(x, y)$ | $y = 0$ | $y = 1$ |
|---|---|---|
| $x = 0$ | $0{,}2$ | $0{,}3$ |
| $x = 1$ | $0{,}1$ | $0{,}4$ |

**Définition (cas continu).** Soit $X$ et $Y$ continues. $f(x, y)$ est la **densité conjointe** (*joint probability density function*) de $X$ et $Y$ si, pour tout ensemble $A$ du plan,
$$P((X, Y) \in A) = \iint_A f(x, y)\,dx\,dy$$
En particulier, si $A$ est le rectangle $\{(x, y) : a \le x \le b,\ c \le y \le d\}$ :
$$P((X, Y) \in A) = P(a \le X \le b,\ c \le Y \le d) = \int_a^b \int_c^d f(x, y)\,dy\,dx$$
(voir [[Intégrale multiple]]).

Comme dans le cas discret, une fonction $f(x, y)$ est une densité conjointe si et seulement si $f(x, y) \ge 0$ partout et $\displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x, y)\,dx\,dy = 1$. Une valeur $f(x, y)$ n'est pas une probabilité (elle peut dépasser 1) : seule l'intégrale sur une région en est une, et $P(X = x, Y = y) = 0$ pour tout couple. [[Complément hors du cours|ⓘ]]

## Loi conjointe de plus de deux variables

**Définition.** Si $X_1, \dots, X_n$ sont discrètes, leur **pmf conjointe** est
$$p(x_1, x_2, \dots, x_n) = P(X_1 = x_1 \cap X_2 = x_2 \cap \dots \cap X_n = x_n)$$
Si elles sont continues, leur **densité conjointe** est la fonction $f(x_1, \dots, x_n)$ telle que, pour tous intervalles $[a_1, b_1], \dots, [a_n, b_n]$ :
$$P(a_1 \le X_1 \le b_1, \dots, a_n \le X_n \le b_n) = \int_{a_1}^{b_1} \cdots \int_{a_n}^{b_n} f(x_1, \dots, x_n)\,dx_n \dots dx_1$$

## Lois marginales : de deux variables à une seule

**Définition (discret).** Les **fonctions de masse marginales** (*marginal pmfs*) de $X$ et de $Y$ sont
$$p_X(x) = \sum_y p(x, y), \qquad p_Y(y) = \sum_x p(x, y)$$
Elles permettent de retrouver la pmf d'une seule variable à partir de la pmf conjointe.

Le nom vient du tableau : on somme chaque ligne et chaque colonne et on écrit le total dans la *marge*. Sur l'exemple : $p_X(0) = 0{,}2 + 0{,}3 = 0{,}5$, $p_X(1) = 0{,}5$, $p_Y(0) = 0{,}2 + 0{,}1 = 0{,}3$, $p_Y(1) = 0{,}7$. L'inverse est faux : les marginales ne suffisent pas à retrouver la loi conjointe, car des lois conjointes différentes ont les mêmes marginales. [[Complément hors du cours|ⓘ]]

**Définition (continu).** Les **densités marginales** (*marginal pdfs*) sont
$$f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,dy \quad (-\infty < x < \infty), \qquad f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\,dx \quad (-\infty < y < \infty)$$

## Indépendance de deux variables

**Définition.** $X$ et $Y$ sont **indépendantes** ([[Indépendance de variables aléatoires]]) si, pour tout couple $(x, y)$ :
$$p(x, y) = p_X(x) \cdot p_Y(y) \text{ (discret)} \qquad \text{ou} \qquad f(x, y) = f_X(x) \cdot f_Y(y) \text{ (continu)} \quad (1)$$
Si (1) n'est pas vraie pour tous les $(x, y)$, $X$ et $Y$ sont **dépendantes**.

Pour prouver la dépendance, un seul couple suffit. Sur l'exemple : $p(0, 0) = 0{,}2$ alors que $p_X(0)\,p_Y(0) = 0{,}5 \times 0{,}3 = 0{,}15$, donc $X$ et $Y$ sont dépendantes. Une case nulle dans un tableau dont la ligne et la colonne ne sont pas nulles suffit de même. [[Complément hors du cours|ⓘ]]

Dans le cas continu, deux réflexes : si la densité s'écrit $f(x, y) = g(x)\,h(y)$ sur un domaine rectangulaire (produit d'intervalles) et vaut 0 ailleurs, $X$ et $Y$ sont indépendantes ; si le domaine où $f > 0$ n'est pas un rectangle (par exemple $0 < x < y < 1$), elles sont dépendantes, puisque la valeur de $X$ restreint les valeurs possibles de $Y$. [[Complément hors du cours|ⓘ]]

## Loi conditionnelle

La notion n'est pas dans le chapitre, mais elle complète naturellement la loi conjointe et les marginales. La **[[Loi conditionnelle|loi conditionnelle]]** de $Y$ sachant $X = x$ applique la [[Probabilité conditionnelle|probabilité conditionnelle]] à chaque valeur de $Y$, pour tout $x$ tel que $p_X(x) > 0$ (ou $f_X(x) > 0$) : [[Complément hors du cours|ⓘ]]
$$p_{Y|X}(y \mid x) = \frac{p(x, y)}{p_X(x)} \qquad \text{ou} \qquad f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)}$$

Pour chaque $x$ fixé, c'est une vraie loi de probabilité en $y$ (positive, de somme ou d'intégrale 1). Sur l'exemple : $P(Y = 1 \mid X = 1) = 0{,}4 / 0{,}5 = 0{,}8$ et $P(Y = 1 \mid X = 0) = 0{,}3 / 0{,}5 = 0{,}6$. $X$ et $Y$ sont indépendantes si et seulement si la loi conditionnelle de $Y$ ne dépend pas de $x$ et égale la marginale $p_Y$. On en tire l'**espérance conditionnelle** $E(Y \mid X = x) = \sum_y y\, p_{Y|X}(y \mid x)$ (ou $\int y\, f_{Y|X}(y \mid x)\,dy$), base de la régression. [[Complément hors du cours|ⓘ]]

## Espérance pour deux variables

**Proposition.** Soit $X$ et $Y$ de pmf conjointe $p$ ou de densité conjointe $f$. L'[[Espérance et variance|espérance]] d'une fonction $h(X, Y)$, notée $E[h(X, Y)]$ ou $\mu_{h(X,Y)}$, est
$$E[h(X, Y)] = \begin{cases} \displaystyle\sum_x \sum_y h(x, y)\, p(x, y) & \text{discret} \\ \displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} h(x, y)\, f(x, y)\,dx\,dy & \text{continu} \end{cases}$$

**Linéarité de l'espérance.** Pour toutes fonctions $h_1, h_2$ et constantes $a_1, a_2, b$ :
$$E[a_1 h_1(X, Y) + a_2 h_2(X, Y) + b] = a_1 E[h_1(X, Y)] + a_2 E[h_2(X, Y)] + b$$

**Théorème.** Si $X$ et $Y$ sont *indépendantes* et $h(X, Y) = g_1(X) \cdot g_2(Y)$, alors
$$E[h(X, Y)] = E[g_1(X) \cdot g_2(Y)] = E[g_1(X)] \cdot E[g_2(Y)]$$

Cas le plus utilisé : $g_1(X) = X$ et $g_2(Y) = Y$, d'où $E(XY) = E(X)\,E(Y)$ pour des variables indépendantes. Sans indépendance, l'égalité est fausse en général : sur l'exemple, $E(XY) = 1 \times 1 \times 0{,}4 = 0{,}4$ alors que $E(X)\,E(Y) = 0{,}5 \times 0{,}7 = 0{,}35$. [[Complément hors du cours|ⓘ]]

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

La figure explique le signe : le produit $(x - \mu_X)(y - \mu_Y)$ est positif quand $x$ et $y$ sont tous deux au-dessus ou tous deux au-dessous de leur moyenne, négatif sinon ; la covariance est la moyenne de ces produits pondérée par $p(x, y)$. Positive, les grandes valeurs vont ensemble ; négative, elles s'opposent. Sa valeur dépend des unités ($X$ en cm plutôt qu'en m multiplie la covariance par 100), d'où le coefficient de corrélation qui suit. [[Complément hors du cours|ⓘ]]

La formule raccourcie s'obtient en développant le produit et en appliquant la linéarité de l'espérance : $E[(X - \mu_X)(Y - \mu_Y)] = E(XY) - \mu_Y E(X) - \mu_X E(Y) + \mu_X\mu_Y = E(XY) - \mu_X\mu_Y$. Avec $Y = X$, on retrouve $\mathrm{Var}(X) = E(X^2) - \mu_X^2$. Sur l'exemple : $\mathrm{Cov}(X, Y) = 0{,}4 - 0{,}35 = 0{,}05$. [[Complément hors du cours|ⓘ]]

Conséquence du théorème précédent : si $X$ et $Y$ sont indépendantes, $E(XY) = \mu_X\mu_Y$, donc $\mathrm{Cov}(X, Y) = 0$. Autre propriété utile : $\mathrm{Cov}(aX + b, cY + d) = ac\,\mathrm{Cov}(X, Y)$ (les constantes ajoutées disparaissent). [[Complément hors du cours|ⓘ]]

## Corrélation

**Définition.** Le **coefficient de corrélation** de $X$ et $Y$, noté $\mathrm{Corr}(X, Y)$, $\rho_{X,Y}$ ou $\rho$, est
$$\rho_{X,Y} = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$

**Proposition.**
1. Si $X$ et $Y$ sont indépendantes, $\rho = 0$ ; mais $\rho = 0$ n'entraîne pas l'indépendance.
2. $\rho = 1$ ou $-1$ si et seulement si $Y = aX + b$ pour des nombres $a, b$ avec $a \ne 0$.

Propriété fondamentale que le chapitre sous-entend : $-1 \le \rho \le 1$. Preuve : avec $\mathrm{Var}(X/\sigma_X \pm Y/\sigma_Y) = 1 + 1 \pm 2\rho = 2(1 \pm \rho)$ (formule de la variance d'une combinaison linéaire, plus bas), une variance étant positive, $1 + \rho \ge 0$ et $1 - \rho \ge 0$. C'est l'[[Inégalité de Cauchy-Schwarz]] appliquée aux variables centrées : $|\mathrm{Cov}(X, Y)| \le \sigma_X\sigma_Y$. Le signe de $a$ dans le point 2 donne celui de $\rho$ : $\rho = 1$ pour $a > 0$, $\rho = -1$ pour $a < 0$. [[Complément hors du cours|ⓘ]]

Contrairement à la covariance, $\rho$ ne dépend pas des unités : $\mathrm{Corr}(aX + b, cY + d) = \mathrm{Corr}(X, Y)$ si $ac > 0$, et $-\mathrm{Corr}(X, Y)$ si $ac < 0$. Sur l'exemple : $\sigma_X^2 = 0{,}25$, $\sigma_Y^2 = 0{,}7 \times 0{,}3 = 0{,}21$, donc $\rho = 0{,}05 / \sqrt{0{,}25 \times 0{,}21} \approx 0{,}22$, une faible association positive. [[Complément hors du cours|ⓘ]]

Contre-exemple classique au point 1 : $X$ uniforme sur $\{-1, 0, 1\}$ et $Y = X^2$. Alors $E(X) = 0$ et $E(XY) = E(X^3) = 0$, donc $\rho = 0$ ; pourtant $Y$ est entièrement déterminée par $X$, et $P(X = 0, Y = 1) = 0 \ne P(X = 0)\,P(Y = 1) = \frac{1}{3} \times \frac{2}{3}$. La corrélation ne mesure que la dépendance **linéaire** ; une relation en U lui échappe (voir aussi le [[Quatuor d'Anscombe]]). [[Complément hors du cours|ⓘ]]

**[[Corrélation et causalité|Corrélation contre causalité]]** (*correlation versus causation*). Un $\rho$ proche de 1 ne signifie pas qu'augmenter $X$ *fait* augmenter $Y$ ; seulement que les grandes valeurs de $X$ sont *associées* aux grandes valeurs de $Y$. Exemple : chez les enfants, la taille du vocabulaire et le nombre de caries sont assez fortement corrélés positivement, mais les caries ne font pas grandir le vocabulaire : les deux augmentent avec une troisième variable, l'âge. À âge fixé, la corrélation est probablement très faible. Une forte corrélation n'est pas une causalité : « la corrélation mesure l'association, pas la causalité ! »

## Variables non corrélées (*uncorrelated*)

**Proposition.** Deux variables $X$ et $Y$ sont non corrélées si et seulement si $E[XY] = \mu_X \cdot \mu_Y$.

Non corrélées signifie $\rho = 0$, c'est-à-dire $\mathrm{Cov}(X, Y) = 0$ ; la proposition découle directement de la formule raccourcie. On a donc la chaîne : indépendantes $\Rightarrow$ non corrélées, sans réciproque en général. [[Complément hors du cours|ⓘ]]

## Combinaisons linéaires de variables aléatoires

Pour des variables $X_1, \dots, X_n$ et des constantes $a_1, \dots, a_n, b$ quelconques, la [[Combinaison linéaire|combinaison linéaire]]
$$a_1 X_1 + \dots + a_n X_n + b$$
est une nouvelle variable aléatoire, avec sa propre loi, sa moyenne et son écart-type. [[Erreurs du cours#^e-6-joint-probability-distributions|✎]]

Combinaison très importante : la **[[Moyenne empirique|moyenne empirique]]** (*sample mean*) $\bar{X} = \dfrac{X_1 + \dots + X_n}{n}$, obtenue avec $a_1 = \dots = a_n = \frac{1}{n}$ et $b = 0$.

On n'exige ni que les $X_i$ soient indépendantes, ni qu'elles aient la même loi : elles peuvent avoir des moyennes et des écarts-types différents.

**Théorème.** Soit $X_1, \dots, X_n$ de moyennes $\mu_1, \dots, \mu_n$ et d'écarts-types $\sigma_1, \dots, \sigma_n$.

1. Que les $X_i$ soient indépendantes ou non :
$$E(a_1 X_1 + \dots + a_n X_n + b) = a_1 E(X_1) + \dots + a_n E(X_n) + b = a_1\mu_1 + \dots + a_n\mu_n + b \quad (4.4)$$
$$\mathrm{Var}(a_1 X_1 + \dots + a_n X_n + b) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_i a_j\,\mathrm{Cov}(X_i, X_j) = \sum_{i=1}^{n} a_i^2 \sigma_i^2 + 2\sum_{i<j}\sum a_i a_j\,\mathrm{Cov}(X_i, X_j) \quad (4.5)$$
2. Si $X_1, \dots, X_n$ sont indépendantes :
$$\mathrm{Var}(a_1 X_1 + \dots + a_n X_n + b) = a_1^2\,\mathrm{Var}(X_1) + \dots + a_n^2\,\mathrm{Var}(X_n) = a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2 \quad (4.6)$$
$$\mathrm{SD}(a_1 X_1 + \dots + a_n X_n + b) = \sqrt{a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2}$$

D'où vient (4.5) : par distributivité de la covariance (appliquée aux deux arguments), $\mathrm{Var}(\sum a_i X_i + b) = \mathrm{Cov}(\sum_i a_i X_i, \sum_j a_j X_j) = \sum_i\sum_j a_i a_j\,\mathrm{Cov}(X_i, X_j)$ ; la constante $b$ disparaît, et les termes $i = j$ donnent les variances. Avec l'indépendance, tous les $\mathrm{Cov}(X_i, X_j)$, $i \ne j$, sont nuls, d'où (4.6) ; il suffit en fait que les $X_i$ soient deux à deux non corrélées. En écriture matricielle, $\mathrm{Var}(a^T X) = a^T \Sigma\, a$, où $\Sigma$ est la [[Matrice de covariance|matrice de covariance]] du vecteur $(X_1, \dots, X_n)$. [[Complément hors du cours|ⓘ]]

Application majeure à la moyenne empirique : si $X_1, \dots, X_n$ sont indépendantes, de même moyenne $\mu$ et de même écart-type $\sigma$ (un échantillon aléatoire), avec $a_i = \frac{1}{n}$ : [[Complément hors du cours|ⓘ]]
$$E(\bar{X}) = \mu, \qquad \mathrm{Var}(\bar{X}) = n \cdot \frac{1}{n^2}\sigma^2 = \frac{\sigma^2}{n}, \qquad \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

La moyenne de $n$ observations vise donc la bonne valeur et fluctue d'autant moins que $n$ est grand : c'est le point de départ de la [[Loi des grands nombres|loi des grands nombres]], du [[Théorème central limite|théorème central limite]] et de l'erreur standard $\sigma/\sqrt{n}$ des intervalles de confiance. Pour un total $T = X_1 + \dots + X_n$, on a de même $E(T) = n\mu$ et $\mathrm{Var}(T) = n\sigma^2$. [[Complément hors du cours|ⓘ]]

**Corollaire (cas $n = 2$).** Pour toutes variables $X_1, X_2$ et constantes $a_1, a_2, b$ :
$$E(a_1 X_1 + a_2 X_2 + b) = a_1 E(X_1) + a_2 E(X_2) + b$$
$$\mathrm{Var}(a_1 X_1 + a_2 X_2 + b) = a_1^2\,\mathrm{Var}(X_1) + a_2^2\,\mathrm{Var}(X_2) + 2 a_1 a_2\,\mathrm{Cov}(X_1, X_2)$$
En particulier :
- $E(X_1 + X_2) = E(X_1) + E(X_2)$ et $E(X_1 - X_2) = E(X_1) - E(X_2)$ ;
- si $X_1$ et $X_2$ sont indépendantes, $\mathrm{Var}(X_1 + X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$ et $\mathrm{Var}(X_1 - X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$.

Les variances s'ajoutent aussi pour une différence, car $a_2 = -1$ donne $a_2^2 = 1$ : soustraire une variable aléatoire ajoute de l'incertitude, elle ne s'annule pas. Ce sont les variances, pas les écarts-types, qui s'additionnent : $\mathrm{SD}(X_1 + X_2) = \sqrt{\sigma_1^2 + \sigma_2^2} \le \sigma_1 + \sigma_2$. Sans indépendance, $\mathrm{Var}(X_1 - X_2) = \sigma_1^2 + \sigma_2^2 - 2\,\mathrm{Cov}(X_1, X_2)$ : une corrélation positive réduit la variance de la différence, ce qu'exploitent les [[Échantillons appariés et indépendants|échantillons appariés]]. [[Complément hors du cours|ⓘ]]

## Densité d'une somme de variables

En général, connaître la moyenne et l'écart-type d'une variable $W$ ne suffit pas à connaître sa loi, donc à calculer $P(W > 10)$ ou $P(W \le -2)$. Pour des [[Indépendance de variables aléatoires|variables indépendantes]], une méthode générale donne la densité de $X_1 + \dots + X_n$ à partir des densités marginales. Le cours donne le cas de deux variables.

**Théorème.** Si $X$ et $Y$ sont indépendantes, continues, de densités marginales $f_X$ et $f_Y$, la densité de $W = X + Y$ est
$$f_W(w) = \int_{-\infty}^{\infty} f_X(x)\, f_Y(w - x)\,dx$$
C'est le **produit de convolution** de $f_X$ et $f_Y$, parfois noté $f_W = f_X \star f_Y$. Les bornes d'intégration sont les $x$ pour lesquels $f_X(x) > 0$ et $f_Y(w - x) > 0$.

L'idée : pour obtenir $X + Y = w$, il faut $Y = w - x$ quand $X = x$ ; on additionne (on intègre) sur toutes les valeurs $x$ possibles, chaque couple pesant $f_X(x)\,f_Y(w - x)$ grâce à l'indépendance. Version discrète : $p_W(w) = \sum_x p_X(x)\,p_Y(w - x)$, par exemple pour la somme de deux dés. [[Complément hors du cours|ⓘ]]

Exemple : $X$ et $Y$ indépendantes, uniformes sur $[0, 1]$ ([[Loi uniforme]]). Pour $0 \le w \le 1$, les conditions $0 \le x \le 1$ et $0 \le w - x \le 1$ donnent $0 \le x \le w$, donc $f_W(w) = \int_0^w 1\,dx = w$ ; pour $1 \le w \le 2$, elles donnent $w - 1 \le x \le 1$, donc $f_W(w) = 2 - w$ ; $f_W = 0$ ailleurs. La somme suit une **loi triangulaire** sur $[0, 2]$, de pic en 1 : la somme de deux uniformes n'est plus uniforme. [[Complément hors du cours|ⓘ]]

Résultats classiques obtenus par convolution (ou par la [[Fonction génératrice des moments|fonction génératrice des moments]]) : une combinaison linéaire de variables **normales indépendantes** est normale : $a_1X_1 + \dots + a_nX_n + b$ suit la [[Loi normale|loi normale]] de moyenne $\sum a_i\mu_i + b$ et de variance $\sum a_i^2\sigma_i^2$, la moyenne et la variance venant de (4.4) et (4.6) ; d'autres familles sont stables par somme (Poisson, binomiales de même $p$, khi-deux : voir [[Stabilité des lois par somme]]). Pour des lois quelconques et $n$ grand, le [[Théorème central limite|théorème central limite]] donne une loi approximativement normale. [[Complément hors du cours|ⓘ]]

Le chapitre ne contient ni exemple numérique ni exercice.
