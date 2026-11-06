---
type: source
sources: ["[[raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres]] (29 diapositives, « Chapitre 3 : Graphes et arbres », groupe ID2), dans [[Year 2 - Algo]].

## Idée générale

Le chapitre rappelle le vocabulaire des graphes, puis définit l'arbre comme un graphe particulier et donne le vocabulaire des arbres.

## Contenu, dans l'ordre du cours

- **Rappel sur les graphes** : un graphe orienté est un couple $(S, A)$ (sommets, arcs) ; dans un graphe non orienté, on parle d'arêtes. Voir [[Graphe orienté]] et [[Graphe non orienté]]. Une boucle relie un sommet à lui-même (interdite en non orienté).
- **Degré** : en non orienté, nombre d'arêtes incidentes (degré 0 : sommet isolé). En orienté : degré sortant, degré entrant, et leur somme.
- **Chemin** de longueur $k$ : suite de sommets reliés par des arcs ; élémentaire si les sommets sont distincts. Exemples : $\langle 1,4,2,5\rangle$ (élémentaire), $\langle 3,6,6,6\rangle$ (non élémentaire). **Circuit** : chemin qui revient à son point de départ. **Cycle** : équivalent non orienté (au moins deux arêtes) ; un graphe sans cycle est acyclique. **Sous-graphe**.
- **Propriétés équivalentes d'un arbre** (graphe non orienté) : deux sommets sont reliés par un unique chemin élémentaire ; il est acyclique avec $|A| = |S| - 1$ ; il est acyclique et l'ajout d'une arête crée un cycle.
- **Arbre comme structure de données** : non linéaire, naturellement récursive, hiérarchique. Exemples : système de fichiers, base de données, sites web, fichiers XML. Les nœuds sont reliés par des arêtes qui expriment la relation parent-fils.
- **Vocabulaire** : racine (sans parent), feuille ou nœud externe (sans fils), nœud interne, arité d'un nœud et d'un arbre, sous-arbre, branche, descendants, ascendants, taille (12 dans l'exemple, 0 pour l'arbre vide), degré, niveau (racine au niveau 0, niveau du fils = niveau du père + 1). Construction récursive : un nœud et des arbres $T_1, \dots, T_m$ connectés comme fils.
- **Hauteur** : profondeur maximale ; 0 pour un arbre à un nœud, $-1$ pour l'arbre vide.
- **Familles d'arbres** : arbre $m$-aire (degré maximal $m$), B-arbre d'ordre $n$ (racine d'au moins deux fils, autres nœuds entre $n/2$ et $n$ fils, feuilles au même niveau), arbre binaire, arbre binaire de recherche (clé supérieure à celles de ses descendants gauches, inférieure à celles des droits).
- **Arbre enraciné ou arborescence** : graphe orienté sans circuit avec une racine d'où part un chemin unique vers chaque sommet ; $n$ sommets, $n-1$ arcs. Ancêtre, père, fils.

## Liens

Suite du cours : [[Chapitre4-Preing2ID (résumé)]] sur les [[Arbre binaire|arbres binaires]], puis [[Chapitre5-ABR (résumé)]] sur l'[[Arbre binaire de recherche]].
