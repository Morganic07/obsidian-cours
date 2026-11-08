---
type: concept
tags: [year1]
aliases: [relation de Pascal, triangle de Pascal]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]", "[[5 - Complexes|Chapitre 5 - Complexes]]"]
maj: 2026-11-08
---

Relation entre [[Coefficient binomial|coefficients binomiaux]], d'où le triangle de Pascal : pour $1 \le p \le n-1$ (et plus généralement pour tout $p$ avec la convention $\binom{n}{p} = 0$ hors de $0 \le p \le n$),
$$\binom{n-1}{p-1} + \binom{n-1}{p} = \binom{n}{p}.$$
Dans le triangle, chaque coefficient est la somme des deux coefficients situés au-dessus de lui.

## Deux preuves (complément, hors du cours)

**Par le calcul** : on réduit au dénominateur commun $p!\,(n-p)!$, en multipliant le premier terme par $\frac{p}{p}$ et le second par $\frac{n-p}{n-p}$ :
$$\binom{n-1}{p-1}+\binom{n-1}{p} = \frac{(n-1)!}{(p-1)!\,(n-p)!} + \frac{(n-1)!}{p!\,(n-1-p)!} = \frac{(n-1)!\,\big(p+(n-p)\big)}{p!\,(n-p)!} = \frac{n!}{p!\,(n-p)!} = \binom np.$$

**Par le dénombrement** : on compte les parties à $p$ éléments de $\{1,\dots,n\}$ selon qu'elles contiennent $n$ ou non. Celles qui contiennent $n$ sont déterminées par leurs $p-1$ autres éléments, pris dans $\{1,\dots,n-1\}$ : il y en a $\binom{n-1}{p-1}$. Celles qui ne le contiennent pas sont des parties à $p$ éléments de $\{1,\dots,n-1\}$ : il y en a $\binom{n-1}{p}$.

**Usage** : c'est elle qui fait passer du rang $n$ au rang $n+1$ dans la preuve par [[Récurrence]] de la [[Formule du binôme de Newton]], après regroupement des deux sommes.

**Analyse Maths** : elle sert à prouver par récurrence que $\binom{n}{p}$ est entier. Appliquée en cascade avec un télescopage, elle donne $\binom{n}{p+1} = \sum_{k=p}^{n-1} \binom{k}{p}$ (TD0).

**Outil Maths** : le chapitre 5 conseille de « revoir votre triangle de Pascal » à propos de la formule de Moivre, et en donne les lignes 1 ; 1 1 ; 1 2 1 ; 1 3 3 1 ; … ; 1 6 15 20 15 6 1. [[Erreurs du cours#^e-formule-de-pascal|✎]]

Notion parente : [[Dénombrement]]. Voir aussi : [[Coefficient binomial]], [[Récurrence]], [[Formule du binôme de Newton]], [[Forme trigonométrique et exponentielle]].

Résumés : [[0 - Rappels-etc]], [[5 - Complexes]]
