---
type: concept
tags: [year2]
aliases: [Gram-Schmidt, Gram–Schmidt, Gram–Schmidt Process, Gram schmidt]
sources: ["[[chp 1 - Orthogonality (résumé)|chp 1 - Orthogonality]]"]
maj: 2026-11-06
---

Méthode qui transforme une base $\{\mathbf{x}_1, \dots, \mathbf{x}_p\}$ d'un sous-espace en une base orthogonale $\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$, en retirant à chaque vecteur ses [[Projection orthogonale|projections]] sur les vecteurs déjà construits :

$$\mathbf{v}_1 = \mathbf{x}_1, \qquad \mathbf{v}_k = \mathbf{x}_k - \frac{\mathbf{x}_k \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 - \dots - \frac{\mathbf{x}_k \cdot \mathbf{v}_{k-1}}{\mathbf{v}_{k-1} \cdot \mathbf{v}_{k-1}}\mathbf{v}_{k-1}$$

À chaque étape, $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \text{Span}\{\mathbf{x}_1, \dots, \mathbf{x}_k\}$. En normalisant les vecteurs, on obtient une base orthonormale.

Notion parente : [[Projection orthogonale]]. Liens : [[Orthogonalité]], [[Base (algèbre linéaire)]], [[Famille orthogonale]], [[Factorisation QR]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
