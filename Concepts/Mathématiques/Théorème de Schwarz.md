---
type: concept
tags: [year2]
aliases: [Schwarz theorem, théorème de Clairaut, Clairaut's theorem, symétrie des dérivées secondes]
sources: ["[[5 - Calcul différentiel d'ordre supérieur|Chp 5 - Calcul différentiel d'ordre supérieur]]", "[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
---

**Théorème 3** du chapitre 5 : soit $f$ de classe $\mathcal{C}^1$ sur un ouvert $U$ de $\mathbb{R}^p$ et $a \in U$ ; si les deux dérivées partielles croisées $\frac{\partial^2 f}{\partial x\partial y}$ et $\frac{\partial^2 f}{\partial y\partial x}$ sont définies et continues en $a$, elles y sont égales. Être de classe $\mathcal{C}^2$ suffit, mais n'est pas nécessaire. La dérivée croisée s'écrit comme limite : $\frac{\partial^2 f}{\partial y\partial x} = \lim_{t \to 0}\frac1t\left[\left.\frac{\partial f}{\partial x}\right|_{x,y+t} - \left.\frac{\partial f}{\partial x}\right|_{x,y}\right]$. [[Erreurs du cours#^e-theoreme-de-schwarz|✎]]

**Contre-exemple quand les dérivées croisées ne sont pas continues** (complément, hors du cours) : $f(x, y) = \dfrac{xy(x^2 - y^2)}{x^2 + y^2}$ pour $(x, y) \neq (0, 0)$, $f(0, 0) = 0$. Cette fonction est de classe $\mathcal{C}^1$ sur $\mathbb{R}^2$. On calcule $\frac{\partial f}{\partial x}(0, y) = -y$ et $\frac{\partial f}{\partial y}(x, 0) = x$, d'où
$$\frac{\partial^2 f}{\partial y \partial x}(0, 0) = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)(0,0) = -1 \neq \frac{\partial^2 f}{\partial x \partial y}(0, 0) = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)(0,0) = 1.$$
Les dérivées croisées existent en $(0, 0)$ mais n'y sont pas continues, et elles diffèrent.

**Conséquences** (complément, hors du cours) : pour $f$ de classe $\mathcal{C}^k$, l'ordre des dérivations n'importe pas jusqu'à l'ordre $k$. Une fonction $\mathcal{C}^2$ de deux variables n'a donc que trois dérivées secondes distinctes ($\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial x \partial y}$, $\frac{\partial^2 f}{\partial y^2}$), et sa [[Matrice hessienne]] est symétrique. C'est aussi ce qui rend nécessaire la condition de compatibilité $\frac{\partial g}{\partial y} = \frac{\partial h}{\partial x}$ du système $\frac{\partial f}{\partial x} = g$, $\frac{\partial f}{\partial y} = h$ ([[Équation aux dérivées partielles]]).

Notion parente : [[Dérivée partielle]]. Voir aussi : [[Fonction de classe Ck]], [[Matrice hessienne]], [[Équation aux dérivées partielles]], [[Extremum local d'une fonction de deux variables]].

Résumés : [[5 - Calcul différentiel d'ordre supérieur]]
