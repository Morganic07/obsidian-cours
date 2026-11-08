---
type: concept
tags: [year4]
aliases: [ID3, Iterative Dichotomiser 3]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Algorithme de construction d'[[Arbre de décision]] : une fonction récursive `construct-tree` choisit à chaque nœud le test de plus grand [[Gain d'information]], calculé à partir de l'[[Entropie (théorie de l'information)|entropie]].

Sur l'exemple PlayTennis : gain(OUTLOOK) $= 0{,}246$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$, gain(TEMP.) $= 0{,}029$ bits, donc Outlook est placé à la racine.

## Compléments (complément, hors du cours)

- ID3 (*Iterative Dichotomiser 3*) est dû à J. R. Quinlan (1986). C'est un [[Algorithme glouton]] sans retour arrière : il ne garantit pas l'arbre le plus petit (trouver celui-ci est NP-complet).
- Si les tests sont épuisés et que le nœud n'est pas pur, la feuille reçoit la classe majoritaire.
- **Détail du calcul PlayTennis** (9 oui, 5 non) : $I(9,5) \approx 0{,}940$. Outlook sépare en *sunny* (2 oui, 3 non), *overcast* (4, 0) et *rain* (3, 2) : $I(2,3) = I(3,2) \approx 0{,}971$ et $I(4,0) = 0$, d'où $\text{gain(OUTLOOK)} \approx 0{,}940 - \frac{10}{14}\cdot 0{,}971 \approx 0{,}246$.
- **Limite** : un critère évalué attribut par attribut ne voit pas les interactions. Sur un XOR ($y = x_1 \oplus x_2$, données équilibrées), le gain de chaque attribut à la racine est nul.

Notion parente : [[Arbre de décision]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Gain d'information]], [[Algorithme C4.5]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
