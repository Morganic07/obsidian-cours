---
type: concept
tags: [year4]
aliases: [Tarjan, lowlink]
matieres: [graph theory]
sources: ["[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

Nommé dans le chapitre sur les graphes orientés sans description de l'algorithme : il calcule les [[Composante fortement connexe|composantes fortement connexes]] avec une complexité $O(V + E)$ et une mémoire $O(V)$ (pile, tableaux d'indices et de lowlinks).

## Fonctionnement (complément, hors du cours)

Publié par Robert Tarjan en 1972, l'algorithme repose sur un seul [[Parcours en profondeur|parcours en profondeur]] :

1. à sa découverte, chaque sommet $v$ reçoit un **indice** (son rang dans l'ordre de visite) et est empilé ; son **lowlink** est initialisé à son indice ;
2. pour chaque arc $v \to w$ :
   - si $w$ n'est pas encore visité, on l'explore récursivement, puis $\text{lowlink}(v) = \min(\text{lowlink}(v), \text{lowlink}(w))$ ;
   - si $w$ est déjà sur la pile, $\text{lowlink}(v) = \min(\text{lowlink}(v), \text{indice}(w))$ ;
3. quand l'exploration de $v$ est finie et que $\text{lowlink}(v) = \text{indice}(v)$, $v$ est la **racine** d'une SCC : on dépile jusqu'à $v$ inclus, et les sommets dépilés forment cette SCC.

Chaque sommet est empilé et dépilé une seule fois, chaque arc examiné une seule fois : d'où $O(V + E)$.

**Alternative : l'algorithme de Kosaraju**, lui aussi en $O(V + E)$ : un premier DFS sur $G$ note l'ordre de fin des sommets ; un second DFS sur le graphe transposé $G^T$ (arcs inversés), lancé depuis les sommets par date de fin décroissante, découvre exactement une SCC à chaque nouveau départ.

Notion parente : [[Composante fortement connexe]]. Voir aussi : [[Parcours en profondeur]], [[Pile et file]], [[Tri topologique]].

Résumés : [[4 - oriented graphs]]
