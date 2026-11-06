---
type: concept
aliases: [distance associée à une norme, distance euclidienne, distance between vectors, distance de Manhattan, distance de Hamming, Euclidean distance, Manhattan distance, Hamming distance]
matieres: [Analyse dans Rn, Bilinear Algebra, data mining]
sources: ["[[Chp 2 - éléments de topologie dans Rn]]", "[[chp 1 - Orthogonality]]", "[[raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof]]"]
maj: 2026-11-06
---

**Analyse dans Rn** : une distance est une application $d:X\times X\to\mathbb{R}^+$, symétrique, nulle seulement si les deux points sont égaux, et vérifiant l'[[Inégalité triangulaire]] ; elle est positive. Toute [[Norme]] définit la distance associée $d(X,Y)=\|X-Y\|$.

**Bilinear Algebra** : $\text{dist}(\mathbf{u},\mathbf{v})=\|\mathbf{u}-\mathbf{v}\|$, longueur du vecteur $\mathbf{u}-\mathbf{v}$.

**data mining** : fonctions de distance proposées pour l'[[Inertie (clustering)|inertie]] :

- euclidienne : $\sqrt{\sum_{i=1}^n (x_i - y_i)^2}$ ;
- de Manhattan : $\sum_{i=1}^n |x_i - y_i|$ ;
- de Hamming (nommée sans formule).

Notion parente : [[Norme]]. Voir aussi : [[Boule et voisinage]], [[Inégalité triangulaire]], [[Inertie (clustering)]], [[K plus proches voisins]].

Résumés : [[Chp 2 - éléments de topologie dans Rn (résumé)]], [[chp 1 - Orthogonality (résumé)]], [[Chp1 - intro to data mining (résumé)]], [[cours data mining du prof (résumé)]]
