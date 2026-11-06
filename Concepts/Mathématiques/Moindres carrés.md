---
type: concept
tags: [year2, year3]
aliases: [least-squares, least squares, least square, moindre carré, normal equations, équations normales, least-squares solution, least-squares error, least square problem]
sources: ["[[chp 1 - Orthogonality]]", "[[Cours 10 - linear regression]]", "[[Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-06
---

Quand $A\mathbf{x} = \mathbf{b}$ n'a pas de solution, on cherche un $\hat{\mathbf{x}}$ qui minimise $\|\mathbf{b} - A\mathbf{x}\|$. Ce minimum $\|\mathbf{b} - A\hat{\mathbf{x}}\|$ est la least-square error. Comme $A\mathbf{x}$ est toujours dans Col $A$, le meilleur choix est le [[Projection orthogonale|projeté orthogonal]] de $\mathbf{b}$ sur Col $A$, c'est-à-dire $A\hat{\mathbf{x}}$.

Les solutions sont celles des équations normales $A^TA\mathbf{x} = A^T\mathbf{b}$. La solution est unique pour tout $\mathbf{b}$ si et seulement si les colonnes de $A$ sont indépendantes, ou de façon équivalente si $A^TA$ est inversible. Alors $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$.

> [!warning] Écart dans le cours
> [[chp 1 - Orthogonality]] écrit que $\hat{\mathbf{x}}$ est le projeté de $\mathbf{b}$ sur Col $A$, mais sa figure montre que c'est $A\hat{\mathbf{x}}$. Cette page suit la figure.

**En Data analysis (Thanos)** : pour ajuster une droite, on minimise la somme des carrés des écarts $SSE = \sum (y_i - \hat y_i)^2$, car les écarts positifs et négatifs se compenseraient dans une simple somme. [[Cours 10 - linear regression]] le fait aussi par [[Dérivée partielle|dérivées partielles]] sur trois points, avec le critère de minimum $f_{bb}f_{mm} - f_{bm}^2 > 0$ et $f_{bb} > 0$. En [[Analyse en composantes principales|ACP]], maximiser la variance projetée équivaut à minimiser l'erreur des moindres carrés ([[Cours 13 - Principal Components Analysis]]).

Notion parente : [[Projection orthogonale]]. Voir aussi : [[Orthogonalité]], [[Espace des colonnes]], [[Régression linéaire]], [[Analyse en composantes principales]], [[Dérivée partielle]]

## À vérifier

- [[chp 1 - Orthogonality]] : le texte dit que $\hat{\mathbf{x}}$ est le projeté de $\mathbf{b}$, la figure montre $A\hat{\mathbf{x}}$ ; la « smallest distance » $\|\mathbf{b}-A\mathbf{x}\|$ n'est atteinte qu'en $\hat{\mathbf{x}}$.
- Transcription de [[Cours 10 - linear regression]] : « −10 + 6b + 12 = 0 », il manque le $m$ ($-10 + 6b + 12m = 0$).

Résumés : [[chp 1 - Orthogonality (résumé)]], [[Cours 10 - linear regression (résumé)]] (méthode par dérivées partielles), [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Cours 13 - Principal Components Analysis (résumé)]]
