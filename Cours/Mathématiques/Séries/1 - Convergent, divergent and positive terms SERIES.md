---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp1 : Convergent, divergent and positive terms SERIES.docx|Chp1 - Convergent, divergent and positive terms SERIES]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Séries/Chp1 : Convergent, divergent and positive terms SERIES.docx|Chp1 - Convergent, divergent and positive terms SERIES]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. Les énoncés en image sont recopiés en texte ; seules les trois figures de la comparaison série-intégrale sont intégrées.

## Idée générale

Définition d'une [[Série numérique]], séries de référence (géométrique, télescopique, harmonique, de Riemann) et critères pour les séries à termes positifs.

## Séries convergentes et divergentes

### Définition

**Définition.** Soit $(a_n)$ une suite réelle. Pour $n \in \mathbb{N}$, on pose $S_n = \sum_{k=0}^{n} a_k$. La suite $(S_n)$ s'appelle une **série**, notée $\sum_{n\in\mathbb{N}} a_n$ ; $S_n$ est une **somme partielle** (*partial sum*).

**Définition (convergence).** La série $\sum a_n$ est convergente si la suite $(S_n)$ converge. Sa limite est alors la **somme** de la série :
$$S = \lim_{n\to+\infty} S_n = \lim_{n\to+\infty} \sum_{k=0}^{n} a_k = \sum_{n=0}^{+\infty} a_n.$$
Si $(S_n)$ diverge, la série est divergente et n'a pas de somme.

**Remarque.** Une série peut commencer à $n = n_0$ au lieu de 0 : on note $\sum_{n \ge n_0} a_n$.

### Série géométrique

**Définition.** Pour $a$ et $r$ réels non nuls, $\sum_{n\in\mathbb{N}} ar^n$ est la série géométrique de raison $r$ (voir [[Suite géométrique]]).

**Théorème.** $\sum ar^n$ converge si et seulement si $|r| < 1$. Sa somme vaut alors
$$S = \frac{a}{1-r}.$$

**Note de cours.** $\Sigma_0$ (somme à partir de $n = 0$) est la formule ci-dessus ; $\Sigma_1$ (somme à partir de $n = 1$) est cette formule moins $a_0$.

**Preuve.**
1. Si $r = 1$ : $S_n = a(n+1) \to \pm\infty$, la série diverge.
2. Si $r \ne 1$ : $S_n = \sum_{k=0}^{n} ar^k$ et $rS_n = \sum_{k=1}^{n+1} ar^k$, donc $S_n - rS_n = a - ar^{n+1}$, d'où
$$S_n = a\,\frac{1-r^{n+1}}{1-r}.$$
   - Si $-1 < r < 1$ : $r^n \to 0$, donc $S_n \to \frac{a}{1-r}$, la série converge.
   - Si $r > 1$ ou $r \le -1$ : $(r^n)$ diverge, $\lim S_n$ n'existe pas, la série diverge.

Exemples : $\sum_{n \ge 0} \frac{1}{2^n} = \frac{1}{1 - 1/2} = 2$, et $\sum_{n \ge 1} \frac{1}{2^n} = 2 - 1 = 1$ (note $\Sigma_1$ ci-dessus). Le développement décimal $0{,}999\ldots = \sum_{n \ge 1} \frac{9}{10^n} = \frac{9/10}{1 - 1/10} = 1$ est une série géométrique : il prouve que $0{,}999\ldots = 1$. [[Complément hors du cours|ⓘ]]

### Série télescopique

**Définition.** Soit $(a_n)$ une suite et $u_n = a_n - a_{n-1}$ pour $n \ge 1$. La série $\sum_{n \ge 1} u_n$ est une série télescopique (*telescoping series*). Voir [[Somme télescopique]].

**Proposition.** $\sum_{n\ge1}(a_n - a_{n-1})$ converge si et seulement si $(a_n)$ converge. Si $a_n \to \ell$, la somme vaut
$$S = \sum_{n=1}^{+\infty}(a_n - a_{n-1}) = \ell - a_0.$$

**Preuve.** $S_n = \sum_{k=1}^{n}(a_k - a_{k-1}) = a_n - a_0$.

**Note de cours.** Si le terme est $a_{k-1} - a_k$, alors $S_n = a_0 - a_n$, de limite $a_0 - \ell$.

**Exercice.** Étudier $\sum_{n\ge1} \frac{1}{n(n+1)}$. Le cours ne donne pas la correction.

Correction : $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$ ([[Décomposition en éléments simples|décomposition en éléments simples]]), donc $S_n = 1 - \frac{1}{n+1} \to 1$ : la série télescopique converge et sa somme vaut 1. [[Complément hors du cours|ⓘ]]

