---
type: concept
tags: [year2]
aliases: [difféomorphismes, C1-difféomorphisme, changement de variables direct, changement de variables indirect]
matieres: [Analyse dans Rn]
sources: ["[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

Définition 7 : $\phi : U \to V$ est un $\mathcal{C}^1$-difféomorphisme si elle est $\mathcal{C}^1$, bijective, et si $\phi^{-1}$ est $\mathcal{C}^1$.

**Critère rapide** : si $\phi$ est $\mathcal{C}^1$, bijective, et si $D_a\phi$ est une application linéaire bijective en tout point $a$, alors $p = n$ et $\phi$ est un difféomorphisme. Un jacobien non nul rend $D_a\phi$ bijective. Une application linéaire bijective de $\mathbb{R}^p$ dans $\mathbb{R}^n$ impose $p = n$ et en est un.

**Changement de variables dans une EDP** :

- **Direct** : $(x, y) = \varphi(u, v)$, avec $\varphi : V \to U$ un $\mathcal{C}^1$-difféomorphisme de $V$ sur $U$, et $g = f \circ \varphi$. [[Erreurs du cours#^e-diffeomorphisme|✎]] On calcule $\frac{\partial g}{\partial u}$ et $\frac{\partial g}{\partial v}$, puis on en déduit $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$ à reporter.
- **Indirect** : $(u, v) = \varphi(x, y)$, avec $\varphi : U \to V$ un $\mathcal{C}^1$-difféomorphisme de $U$ sur $V$, et $f = g \circ \varphi$. On injecte directement $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$.

**[[Coordonnées polaires]]** : $(\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$, avec $\rho > 0$, est un difféomorphisme sur un demi-plan :

- $x > 0$ : $\theta \in \,]-\frac{\pi}{2}, \frac{\pi}{2}[$ et $\theta = \text{Arctan}(y/x)$ ;
- $x < 0$ : $\theta \in \,]\frac{\pi}{2}, \frac{3\pi}{2}[$ et $\theta = \pi + \text{Arctan}(y/x)$ ;
- $y > 0$ : $\theta \in \,]0, \pi[$ et $\theta = \text{Arccos}(x/\sqrt{x^2 + y^2})$.

Notion parente : [[Différentielle]]. Voir aussi : [[Matrice jacobienne]], [[Coordonnées polaires]], [[Équation aux dérivées partielles]], [[Fonction de classe Ck]], [[Changement de base]]

Résumés : [[4 - Calcul différentiel du premier ordre]], [[2 - intégrales multiples]]
