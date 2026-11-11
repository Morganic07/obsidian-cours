---
type: concept
tags:
  - year1
  - year4
aliases:
  - somme des n premiers entiers
  - nombre triangulaire
  - nombres triangulaires
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]"
maj: 2026-11-11
---

$S = 1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$.

**Cours 1** en donne une interprétation géométrique : deux copies de la somme forment un rectangle, $2S = n(n+1)$, donc $S = n(n+1)/2$. [[Erreurs du cours#^e-somme-des-premiers-entiers|✎]] **AlgoID1** l'écrit en pseudo-code avec une boucle. Le **TD0** la calcule ($\sum k$, et la somme des impairs $= n^2$). L'examen d'informatique de novembre 2022 (page 32 de [[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]) demande une fonction `triangulaire(n : entier) : booléen` : un nombre triangulaire est le nombre de pastilles d'un triangle (1, 3, 6, 10 sur la figure, avec des rangées de 1, 2, 3 puis 4 pastilles), et $n$ est triangulaire si $\sqrt{8n + 1}$ est entier (exemple : $3 \times 8 + 1 = 25$). L'examen ne relie pas lui-même ces nombres à la formule $\frac{n(n+1)}{2}$.

## Compléments (complément, hors du cours)

**Preuve par [[Changement d'indice]]** : avec $j = n - k$, quand $k$ va de $0$ à $n$, $j$ va de $n$ à $0$, donc
$$S_n = \sum_{k=0}^{n} k = \sum_{k=0}^{n} (n-k).$$
En additionnant les deux écritures, $2S_n = \sum_{k=0}^{n} n = (n+1)\,n$, d'où $S_n = \frac{n(n+1)}{2}$. C'est la version calculatoire de l'astuce de la somme écrite à l'endroit puis à l'envers ($1 + n$, $2 + (n-1)$, … : chaque paire vaut $n+1$), traditionnellement attribuée à Gauss enfant ; c'est aussi la lecture du rectangle du Cours 1.

**Sommes voisines**, démontrées par [[Récurrence]] :
$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}, \qquad \sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2.$$
La seconde dit que la somme des $n$ premiers cubes est le carré de la somme des $n$ premiers entiers. Exemple : $1 + 8 + 27 = 36 = 6^2$.

Notion parente : [[Symboles somme et produit]]. Voir aussi : [[Récurrence]], [[Carré magique]], [[Changement d'indice]], [[Suite arithmétique]].

## Dans le cours (C++)

[[4 - Cours complet]] calcule la somme des entiers de 1 à 100 (5050) par une boucle `while` et un accumulateur (`somme1-100.cpp`), puis la transforme en fonction `somme1aN(n)` placée dans un module séparé (exercice 4).

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[0 - diapo prof]], [[0 - Rappels-etc]], [[4 - Cours complet]]
