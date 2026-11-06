---
type: concept
aliases: [cumulative distribution function, cdf, fonction de répartition cumulée]
matieres: [Probability, Statistics]
sources: ["[[Chp 4 - Discrete random variables]]", "[[Chp 5 - Continuous random variable]]", "[[Chp3 - More on probability]]"]
maj: 2026-11-06
---

$F(x) = P(X \le x)$.

**Discret** : $F(x) = \sum_{y \le x} p(y)$, fonction en escalier. Pour $a \le b$, $P(a \le X \le b) = F(b) - F(a^-)$ où $a^-$ est la plus grande valeur possible strictement inférieure à $a$. On a donc $P(2 \le X \le 4) = F(4) - F(1)$ dans l'exemple du cours, et $P(2 < X \le 4) = F(4) - F(2)$. Entre deux valeurs possibles, $F$ est constante : dans l'exemple des clés USB, $F(2{,}7) = F(2) = 0{,}15$.

**Continu** : $F(x) = \int_{-\infty}^x f$, donc $F$ est une [[Primitive]] de la densité et $F'(x) = f(x)$ là où elle existe. $P(X > a) = 1 - F(a)$ et $P(a \le X \le b) = F(b) - F(a)$.

**Percentile** : $\eta_p$ vérifie $F(\eta_p) = p$, soit $\eta_p = F^{-1}(p)$ si l'inverse existe. La médiane est $\eta_{0{,}5}$. Voir aussi [[Méthode de la fonction de répartition inverse]].

**En Statistics** ([[Chp3 - More on probability]]) : la fonction de répartition sert à la simulation par inversion, $X = F^{-1}(U)$, et à définir la loi de Weibull, $F(x) = 1 - e^{-(x/\beta)^\alpha}$, et la loi log-normale, $F(x) = \Phi\left(\frac{\ln x - \mu}{\sigma}\right)$. Voir [[Loi exponentielle]], [[Loi normale]].

Notion parente : [[Variable aléatoire]].

## À vérifier

- [[Chp 4 - Discrete random variables]] : la formule apparaît sous la forme « F(b) _ F(a_) », le signe moins ayant été perdu à la conversion ; il faut lire $F(b) - F(a^-)$.

Résumés : [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]], [[Chp3 - More on probability (résumé)]]
