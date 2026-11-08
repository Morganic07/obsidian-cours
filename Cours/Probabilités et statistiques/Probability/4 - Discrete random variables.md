---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 4 : Discrete random variables.docx|Chp 4 - Discrete random variables]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 4 : Discrete random variables.docx|Chp 4 - Discrete random variables]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les images à texte et à formule sont recopiées ; les trois graphiques (diagramme en bâtons, histogrammes, fonction de répartition) sont intégrés. Les passages ajoutés finissent par ⓘ.

## Idée générale

Passer des événements aux variables aléatoires : une fonction qui associe un nombre à chaque issue. Le chapitre traite le cas discret : loi de probabilité, fonction de répartition, espérance, variance.

## Variables aléatoires, discrètes et continues

- Une **[[Variable aléatoire|variable aléatoire]]** (*random variable*, rv) est une fonction dont le domaine est l'[[Espace probabilisé|espace d'échantillonnage]] (*sample space*) et dont l'image est une partie de $\mathbb{R}$.
- Une **variable aléatoire discrète** a des valeurs possibles qui forment un ensemble fini ou [[Ensemble dénombrable|infini dénombrable]].
- Une **variable aléatoire continue** a des valeurs possibles qui forment un intervalle ou une union d'intervalles, et aucune valeur n'a une probabilité positive : $P(X = c) = 0$ pour tout $c$.

Exemple : on lance deux fois une pièce ; l'espace d'échantillonnage est $S = \{PP, PF, FP, FF\}$ et $X$ = nombre de « pile » associe $X(PP) = 2$, $X(PF) = X(FP) = 1$, $X(FF) = 0$. Malgré son nom, une variable aléatoire n'est ni une variable ni aléatoire : c'est une fonction fixée, le hasard porte sur l'issue $s$ à laquelle on l'applique. On note en majuscule la variable ($X$) et en minuscule une valeur qu'elle prend ($x$). [[Complément hors du cours|ⓘ]]

Discrète ou continue dépend de ce que l'on mesure : un **comptage** (nombre de clients, de défauts) donne une variable discrète, une **mesure** (durée, taille, masse) une variable continue, traitée au [[5 - Continuous random variable|chapitre 5]]. [[Complément hors du cours|ⓘ]]

## Variables de Bernoulli

Une variable aléatoire qui prend les valeurs 1 et 0 est une **variable de Bernoulli**.

## Loi de probabilité (*probability distribution*, pmf)

