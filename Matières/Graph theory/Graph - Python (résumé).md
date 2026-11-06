---
type: source
tags: [year4]
sources: ["[[Graph - Python]]"]
maj: 2026-11-05
---

Résumé de [[Graph - Python]], dans [[Graph theory (matière)]]. Notes de TP en Python, sans image. Les définitions viennent de [[Chp 1 - Undirected graph (résumé)]] et [[Chp2 - tree (résumé)]].

## Contenu, dans l'ordre de la note

- **Dictionnaires Python** : `{"nom": "Michel", "age": 33}`, accès par clé (pas par valeur), ajout d'une clé, parcours avec `keys()` et `items()`. Un exemple ajoute une clé « numéro » ; la valeur n'est pas reprise ici.
- **Affichage d'un graphe** par sa matrice d'adjacence puis par son dictionnaire (clé = sommet, valeur = liste des voisins). On n'imprime chaque arête qu'une fois grâce à une comparaison entre sommets.
- **`isChain`** : vérifie qu'une liste de sommets est une chaîne, en testant que chaque sommet suivant est voisin du précédent.
- **Exercices d'entraînement** : `estVoisin`, `estChaine`, `estChaineElementaire` (sommets tous distincts), `isSimpleChain` (arêtes distinctes), `isGraphFull` (tous les degrés valent $n - 1$), `infoGraphFull` (nombre d'arêtes $n(n-1)/2$), `degre`, `isGraphBipartite` (parcours qui colorie chaque sommet de 0 ou 1 et échoue sur deux voisins de même couleur).
- **Algorithme de Kruskal** commenté : `add_edge`, `find_parent` (récursif, racine si `parent[i] == i`), `union` par rang, `kruskal` qui trie les arêtes par poids, parcourt jusqu'à $V - 1$ arêtes acceptées et rejette celles dont les extrémités ont la même racine. Voir [[Arbre couvrant minimal]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Affichage par matrice** : le test `if (mat[i] < mat[j])` compare deux lignes de la matrice (des listes), non des indices. Le commentaire annonce l'élimination des doublons et des boucles, ce que fait `node < neighbor` dans la version à dictionnaire. Pour la matrice, il faudrait tester `mat[i][j] == 1 and i < j` (complément).
2. **Version à dictionnaire** : le dernier `print` est écrit sans parenthèse fermante.
3. **`kruskal`** : la boucle lit `graph[i]` sans vérifier que `i` reste dans la liste. Sur un graphe non connexe, l'indice dépasse la taille de la liste (complément). Le cours suppose le graphe connexe (préconditions de Kruskal).
4. **`isGraphFull`** : suppose un graphe simple (commentaire de la note). Une boucle ou une arête multiple fausserait le test.
5. **Sorties** : les affichages de la note ne sont pas identiques à ceux du code (« Age » et « Numero » avec majuscules). Écart d'affichage sans importance.
6. Le code des autres fonctions n'a pas été exécuté ici, sauf lecture.
