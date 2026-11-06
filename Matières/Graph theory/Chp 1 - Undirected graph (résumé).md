---
type: source
tags: [year4]
sources: ["[[Chp 1 - Undirected graph]]"]
maj: 2026-11-05
---

Résumé de [[Chp 1 - Undirected graph]], dans [[Graph theory (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes. Voir [[Graphe non orienté]].

## Idée générale

Définitions de base des graphes non orientés (multigraphes avec boucles), puis graphes particuliers : complet, connexe, biparti, régulier, pondéré.

## Contenu, dans l'ordre du cours

- **Graphe non orienté** $G = (V, E, \gamma)$ : $V$ fini non vide (sommets), $E$ fini (arêtes), $\gamma$ associe à chaque arête ses extrémités.
- **Vocabulaire** : sommets adjacents (voisins), sommet isolé, boucle, arêtes multiples (parallèles), graphe **simple** (ni boucle ni arête multiple), graphe **sous-jacent** (simple, obtenu en supprimant boucles et multiplicités). Exemple dessiné avec $v_1$ à $v_4$ et $e_1$ à $e_6$.
- **Matrice d'adjacence** : $M_{i,j}$ est le nombre d'arêtes entre $v_i$ et $v_j$. Symétrique pour un graphe non orienté. Exemple du cours : une boucle sur $v_4$ vaut 1 sur la diagonale, deux arêtes parallèles $v_2 v_3$ valent 2.
- **Isomorphisme** : couple de bijections $(\varphi, \psi)$ sur sommets et arêtes qui respecte les extrémités. Exemple : un triangle avec un sommet pendant dessiné avec des sommets numérotés et avec des symboles de cartes.
- **Chaînes** : suite $(v_0, e_1, v_1, \ldots, e_p, v_p)$, de longueur $p$. **Simple** si les arêtes sont distinctes, **élémentaire** si les sommets le sont (une chaîne élémentaire est simple). **Cycle** : chaîne simple de longueur $> 0$ avec $v_p = v_0$.
- **Graphe planaire** : dessinable sans croisement. Sous-graphes et graphes isomorphes d'un planaire sont planaires.
- **Graphe complet** : simple, toute paire de sommets adjacente. $\text{card}(E) = \binom{n}{2}$. Un graphe simple a au plus $\frac{n(n-1)}{2}$ arêtes. Note : le degré de chaque sommet d'un graphe simple complet vaut $n - 1$.
- **Connexe** : deux sommets sont toujours reliés. **Composante connexe** : sous-graphe connexe maximal. Un graphe est connexe si et seulement s'il a une seule composante ; les composantes sont disjointes.
- **Biparti** : partition $(V_1, V_2)$ avec chaque arête entre les deux. **Complet** si tous les sommets de $V_1$ sont adjacents à tous ceux de $V_2$ ($K_{2,2}$, $K_{2,3}$, $K_{3,3}$ dessinés). Caractérisation : biparti si et seulement si tout cycle est de longueur paire.
- **Graphe $k$-régulier** : tout sommet de degré $k$, alors $k \cdot \text{card}(V) = 2 \cdot \text{card}(E)$.
- **Graphe pondéré** $(V, E, \gamma, w)$ avec $w : E \to \mathbb{R}$. Matrice d'adjacence d'un graphe simple pondéré : 0 sur la diagonale, $w(v_i v_j)$ si l'arête existe, $+\infty$ sinon.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Note sur les sous-ensembles du biparti** : « les sous-partitions $V_1$ et $V_2$ doivent avoir minimum 2 noeuds ». La définition du cours demande seulement $V_1$ et $V_2$ non vides, et l'exemple $G = (\{v_1, v_3, v_4\}, \{v_2, v_5\}, \ldots)$ est compatible avec les deux. La note de l'étudiant contredit la définition : un seul sommet de chaque côté suffit (par exemple une étoile).
2. **$\gamma : E \to V^2$** : un couple ordonné pour un graphe non orienté (alerte de la transcription). Il faudrait des paires non ordonnées (complément).
3. **Chaîne $C_2$** : $e_1$ relie $v_1$ et $v_2$, pas $v_4$ et $v_1$, donc $C_2 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_1, v_1)$ n'est pas une chaîne. Dans l'image elle est en rouge, $C_1$ en vert : probablement un contre-exemple voulu. Image non ouverte.
4. **Graphe sous-jacent** : la condition « $\forall (v, v') \in E' \Leftrightarrow v \ne v'$ » est mal formulée (alerte de la transcription). L'idée est : $E'$ contient une arête entre deux sommets distincts adjacents dans $G$ (complément).
5. **Degré non défini** : $d(v)$ sert pour les graphes réguliers, mais le chapitre ne le définit pas. La formule $k\,\text{card}(V) = 2\,\text{card}(E)$ suppose qu'une boucle compte deux fois (complément).
6. **« Path » à la place de « chain »** : la connexité est définie par un « path », alors que le chapitre définit des chaînes. Il faut lire chaîne (complément).
