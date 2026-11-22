---
type: concept
tags: [year4]
aliases: [register allocation]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition (complément, hors du cours)** : étape d'un [[Compilateur|compilateur]] qui décide quelles [[Variable (programmation)|variables]] du programme seront rangées dans les [[Registre du processeur|registres du processeur]], peu nombreux mais bien plus rapides que la mémoire. Deux variables « vivantes » en même temps (dont les valeurs seront encore lues) ne peuvent pas partager un registre : on construit leur [[Graphe d'incompatibilité|graphe d'interférence]] et l'on cherche une [[Coloration de graphe|coloration propre]] avec autant de couleurs que de registres. Gregory Chaitin a proposé cette méthode en 1981 ; quand le graphe n'est pas coloriable, certaines variables sont « déversées » (*spilled*) en mémoire.

## Dans le cours

Pas nommée : citée en complément dans [[5 - colorier graph]] (Graph theory), parmi les applications de la coloration.

Résumés : [[5 - colorier graph]]
