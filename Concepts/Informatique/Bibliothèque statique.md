---
type: concept
tags: [year4]
aliases: [static library, bibliothèques statiques, archive .a]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : bibliothèque dont le code est **recopié dans l'exécutable** au moment de l'[[Édition de liens|édition de liens]] (fichier `.a` sous Linux, `.lib` sous Windows). L'exécutable est plus gros mais autonome ; une mise à jour de la bibliothèque impose de refaire l'édition de liens. Elle s'oppose à la [[Bibliothèque partagée|bibliothèque dynamique]], chargée à l'exécution. Sous Linux on la crée avec `ar rcs libx.a a.o b.o`.

## Dans le cours

[[4 - Cours complet]] ne décrit que la bibliothèque dynamique ; la bibliothèque statique y est ajoutée en complément pour la comparaison.

Résumés : [[4 - Cours complet]]
