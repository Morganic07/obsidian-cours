---
type: concept
tags: [year2]
aliases: [dérivée selon un vecteur, dérivées directionnelles, directional derivative, directional derivatives]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : soit $f : U \subset \mathbb{R}^p \to F$, $U$ ouvert, $a \in U$ et $v \in \mathbb{R}^p$. La dérivée de $f$ en $a$ selon le vecteur $v$ est, si elle existe,
$$D_v f(a) = \lim_{t \to 0} \frac{f(a + tv) - f(a)}{t}.$$
C'est la dérivée en $0$ de la fonction d'une variable $t \mapsto f(a + tv)$ : on regarde $f$ le long de la droite passant par $a$ et dirigée par $v$.

- Les [[Dérivée partielle|dérivées partielles]] en sont le cas $v = e_j$ (vecteurs de la base canonique) : $D_{e_j} f(a) = \dfrac{\partial f}{\partial x_j}(a)$.
- **Lien avec la différentielle** : si $f$ est [[Différentielle|différentiable]] en $a$, toutes les dérivées directionnelles existent et $D_v f(a) = D_a f(v)$. Pour $f$ à valeurs réelles, $D_v f(a) = \vec\nabla_a f \cdot v = \sum_j v_j \dfrac{\partial f}{\partial x_j}(a)$ ; elle dépend alors linéairement de $v$.
- **Direction de plus grande pente** : pour $v$ unitaire, l'[[Inégalité de Cauchy-Schwarz]] donne $|D_v f(a)| \le \|\vec\nabla_a f\|_2$, avec égalité si et seulement si $v$ est colinéaire au gradient. La pente est maximale dans la direction $v = \vec\nabla_a f / \|\vec\nabla_a f\|_2$, et nulle pour $v \perp \vec\nabla_a f$, le long de la ligne de niveau.
- **Existence ne veut pas dire continuité** : $f(x, y) = \dfrac{x^2 y}{x^4 + y^2}$, prolongée par $f(0, 0) = 0$, admet en $(0, 0)$ une dérivée selon tout vecteur $v = (a, b)$ ($D_v f(0, 0) = a^2/b$ si $b \ne 0$, $0$ si $b = 0$), mais vaut $1/2$ sur la parabole $y = x^2$ : elle n'est pas continue en $(0, 0)$, donc pas différentiable. On note aussi que $v \mapsto D_v f(0, 0)$ n'y est pas linéaire.

## Dans le cours

Le cours ne la nomme pas : il ne définit que les dérivées partielles, et énonce sans démonstration que le gradient pointe dans la direction de plus grande variation (propriété 9). Elle apparaît dans les compléments de [[4 - Calcul différentiel du premier ordre]], où elle sert de justification à la propriété 9.

Notion parente : [[Dérivée partielle]]. Voir aussi : [[Gradient]], [[Différentielle]], [[Vecteur unitaire]], [[Limite et continuité]].

Résumés : [[4 - Calcul différentiel du premier ordre]]
