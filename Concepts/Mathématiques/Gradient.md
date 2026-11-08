---
type: concept
tags: [year2]
aliases: [gradients, nabla, vecteur gradient, descente de gradient, gradient descent]
matieres: [Analyse dans Rn]
sources: ["[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]", "[[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

Pour $f : U \subset \mathbb{R}^p \to \mathbb{R}$ différentiable en $a$, $\vec{\nabla}_af$ est le vecteur de ses dérivées partielles, soit la transposée de sa [[Matrice jacobienne]]. La différentielle s'en déduit par un [[Produit scalaire]] : $D_af(h) = \vec{\nabla}_af \cdot h$.

**Interprétation** : le gradient est perpendiculaire aux directions où $f$ est constante, et pointe vers sa variation maximale (plus grande pente). Sa norme est d'autant plus grande que la variation est forte.

**Justification** (complément, hors du cours) : pour un vecteur unitaire $v$, la [[Dérivée directionnelle]] de $f$ en $a$ selon $v$ vaut $D_v f(a) = \vec{\nabla}_af \cdot v$. Par l'[[Inégalité de Cauchy-Schwarz]], $|\vec{\nabla}_af \cdot v| \le \|\vec{\nabla}_af\|_2 \|v\|_2 = \|\vec{\nabla}_af\|_2$, avec égalité si et seulement si $v$ est colinéaire au gradient. La pente est donc maximale, égale à $\|\vec{\nabla}_af\|_2$, pour $v = \vec{\nabla}_af / \|\vec{\nabla}_af\|_2$, minimale (égale à $-\|\vec{\nabla}_af\|_2$) pour la direction opposée, et nulle pour $v \perp \vec{\nabla}_af$, c'est-à-dire le long de la ligne de niveau $f = f(a)$.

*Exemple* : $f(x, y) = x^2 + y^2$ a pour gradient $(2x, 2y)$, dirigé selon le rayon, donc perpendiculaire aux cercles de niveau $x^2 + y^2 = c$, et orienté vers l'extérieur, où $f$ croît.

**Application : la descente de gradient** (complément, hors du cours). Pour faire décroître $f$, on avance dans la direction $-\vec{\nabla}f$, celle de la plus forte pente descendante : $x_{k+1} = x_k - \eta\,\vec{\nabla}_{x_k}f$, avec un pas $\eta > 0$. Cette méthode itérative est au cœur de l'optimisation numérique et de l'apprentissage automatique, où elle minimise une fonction de coût.

**Accroissements finis** : si $\|\vec{\nabla}_xf\|_1 \le M$ sur le segment $[a, b]$, alors $|f(b) - f(a)| \le M\|b - a\|_1$. Sur un ouvert convexe (qui contient chaque segment entre deux de ses points), $f$ est constante si et seulement si son gradient est nul.

C'est la version à plusieurs variables de l'inégalité des accroissements finis de [[Dérivabilité]].

Notion parente : [[Différentielle]]. Voir aussi : [[Dérivée partielle]], [[Matrice jacobienne]], [[Produit scalaire]], [[Application lipschitzienne]], [[Dérivabilité]], [[Inégalité des accroissements finis]], [[Dérivée directionnelle]], [[Inégalité de Cauchy-Schwarz]], [[Extremum local d'une fonction de deux variables]].

Résumé : [[4 - Calcul différentiel du premier ordre]]
