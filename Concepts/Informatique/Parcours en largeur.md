---
type: concept
tags: [year4]
aliases: [BFS, breadth first search]
matieres: [graph theory]
sources: ["[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

Parcours d'un graphe qui utilise une file : on enfile le sommet de départ et on le marque à son entrée dans la file ; on affiche un sommet à sa sortie de la file, puis on enfile ses voisins non marqués. Complexité $O(|V| + |E|)$.

## Compléments (hors du cours)

- Le BFS visite les sommets **par distance croissante** au départ (d'abord ceux à un arc, puis à deux arcs…) : il donne les **plus courts chemins en nombre d'arcs**, ce que le [[Parcours en profondeur|DFS]] ne garantit pas. Pour des arcs pondérés, il faut un autre algorithme, comme l'[[Algorithme de Dijkstra]] (poids positifs).
- Exemple du cours, graphe à 7 sommets (arcs 1→0, 0→2, 0→5, 0→4, 4→0, 2→1, 2→5, 3→1, 3→6, 6→3, 4→5, 6→5) : depuis 0, en prenant les fils dans l'ordre 2, 5, 4, le BFS donne 0, 2, 5, 4, 1.
- La borne $O(|V| + |E|)$ suppose des [[Liste d'adjacence|listes d'adjacence]] ; avec une [[Matrice d'adjacence|matrice d'adjacence]], lire les voisins d'un sommet coûte toute une ligne, et le parcours $O(|V|^2)$.
- Le BFS sert aussi à tester si un graphe est [[Graphe biparti|biparti]] (2-coloration).

Notion parente : [[Graphe orienté]]. Voir aussi : [[Parcours en profondeur]], [[Pile et file]].

Résumés : [[4 - oriented graphs]]
