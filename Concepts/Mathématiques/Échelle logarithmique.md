---
type: concept
tags: [year4]
aliases: [logarithmic scale, échelle log, graduation logarithmique]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.11.c|3.11.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : sur une échelle logarithmique, des écarts égaux correspondent à des **rapports** égaux, et non à des différences égales : passer d'une graduation à la suivante multiplie la grandeur par une constante, le plus souvent 10. On place une grandeur $x > 0$ à la position $\log_{10} x$ (ou $\ln x$) : 1, 10, 100 et 1 000 sont alors régulièrement espacés.

Cela vient de la propriété fondamentale du logarithme, qui transforme les produits en sommes : $\log(ab) = \log a + \log b$. Multiplier $x$ par 10 revient donc à ajouter 1 à $\log_{10} x$.

Usages :

- grandeurs qui couvrent plusieurs **ordres de grandeur** : magnitude des [[Séisme|séismes]] ([[Échelle de Richter]], [[Magnitude de moment]]), niveau sonore en décibels ($10 \log_{10}(I/I_0)$, +10 dB pour une intensité 10 fois plus grande), pH ($-\log_{10}[\mathrm{H_3O^+}]$), magnitude des étoiles ;
- graphiques : un axe logarithmique rend lisibles des données très étalées, et une croissance exponentielle $y = a\,b^x$ y devient une droite (axe des ordonnées seul logarithmique) ; une loi de puissance $y = a\,x^k$ devient une droite sur deux axes logarithmiques, de pente $k$ ;
- en informatique, les [[Complexité algorithmique|complexités]] $O(1)$, $O(\log n)$, $O(n)$, $O(n^2)$ se comparent sur un axe logarithmique, et la [[Loi de Moore|loi de Moore]] se lit comme une droite.

Piège : sur une telle échelle, une petite différence de position cache une grande différence de valeur. Un séisme de magnitude 7 n'est pas « un peu plus fort » qu'un séisme de magnitude 6 : ses ondes ont une amplitude 10 fois plus grande.

## Dans le cours

- [[tp3]] : complément au programme 3.11 ; l'échelle de Richter est logarithmique, un degré de plus multipliant par 10 l'amplitude des ondes.

Voir aussi : [[Exponentiation]], [[Puissance (mathématiques)]], [[Suite géométrique]].
