---
type: source
tags: [year1]
sources: [".raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf"]
maj: 2026-11-06
---

Résumé de Chap1-reels (`.raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf`) (PDF de 6 pages), dans [[Analyse Maths (matière)]]. Scan sans texte, lu en image.

## Contenu, dans l'ordre du cours

1. **Ensembles de nombres** : $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, plus les décimaux $\mathbb{D} = \{m/10^p\}$. Un nombre est rationnel si et seulement si son écriture décimale est finie ou périodique. Méthode : multiplier par une puissance de 10 pour faire apparaître la période, puis par $10^{\text{période}}$ et soustraire (exemple $12{,}34\,2021\,2021\ldots = 12\,340\,787/999\,900$). $\mathbb{R}$ est un corps contenant $\mathbb{Q}$, totalement ordonné, et vérifie la propriété de la borne supérieure.
2. **Relation d'ordre** : majorant, minorant, partie bornée ($\exists K,\ \forall a \in A,\ |a| \le K$). Un majorant n'est jamais « le » majorant. Plus grand et plus petit élément : uniques s'ils existent, mais ils peuvent ne pas exister. Dans $\mathbb{N}$, toute partie non vide a un plus petit élément, et toute partie non vide majorée a un plus grand élément (preuves par récurrence). Voir [[Relation d'ordre]].
3. **Borne supérieure et inférieure** : plus petit majorant, plus grand minorant, s'ils existent. Exemple : $[0,1[$ a pour borne supérieure $1$ sans plus grand élément. Si $A$ a un maximum, $\sup A = \max A$. **Théorème** : toute partie non vide majorée de $\mathbb{R}$ a une borne supérieure (minorée : borne inférieure). Le cours le présente comme la base de toute l'analyse (limite monotone, suites adjacentes, Bolzano-Weierstrass, valeurs intermédiaires, Rolle, accroissements finis, construction de l'intégrale). Caractérisations : $\sup A$ est l'unique réel qui majore $A$ et tel que $\forall y < \sup A,\ \exists x \in A,\ y < x$ ; ou qui majore $A$ et est limite d'une suite d'éléments de $A$. Voir [[Borne supérieure]].
4. **Archimède, partie entière, approximation décimale** : $\forall x,\ \exists n \in \mathbb{N},\ n > x$. Partie entière $E(x)$ : unique entier avec $E(x) \le x < E(x)+1$ (par exemple $E(-3{,}5) = -4$). Approximations décimales à $10^{-p}$ par défaut $E(10^p x)/10^p$ et par excès.
5. **Intervalles** : partie $I$ telle que $x, y \in I,\ x \le t \le y \Rightarrow t \in I$. Une intersection d'intervalles est un intervalle. Ce sont les ensembles du type $[a,b]$, $[a,b[$, etc., avec bornes éventuellement infinies. L'ensemble vide est un intervalle ouvert.
6. **Densité de $\mathbb{Q}$** : entre deux réels distincts, il y a une infinité de rationnels et d'irrationnels. Preuve : choisir $n$ tel que $10^{-n} < y - x$, puis $r = d_n + 10^{-n}$ où $d_n$ est l'approximation décimale par défaut de $x$ ; alors $x < r < y$.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Récurrence]] (preuves sur $\mathbb{N}$). Les théorèmes cités comme conséquences servent dans [[Limite et continuité]], [[Dérivabilité]] et [[Intégrale]].
