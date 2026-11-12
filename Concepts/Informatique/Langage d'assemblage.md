---
type: concept
tags: [year4]
aliases: [assembleur, assembly language, assemblage]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : langage de bas niveau où chaque instruction correspond à une instruction du [[Code machine|code machine]], écrite sous forme mnémonique (`mov`, `add`, `jmp`) avec des noms de [[Registre du processeur|registres]]. Un programme appelé assembleur le traduit en code objet ; c'est l'étape d'**assemblage**. `g++ -S fichier.cpp` montre l'assembleur produit par le compilateur.

## Dans le cours

[[4 - Cours complet]] indique que `g++ -c` réalise le prétraitement, la compilation et **l'assemblage** du source en fichier objet `.o`.

Résumés : [[4 - Cours complet]]
