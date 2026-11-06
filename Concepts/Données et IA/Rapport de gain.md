---
type: concept
tags: [year4]
aliases: [GainRatio, gain ratio, SplitInfo]
matieres: [data mining]
sources: [".raw/Year 4/data mining/cours data mining du prof.pdf"]
maj: 2026-11-06
---

Normalisation du [[Gain d'information]] dans l'algorithme C4.5. Pour un test $T$ qui partage les exemples en $k$ sous-ensembles $T_1, \dots, T_k$ :

$$SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2\frac{|T_i|}{|T|}, \qquad GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}.$$

Notion parente : [[Algorithme C4.5]]. Voir aussi : [[Arbre de décision]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
