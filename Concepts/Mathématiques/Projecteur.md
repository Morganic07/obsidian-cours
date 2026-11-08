---
type: concept
tags: [year1]
aliases: [projecteurs, projection vectorielle, projection parallèlement, projector, symétrie vectorielle, symétries vectorielles]
sources: ["[[Raw/Year 1/Algèbre Linéaire/Cours /chp2 .docx|chp2 (Algèbre)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un **projecteur** est un endomorphisme $p$ d'un espace vectoriel $E$ (application linéaire de $E$ dans $E$) tel que
$$p \circ p = p.$$
Appliquer deux fois la projection ne change rien de plus qu'une fois.

**Projection sur $F$ parallèlement à $G$.** Si $E = F \oplus G$ (voir [[Somme directe]]), tout $x \in E$ s'écrit de façon unique $x = x_F + x_G$ avec $x_F \in F$ et $x_G \in G$. L'application $p : x \mapsto x_F$ est linéaire et vérifie $p \circ p = p$ : c'est la projection sur $F$ parallèlement à $G$. Son image est $F$, son noyau est $G$.

**Réciproque.** Tout projecteur $p$ est la projection sur $\operatorname{Im} p$ parallèlement à $\operatorname{Ker} p$, et
$$E = \operatorname{Im} p \oplus \operatorname{Ker} p.$$
En effet, $x = p(x) + (x - p(x))$, avec $p(x) \in \operatorname{Im} p$ et $x - p(x) \in \operatorname{Ker} p$ puisque $p(x - p(x)) = p(x) - p(p(x)) = 0$. Sur $\operatorname{Im} p$, $p$ agit comme l'identité.

**Symétrie associée.** La symétrie par rapport à $F$ parallèlement à $G$ est $s(x) = x_F - x_G$. Elle vérifie $s \circ s = \mathrm{Id}_E$ et
$$s = 2p - \mathrm{Id}_E.$$

**Exemple** dans $\mathbb{R}^2$ : $p(x, y) = (x, 0)$ est la projection sur l'axe des abscisses parallèlement à l'axe des ordonnées ; $s(x, y) = (x, -y)$ est la symétrie correspondante. On vérifie $2p(x,y) - (x,y) = (2x - x, 0 - y) = (x, -y)$.

**Cas particulier** : quand $G$ est le supplémentaire orthogonal de $F$, on obtient la [[Projection orthogonale]].

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - Algèbre linéaire]], à propos des applications linéaires, de leur noyau et de leur image.

Voir aussi : [[Somme directe]], [[Transformation linéaire]], [[Espace nul]], [[Image d'une application linéaire]], [[Projection orthogonale]], [[Transformations géométriques du plan]]

Résumés : [[2 - Algèbre linéaire]]
