---
type: concept
tags: [year3]
aliases: [convergence dominée, théorème de Lebesgue, dominated convergence theorem]
sources: ["[[Raw/Year 3/Séries/Chp3 : Sequence of function.docx|Chp3 - Sequence of function]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)**, version pour les fonctions continues par morceaux : soit $I$ un intervalle quelconque de $\mathbb{R}$ et $(f_n)$ une suite de fonctions. Si
1. chaque $f_n$ est [[Fonction continue par morceaux|continue par morceaux]] sur $I$,
2. $(f_n)$ converge simplement sur $I$ vers une fonction $f$ continue par morceaux,
3. (**hypothèse de domination**) il existe $\varphi$ continue par morceaux, positive et intégrable sur $I$ telle que $|f_n(x)| \le \varphi(x)$ pour tout $n$ et tout $x \in I$,

alors les $f_n$ et $f$ sont intégrables sur $I$ et
$$\lim_{n \to +\infty} \int_I f_n(x)\,dx = \int_I f(x)\,dx.$$

**Ce qu'il apporte par rapport au cours.** Il ne demande pas la [[Convergence uniforme]], seulement la convergence simple, et il vaut sur un intervalle quelconque, borné ou non (intégrales généralisées comprises), alors que l'interversion par convergence uniforme se fait sur un segment. Point essentiel : $\varphi$ ne dépend pas de $n$.

**Exemple.** Sur $[0, +\infty[$, $f_n(x) = \left(1 - \frac{x}{n}\right)^n$ pour $x \le n$ et $0$ sinon converge simplement vers $e^{-x}$, et $0 \le f_n(x) \le e^{-x}$ (car $\ln(1-u) \le -u$). D'où $\int_0^n \left(1 - \frac{x}{n}\right)^n dx \to \int_0^{+\infty} e^{-x}\,dx = 1$.

**Contre-exemple quand la domination manque.** Les « triangles » de hauteur $n$ du chapitre 3 convergent simplement vers $0$ alors que leur intégrale vaut toujours $1$ : aucune fonction intégrable ne majore toutes les $f_n$ (leur borne supérieure se comporte comme $\frac{1}{x}$ près de $0$).

**Cadre général.** Le théorème est dû à Lebesgue et s'énonce dans la théorie de l'intégrale de Lebesgue, pour des fonctions mesurables ; la version ci-dessus en est le cas particulier utilisé en premier cycle.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[3 - Sequence of function]], après l'interversion limite-intégrale par convergence uniforme et son contre-exemple des « triangles ».

Voir aussi : [[Interversion de limites]], [[Intégrale]], [[Intégrale généralisée]], [[Convergence uniforme]], [[Théorème de Dini]].

Résumés : [[3 - Sequence of function]]
