---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp4 : Series of functions.docx|Chp4 - Series of functions]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Séries/Chp4 : Series of functions.docx|Chp4 - Series of functions]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. Les énoncés en image sont recopiés en texte ; seul le schéma des modes de convergence est intégré.

## Idée générale

Une série de fonctions est la suite de ses sommes partielles : on applique les résultats sur les séries numériques (en fixant $x$) et ceux de [[3 - Sequence of function|la convergence uniforme]]. Voir [[Convergence uniforme]] et [[Série numérique]].

## Définition d'une série de fonctions

**Définition.** Soit $(f_n)$ une suite de fonctions définies sur $X \subset \mathbb{R}$. La suite des sommes partielles $(S_n)$ est définie par
$$\forall x \in X,\ S_n(x) = \sum_{k=0}^{n} f_k(x).$$
La série de fonctions, notée $\sum_{n\in\mathbb{N}} f_n$ (ou $\sum_{n\ge n_0} f_n$ si elle commence à $n_0$), est la suite des sommes partielles. [[Erreurs du cours#^e-4-series-of-functions|✎]]

## Convergence simple

**Définition.** $\sum f_n$ converge simplement sur $X$ si la suite de fonctions $(S_n)$ converge simplement sur $X$. Sa limite simple est la **somme** de la série : [[Erreurs du cours#^e-4-series-of-functions|✎]]
$$\forall x \in X,\ S(x) = \left(\sum_{n=0}^{+\infty} f_n\right)(x) = \lim_{n\to+\infty} S_n(x) = \lim_{n\to+\infty} \sum_{k=0}^{n} f_k(x).$$
Sinon, la série est divergente.

**Remarques.**
- Pour étudier la convergence simple, on fixe $x$ : on obtient une série numérique, à laquelle s'appliquent toutes les méthodes du chapitre sur les séries numériques ([[1 - Convergent, divergent and positive terms SERIES|chapitre 1]], [[2 - Alternating and absolutly convergent series|chapitre 2]]).
- Les sommes partielles sont des suites de fonctions : on étudie donc aussi plusieurs types de convergence et des théorèmes d'interversion.
- Ce chapitre utilise donc les définitions, propriétés et théorèmes des deux chapitres précédents.

## Reste d'une série simplement convergente

**Définition.** Si $\sum f_n$ converge simplement vers $S$ sur $X$, le $n$-ième reste est
$$R_n = S - S_n = \sum_{k\ge n+1} f_k, \qquad R_n(x) = S(x) - S_n(x) = \sum_{k\ge n+1} f_k(x).$$
Voir [[Reste d'une série]].

**Proposition.** $(R_n)$ converge simplement vers la fonction nulle.

## Convergence uniforme

**Définition.** $\sum f_n$ converge uniformément sur $X$ si la suite $(S_n)$ converge uniformément sur $X$.

**Proposition.** $\sum f_n$ converge uniformément sur $X$ si et seulement si elle converge simplement sur $X$ **et** la suite des restes $(R_n)$ converge uniformément vers la fonction nulle sur $X$.

En pratique, on majore $|R_n(x)|$ indépendamment de $x$. Le cas classique est celui d'une série alternée en chaque $x$ : par le [[Critère des séries alternées]], $|R_n(x)| \le |f_{n+1}(x)|$, donc $\|R_n\|_\infty \le \|f_{n+1}\|_\infty$, et il suffit que $\|f_{n+1}\|_\infty \to 0$. Exemple : $\sum_{n\ge1} (-1)^{n} \frac{x^n}{n}$ sur $[0, 1]$, où $\|R_n\|_\infty \le \frac{1}{n+1} \to 0$ : la convergence est uniforme. [[Complément hors du cours|ⓘ]]

**Proposition.** Si $\sum f_n$ converge uniformément sur $X$, alors $(f_n)$ converge uniformément vers la fonction nulle sur $X$.

**Corollaire.** Si $f_n = S_n - S_{n-1}$ ne converge pas uniformément vers 0 sur $X$, alors $\sum f_n$ ne converge pas uniformément sur $X$.
Preuve : contraposée de la proposition précédente.

## Convergence normale

**Définition.** $\sum f_n$ converge normalement sur $X$ si chaque $f_n$ est bornée sur $X$ et si la série numérique $\sum \|f_n\|_\infty$ converge.

**Proposition (critère de Weierstrass, *Weierstrass M-test*) — condition suffisante.** S'il existe une série numérique convergente à termes positifs $\sum a_n$ telle que
$$\forall n,\ \|f_n\|_\infty \le a_n,$$
alors $\sum f_n$ converge normalement sur $X$.

**Exemple : la série géométrique $\sum x^n$.** Elle converge simplement sur $]-1, 1[$ vers $\frac{1}{1-x}$, avec $R_n(x) = \frac{x^{n+1}}{1-x}$. Sur $[-a, a]$ avec $0 < a < 1$, $\|x^n\|_\infty = a^n$ et $\sum a^n$ converge : la convergence est normale. Sur $]-1, 1[$ entier, $\|x^n\|_\infty = 1$ ne tend pas vers 0 : la convergence n'y est ni normale ni même uniforme (proposition sur $(f_n)$ ci-dessus). [[Complément hors du cours|ⓘ]]

**Autre exemple.** Pour $\sum_{n\ge1} \frac{\sin(nx)}{n^2}$ sur $\mathbb{R}$, $\left|\frac{\sin(nx)}{n^2}\right| \le \frac{1}{n^2}$ et $\sum \frac{1}{n^2}$ converge : convergence normale, donc somme continue sur $\mathbb{R}$. [[Complément hors du cours|ⓘ]]

## Convergence absolue

**Définition.** $\sum f_n$ est absolument convergente sur $X$ si, pour tout $x \in X$, la série numérique $\sum f_n(x)$ est absolument convergente, c'est-à-dire si $\sum |f_n(x)|$ converge.

La convergence absolue implique la convergence simple.

## Relations entre les modes de convergence

**Théorème.** Si $\sum f_n$ converge normalement sur $X$, elle converge uniformément, absolument et simplement.

![[Chp4 - Series of functions - image17.png]]

*Figure : la convergence normale implique la convergence uniforme et la convergence absolue, qui impliquent chacune la convergence simple.*

$$\text{normale} \Rightarrow \text{uniforme} \Rightarrow \text{simple}, \qquad \text{normale} \Rightarrow \text{absolue} \Rightarrow \text{simple}.$$

**Pourquoi normale implique uniforme.** Pour tout $x$, $|R_n(x)| \le \sum_{k\ge n+1} |f_k(x)| \le \sum_{k\ge n+1} \|f_k\|_\infty$. Le majorant est le reste d'une série numérique convergente : il tend vers 0 et ne dépend pas de $x$, donc $\|R_n\|_\infty \to 0$. [[Complément hors du cours|ⓘ]]

**Les réciproques sont fausses.** [[Complément hors du cours|ⓘ]]
- Uniforme sans être normale ni absolue : les fonctions constantes $f_n(x) = \frac{(-1)^n}{n}$ ($n \ge 1$). La série converge uniformément (ses restes ne dépendent pas de $x$ et tendent vers 0), mais $\sum \|f_n\|_\infty = \sum \frac{1}{n}$ diverge. [[Complément hors du cours|ⓘ]]
- Absolue sans être uniforme : $\sum x^n$ sur $]-1, 1[$ (exemple ci-dessus). [[Complément hors du cours|ⓘ]]

## Interversion somme-limite

**Théorème.** Soit $a$ un [[Point limite]] de $X$. On suppose :
- pour tout $n$, il existe $\ell_n \in \mathbb{R}$ tel que $\lim_{x\to a} f_n(x) = \ell_n$ ;
- $\sum f_n$ converge uniformément sur $X$ vers $S$. [[Erreurs du cours#^e-4-series-of-functions|✎]]

Alors $\sum \ell_n$ converge et $\lim_{x\to a} S(x) = \sum_{n=0}^{+\infty} \ell_n$, soit
$$\lim_{x\to a}\left(\sum_{n=0}^{+\infty} f_n(x)\right) = \sum_{n=0}^{+\infty} \lim_{x\to a} f_n(x).$$
Voir [[Interversion de limites]].

## Continuité en un point et sur un ensemble

**Corollaire.** Soit $x_0 \in X$. Si chaque $f_n$ est continue en $x_0$ et si $\sum f_n$ converge uniformément sur $X$, alors $S = \sum_{n=0}^{+\infty} f_n$ est continue en $x_0$.

**Corollaire.** Si chaque $f_n$ est continue sur $X$ et si $\sum f_n$ converge uniformément sur $X$, alors $S$ est continue sur $X$.

**Exemple : la fonction zêta de Riemann.** $\zeta(x) = \sum_{n\ge1} \frac{1}{n^x}$ converge simplement sur $]1, +\infty[$ (séries de Riemann). Elle ne converge pas normalement sur $]1, +\infty[$ entier ($\sup_{x>1} \frac{1}{n^x} = \frac{1}{n}$), mais sur tout $[a, +\infty[$ avec $a > 1$, $\frac{1}{n^x} \le \frac{1}{n^a}$ et $\sum \frac{1}{n^a}$ converge. La continuité étant locale, $\zeta$ est continue sur $]1, +\infty[$. C'est la démarche type : convergence normale sur des parties bien choisies, puis conclusion sur l'ensemble entier. [[Complément hors du cours|ⓘ]]

## Interversion somme-intégrale et somme-dérivée

**Théorème (intégration terme à terme).** Soient $a < b$ et des $f_n$ définies sur $[a, b]$. Si
1. chaque $f_n$ est continue sur $[a, b]$,
2. $\sum f_n$ converge uniformément sur $[a, b]$,

alors $S$ est continue sur $[a, b]$, la série $\sum \int_a^b f_n$ converge vers $\int_a^b S$, et
$$\sum_{n=0}^{+\infty} \int_a^b f_n(t)\,dt = \int_a^b \sum_{n=0}^{+\infty} f_n(t)\,dt.$$

**Théorème (dérivation terme à terme).** Soit $(f_n)$ une suite de fonctions dérivables sur un intervalle **borné** $I$, telle que
1. il existe $x_0 \in I$ tel que $\sum f_n(x_0)$ converge,
2. $\sum f_n'$ converge uniformément sur $I$.

Alors $\sum f_n$ converge uniformément sur $I$ vers une fonction $S$ dérivable, et
$$S' = \left(\sum f_n\right)' = \sum f_n'.$$

**Théorème (version $\mathcal{C}^1$).** Mêmes hypothèses avec des $f_n$ de [[Fonction de classe Ck|classe $\mathcal{C}^1$]] : $\sum f_n$ converge uniformément sur $I$ vers une fonction $S$ de classe $\mathcal{C}^1$, et $S' = \sum f_n'$.

**Exemple.** $\sum_{n\ge1} \frac{\sin(nx)}{n^3}$ : sa série dérivée $\sum \frac{\cos(nx)}{n^2}$ converge normalement sur $\mathbb{R}$, et la série converge en $x_0 = 0$. Sur tout intervalle borné, la somme $S$ est donc de classe $\mathcal{C}^1$, avec $S'(x) = \sum_{n\ge1} \frac{\cos(nx)}{n^2}$ ; la dérivabilité étant locale, cela vaut sur $\mathbb{R}$. [[Complément hors du cours|ⓘ]]

## Méthode : étudier une série de fonctions

Ordre habituel des vérifications, du plus simple au plus fin. [[Complément hors du cours|ⓘ]]
1. **Convergence simple** : fixer $x$ et utiliser les critères des séries numériques. [[Complément hors du cours|ⓘ]]
2. **Convergence normale** : calculer ou majorer $\|f_n\|_\infty$ (souvent par une étude de fonction), puis étudier $\sum \|f_n\|_\infty$. Si elle échoue sur $X$ entier, la chercher sur des parties plus petites (segments, $[a, +\infty[$). [[Complément hors du cours|ⓘ]]
3. **Convergence uniforme sans convergence normale** : majorer le reste $\|R_n\|_\infty$, en général grâce au critère des séries alternées. [[Complément hors du cours|ⓘ]]
4. **Non-convergence uniforme** : montrer que $\|f_n\|_\infty \not\to 0$, ou utiliser la contraposée d'un théorème (somme discontinue alors que les $f_n$ sont continues). [[Complément hors du cours|ⓘ]]
