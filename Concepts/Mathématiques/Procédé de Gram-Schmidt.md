---
type: concept
tags: [year2]
aliases: [Gram-Schmidt, Gram–Schmidt, Gram–Schmidt Process, Gram schmidt]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]"]
maj: 2026-11-08
---

Méthode qui transforme une base $\{\mathbf{x}_1, \dots, \mathbf{x}_p\}$ d'un sous-espace en une base orthogonale $\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$, en retirant à chaque vecteur ses [[Projection orthogonale|projections]] sur les vecteurs déjà construits :

$$\mathbf{v}_1 = \mathbf{x}_1, \qquad \mathbf{v}_k = \mathbf{x}_k - \frac{\mathbf{x}_k \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\mathbf{v}_1 - \dots - \frac{\mathbf{x}_k \cdot \mathbf{v}_{k-1}}{\mathbf{v}_{k-1} \cdot \mathbf{v}_{k-1}}\mathbf{v}_{k-1}$$

À chaque étape, $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \text{Span}\{\mathbf{x}_1, \dots, \mathbf{x}_k\}$. En normalisant les vecteurs, on obtient une base orthonormale.

## Compléments (hors du cours)

**Mécanisme** : $\mathbf{v}_k$ est $\mathbf{x}_k$ moins sa [[Projection orthogonale|projection orthogonale]] sur $W_{k-1} = \text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_{k-1}\}$ (formule de la projection sur une base orthogonale). Donc $\mathbf{v}_k \in W_{k-1}^\perp$, c'est-à-dire orthogonal à tous les vecteurs précédents. Et $\mathbf{v}_k \neq \mathbf{0}$, car la famille de départ est libre : $\mathbf{x}_k$ n'appartient pas à $W_{k-1} = \text{Span}\{\mathbf{x}_1, \dots, \mathbf{x}_{k-1}\}$.

**Exemple** : $\mathbf{x}_1 = (3,6,0)$, $\mathbf{x}_2 = (1,2,2)$. On pose $\mathbf{v}_1 = \mathbf{x}_1$, puis
$$\mathbf{v}_2 = \mathbf{x}_2 - \frac{\mathbf{x}_2\cdot\mathbf{v}_1}{\mathbf{v}_1\cdot\mathbf{v}_1}\mathbf{v}_1 = (1,2,2) - \frac{15}{45}(3,6,0) = (0,0,2).$$
En normalisant : base orthonormale $\left(\tfrac{1}{\sqrt5}, \tfrac{2}{\sqrt5}, 0\right)$, $(0,0,1)$.

**En calcul numérique** : le Gram-Schmidt classique perd l'orthogonalité à cause des erreurs d'arrondi quand les vecteurs sont presque dépendants. On utilise plutôt le **Gram-Schmidt modifié**, qui retire les projections une à une en les calculant sur le vecteur déjà corrigé, ou les **réflexions de Householder**, méthode employée par LAPACK et donc par `numpy.linalg.qr`.

Notion parente : [[Projection orthogonale]]. Liens : [[Orthogonalité]], [[Base (algèbre linéaire)]], [[Famille orthogonale]], [[Factorisation QR]]

Résumé : [[1 - Orthogonality]]
