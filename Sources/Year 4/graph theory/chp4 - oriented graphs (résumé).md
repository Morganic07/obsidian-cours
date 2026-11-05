---
type: source
sources: ["[[chp4 - oriented graphs]]"]
maj: 2026-11-05
---

Résumé de [[chp4 - oriented graphs]], dans [[Year 4 - graph theory]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes. Voir [[Graphe orienté]].

## Idée générale

Graphes orientés : chemins, degrés entrants et sortants, parcours en profondeur et en largeur, composantes fortement connexes.

## Contenu, dans l'ordre du cours

- **Graphe orienté** $G = (V, A)$ avec $A \subseteq V \times V$ (arcs).
- **Chemin** : suite de sommets $v_1, \ldots, v_k$ avec un arc entre $v_i$ et $v_{i+1}$ ; élémentaire s'il ne répète pas de sommet, simple s'il ne répète pas d'arc. **Circuit** : chemin fermé.
- **Degrés** : $d^-(v)$ arcs entrants, $d^+(v)$ arcs sortants. $\sum_v d^+(v) = \sum_v d^-(v) = |A|$. Exemple à quatre sommets $A$ à $D$ avec tableau des degrés.
- **DFS (parcours en profondeur)** : marquer, afficher, appeler récursivement sur chaque fils non visité. Sur le graphe de l'exemple à sept sommets, un parcours depuis 0 peut visiter 0, 2, 1, 5, 4. Complexité $O(|V| + |E|)$ : chaque sommet et chaque arête une fois.
- **BFS (parcours en largeur)** : file, marquer à l'entrée dans la file, afficher à la sortie. Même complexité $O(|V| + |E|)$.
- **Composante fortement connexe (SCC)** : sous-graphe maximal où tout sommet atteint tout autre. Exemple à huit sommets : $\{B, C, E, F, G\}$ et trois composantes à un sommet $\{A\}$, $\{D\}$, $\{H\}$.
- **Algorithme 1** : $D(v)$ descendants, $A(v)$ ancêtres, la SCC de $v$ est $\{v\} \cup (A(v) \cap D(v))$.
- **Tarjan** : mentionné avec sa complexité $O(V + E)$ et une mémoire $O(V)$ (pile, indices, lowlinks), sans description de l'algorithme.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes.

1. **« Oriented graph » défini par $A \subseteq V \times V$** : le texte dit qu'on oriente un graphe non orienté, mais le graphe de l'exemple DFS contient $0 \to 4$ et $4 \to 0$, ainsi que $3 \to 6$ et $6 \to 3$. C'est un graphe orienté au sens large, pas un graphe sans arcs opposés (complément). La transcription a aussi gardé un début de définition inachevé (« An oriented graph est… »).
2. **Définition du chemin** : « un arc connecte $v_i$ et $v_{i+1}$ » ne précise pas le sens de l'arc ; il faut un arc de $v_i$ vers $v_{i+1}$ (complément).
3. **Notations** : $G = (V, A)$ puis $G = (V, E)$ pour la SCC, avec $E$ ou $A$ pour les arcs.
4. **Complexité des parcours** : $O(|V| + |E|)$ vaut avec des listes d'adjacence ; avec une matrice d'adjacence elle devient $O(|V|^2)$ (complément).
5. **Exemple DFS** : l'ordre 0, 2, 1, 5, 4 suppose que les fils sont pris dans l'ordre de la figure. Je l'ai vérifié sur la liste d'arcs de la transcription : il est correct sous cette hypothèse.
6. **Typos** : « DSF » et « BSF » pour DFS et BFS, numérotation « 2. » répétée, point final doublé.
7. **SCC de l'exemple** : relue avec les arcs de la transcription ($B \to C \to F \to B$, $B \to E \to F$, $C \to G \to F$), la grande composante est bien $\{B, C, E, F, G\}$ ; $A$, $D$ n'ont pas d'arc entrant et $H$ n'en reçoit que de $D$.
