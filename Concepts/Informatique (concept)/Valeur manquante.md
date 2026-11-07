---
type: concept
tags: [year4]
aliases: [valeurs manquantes, missing values]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
---

Les valeurs manquantes font partie de ce qu'on nettoie lors du [[Prétraitement des données]].

L'[[Algorithme C4.5]] les traite ainsi : si la valeur de l'attribut $a_i$ manque, l'exemple est affecté à chacun des $n$ groupes définis par les valeurs de $a_i$, avec une probabilité estimée par la fréquence du groupe ; cette probabilité entre dans le calcul du gain et se propage dans l'arbre.

Notion parente : [[Prétraitement des données]].

Résumés : [[1 - pdf du prof (résumé)]], [[1 - intro to data mining (résumé)]]