La loi de probabilité (ou fonction de masse, *probability mass function*, pmf) d'une variable discrète $X$ est définie pour tout nombre $x$ par :
$$p(x) = P(X = x) = P(\{s \in S \text{ tel que } X(s) = x\})$$
avec $p(x) \ge 0$ et $\sum_x p(x) = 1$. [[Erreurs du cours#^e-4-discrete-random-variables|✎]]

## Diagramme en bâtons et histogramme de probabilité

**Exemple.** Soit la pmf
$$p(x) = \begin{cases} 0{,}8 & \text{si } x = 0 \\ 0{,}2 & \text{si } x = 1 \\ 0 & \text{si } x \ne 0 \text{ et } x \ne 1 \end{cases}$$
On peut la représenter par un **diagramme en bâtons** (*[[Diagramme en bâtons et histogramme de probabilité|line graph]]*) :

![[Chp 4 - Discrete random variables - image1.png]]
*Figure : diagramme en bâtons de $p(x)$ — un bâton de hauteur 0,8 en $x = 0$, un bâton de hauteur 0,2 en $x = 1$.*

**Histogramme de probabilité** (*probability histogram*) : au-dessus de chaque $x$ tel que $p(x) > 0$, placer un rectangle centré en $x$, de hauteur proportionnelle à $p(x)$ ; la base est la même pour tous les rectangles.

![[Chp 4 - Discrete random variables - image9.png]]
*Figure : deux histogrammes de probabilité — (a) rectangles centrés en 0 et 1, celui en 0 bien plus haut ; (b) quatre rectangles contigus centrés en 1, 2, 3, 4, de hauteur décroissante.*

## Probabilité de l'événement $\{X \le x\}$

**Exemple (lits des urgences).** $X$ = nombre de lits occupés aux urgences d'un hôpital à une heure donnée, de pmf :

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $p(x)$ | 0,20 | 0,25 | 0,30 | 0,15 | 0,10 |

Probabilité qu'au plus deux lits soient occupés :
$$P(X \le 2) = p(0) + p(1) + p(2) = 0{,}75$$
Comme $X$ ne prend que des valeurs entières, $\{X \le 2{,}7\}$ et $\{X \le 2\}$ sont le même événement : $P(X \le 2{,}7) = P(X \le 2) = 0{,}75$, et de même $P(X \le 2{,}99) = 0{,}75$.

## Fonction de répartition (*cumulative distribution function*, cdf)

**Définition.** La [[Fonction de répartition|fonction de répartition]] $F$ d'une variable discrète $X$ de pmf $p$ est définie pour tout $x$ par :
$$F(x) = P(X \le x) = \sum_{y\,;\, y \le x} p(y)$$
$F(x)$ est la probabilité que la valeur observée de $X$ soit au plus $x$.

Toute fonction de répartition a quatre propriétés, visibles sur l'exemple qui suit : elle est **croissante** (au sens large) ; elle tend vers 0 en $-\infty$ et vers 1 en $+\infty$ ; elle est **continue à droite** (chaque palier est fermé à gauche) ; dans le cas discret, elle est en escalier et **saute** en chaque valeur possible $x$ d'une hauteur égale à $p(x)$. Réciproquement, toute fonction ayant les trois premières propriétés est la fonction de répartition d'une variable aléatoire. [[Complément hors du cours|ⓘ]]

**Exemple 2.11 (clés USB).** Un magasin vend des clés USB de 1, 2, 4, 8 ou 16 Go. $X$ = mémoire de la clé achetée :

| $x$ | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| $p(x)$ | 0,05 | 0,10 | 0,35 | 0,40 | 0,10 |

Valeurs de $F$ aux cinq valeurs possibles :
- $F(1) = P(X \le 1) = p(1) = 0{,}05$
- $F(2) = P(X = 1 \text{ ou } 2) = p(1) + p(2) = 0{,}15$
- $F(4) = p(1) + p(2) + p(4) = 0{,}50$
- $F(8) = p(1) + p(2) + p(4) + p(8) = 0{,}90$
- $F(16) = P(X \le 16) = 1$

Pour tout autre $x$, $F(x)$ vaut $F$ à la valeur possible de $X$ la plus proche à gauche de $x$ : $F(2{,}7) = P(X \le 2) = 0{,}15$ ; $F(7{,}999) = P(X \le 4) = 0{,}50$. Si $x < 1$, $F(x) = 0$ (ex. $F(0{,}58) = 0$) ; si $x \ge 16$, $F(x) = 1$ (ex. $F(25) = 1$). D'où :
$$F(x) = \begin{cases} 0 & x < 1 \\ 0{,}05 & 1 \le x < 2 \\ 0{,}15 & 2 \le x < 4 \\ 0{,}50 & 4 \le x < 8 \\ 0{,}90 & 8 \le x < 16 \\ 1 & 16 \le x \end{cases}$$

![[Chp 4 - Discrete random variables - image11.jpg]]
*Figure : Fig. 2.5 — graphe en escalier de la cdf de l'exemple 2.11 ; paliers 0, 0,05, 0,15, 0,5, 0,9, puis 1 à partir de $x = 16$, chaque palier fermé à gauche.*

## De la cdf à la pmf

Jusqu'ici on a déduit la cdf de la pmf ; voici l'inverse. Pour deux nombres $a \le b$ : [[Erreurs du cours#^e-4-discrete-random-variables|✎]]
$$P(a \le X \le b) = F(b) - F(a^-)$$
où $a^-$ est la plus grande valeur possible de $X$ strictement inférieure à $a$.

**Exemple (composants défectueux).** $X$ = nombre de composants défectueux dans un lot de six, valeurs $0, 1, \dots, 6$.
$$p(3) = P(X = 3) = [p(0) + p(1) + p(2) + p(3)] - [p(0) + p(1) + p(2)] = P(X \le 3) - P(X \le 2) = F(3) - F(2)$$
$$P(2 \le X \le 4) = p(2) + p(3) + p(4) = [p(0) + \dots + p(4)] - [p(0) + p(1)] = F(4) - F(1)$$
Attention : $P(2 \le X \le 4) \ne F(4) - F(2)$, car la valeur 2 est incluse dans $2 \le X \le 4$ et il ne faut pas retirer sa probabilité. En revanche $P(2 < X \le 4) = F(4) - F(2)$.

## Espérance d'une variable aléatoire

Soit $X$ discrète, d'ensemble de valeurs $D$ et de pmf $p(x)$. L'**espérance** (*[[Espérance et variance|expected value]]*, ou valeur moyenne) de $X$ est :
$$E(X) = \sum_{x \in D} x \cdot p(x)$$

C'est la moyenne des valeurs possibles, chacune pondérée par sa probabilité, ou encore le **centre de gravité** du diagramme en bâtons. Elle s'interprète comme la moyenne des valeurs observées sur un très grand nombre de répétitions indépendantes de l'expérience ([[Loi des grands nombres]]). Elle n'est pas forcément une valeur possible de $X$, et elle a l'unité de $X$. Quand $D$ est infini, la somme est une [[Série numérique|série]] et l'espérance n'existe que si $\sum |x|\,p(x)$ converge. [[Complément hors du cours|ⓘ]]

Exemple (lits des urgences, ci-dessus) : $E(X) = 0 \times 0{,}20 + 1 \times 0{,}25 + 2 \times 0{,}30 + 3 \times 0{,}15 + 4 \times 0{,}10 = 1{,}7$ lit occupé en moyenne, une valeur que $X$ ne prend jamais. [[Complément hors du cours|ⓘ]]

## Espérance d'une fonction d'une variable aléatoire

Si $X$ a pour ensemble de valeurs $D$ et pour pmf $p(x)$, l'espérance de toute fonction $h(X)$ est :
$$E(h(X)) = \sum_{x \in D} h(x) \cdot p(x)$$

**Exemple (diagnostic automobile).** Le coût d'un diagnostic dépend du nombre $X$ de cylindres du moteur : $h(X) = 20 + 3X + 0{,}5X^2$. $Y = h(X)$ est aussi une variable aléatoire :

| $x$ | 4 | 6 | 8 |
|---|---|---|---|
| $p(x)$ | 0,5 | 0,3 | 0,2 |

$\Rightarrow$

| $y$ | 40 | 56 | 76 |
|---|---|---|---|
| $p(y)$ | 0,5 | 0,3 | 0,2 |

Le cours s'arrête aux tables. $E(Y) = 40 \cdot 0{,}5 + 56 \cdot 0{,}3 + 76 \cdot 0{,}2 = 52$. [[Complément hors du cours|ⓘ]]

On obtient le même résultat sans construire la loi de $Y$, avec la formule ci-dessus et la linéarité : $E(X) = 4 \times 0{,}5 + 6 \times 0{,}3 + 8 \times 0{,}2 = 5{,}4$, $E(X^2) = 16 \times 0{,}5 + 36 \times 0{,}3 + 64 \times 0{,}2 = 31{,}6$, d'où $E(Y) = 20 + 3 \times 5{,}4 + 0{,}5 \times 31{,}6 = 52$. Attention : en général $E(h(X)) \ne h(E(X))$. Ici $h(5{,}4) = 20 + 16{,}2 + 14{,}58 = 50{,}78 \ne 52$. Calculer le coût au nombre moyen de cylindres sous-estime le coût moyen. [[Complément hors du cours|ⓘ]]

**Propriétés.**
1. Pour **toutes** fonctions $h_1(X), h_2(X)$ et **toutes** constantes $a_1, a_2, b$ :
$$E(a_1 h_1(X) + a_2 h_2(X) + b) = a_1 E(h_1(X)) + a_2 E(h_2(X)) + b$$
2. En particulier, pour $h(X) = aX + b$ :
$$E(aX + b) = aE(X) + b$$
   On peut alors écrire $\mu_{aX+b} = a\,\mu_X + b$ (seulement dans ce cas !) :
   - a) pour toute constante $a$, $\mu_{aX} = a\,\mu_X$ ;
   - b) pour toute constante $b$, $\mu_{X+b} = \mu_X + b$.

## Variance et écart-type d'une variable aléatoire

**Définition.** Soit $X$ à valeurs dans $D$, de pmf $p(x)$ et d'espérance $\mu$. La **variance** de $X$, notée $\mathrm{Var}(X)$, $\sigma_X^2$ ou $\sigma^2$, est :
$$\mathrm{Var}(X) = \sum_{x \in D} \left[(x - \mu)^2 \cdot p(x)\right] = E\left[(X - \mu)^2\right]$$
L'**écart-type** (*standard deviation*, SD), noté $\sigma_X$ ou $\sigma$, est :
$$\sigma_X = \sqrt{\mathrm{Var}(X)}$$

**Proposition.**
- a) Formule raccourcie (*shortcut formula*) : $\mathrm{Var}(X) = E(X^2) - \mu^2$.
- b) Pour toutes constantes $a, b$ : $\mathrm{Var}(aX + b) = \sigma^2_{aX+b} = a^2 \sigma_X^2$ et $\sigma_{aX+b} = |a|\,\sigma_X$.

