---
type: concept
tags: [year2]
aliases: [tri par fusion, merge sort, mergesort]
sources: ["[[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : algorithme de tri de type [[Diviser pour régner|diviser pour régner]]. On coupe le tableau en deux moitiés, on trie chacune récursivement, puis on fusionne les deux moitiés triées : on avance dans chacune et on prend à chaque pas le plus petit des deux éléments en tête, jusqu'à épuiser l'une des deux, puis on recopie le reste de l'autre.

- **Cas de base** : un tableau de 0 ou 1 élément est déjà trié.
- **Fusion** : fusionner deux listes triées de longueurs $p$ et $q$ coûte $O(p + q)$, chaque comparaison plaçant un élément.
- **Récurrence** : $T(n) = 2\,T(n/2) + cn$, donc $a = 2$, $b = 2$, $k = 1$ et $a = b^k$ ; par le [[Calcul de complexité et théorème de résolution|théorème de résolution]], $T(n) = O(n^k \log_b n) = O(n \log n)$. Ce coût vaut au pire comme au meilleur cas : le découpage ne dépend pas des données.
- **Mémoire** : $O(n)$ pour le tableau auxiliaire de la fusion (le tri n'est pas en place).
- **Stabilité** : le tri est stable (deux éléments égaux gardent leur ordre), à condition de prendre l'élément de la moitié gauche en cas d'égalité.

```python
def tri_fusion(t):
    if len(t) <= 1:
        return t
    m = len(t) // 2
    g, d = tri_fusion(t[:m]), tri_fusion(t[m:])
    res, i, j = [], 0, 0
    while i < len(g) and j < len(d):
        if g[i] <= d[j]:
            res.append(g[i]); i += 1
        else:
            res.append(d[j]); j += 1
    return res + g[i:] + d[j:]
```

Exemple : `[5, 2, 4, 1]` se coupe en `[5, 2]` et `[4, 1]`, triés en `[2, 5]` et `[1, 4]`, puis fusionnés en `[1, 2, 4, 5]`.

Comparaison : [[Tri par insertion]] et [[Tri par sélection]] sont en $O(n^2)$ au pire, mais en place ; $O(n \log n)$ est la meilleure complexité possible au pire pour un tri par comparaisons.

## Dans le cours

Le cours ne le détaille pas. [[1 - récursivité et complexité]] le cite dans ses compléments comme exemple du cas $a = b^k$ du théorème de résolution, et comme exemple de la classe quasi-linéaire $O(n \log n)$.

Voir aussi : [[Diviser pour régner]], [[Calcul de complexité et théorème de résolution]], [[Classe de complexité]], [[Complexité algorithmique]], [[Récursivité]].

Résumés : [[1 - récursivité et complexité]]
