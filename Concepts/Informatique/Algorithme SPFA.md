---
type: concept
tags: [year4]
aliases: [SPFA, Shortest Path Faster Algorithm, Bellman-Ford avec file]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : variante de l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] qui ne relâche que les arcs issus des sommets dont la distance vient de changer. Ces sommets « actifs » attendent dans une file FIFO (voir [[Pile et file]]), sans doublon ; on retire un sommet, on [[Relâchement d'un arc|relâche]] ses arcs sortants, et tout voisin dont la distance baisse entre dans la file. La complexité dans le pire cas reste celle de Bellman-Ford, $O(nm)$, mais l'algorithme est souvent bien plus rapide en pratique. Sans garde-fou, il ne termine pas en présence d'un [[Circuit absorbant|circuit absorbant]] accessible ; on compte alors les entrées de chaque sommet dans la file, $n$ au plus sinon.

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : c'est l'algorithme « BELLMAN-FORD-Asynchrone » du cours, avec son ensemble $F$ de nœuds actifs, quand $F$ est géré comme une file.

Résumés : [[4 - bellman ford]]
