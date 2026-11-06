---
type: source
tags: [year2]
sources: ["[[AVL momo]]"]
maj: 2026-11-05
---

Résumé de [[AVL momo]], dans [[Algo (matière)]]. Note de préparation d'un exposé sur les arbres AVL, avec le code Python des fonctions. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un [[Arbre AVL]] est un arbre binaire de recherche qui garde, à chaque ajout ou suppression, une différence de hauteur d'au plus 1 entre les deux sous-arbres de chaque nœud. La hauteur reste alors en $O(\log n)$.

## Contenu, dans l'ordre du cours

- **Hauteur** : $h = 1 + \max(h_{gauche}, h_{droite})$, avec $h = -1$ pour un sous-arbre vide.
- **Facteur d'équilibrage** : la note l'écrit droite moins gauche, « comme la prof » (ailleurs on prend gauche moins droite). L'arbre est équilibré si le facteur vaut $-1$, $0$ ou $1$ en chaque nœud. À $\pm 2$, il faut une rotation.
- **Ajout et suppression** : on fait comme pour un arbre binaire de recherche, puis on calcule les facteurs et on tourne. Les rotations sont les mêmes dans les deux cas, car elles ne dépendent que du facteur obtenu.
- **Propriété (amphi)** : $\log_2(1+n) \le 1 + h \le \alpha \log_2(2+n)$ avec $\alpha \le 1{,}44$, et $n \le 2^{h+1} - 1$.
- **Nombre de rotations** : une rotation simple ou double suffit après un ajout. Après une suppression, il peut en falloir jusqu'à $h$.
- **Rotations** : la rotation droite autour de $y$ fait descendre $y$ et remonter son fils gauche $x$, sans casser l'ordre. La rotation gauche est l'opération inverse. Si $h(G) - h(D) = 2$ : rotation droite, précédée d'une rotation gauche de $G$ si $h(g) < h(d)$. Cas $-2$ symétrique.
- **Cas à l'insertion** (avec facteur droite moins gauche) : pour $eq(y) = -2$ et $x$ fils gauche, si $eq(x) = -1$ ou $0$, rotation droite ; si $eq(x) = 1$, rotation gauche autour de $x$ puis rotation droite autour de $y$. Pseudo-code en `IF tree is right heavy / left heavy`, avec « double left : right → left » et « double right : left → right ».
- **Complexité des fonctions** : `hauteur`, `facteur_equilibrage`, `rotation_gauche` et `rotation_droite` servent à `equilibrer`, qui sert à `ajouter` et `supprimer` (avec `trouver_min` pour la suppression). La note donne $O(n)$ pour `hauteur` et `facteur_equilibrage`, $O(1)$ pour une rotation, et $O(\log n)$ pour `rebalance`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 1 (propriété de hauteur) a été ouverte ; les autres sont lues par leur transcription.

1. **Complexité de `rebalance`** (complément). **À corriger avant un examen.** La note annonce $O(\log n)$ avec une justification faible. Dans le code donné, `rebalance` appelle `facteur_equilibrage`, qui appelle `hauteur` deux fois, et `hauteur` parcourt tout le sous-arbre. `rebalance` est donc en $O(n)$ dans ce code. Elle n'est en $O(1)$ que si la hauteur est stockée dans chaque nœud. L'autre note de l'exposé, [[qui dit quoi AVL]], dit $O(1)$ : les deux notes se contredisent.
2. **Convention de hauteur** : la formule écrit $h = -1$ pour un sous-arbre vide, mais le code renvoie 0 pour un sous-arbre vide, donc 1 pour une feuille. La propriété $\log_2(1+n) \le 1 + h$ suppose qu'une feuille a $h = 0$.
3. **Exemple chiffré de la propriété** : image lue directement, « si $n = 100000$, $17 \le h \le 25$ ». Avec les formules écrites au-dessus, on trouve environ $16 \le h \le 22$ (complément). Les bornes de l'amphi ne suivent donc pas exactement ses formules.
4. **Facteurs après rotation** : la transcription juge incohérents $x = 1$ et $y = -1$ pour le cas $eq(x) = 0$. Fausse alerte (complément) : avec les sous-arbres de hauteurs $h+1$, $h+1$ et $h$, le calcul donne bien $x = 1$ et $y = -1$. Ce cas n'arrive qu'à la suppression.
5. **Étiquettes d'équilibre de la double rotation** : lues avec incertitude par la transcription, non vérifiées.
6. **Liens vidéo** (insertion et suppression) : non consultés.
