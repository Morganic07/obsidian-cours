---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Important discrete distributions.docx|Chp 3 - Important discrete distributions]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Probability/Chp 3 : Important discrete distributions.docx|Chp 3 - Important discrete distributions]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Toutes les images du chapitre sont des énoncés ou des formules : elles sont recopiées ci-dessous, aucune n'est intégrée.

## Idée générale

Catalogue des lois discrètes usuelles, avec leur fonction de masse (*pmf*), leur espérance et leur variance ([[Espérance et variance]]).

## Récapitulatif

| Loi | Paramètres | $P(X = x)$ | Valeurs | $E(X)$ | $V(X)$ |
|---|---|---|---|---|---|
| Bernoulli | $p$ | $p$ si $x=1$, $1-p$ si $x=0$ | $\{0,1\}$ | $p$ | $p(1-p)$ |
| [[Loi binomiale\|Binomiale]] | $n, p$ | $\binom{n}{x}p^x(1-p)^{n-x}$ | $0,\dots,n$ | $np$ | $np(1-p)$ |
| [[Loi de Poisson\|Poisson]] | $\lambda > 0$ | $e^{-\lambda}\lambda^x/x!$ | $0,1,2,\dots$ | $\lambda$ | $\lambda$ |
| [[Loi hypergéométrique\|Hypergéométrique]] | $n, M, N$ | $\binom{M}{x}\binom{N-M}{n-x}/\binom{N}{n}$ | — | $n\frac{M}{N}$ | $\frac{N-n}{N-1}\,n\frac{M}{N}\left(1-\frac{M}{N}\right)$ |
| [[Loi binomiale négative\|Binomiale négative]] | $r, p$ | $\binom{x-1}{r-1}p^r(1-p)^{x-r}$ | $r, r+1,\dots$ | $r/p$ | $r(1-p)/p^2$ |

## Variable de Bernoulli et loi binomiale

### Variable de Bernoulli (*Bernoulli RV*)

Si $X$ est la [[Variable aléatoire|variable aléatoire]] qui représente le résultat d'un essai, on écrit $X = 1$ pour un succès et $X = 0$ pour un échec. Alors :
$$P\{X = 0\} = 1 - p, \qquad P\{X = 1\} = p$$
$$E(X) = p, \qquad E(X^n) = p, \qquad V(X) = p(1-p)$$

### Expérience binomiale (*binomial experiment*)

Une expérience est binomiale si et seulement si :
1. elle consiste en une suite de $n$ petites expériences appelées **essais** (*trials*), $n$ étant fixé avant l'expérience ;
2. chaque essai a deux issues possibles : succès (S) ou échec (F) ;
3. $p(S) = p$, $p(F) = 1 - p$ ;
4. les essais sont indépendants.

### Loi binomiale (*binomial distribution*)

Si $X$ représente le nombre de succès en $n$ essais, avec probabilité de succès $p$, $X$ est une **variable binomiale de paramètres** $(n, p)$, et :
$$P\{X = i\} = \binom{n}{i} p^i (1-p)^{n-i}, \quad i = 0, 1, \dots, n$$

**Théorème.** La *pmf* de la variable binomiale associée à une expérience binomiale s'appelle loi binomiale :
$$b(x; n, p) = \begin{cases} \dbinom{n}{x} p^x (1-p)^{n-x} & x = 0, 1, 2, \dots, n \\ 0 & \text{sinon} \end{cases}$$
$$E(X) = np, \qquad V(X) = np(1-p)$$

## Loi de Poisson (*Poisson distribution*)

Une variable de Poisson approche une variable binomiale de paramètres $(n, p)$ quand $n$ est grand et $p$ petit.

**Théorème (limite).** Si, dans la *pmf* binomiale $b(x; n, p)$, on fait $n \to \infty$ et $p \to 0$ de sorte que $np \to \mu > 0$, alors $b(x; n, p) \to p(x; \mu)$, la loi de Poisson :
$$p(x; \mu) = \frac{e^{-\mu}\mu^x}{x!}, \qquad x = 0, 1, 2, \dots$$

**Définition.** Une variable aléatoire à valeurs dans $\{0, 1, 2, 3, \dots\}$ est une **variable de Poisson de paramètre $\lambda > 0$** si
$$P\{X = i\} = e^{-\lambda}\frac{\lambda^i}{i!}, \qquad i = 0, 1, \dots$$
$$E[X] = \lambda, \qquad \mathrm{Var}(X) = \lambda$$

## Loi hypergéométrique (*hypergeometric distribution*)

Contexte : [[Tirage avec et sans remise|tirage sans remise]] dans une population finie, avec succès/échec, et dépendance entre les tirages.

**Théorème.** Si $X$ est le nombre de succès dans un échantillon aléatoire de taille $n$ tiré d'une population de $M$ succès et $(N - M)$ échecs, la loi de $X$, dite hypergéométrique, est :
$$P(X = x) = h(x; n, M, N) = \frac{\dbinom{M}{x}\dbinom{N-M}{n-x}}{\dbinom{N}{n}}$$

**Proposition.** L'espérance et la variance de $X$, de *pmf* $h(x; n, M, N)$, sont :
$$E(X) = n \cdot \frac{M}{N}, \qquad \mathrm{Var}(X) = \left(\frac{N-n}{N-1}\right) \cdot n \cdot \frac{M}{N}\left(1 - \frac{M}{N}\right)$$

## Loi binomiale négative (*negative binomial distribution*)

Contexte (note) : nombre d'essais pour obtenir $r$ succès, essais indépendants, probabilité de succès $p$.

**Proposition.** La *pmf* de la variable binomiale négative $X$, de paramètres $r$ = nombre de succès voulus et $p = P(S)$, est :
$$nb(x; r, p) = \binom{x-1}{r-1} p^r (1-p)^{x-r}, \qquad x = r, r+1, r+2, \dots$$

**Proposition.** Si $X$ suit une binomiale négative de paramètres $r$ et $p$ :
$$E(X) = \frac{r}{p}, \qquad \mathrm{Var}(X) = \frac{r(1-p)}{p^2}$$

Le chapitre ne contient ni exemple ni exercice.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Poisson, deux notations** : le cours utilise $\mu$ (limite de la binomiale), puis $\lambda$ pour la définition. Le texte de présentation de $\lambda$ s'arrête après « if », et la formule vient dans l'image suivante : fausse alerte sur le fond, la formule est bien là.
2. **Binomiale négative** : la phrase d'introduction dit « nombre d'essais avant d'obtenir $r$ succès ». La formule, avec $x \ge r$, compte les essais jusqu'au $r$-ième succès inclus : $x$ est le nombre total d'essais, pas le nombre d'essais avant le succès (complément). La moyenne $r/p$ correspond bien à cette lecture.
3. **Bernoulli** : $E(X^n) = p$ est juste pour $n \ge 1$, puisque $X^n = X$ (complément).
4. **Lien Bernoulli** : dans la note, le mot « Bernoulli RV » est relié à [[Loi binomiale]] (le wiki n'a pas de page Bernoulli à part) ; une variable de Bernoulli est une binomiale de paramètres $(1, p)$ (complément).
5. **Valeurs de l'hypergéométrique** : le cours ne donne pas l'ensemble des valeurs de $x$ (complément : $\max(0, n - N + M) \le x \le \min(n, M)$).
