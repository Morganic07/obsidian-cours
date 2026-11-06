---
type: concept
tags: [year2, year3]
aliases: [orthogonal projection, orthogonal projections, projections orthogonales, projeté orthogonal, projeté orthogonalement, Orthogonal Decomposition Theorem, théorème de décomposition orthogonale, best approximation, meilleure approximation]
sources: ["[[chp 1 - Orthogonality]]", "[[Chp2 - Symmetric matrices and quadratic forms]]", "[[Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-06
---

Tout $\mathbf{y}$ de $\mathbb{R}^n$ s'écrit de façon unique $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, avec $\hat{\mathbf{y}}$ dans le sous-espace $W$ et $\mathbf{z}$ dans $W^\perp$. On note $\hat{\mathbf{y}} = \text{proj}_W\,\mathbf{y}$. C'est le **théorème de décomposition orthogonale** (Orthogonal Decomposition Theorem) ; $\hat{\mathbf{y}}$ ne dépend que de $W$.

- **Sur un vecteur** $\mathbf{u} \neq \mathbf{0}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}$. Le résultat ne change pas si l'on remplace $\mathbf{u}$ par $c\mathbf{u}$, car il ne dépend que de la droite engendrée.
- **Sur un sous-espace** de base orthogonale $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\mathbf{u}_1 + \dots + \frac{\mathbf{y} \cdot \mathbf{u}_p}{\mathbf{u}_p \cdot \mathbf{u}_p}\mathbf{u}_p$. Le résultat ne dépend que de $W$, pas de la base choisie.
- **Sur un sous-espace de base orthonormale** : $\text{proj}_W\,\mathbf{y} = (\mathbf{y} \cdot \mathbf{u}_1)\mathbf{u}_1 + \dots + (\mathbf{y} \cdot \mathbf{u}_p)\mathbf{u}_p = UU^T\mathbf{y}$, avec $U = [\mathbf{u}_1 \cdots \mathbf{u}_p]$.
- **Meilleure approximation** (théorème de meilleure approximation, best approximation) : $\hat{\mathbf{y}}$ est le point de $W$ le plus proche de $\mathbf{y}$, soit $\|\mathbf{y} - \hat{\mathbf{y}}\| < \|\mathbf{y} - \mathbf{v}\|$ pour tout $\mathbf{v}$ de $W$ différent de $\hat{\mathbf{y}}$.
- **Si $\mathbf{y}$ est déjà dans $W$** : $\text{proj}_W\,\mathbf{y} = \mathbf{y}$.
- **Matrice de projection** : pour un $\mathbf{u}_j$ d'une décomposition spectrale, $(\mathbf{u}_j\mathbf{u}_j^T)\mathbf{x}$ est la projection de $\mathbf{x}$ sur la droite engendrée par $\mathbf{u}_j$.

**En ACP** (Data analysis) : chaque point est projeté orthogonalement sur la composante, d'où $\|a_i\|^2 = \|w_ic\|^2 + \|a_i - w_ic\|^2$ (variance initiale = variance restante + variance perdue).

Notion parente : [[Complément orthogonal]]. Liens : [[Orthogonalité]], [[Famille orthogonale]], [[Procédé de Gram-Schmidt]], [[Moindres carrés]], [[Matrice symétrique]], [[Décomposition spectrale]], [[Analyse en composantes principales]] (projection des données sur les composantes)

Résumés : [[chp 1 - Orthogonality (résumé)]], [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[Séance 13 - Principal Components Analysis (résumé)]]
