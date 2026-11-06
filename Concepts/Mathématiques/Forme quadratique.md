---
type: concept
tags: [year2]
aliases: [quadratic form, quadratic forms, formes quadratiques, change of variable in a quadratic form, Classifying quadratic forms]
sources: ["[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-06
---

Fonction $Q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$ avec $A$ symétrique, la matrice de la forme. Exemple le plus simple : $\mathbf{x}^TI\mathbf{x} = \|\mathbf{x}\|^2$. Dans le plan, $ax^2 + bxy + cy^2$ s'écrit avec la matrice symétrique associée.

- **Changement de variable** : avec $\mathbf{x} = P\mathbf{y}$, la matrice devient $P^TAP$. Si $P$ est orthogonale et diagonalise $A$, on obtient $\mathbf{y}^TD\mathbf{y}$, sans terme croisé.
- **Axes principaux** : les colonnes de $P$. Ils donnent un repère où la courbe $\mathbf{x}^TA\mathbf{x} = c$ (ellipse, hyperbole, etc.) est en position standard.
- **Classement selon les valeurs propres de $A$** : définie positive si toutes sont positives, définie négative si toutes sont négatives, indéfinie s'il y a les deux signes.
- **Optimisation sous $\|\mathbf{x}\| = 1$** : le maximum de $\mathbf{x}^TA\mathbf{x}$ est la plus grande valeur propre, atteinte en un vecteur propre unitaire $\mathbf{u}_1$, et le minimum la plus petite. Si l'on impose en plus $\mathbf{x}^T\mathbf{u}_1 = \dots = \mathbf{x}^T\mathbf{u}_{k-1} = 0$, le maximum est $\lambda_k$, atteint en $\mathbf{u}_k$.

> [!warning] Écart dans le cours
> [[Chp2 - Symmetric matrices and quadratic forms]] définit « negative definite » par $Q(\mathbf{x}) > 0$. La figure et le théorème sur les valeurs propres indiquent $Q(\mathbf{x}) < 0$ pour $\mathbf{x} \neq \mathbf{0}$. Cette page suit ces derniers.

Notion parente : [[Forme bilinéaire]]. Voir aussi : [[Matrice symétrique]], [[Valeur propre]], [[Diagonalisation]], [[Norme]], [[Théorème des axes principaux]], [[Forme quadratique définie positive]], [[Optimisation sous contrainte]].

## À vérifier

- Dans [[Chp2 - Symmetric matrices and quadratic forms]], les coupes horizontales de $z = 3x_1^2$ sont deux droites, pas une parabole.

Résumé : [[Chp2 - Symmetric matrices and quadratic forms (résumé)]]
