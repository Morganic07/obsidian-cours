---
type: concept
tags: [year4]
aliases: [GainRatio, gain ratio, SplitInfo]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Normalisation du [[Gain d'information]] dans l'algorithme C4.5. Pour un test $T$ qui partage les exemples en $k$ sous-ensembles $T_1, \dots, T_k$ :

$$SplitInfo(T) = -\sum_{i=1}^{k} \frac{|T_i|}{|T|}\log_2\frac{|T_i|}{|T|}, \qquad GainRatio(T) = \frac{gain(T)}{SplitInfo(T)}.$$

**Pourquoi normaliser (complément, hors du cours)** : le [[Gain d'information]] favorise les attributs à nombreuses valeurs. Sur le jeu météo du cours, un identifiant comme NUM (14 valeurs) découpe les 14 exemples en 14 sous-ensembles d'un seul exemple, tous purs : son gain atteint le maximum $I(E) = I(9,5) \approx 0{,}940$ bit, sans aucun pouvoir de prédiction sur un nouvel exemple. SplitInfo, entropie de la partition elle-même, croît avec le nombre de branches : pour NUM, $SplitInfo = \log_2 14 \approx 3{,}81$, d'où $GainRatio \approx 0{,}940 / 3{,}81 \approx 0{,}25$, ce qui pénalise ce découpage.

Notion parente : [[Algorithme C4.5]]. Voir aussi : [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
