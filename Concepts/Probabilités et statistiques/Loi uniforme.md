---
type: concept
tags: [year2, year3]
aliases: [uniform distribution, loi uniforme continue, distribution uniforme]
sources: ["[[5 - Continuous random variable|Chp 5 - Continuous random variable]]", "[[3 - More on probability|Chp3 - More on probability]]", "[[Raw/Year 2/Probability/Chp 5 : Continuous random variable.docx|Chp 5 - Continuous random variable]]"]
maj: 2026-11-08
---

**Probability** : $X$ suit une loi uniforme sur $[A,B]$ si sa densité vaut $\frac{1}{B-A}$ sur $[A,B]$ et 0 ailleurs ; on note $X\sim\text{Unif}[A,B]$.

**Statistics** : $U \sim \text{Unif}[0;1)$ sert de point de départ à la simulation par inversion ([[Méthode de la fonction de répartition inverse]]).

## Compléments (hors du cours)

- **Probabilité proportionnelle à la longueur** : pour $A \le c \le d \le B$, $P(c \le X \le d) = \dfrac{d - c}{B - A}$.
- **Fonction de répartition** ([[Fonction de répartition]]) :
  $$F(x) = \begin{cases} 0 & x < A \\ \dfrac{x - A}{B - A} & A \le x \le B \\ 1 & x > B \end{cases}$$
- **Moments** : $E(X) = \dfrac{A + B}{2}$ (le milieu de l'intervalle) et $\mathrm{Var}(X) = \dfrac{(B - A)^2}{12}$.
- **Exemple** : un bus passe toutes les 10 minutes et l'on arrive au hasard ; l'attente suit $\text{Unif}[0, 10]$, d'attente moyenne 5 minutes, et $P(\text{attente} > 7) = (10 - 7)/10 = 0{,}3$.

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Loi normale]], [[Espérance et variance]].

Résumés : [[5 - Continuous random variable]], [[3 - More on probability]]
