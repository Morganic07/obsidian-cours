---
type: concept
tags: [year2]
aliases: [difféomorphismes, C1-difféomorphisme, changement de variables direct, changement de variables indirect]
matieres: [Analyse dans Rn]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre (résumé)|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-06
---

Définition 7 : $\phi : U \to V$ est un $\mathcal{C}^1$-difféomorphisme si elle est $\mathcal{C}^1$, bijective, et si $\phi^{-1}$ est $\mathcal{C}^1$.

**Critère rapide** : si $\phi$ est $\mathcal{C}^1$, bijective, et si $D_a\phi$ est une application linéaire bijective en tout point $a$, alors $p = n$ et $\phi$ est un difféomorphisme. Un jacobien non nul rend $D_a\phi$ bijective. Une application linéaire bijective de $\mathbb{R}^p$ dans $\mathbb{R}^n$ impose $p = n$ et en est un.

**Changement de variables dans une EDP** :

- **Direct** : $(x, y) = \varphi(u, v)$ et $g = f \circ \varphi$. On calcule $\frac{\partial g}{\partial u}$ et $\frac{\partial g}{\partial v}$, puis on en déduit $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$ à reporter.
- **Indirect** : $(u, v) = \varphi(x, y)$ et $f = g \circ \varphi$. On injecte directement $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$.

**[[Coordonnées polaires]]** : $(\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$, avec $\rho > 0$, est un difféomorphisme sur un demi-plan :

- $x > 0$ : $\theta \in \,]-\frac{\pi}{2}, \frac{\pi}{2}[$ et $\theta = \text{Arctan}(y/x)$ ;
- $x < 0$ : $\theta \in \,]\frac{\pi}{2}, \frac{3\pi}{2}[$ et $\theta = \pi + \text{Arctan}(y/x)$ ;
- $y > 0$ : $\theta \in \,]0, \pi[$ et $\theta = \text{Arccos}(x/\sqrt{x^2 + y^2})$.

Notion parente : [[Différentielle]]. Voir aussi : [[Matrice jacobienne]], [[Coordonnées polaires]], [[Équation aux dérivées partielles]], [[Fonction de classe Ck]], [[Changement de base]]

## À vérifier

- Tableau du changement de variables : $\varphi : V \to U$ contre « de $U$ sur $V$ » (résumé Chp 4, point 6).

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]], [[Chp9-intégrales multiples (résumé)]]