La variance mesure la **dispersion** de $X$ autour de sa moyenne : c'est l'écart quadratique moyen à $\mu$. Elle est toujours positive ou nulle, et nulle seulement si $X$ est constante (avec probabilité 1). Elle s'exprime dans l'unité de $X$ au carré, d'où l'usage de l'écart-type, dans l'unité de $X$. [[Complément hors du cours|ⓘ]]

Démonstration de la formule raccourcie, en développant le carré et en utilisant la linéarité de l'espérance : $E[(X - \mu)^2] = E(X^2 - 2\mu X + \mu^2) = E(X^2) - 2\mu E(X) + \mu^2 = E(X^2) - \mu^2$. De même pour b) : $aX + b$ a pour moyenne $a\mu + b$, donc $(aX + b) - (a\mu + b) = a(X - \mu)$ et $\mathrm{Var}(aX + b) = E[a^2(X - \mu)^2] = a^2\sigma_X^2$. Ajouter une constante décale les valeurs sans changer leur dispersion ; multiplier par $a$ multiplie les écarts par $|a|$. [[Complément hors du cours|ⓘ]]

Exemple (lits des urgences, $\mu = 1{,}7$) : $E(X^2) = 0 + 1 \times 0{,}25 + 4 \times 0{,}30 + 9 \times 0{,}15 + 16 \times 0{,}10 = 4{,}4$, donc $\mathrm{Var}(X) = 4{,}4 - 1{,}7^2 = 1{,}51$ et $\sigma \approx 1{,}23$ lit. [[Complément hors du cours|ⓘ]]

**Fonction génératrice des moments, cas discret.** Le [[5 - Continuous random variable|chapitre 5]] renvoie au « cas discret » de la [[Fonction génératrice des moments|fonction génératrice des moments]] : pour $X$ discrète, $M_X(t) = E(e^{tX}) = \sum_{x \in D} e^{tx}p(x)$, avec les mêmes propriétés ($M_X(0) = 1$, $E(X^r) = M_X^{(r)}(0)$, unicité). Exemple : pour une variable de Bernoulli, $M_X(t) = (1 - p) + pe^t$, et $M_X'(0) = p = E(X)$. [[Complément hors du cours|ⓘ]]

Le chapitre ne contient pas d'exercice.
