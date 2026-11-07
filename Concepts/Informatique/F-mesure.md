---
type: concept
tags: [year4]
aliases: [F-score]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : la F-mesure (ou F-score, F1) est une mesure de performance d'un [[Classifieur|classifieur]] qui combine la précision $P$ (part des prédictions positives qui sont correctes) et le rappel $R$ (part des vrais positifs retrouvés) par leur moyenne harmonique : $F_1 = \dfrac{2PR}{P + R}$. Elle varie entre 0 et 1, et n'est élevée que si la précision et le rappel le sont tous les deux, ce qui la rend utile quand les classes sont déséquilibrées. La variante $F_\beta$ donne plus de poids au rappel quand $\beta > 1$.

## Dans le cours

Nommé dans le cours de data mining sans définition : le F-score est cité parmi les mesures des travaux pratiques (matrice de confusion, erreur, précision, rappel, F-score), sans formule.

Notion parente : [[Validation d'un classifieur]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
