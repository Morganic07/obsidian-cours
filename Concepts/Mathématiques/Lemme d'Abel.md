---
type: concept
tags: [year3]
aliases: [Abel's lemma, lemme d'Abel pour les séries entières]
sources: ["[[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : soit $\sum a_n x^n$ une [[Série entière]]. S'il existe $r > 0$ tel que la suite $(a_n r^n)$ soit bornée, alors $\sum a_n x^n$ converge absolument pour tout $x$ tel que $|x| < r$.

**Preuve.** Si $|a_n r^n| \le M$ pour tout $n$, alors
$$|a_n x^n| = |a_n r^n| \left|\frac{x}{r}\right|^n \le M \left|\frac{x}{r}\right|^n,$$
terme d'une série géométrique convergente puisque $\left|\frac{x}{r}\right| < 1$ ([[Suite géométrique]]). On conclut par le [[Critère de comparaison]].

**Conséquence : le rayon de convergence.** Le nombre
$$R = \sup\{r \ge 0 : (a_n r^n) \text{ est bornée}\} \in [0, +\infty]$$
est bien défini, et le lemme donne : convergence absolue pour $|x| < R$, divergence grossière pour $|x| > R$ (le terme général n'est pas borné, donc ne tend pas vers 0). On retrouve les trois cas du théorème du cours : $R = 0$ (convergence en $0$ seulement), $R = +\infty$ (convergence partout), $0 < R < +\infty$. Le lemme ne dit rien du comportement en $|x| = R$, qui s'étudie au cas par cas.

**À ne pas confondre** avec le théorème d'Abel radial, qui porte sur la continuité de la somme au bord de l'intervalle de convergence : si $\sum a_n R^n$ converge, alors $\sum a_n x^n \to \sum a_n R^n$ quand $x \to R^-$.

## Dans le cours

Le cours ne le nomme pas : il énonce directement les trois cas du rayon de convergence. Le lemme apparaît dans les compléments de [[5 - power series]], comme origine de ce théorème.

Voir aussi : [[Série entière]], [[Série numérique]], [[Critère de comparaison]], [[Borne supérieure]].

Résumés : [[5 - power series]]
