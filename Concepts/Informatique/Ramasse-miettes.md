---
type: concept
tags: [year3]
aliases: [garbage collector, garbage collection, glaneur de cellules]
sources: ["[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le ramasse-miettes (*garbage collector*, GC) est le mécanisme de gestion automatique de la mémoire : il libère les objets que plus aucune référence ne désigne, devenus inaccessibles au programme.

- En Java, les objets et les tableaux sont créés par `new` dans le **tas** et ne sont jamais libérés explicitement : il n'y a ni `free` (C) ni `delete` (C++). C'est la JVM qui lance le ramassage quand elle le juge utile.
- Avantages : pas d'oubli de libération (fuite mémoire), ni de pointeur vers une zone déjà libérée, ni de double libération.
- Contreparties : le moment de la libération n'est pas maîtrisé par le programmeur, et le ramassage consomme du temps processeur (avec parfois de courtes pauses de l'exécution).
- Python, C# et JavaScript utilisent aussi un ramasse-miettes ; C et C++ laissent la libération au programmeur ([[Allocation dynamique]]).

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - Intro Java]].

Voir aussi : [[Langage Java]], [[Allocation dynamique]], [[Compilation et bytecode]].

Résumés : [[1 - Intro Java]]
