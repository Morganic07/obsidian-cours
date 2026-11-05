---
type: concept
aliases: [least-squares, least squares, least square, moindre carré]
sources: ["[[chp 1 - Orthogonality]]"]
maj: 2026-11-05
---

Quand $A\mathbf{x} = \mathbf{b}$ n'a pas de solution, on cherche un $\hat{\mathbf{x}}$ qui minimise $\|\mathbf{b} - A\mathbf{x}\|$. Ce minimum $\|\mathbf{b} - A\hat{\mathbf{x}}\|$ est la least-square error. Comme $A\mathbf{x}$ est toujours dans Col $A$, le meilleur choix est le [[Projection orthogonale|projeté orthogonal]] de $\mathbf{b}$ sur Col $A$, c'est-à-dire $A\hat{\mathbf{x}}$.

Les solutions sont celles des équations normales $A^TA\mathbf{x} = A^T\mathbf{b}$. La solution est unique pour tout $\mathbf{b}$ si et seulement si les colonnes de $A$ sont indépendantes, ou de façon équivalente si $A^TA$ est inversible. Alors $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$.

> [!warning] Écart dans le cours
> [[chp 1 - Orthogonality]] écrit que $\hat{\mathbf{x}}$ est le projeté de $\mathbf{b}$ sur Col $A$, mais sa figure montre que c'est $A\hat{\mathbf{x}}$. Cette page suit la figure.

Liens : [[Orthogonalité]], [[Espace des colonnes]], [[Régression linéaire]]

Résumés : [[chp 1 - Orthogonality (résumé)]], [[Cours 10 - linear regression (résumé)]] (méthode par dérivées partielles)
