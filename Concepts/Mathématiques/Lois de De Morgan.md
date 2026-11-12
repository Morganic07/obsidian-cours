---
type: concept
tags: [year1, year4]
aliases: [loi de De Morgan, règle de Morgan, De Morgan]
sources: ["[[1 - logique|Chapitre 1 logique]]", "[[2 - ensembles|Chapitre 2 ensembles]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre2-Ensemble (4).pdf]]"]
maj: 2026-11-12
---

**En logique** : $\neg(p \vee q) \equiv \neg p \wedge \neg q$ et $\neg(p \wedge q) \equiv \neg p \vee \neg q$. Le cours appelle aussi « règle de Morgan » la négation des [[Quantificateur|quantificateurs]].

**Pour les ensembles** : $\overline{A \cap B} = \overline{A} \cup \overline{B}$, $\overline{A \cup B} = \overline{A} \cap \overline{B}$ [[Erreurs du cours#^e-lois-de-de-morgan|✎]], et pour une famille $\overline{\bigcap A_i} = \bigcup \overline{A_i}$, $\overline{\bigcup A_i} = \bigcap \overline{A_i}$.

## Dans le cours

- [[tp3]] : en C, la condition `!(age>=18)` équivaut à `age<18` (programme 3.5), et les lois s'écrivent `!(A && B)` = `!A || !B`, `!(A || B)` = `!A && !B`.
- [[tp4]] : le dessin du contour d'un rectangle (4.9) passe de la condition « case intérieure » à sa négation « case du bord », `i==1 || i==longueur || j==1 || j==largeur`.

Notion parente : [[Opérations sur les ensembles]]. Voir aussi : [[Propriétés des connecteurs logiques]], [[Complémentaire d'un ensemble]].

Résumés : [[1 - logique]], [[2 - ensembles]], [[2 - pdf]]
