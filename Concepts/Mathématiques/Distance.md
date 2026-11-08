---
type: concept
tags: [year2, year4]
aliases: [distance associée à une norme, distance euclidienne, distance between vectors, distance de Manhattan, distance de Hamming, Euclidean distance, Manhattan distance, Hamming distance]
matieres: [Analyse dans Rn, Bilinear Algebra, data mining, C++]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
---

**Analyse dans Rn** : une distance est une application $d:X\times X\to\mathbb{R}^+$, symétrique, nulle seulement si les deux points sont égaux, et vérifiant l'[[Inégalité triangulaire]] ; elle est positive. Toute [[Norme]] définit la distance associée $d(X,Y)=\|X-Y\|$.

**Bilinear Algebra** : $\text{dist}(\mathbf{u},\mathbf{v})=\|\mathbf{u}-\mathbf{v}\|$, longueur du vecteur $\mathbf{u}-\mathbf{v}$.

**data mining** : fonctions de distance proposées pour l'[[Inertie (clustering)|inertie]] :

- euclidienne : $\sqrt{\sum_{i=1}^n (x_i - y_i)^2}$ ;
- de Manhattan : $\sum_{i=1}^n |x_i - y_i|$ ;
- de Hamming (nommée sans formule dans le cours).

**Distance de Hamming (complément, hors du cours)** : pour deux vecteurs de même longueur, le nombre de positions où ils diffèrent,
$$d_H(x,y) = \operatorname{card}\{i : x_i \neq y_i\}.$$
Elle convient aux attributs qualitatifs ou binaires, où une différence de valeurs n'a pas de sens. Sur le jeu météo du cours (attributs Outlook, TEMP., HUMI., Wind), les exemples 1 (sunny, high, strong, no) et 2 (sunny, high, strong, yes) ne diffèrent que par Wind : $d_H = 1$ ; les exemples 2 et 8 (sunny, mild, strong, no) diffèrent par TEMP. et Wind : $d_H = 2$.

**C++** : l'exercice `Maze` de [[4 - C++]] demande de calculer la distance euclidienne et la distance de Manhattan entre un agent et la sortie d'un labyrinthe (sans formule ; ce sont les deux premières ci-dessus, en dimension 2).

Notion parente : [[Norme]]. Voir aussi : [[Boule et voisinage]], [[Inégalité triangulaire]], [[Inertie (clustering)]], [[K plus proches voisins]].

Résumés : [[2 - éléments de topologie dans Rn]], [[1 - Orthogonality]], [[1 - intro to data mining]], [[1 - pdf du prof]], [[4 - C++]]
