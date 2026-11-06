---
type: source
tags: [year1]
sources: ["[[Cours/Year 1/Algèbre Linéaire/Cours/chp3|chp3 (Algèbre)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 1/Algèbre Linéaire/Cours/chp3|chp3 (Algèbre)]], dans [[Algèbre linéaire (matière)]]. En cas d'écart, le cours et ses images font foi.

## Contenu

- **[[Forme échelonnée|Pivot de Gauss]]** : on choisit une ligne pivot, on élimine les inconnues pour obtenir un système en cascade, puis on remonte.
- **Opérations autorisées** : échanger deux lignes, multiplier une ligne par un scalaire non nul, ajouter à une ligne une combinaison des autres.
- **[[Système linéaire]]** : il est compatible s'il a au moins une solution. Une équation $0 = \lambda$ avec $\lambda \neq 0$ le rend incompatible. Avec plus d'inconnues que d'équations, on exprime la solution en fonction d'une inconnue.
- **Systèmes homogènes** : toujours compatibles, avec un ensemble de solutions qui est un sev de $\mathbb{R}^n$. Avec plus d'inconnues que d'équations, ils ont des solutions non nulles. Si $s_1$ et $s_2$ résolvent $(S)$, alors $s_1 - s_2$ résout le système homogène associé.

La partie « Applications aux familles libres et/ou génératrices » s'arrête sur un « Exemple : » sans contenu.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Opération $L_i \leftarrow \alpha L_i + \beta L_j$** : il faut préciser $\alpha \neq 0$, sinon on perd une équation (complément).
2. **« 1 inconnue = dim 0, 2 inconnues = dim 1, 3 inconnues = dim 2 »** : valable pour une seule équation non triviale, pas en général (complément).
3. **« En fonction d'une inconnue »** : il peut y en avoir plusieurs, selon le nombre de variables libres (complément, l'exemple du cours n'en a qu'une).
