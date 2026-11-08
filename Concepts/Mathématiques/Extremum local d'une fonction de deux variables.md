---
type: concept
tags: [year2, year3]
aliases: [points critiques d'une fonction de deux variables, critère du discriminant, point col, point selle, saddle point, local extremum, notations de Monge]
sources: ["[[10 - linear regression|Cours 10 - linear regression]]", "[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]", "[[5 - Calcul différentiel d'ordre supérieur|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
---

Pour obtenir la droite des [[Moindres carrés]], [[10 - linear regression|Cours 10 - linear regression]] minimise $f(b, m)$ : il cherche les points critiques (dérivées partielles nulles), puis vérifie $f_{bb}f_{mm} - f_{bm}^2 > 0$ et $f_{bb} > 0$, ce qui donne un minimum local. Ici, il est global, car la surface est une « cuvette parabolique ».

Le cours s'en sert comme d'un outil, sans en donner d'énoncé général.

## Énoncé général (complément, hors du cours)

Ajouté dans la fiche [[5 - Calcul différentiel d'ordre supérieur]].

**Condition nécessaire (ordre 1).** Si $f : U \to \mathbb{R}$, différentiable sur un ouvert $U \subset \mathbb{R}^2$, admet un extremum local en $a$, alors $a$ est un **point critique** : $\vec\nabla_a f = 0$, soit $\frac{\partial f}{\partial x}(a) = \frac{\partial f}{\partial y}(a) = 0$.

La réciproque est fausse : $f(x, y) = x^2 - y^2$ a un point critique en $(0, 0)$, mais $f(x, 0) = x^2 > 0$ et $f(0, y) = -y^2 < 0$ près de l'origine. Ce n'est ni un minimum ni un maximum : c'est un **point col** (ou point selle).

**Condition suffisante (ordre 2).** Soit $f$ de classe $\mathcal{C}^2$ et $a$ un point critique. Avec les notations de Monge $r = \frac{\partial^2 f}{\partial x^2}(a)$, $s = \frac{\partial^2 f}{\partial x \partial y}(a)$, $t = \frac{\partial^2 f}{\partial y^2}(a)$ :

| Signe de $rt - s^2$ | Conclusion |
|---|---|
| $rt - s^2 > 0$ et $r > 0$ | minimum local strict |
| $rt - s^2 > 0$ et $r < 0$ | maximum local strict |
| $rt - s^2 < 0$ | point col (pas d'extremum) |
| $rt - s^2 = 0$ | on ne peut pas conclure à l'ordre 2 |

**Lien avec la [[Matrice hessienne]].** $rt - s^2$ est le déterminant de la hessienne $H = \begin{pmatrix} r & s \\ s & t \end{pmatrix}$ (symétrique par le [[Théorème de Schwarz]]). Le critère revient à dire : $H$ définie positive donne un minimum local strict, définie négative un maximum local strict, et des valeurs propres de signes opposés un point col. Il découle de la formule de Taylor à l'ordre 2, $f(a + h) = f(a) + \tfrac12\, h^T H h + o(\|h\|^2)$ en un point critique.

**Exemple.** $f(x, y) = x^2 + xy + y^2 - 3x$. Points critiques : $2x + y - 3 = 0$ et $x + 2y = 0$, d'où $(x, y) = (2, -1)$. On a $r = 2$, $s = 1$, $t = 2$, donc $rt - s^2 = 3 > 0$ et $r > 0$ : minimum local strict, de valeur $f(2, -1) = 4 - 2 + 1 - 6 = -3$.

Notion parente : [[Dérivée partielle]]. Voir aussi : [[Moindres carrés]], [[Gradient]], [[Matrice hessienne]], [[Théorème de Schwarz]], [[Forme quadratique définie positive]], [[Fonction de classe Ck]].

Résumés : [[10 - linear regression]], [[5 - Calcul différentiel d'ordre supérieur]]