### Série harmonique

**Définition.** $\sum_{n\ge1}\frac{1}{n}$ est la série harmonique.

**Proposition.** La série harmonique diverge.

**Preuve (par l'absurde, voir [[Raisonnement par l'absurde]]).** Si elle convergeait vers $S$, on aurait $S_{2n} - S_n \to S - S = 0$. Or
$$S_{2n} - S_n = \sum_{k=n+1}^{2n} \frac{1}{k} \ge n \times \frac{1}{2n} = \frac{1}{2}.$$
À la limite, $0 \ge \frac{1}{2}$ : contradiction.

**Note de cours.** Ajouter des termes de plus en plus petits ne donne pas toujours une série convergente.

La divergence est très lente : la comparaison avec $\int \frac{dx}{x}$ donne $\ln(n+1) \le S_n \le 1 + \ln n$, donc $S_n \sim \ln n$, et $S_n - \ln n$ tend vers la [[Constante d'Euler|constante d'Euler]] $\gamma \approx 0{,}5772$. Il faut environ $1{,}2 \times 10^{4}$ termes pour que $S_n$ dépasse 10. La première preuve connue de la divergence, par regroupement des termes ($\frac13 + \frac14 \ge \frac12$, $\frac15 + \dots + \frac18 \ge \frac12$, etc.), est due à Nicole Oresme au XIVe siècle. [[Complément hors du cours|ⓘ]]

### Condition nécessaire de convergence

**Théorème.** Si $\sum a_n$ converge, alors $\lim a_n = 0$. Voir [[Condition nécessaire de convergence]].

**Preuve.** $a_n = S_n - S_{n-1}$ et $S_n, S_{n-1} \to S$, donc $a_n \to 0$.

**Remarque.** Condition nécessaire, pas suffisante : la série harmonique en est le contre-exemple.

**Théorème (contraposée).** Si $\lim a_n$ n'existe pas ou est non nulle, la série diverge (divergence grossière).

### Reste d'une série convergente

