---
type: concept
aliases: [orthogonal projection, orthogonal projections, projections orthogonales, projeté orthogonal, projeté orthogonalement]
sources: ["[[chp 1 - Orthogonality]]"]
maj: 2026-11-05
---

Tout $\mathbf{y}$ de $\mathbb{R}^n$ s'écrit de façon unique $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, avec $\hat{\mathbf{y}}$ dans le sous-espace $W$ et $\mathbf{z}$ dans $W^\perp$. On note $\hat{\mathbf{y}} = \text{proj}_W\,\mathbf{y}$.

- **Sur un vecteur** $\mathbf{u} \neq \mathbf{0}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}$. Le résultat ne change pas si l'on remplace $\mathbf{u}$ par $c\mathbf{u}$, car il ne dépend que de la droite engendrée.
- **Sur un sous-espace** de base orthogonale $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\mathbf{u}_1 + \dots + \frac{\mathbf{y} \cdot \mathbf{u}_p}{\mathbf{u}_p \cdot \mathbf{u}_p}\mathbf{u}_p$. Le résultat ne dépend que de $W$, pas de la base choisie.
- **Meilleure approximation** : $\hat{\mathbf{y}}$ est le point de $W$ le plus proche de $\mathbf{y}$, soit $\|\mathbf{y} - \hat{\mathbf{y}}\| < \|\mathbf{y} - \mathbf{v}\|$ pour tout $\mathbf{v}$ de $W$ différent de $\hat{\mathbf{y}}$.
- **Si $\mathbf{y}$ est déjà dans $W$** : $\text{proj}_W\,\mathbf{y} = \mathbf{y}$.

Liens : [[Orthogonalité]], [[Complément orthogonal]], [[Famille orthogonale]], [[Procédé de Gram-Schmidt]], [[Moindres carrés]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
