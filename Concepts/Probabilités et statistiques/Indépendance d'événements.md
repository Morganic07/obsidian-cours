---
type: concept
tags: [year2]
aliases: [independent events, événements indépendants, indépendance mutuelle, indépendance deux à deux, mutual independence, pairwise independence]
matieres: [Probability]
sources: ["[[2 - Conditional proba and independence|Chp 2 - Conditional proba and independence]]", "[[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]]"]
maj: 2026-11-08
---

Deux événements $A$ et $B$ sont indépendants si $P(A|B)=P(A)$. Cela équivaut à $P(A\cap B)=P(A)P(B)$ et entraîne $P(B|A)=P(B)$.

Dans ce cas, $(A^c,B)$, $(A,B^c)$ et $(A^c,B^c)$ sont aussi indépendants ; le cours le démontre à la main avec $P(A^c\cap B)=P(B)-P(A\cap B)$.

## Compléments (hors du cours)

- **Forme produit** : la définition usuelle des manuels est $P(A \cap B) = P(A)P(B)$, qui n'exige pas $P(B) > 0$ (contrairement à $P(A|B) = P(A)$). Conséquence : un événement de probabilité 0 ou 1 est indépendant de tout événement.
- **Indépendant n'est pas incompatible** : si $A$ et $B$ sont [[Événements incompatibles|incompatibles]] avec $P(A) > 0$ et $P(B) > 0$, alors $P(A \cap B) = 0 \ne P(A)P(B)$ : ils sont dépendants (savoir que $A$ s'est produit dit que $B$ ne s'est pas produit).
- **Exemple** : on tire une carte d'un jeu de 52. « As » et « cœur » sont indépendants : $P(\text{as de cœur}) = \frac{1}{52} = \frac{4}{52} \times \frac{13}{52}$.
- **Indépendance mutuelle** de $A_1, \dots, A_n$ : pour toute sous-famille $A_{i_1}, \dots, A_{i_k}$ ($2 \le k \le n$, indices distincts),
  $$P(A_{i_1} \cap \dots \cap A_{i_k}) = P(A_{i_1}) \cdots P(A_{i_k}).$$
- **L'indépendance deux à deux ne suffit pas**. Contre-exemple : deux lancers d'une pièce équilibrée, $A$ = pile au 1er, $B$ = pile au 2e, $C$ = les deux résultats sont égaux. Chacun a probabilité $1/2$, et chaque intersection de deux d'entre eux vaut $P(\text{pile, pile}) = 1/4$ : ils sont indépendants deux à deux. Mais $P(A \cap B \cap C) = 1/4 \ne 1/8 = P(A)P(B)P(C)$ : ils ne sont pas mutuellement indépendants.

Notion parente : [[Probabilité conditionnelle]]. Voir aussi : [[Loi conjointe]], [[Indépendance de variables aléatoires]], [[Événements incompatibles]].

Résumés : [[2 - Conditional proba and independence]]
