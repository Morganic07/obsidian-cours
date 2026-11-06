---
type: concept
tags: [year4]
aliases: [information gain]
sources: [".raw/Year 4/data mining/cours data mining du prof.pdf"]
maj: 2026-11-06
---

Critère de choix du test dans ID3. Pour un test $T$ qui partage $E$ en $k$ sous-ensembles de proportions $W_l$ :

$$\text{gain}(T) = I(E) - \sum_{l=1}^k W_l\, I(E_l)$$

où $I$ est l'[[Entropie (théorie de l'information)|entropie]]. Exemple du cours :

$$\text{gain(OUTLOOK)} = I(9,5) - \left(\tfrac{5}{14}I(2,3) + \tfrac{4}{14}I(4,0) + \tfrac{5}{14}I(3,2)\right) = 0{,}246 \text{ bits}$$

Notion parente : [[Algorithme ID3]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Rapport de gain]], [[Arbre de décision]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
