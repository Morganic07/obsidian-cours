---
type: concept
tags: [year1]
aliases: [récursion terminale, récursivité non terminale, récursion non terminale, récursivité enveloppée, tail recursion, élimination des appels terminaux, tail-call optimization]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-08
---

Une récursion est terminale si l'appel récursif est la dernière instruction ; elle est non terminale (enveloppée) sinon.

Pour éviter le coût de la pile, on place les opérations qui suivent l'appel à l'intérieur de l'appel, avec un accumulateur : `factRT(n, acc)`, `fiboRT(n, fn-2, fn-1)`, puissance terminale (TD3).

**Élimination des appels terminaux (complément, hors du cours)** : comme il ne reste rien à faire après l'appel terminal, le bloc de l'appel en cours dans la [[Pile d'exécution]] ne sert plus ; un compilateur peut le réutiliser au lieu d'en empiler un nouveau (*tail-call optimization*). La récursion devient alors une boucle : mémoire en $O(1)$ au lieu de $O(n)$, sans risque de débordement de pile. Scheme l'impose par sa norme et OCaml le garantit ; GCC et Clang le font en général dès `-O2`, sans garantie du langage C ; Python ne le fait pas, si bien que `factRT` y consomme autant de pile que la version enveloppée et lève la même `RecursionError` au-delà de la limite.

Notion parente : [[Récursivité]]. Voir aussi : [[Factorielle]], [[Suite de Fibonacci]], [[Pile et file]].

Résumés : [[0 - diapo prof]]
