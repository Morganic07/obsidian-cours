---
type: concept
tags: [year2, year4]
aliases: [shared library, shared libraries, bibliothèques partagées]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-11
---

Fichiers du répertoire `/lib` utilisés par plusieurs programmes. Partagés au lieu d'être chargés plusieurs fois, ils économisent la mémoire et évitent de dupliquer du code.

Notion parente : [[Arborescence des répertoires Linux]].

## Dans le cours

[[4 - Cours complet]] (C++) définit la bibliothèque dynamique : son code est intégré au moment de l'exécution ; le programme est plus petit et profite des mises à jour, mais dépend de la présence de la bibliothèque sur le système cible. Elle s'appelle *Dynamic Link Library* (`.dll`) sous Windows et *shared object* (`.so`) sous Unix/Linux. Comparer avec la [[Bibliothèque statique]].

Résumés : [[4 - OS]], [[4 - Cours complet]]
