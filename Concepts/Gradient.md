---
type: concept
aliases: [gradients, nabla, vecteur gradient]
matieres: [Analyse dans Rn]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-06
---

Pour $f : U \subset \mathbb{R}^p \to \mathbb{R}$ différentiable en $a$, $\vec{\nabla}_af$ est le vecteur de ses dérivées partielles, soit la transposée de sa [[Matrice jacobienne]]. La différentielle s'en déduit par un [[Produit scalaire]] : $D_af(h) = \vec{\nabla}_af \cdot h$.

**Interprétation** : le gradient est perpendiculaire aux directions où $f$ est constante, et pointe vers sa variation maximale (plus grande pente). Sa norme est d'autant plus grande que la variation est forte.

**Accroissements finis** : si $\|\vec{\nabla}_xf\|_1 \le M$ sur le segment $[a, b]$, alors $|f(b) - f(a)| \le M\|b - a\|_1$. Sur un ouvert convexe (qui contient chaque segment entre deux de ses points), $f$ est constante si et seulement si son gradient est nul.

C'est la version à plusieurs variables de l'inégalité des accroissements finis de [[Dérivabilité]].

Notion parente : [[Différentielle]]. Voir aussi : [[Dérivée partielle]], [[Matrice jacobienne]], [[Produit scalaire]], [[Application lipschitzienne]], [[Dérivabilité]], [[Inégalité des accroissements finis]].

Résumé : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]]