**Définition.** Pour une série convergente de somme $S$, le $n$-ième [[Reste d'une série|reste]] est
$$R_n = S - S_n = \sum_{k \ge n+1} a_k.$$

**Proposition.** $\lim R_n = 0$ (car $R_n = S - S_n$).

**Remarque.** Si $\sum_{k \ge n+1} a_k$ n'a pas de limite ou ne tend pas vers 0, la série diverge. [[Erreurs du cours#^e-1-convergent-divergent-and-positive-terms-series|✎]]

### Opérations sur les séries

**Définition.** Pour $\lambda \in \mathbb{R}$, $\sum (a_n + \lambda b_n)$ est une [[Combinaison linéaire]] de $\sum a_n$ et $\sum b_n$.

**Théorème.** Si $\sum a_n$ et $\sum b_n$ convergent, alors $\sum(a_n + \lambda b_n)$ converge et
$$\sum_{n=0}^{+\infty} (a_n + \lambda b_n) = \sum_{n=0}^{+\infty} a_n + \lambda \sum_{n=0}^{+\infty} b_n.$$

**Preuve.** Avec $S_n = \sum_{k=0}^n a_k \to S$ et $T_n = \sum_{k=0}^n b_k \to T$, la somme partielle vaut $U_n = S_n + \lambda T_n \to S + \lambda T$. [[Erreurs du cours#^e-1-convergent-divergent-and-positive-terms-series|✎]]

**Conséquences (notes de cours).**
1. Somme de deux séries convergentes : convergente ($\lambda = 1$).
2. Différence de deux séries convergentes : convergente ($\lambda = -1$).
3. Convergente + divergente : divergente. Preuve : si $\sum(a_n + b_n)$ convergeait, $\sum b_n = \sum (a_n + b_n) + \sum(-a_n)$ convergerait, contradiction.
4. Divergente + divergente : convergente ou divergente, selon les cas.

## Séries à termes positifs

### Critère de la suite majorée

**Lemme.** Une série à termes positifs converge si et seulement si $(S_n)$ est majorée :
$$\sum a_n \text{ converge} \Leftrightarrow \exists M \ge 0,\ \forall n,\ S_n \le M.$$

**Preuve.** Si la série converge, $(S_n)$ converge, donc est bornée. Réciproquement, $S_{n+1} - S_n = a_{n+1} \ge 0$ : $(S_n)$ est croissante et majorée, donc converge.

**Proposition.** Pour une série à termes positifs :
1. si elle converge de somme $S$, alors $\forall n,\ S_n \le S$ (car $R_n = \sum_{k\ge n+1} a_k \ge 0$) ;
2. si elle diverge, alors $S_n \to +\infty$ (suite croissante non majorée).

### Critères de comparaison

Voir [[Critère de comparaison]].

**Proposition (inégalité).** Si $\sum a_n$, $\sum b_n$ sont à termes positifs et $\forall n,\ a_n \le b_n$ :
1. $\sum b_n$ converge $\Rightarrow$ $\sum a_n$ converge ;
2. $\sum a_n$ diverge $\Rightarrow$ $\sum b_n$ diverge.

**Proposition (grand $O$).** Mêmes conclusions si $a_n = O(b_n)$.
Preuve : il existe $M > 0$ tel que $0 \le a_n \le M b_n$ ; si $\sum b_n$ converge, $\sum M b_n$ aussi, donc $\sum a_n$. Le point 2 est la contraposée.

**Corollaire (petit $o$).** Mêmes conclusions si $a_n = o(b_n)$, car $o$ implique $O$.

**Exemples.**
1. $e^{-n^2} = o\left(\frac{1}{n^2}\right)$ et $\sum_{n\ge1}\frac{1}{n^2}$ converge, donc $\sum_{n\ge0} e^{-n^2}$ converge.
2. $\frac{1}{n} = o\left(\frac{\ln n}{\sqrt n}\right)$ et $\sum \frac{1}{n}$ diverge, donc $\sum_{n\ge1}\frac{\ln n}{\sqrt n}$ diverge.

**Proposition (limite du quotient).** Si $\sum a_n$, $\sum b_n$ sont à termes positifs et $\lim \frac{a_n}{b_n} = c$ avec $c$ réel fini **strictement positif**, les deux séries sont de même nature. Le cours insiste : $c$ doit être $\ne 0$.

**Preuve.** On choisit $0 < m < c < M$. À partir d'un rang $N$, $m < \frac{a_n}{b_n} < M$, donc $m b_n < a_n < M b_n$. Si $\sum b_n$ converge, $\sum M b_n$ converge, donc $\sum a_n$ ; si $\sum b_n$ diverge, $\sum m b_n$ diverge, donc $\sum a_n$ diverge.

**Corollaire (équivalents).** Si $a_n \underset{+\infty}{\sim} b_n$ (termes positifs), les deux séries sont de même nature. Voir [[Équivalent (comparaison asymptotique)]].

Exemple : $\frac{n+1}{n^3 + 2} \sim \frac{1}{n^2}$, de signe positif, donc $\sum \frac{n+1}{n^3+2}$ converge ; $\sin \frac{1}{n} \sim \frac{1}{n}$, donc $\sum \sin\frac{1}{n}$ diverge. Il suffit que les termes soient positifs à partir d'un certain rang, ou tous négatifs (on raisonne alors sur $-a_n$). [[Complément hors du cours|ⓘ]]

### Comparaison série-intégrale

Voir [[Comparaison série-intégrale]].

**Théorème.** Soit $n_0 \in \mathbb{N}$ et $f$ continue, positive et décroissante sur $[n_0, +\infty[$, et $a_n = f(n)$. Alors $\sum_{n\ge n_0} a_n$ converge si et seulement si l'intégrale impropre $\int_{n_0}^{+\infty} f(x)\,dx$ converge.

**Preuve.** On peut supposer $n_0 = 1$ ; $S_n = \sum_{k=1}^{n} a_k$.

![[Chp1 - Convergent, divergent and positive terms SERIES - image39.png]]

*Figure : aire sous la courbe. Les rectangles de largeur 1 et de hauteurs $a_2, \ldots, a_n$ sont sous la courbe décroissante $y = f(x)$, entre 1 et $n$.*

![[Chp1 - Convergent, divergent and positive terms SERIES - image42.png]]

*Figure : aire au-dessus de la courbe. Les rectangles de hauteurs $a_1, \ldots, a_{n-1}$ dépassent la courbe, entre 1 et $n$.*

En comparant les aires :
$$S_n - a_1 = a_2 + \dots + a_n \le \int_1^n f(x)\,dx \quad (1)$$
$$\int_1^n f(x)\,dx \le a_1 + \dots + a_{n-1} = S_{n-1} \quad (2)$$

- Si $\int_1^{+\infty} f$ converge, (1) et $f \ge 0$ donnent $S_n \le a_1 + \int_1^{+\infty} f(x)\,dx$ : $(S_n)$ est majorée, la série converge (lemme ci-dessus).
- Si $\int_1^{+\infty} f$ diverge, $\int_1^n f \to +\infty$ (car $f \ge 0$), et (2) donne $S_{n-1} \to +\infty$ : la série diverge.

### Encadrement du reste

**Proposition.** Mêmes hypothèses sur $f$, et $\sum_{n\ge n_0} a_n$ convergente de somme $S$. Pour tout $n \ge n_0$ :
$$S_n + \int_{n+1}^{+\infty} f(x)\,dx \le S \le S_n + \int_{n}^{+\infty} f(x)\,dx.$$

**Preuve.** Avec $R_n = S - S_n = \sum_{k\ge n+1} a_k$, la figure donne $\int_{n+1}^{+\infty} f \le R_n \le \int_n^{+\infty} f$, puis on ajoute $S_n$.

![[Chp1 - Convergent, divergent and positive terms SERIES - image34.png]]

*Figure : encadrement du reste $R_n$ par deux intégrales, rectangles de hauteurs $a_{n+1}, a_{n+2}, \ldots$ partant de $n$ (à gauche) et de $n+1$ (à droite).*

**Remarque.** Cet encadrement estime la somme bien mieux que la seule somme partielle.

**Exemple.** Estimation de $\sum_{n=1}^{+\infty}\frac{1}{n^3}$ avec $n = 20$ :
$$S_{20} + \int_{21}^{+\infty}\frac{dx}{x^3} \le S \le S_{20} + \int_{20}^{+\infty}\frac{dx}{x^3}, \quad\text{soit}\quad S_{20} + \frac{1}{2(21)^2} \le S \le S_{20} + \frac{1}{2(20)^2}.$$
Avec $S_{20} = 1.20087$, on obtient $1.20200 \le S \le 1.20212$. [[Erreurs du cours#^e-1-convergent-divergent-and-positive-terms-series|✎]]

### Séries de Riemann

**Théorème.** Pour $p$ réel, la série $\sum_{n\ge1}\frac{1}{n^p}$ (*p-series*, série de Riemann) converge si et seulement si $p > 1$.

Preuve : si $p \le 0$, $\frac{1}{n^p}$ ne tend pas vers 0 (divergence grossière). Si $p > 0$, $f(x) = \frac{1}{x^p}$ est continue, positive et décroissante sur $[1, +\infty[$, et $\int_1^{X} \frac{dx}{x^p}$ vaut $\frac{X^{1-p} - 1}{1-p}$ si $p \ne 1$ et $\ln X$ si $p = 1$ : l'intégrale converge si et seulement si $p > 1$, et la comparaison série-intégrale conclut. [[Complément hors du cours|ⓘ]]

La somme $\sum_{n \ge 1} \frac{1}{n^p}$ définit, pour $p > 1$, la fonction zêta de Riemann $\zeta(p)$. Euler a établi en 1735 que $\zeta(2) = \sum \frac{1}{n^2} = \frac{\pi^2}{6}$ (problème de Bâle) ; on sait aussi que $\zeta(4) = \frac{\pi^4}{90}$, et l'exemple ci-dessus estime $\zeta(3) \approx 1{,}202$. La valeur $\frac{\pi^2}{6}$ se retrouve avec les [[Série de Fourier|séries de Fourier]] et l'égalité de Parseval ([[6 - Fourier Series|chapitre 6]]). [[Complément hors du cours|ⓘ]]

Les [[Série de Bertrand|séries de Bertrand]] $\sum_{n \ge 2} \frac{1}{n^\alpha (\ln n)^\beta}$ affinent l'échelle de Riemann : elles convergent si et seulement si $\alpha > 1$, ou $\alpha = 1$ et $\beta > 1$. Exemple : $\sum \frac{1}{n \ln n}$ diverge (comparaison avec $\int \frac{dx}{x \ln x} = \ln(\ln x)$), alors que $\sum \frac{1}{n (\ln n)^2}$ converge. [[Complément hors du cours|ⓘ]]

**Corollaire (règle $n^p a_n$).** Pour une série à termes positifs :
1. s'il existe $p > 1$ tel que $\lim n^p a_n = 0$, la série converge ;
2. s'il existe $p \le 1$ tel que $\lim n^p a_n = +\infty$, la série diverge.

**Preuve.**
1. $p > 1$ : $\sum \frac{1}{n^p}$ converge, et $n^p a_n \to 0$ signifie $a_n = o\left(\frac{1}{n^p}\right)$, donc $\sum a_n$ converge.
2. $p \le 1$ : $\sum\frac{1}{n^p}$ diverge ; à partir d'un rang $n_0$, $n^p a_n \ge 1$, donc $a_n \ge \frac{1}{n^p}$, et la comparaison conclut à la divergence.

La note se termine sur le titre « Alternating series », traité dans [[2 - Alternating and absolutly convergent series|le chapitre 2]].