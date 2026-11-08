---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

## Idée générale

Séries de signe quelconque : séries alternées, convergence absolue, puis critères de d'Alembert et de Cauchy, et une méthode pour choisir le bon critère. Voir [[Série numérique]] et [[Critère de d'Alembert et de Cauchy]].

## Séries alternées (*alternating series*)

**Définition.** Une série alternée est une série $\sum a_n$ avec
$$a_n = (-1)^n b_n \quad\text{ou}\quad a_n = (-1)^{n+1} b_n, \qquad b_n = |a_n| \ge 0.$$
Ses termes sont alternativement positifs et négatifs.

**Théorème (critère des séries alternées, *alternating test*).** Soit $\sum (-1)^{n+1} b_n$ (ou $\sum (-1)^n b_n$). Si
1. la suite $(b_n)$ est décroissante,
2. $\lim b_n = 0$,

alors la série alternée converge. Voir [[Critère des séries alternées]].

Idée de la preuve, pour $\sum (-1)^n b_n$ : $S_{2n+2} - S_{2n} = b_{2n+2} - b_{2n+1} \le 0$ et $S_{2n+3} - S_{2n+1} = b_{2n+2} - b_{2n+3} \ge 0$, donc $(S_{2n})$ décroît, $(S_{2n+1})$ croît, et $S_{2n} - S_{2n+1} = b_{2n+1} \to 0$. Les deux suites sont [[Suites adjacentes|adjacentes]] : elles ont une même limite $S$, donc $(S_n)$ converge vers $S$, et $S$ est toujours compris entre deux sommes partielles consécutives (d'où la proposition sur le reste ci-dessous). [[Complément hors du cours|ⓘ]]

L'hypothèse de décroissance ne peut pas être supprimée : avec $b_n = \frac{1}{\sqrt n} + \frac{(-1)^n}{n}$ (positif, de limite nulle, non décroissant), $\sum (-1)^n b_n = \sum \frac{(-1)^n}{\sqrt n} + \sum \frac{1}{n}$ est la somme d'une série convergente et d'une série divergente, donc diverge. [[Complément hors du cours|ⓘ]]

**Exercice.** Étudier :
1. $\sum_{n\ge1}(-1)^{n-1}\frac{1}{n}$, la série harmonique alternée ;
2. $\sum_{n\in\mathbb{N}}(-1)^n\frac{n^2}{n^3+1}$.

La note indique « Fait sur feuille » : la correction n'est pas rédigée.

Correction : 1. $b_n = \frac{1}{n}$ décroît vers 0, la série harmonique alternée converge ; sa somme vaut $\ln 2$ (développement de $\ln(1+x)$ en $x = 1$, voir [[5 - power series|chapitre 5]]). 2. $b_n = \frac{n^2}{n^3+1} \to 0$, et $f(x) = \frac{x^2}{x^3+1}$ a pour dérivée $\frac{x(2 - x^3)}{(x^3+1)^2}$, négative pour $x \ge 2^{1/3}$ : $(b_n)$ décroît à partir de $n = 2$, et la série converge. Elle n'est pas absolument convergente, car $b_n \sim \frac{1}{n}$. [[Complément hors du cours|ⓘ]]

**Proposition (reste).** Si $\sum (-1)^{n+1} b_n$ vérifie les hypothèses du critère, de somme $S$, alors $S$ est compris entre deux sommes partielles consécutives $S_n$ et $S_{n+1}$, et pour tout $n$ :
$$|R_n| = |S - S_n| \le b_{n+1}.$$

Usage : pour approcher $\ln 2 = \sum_{n \ge 1} \frac{(-1)^{n-1}}{n}$ à $10^{-3}$ près, il suffit que $b_{n+1} = \frac{1}{n+1} \le 10^{-3}$, soit $n \ge 999$ termes. Le reste a en outre le signe de son premier terme, $(-1)^{n+1} b_{n+1}$ pour $\sum (-1)^n b_n$. [[Complément hors du cours|ⓘ]]

**Théorème ($p$-série alternée).** Pour $p$ réel, $\sum_{n} (-1)^n \frac{1}{n^p}$ converge si et seulement si $p > 0$.

Justification : si $p > 0$, $\frac{1}{n^p}$ décroît vers 0 et le critère s'applique ; si $p \le 0$, $\left|\frac{(-1)^n}{n^p}\right| = n^{-p} \ge 1$ ne tend pas vers 0, la série diverge grossièrement. Elle est absolument convergente pour $p > 1$ et conditionnellement convergente pour $0 < p \le 1$. [[Complément hors du cours|ⓘ]]

**Remarque (note de l'étudiante).** On ne peut pas utiliser les équivalents avec des séries alternées : ils sont réservés aux séries à termes positifs.

Contre-exemple : $a_n = \frac{(-1)^n}{\sqrt n}$ et $c_n = \frac{(-1)^n}{\sqrt n} + \frac{1}{n}$ vérifient $a_n \sim c_n$, mais $\sum a_n$ converge (critère des séries alternées) alors que $\sum c_n$ diverge (convergente + divergente). Pour une série de signe variable, on écrit plutôt un [[Développement asymptotique|développement asymptotique]] du terme général et on étudie chaque morceau. [[Complément hors du cours|ⓘ]]

## Séries absolument convergentes

**Définition.** $\sum a_n$ est absolument convergente si $\sum |a_n|$ converge.

**Exemples.**
1. $\sum \frac{(-1)^n}{n^2}$ est absolument convergente, car la $p$-série $\sum \frac{1}{n^2}$ converge.
2. La série harmonique alternée $\sum\frac{(-1)^n}{n}$ converge (critère des séries alternées) mais n'est pas absolument convergente, car $\sum\frac{1}{n}$ diverge.

Pour une série à termes positifs, convergence absolue et convergence coïncident (voir [[Critère de comparaison]]).

**Théorème.** Une série absolument convergente est convergente, et
$$\left|\sum_{n=0}^{+\infty} a_n\right| \le \sum_{n=0}^{+\infty} |a_n|.$$

Preuve : $0 \le a_n + |a_n| \le 2|a_n|$, donc $\sum (a_n + |a_n|)$ converge par comparaison (termes positifs), puis $a_n = (a_n + |a_n|) - |a_n|$ est la différence de deux séries convergentes. L'inégalité vient de l'[[Inégalité triangulaire|inégalité triangulaire]] sur les sommes partielles, $|S_n| \le \sum_{k=0}^n |a_k|$, passée à la limite. [[Complément hors du cours|ⓘ]]

**Définition.** $\sum a_n$ est [[Convergence conditionnelle|conditionnellement convergente]] si elle converge sans être absolument convergente.

La différence compte dès qu'on change l'ordre des termes. Une série absolument convergente peut être réordonnée librement : sa somme ne change pas. Pour une série conditionnellement convergente, le [[Théorème de réarrangement de Riemann]] dit qu'un réordonnancement bien choisi donne n'importe quelle somme réelle fixée à l'avance, ou une série divergente. Exemple : en prenant dans la série harmonique alternée un terme positif puis deux négatifs, $1 - \frac12 - \frac14 + \frac13 - \frac16 - \frac18 + \dots$, on obtient $\frac{\ln 2}{2}$ au lieu de $\ln 2$. [[Complément hors du cours|ⓘ]]

## Critère du rapport (*ratio test*, d'Alembert)

**Théorème.** Soit $\sum a_n$ avec $a_n \ne 0$ à partir d'un rang $n_0$.
1. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = L < 1$, la série est absolument convergente.
2. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = L > 1$ ou $= +\infty$, la série diverge.
3. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = 1$, on ne peut rien conclure.

Idée de la preuve : si $L < 1$, on fixe $q$ avec $L < q < 1$ ; à partir d'un rang $N$, $|a_{n+1}| \le q |a_n|$, donc $|a_n| \le |a_N| q^{n-N}$, et $\sum |a_n|$ converge par comparaison avec une série géométrique de raison $q$. Si $L > 1$, $|a_n|$ finit par croître, donc ne tend pas vers 0 : divergence grossière. [[Complément hors du cours|ⓘ]]

Exemple : pour $a_n = \frac{x^n}{n!}$ ($x$ réel non nul), $\left|\frac{a_{n+1}}{a_n}\right| = \frac{|x|}{n+1} \to 0 < 1$ : la série converge absolument pour tout $x$, et sa somme est $e^x$ (voir [[5 - power series|chapitre 5]]). [[Complément hors du cours|ⓘ]]

**Exemples avec $L = 1$** :

| $a_n$ | Nature de $\sum a_n$ |
|---|---|
| $(-1)^n \frac{n}{n^2+1}$ | conditionnellement convergente |
| $\frac{1}{n}$ | divergente |
| $(-1)^n \frac{1}{n^2+1}$ | absolument convergente |

## Critère de la racine (*root test*, Cauchy)

Pratique quand apparaissent des puissances $n$-ièmes ; la preuve est analogue à celle du critère du rapport.

**Théorème.** Soit $\sum a_n$ avec $a_n \ne 0$ à partir d'un rang $n_0$.
1. Si $\lim \sqrt[n]{|a_n|} = L < 1$, la série est absolument convergente.
2. Si $\lim \sqrt[n]{|a_n|} = L > 1$ ou $= +\infty$, la série diverge.
3. Si $\lim \sqrt[n]{|a_n|} = 1$, on ne peut rien conclure.

**Exercice.** Étudier $\sum_{n\ge1}\left(\frac{2n+3}{3n+2}\right)^n$ et $\sum_{n\ge2}\frac{n^{\ln n}}{n^n}$. Le cours ne donne pas la correction.

Correction : 1. $\sqrt[n]{a_n} = \frac{2n+3}{3n+2} \to \frac{2}{3} < 1$, la série converge. 2. $\sqrt[n]{a_n} = \frac{n^{(\ln n)/n}}{n} = \frac{e^{(\ln n)^2/n}}{n}$ ; par croissances comparées $\frac{(\ln n)^2}{n} \to 0$, donc le numérateur tend vers 1 et $\sqrt[n]{a_n} \to 0 < 1$ : la série converge. [[Complément hors du cours|ⓘ]]

**Remarque.** On peut montrer que si la limite du critère du rapport existe et vaut $L = 1$, alors $L = 1$ dans celui de la racine : les deux critères échouent alors. La réciproque est fausse en général : la limite de la racine peut exister (et valoir 1) sans que celle du rapport existe. [[Erreurs du cours#^e-2-alternating-and-absolutly-convergent-series|✎]]

## Méthode pour choisir le bon critère

- Forme $\sum_{n\ge1}\frac{1}{n^p}$ : $p$-série ([[1 - Convergent, divergent and positive terms SERIES|séries de Riemann]]).
- Forme $\sum ar^n$ : série géométrique.
- Forme voisine d'une $p$-série ou d'une série géométrique : comparaison, comparaison par la limite, ou équivalents. En particulier, si $a_n$ est une fraction rationnelle ou une fonction algébrique, comparer à une $p$-série. Ces critères ne valent que pour des termes positifs ; si la série a des termes négatifs, les appliquer à $\sum |a_n|$ pour tester la convergence absolue.
- Si $\lim a_n \ne 0$ : [[Condition nécessaire de convergence|divergence grossière]] (*test for divergence*).
- Forme $\sum(-1)^n b_n$ ou $\sum(-1)^{n+1} b_n$ : critère des séries alternées.
- Factorielles ou produits : critère du rapport, sauf pour les $p$-séries, où la limite du rapport vaut 1.
- $a_n = (b_n)^n$ : critère de la racine.
- $a_n = f(n)$ avec $\int_1^{+\infty} f$ facile à calculer et $f$ vérifiant les bonnes hypothèses : [[Comparaison série-intégrale|critère intégral]] (*integral test*).
