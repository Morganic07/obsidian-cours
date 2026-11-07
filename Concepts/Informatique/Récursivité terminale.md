---
type: concept
tags: [year1]
aliases: [récursion terminale, récursivité non terminale, récursion non terminale, récursivité enveloppée]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-06
---

Une récursion est terminale si l'appel récursif est la dernière instruction ; elle est non terminale (enveloppée) sinon.

Pour éviter le coût de la pile, on place les opérations qui suivent l'appel à l'intérieur de l'appel, avec un accumulateur : `factRT(n, acc)`, `fiboRT(n, fn-2, fn-1)`, puissance terminale (TD3).

Notion parente : [[Récursivité]]. Voir aussi : [[Factorielle]], [[Suite de Fibonacci]], [[Pile et file]].

Résumés : [[AlgoID1 (résumé)]]
