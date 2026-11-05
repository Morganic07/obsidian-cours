---
type: source
sources: ["[[Chp 3 - Important discrete distributions]]"]
maj: 2026-11-05
---

Résumé de [[Chp 3 - Important discrete distributions]], dans [[Year 2 - Probability]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Catalogue des lois discrètes usuelles, avec leur fonction de masse, leur espérance et leur variance.

## Contenu, dans l'ordre du cours

- **Bernoulli** : $X = 1$ (succès) avec probabilité $p$, $X = 0$ avec probabilité $1-p$. $E(X) = p$, $E(X^n) = p$, $V(X) = p(1-p)$.
- **Expérience binomiale** : $n$ essais fixés à l'avance, deux issues (succès/échec), $P(S) = p$, essais indépendants.
- **[[Loi binomiale]]** : si $X$ compte les succès, $P(X = i) = \binom{n}{i}p^i(1-p)^{n-i}$ pour $i = 0, \dots, n$. $E(X) = np$ et $V(X) = np(1-p)$.
- **[[Loi de Poisson]]** : elle approche la binomiale $(n, p)$ quand $n$ est grand et $p$ petit. Si $n \to \infty$, $p \to 0$ et $np \to \mu > 0$, $b(x; n, p) \to e^{-\mu}\mu^x/x!$. Pour une variable de paramètre $\lambda > 0$, $P(X = i) = e^{-\lambda}\lambda^i/i!$, $E(X) = \mathrm{Var}(X) = \lambda$.
- **Hypergéométrique** : tirage sans remise de $n$ éléments dans une population de $N$ comportant $M$ succès, avec dépendance entre les tirages. $P(X = x) = \binom{M}{x}\binom{N-M}{n-x}/\binom{N}{n}$. $E(X) = nM/N$ et $\mathrm{Var}(X) = \frac{N-n}{N-1}\, n\frac{M}{N}\left(1 - \frac{M}{N}\right)$.
- **Binomiale négative** : paramètres $r$ (nombre de succès voulus) et $p$. $nb(x; r, p) = \binom{x-1}{r-1}p^r(1-p)^{x-r}$ pour $x = r, r+1, \dots$. $E(X) = r/p$ et $\mathrm{Var}(X) = r(1-p)/p^2$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Poisson, deux notations** : le cours utilise $\mu$ (limite de la binomiale), puis $\lambda$ pour la définition. Le texte de présentation de $\lambda$ s'arrête après « if », et la formule vient dans l'image suivante : fausse alerte sur le fond, la formule est bien là.
2. **Binomiale négative** : la phrase d'introduction dit « nombre d'essais avant d'obtenir $r$ succès ». La formule, avec $x \ge r$, compte les essais jusqu'au $r$-ième succès inclus : $x$ est le nombre total d'essais, pas le nombre d'essais avant le succès (complément). La moyenne $r/p$ correspond bien à cette lecture.
3. **Bernoulli** : $E(X^n) = p$ est juste pour $n \ge 1$, puisque $X^n = X$ (complément).
