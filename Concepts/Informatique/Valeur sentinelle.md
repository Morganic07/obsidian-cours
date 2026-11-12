---
type: concept
tags: [year4]
aliases: [sentinelle, sentinel value, marque de fin]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : valeur particulière, impossible parmi les données réelles, qui signale la fin d'une série ou un état « vide ». Elle permet une [[Boucle (programmation)|boucle]] dont le nombre de tours n'est pas connu d'avance : on lit jusqu'à rencontrer la sentinelle, qui n'est pas traitée comme une donnée. Le `'\0'` qui termine une chaîne C en est un exemple.

## Dans le cours

[[4 - Cours complet]] en donne deux : la note **−1**, « uniquement une marque de fin » de la saisie des notes (exercice 3), et la chaîne `" "` qui initialise `motPrecedent` dans le détecteur de mots répétés, valeur que `cin` ne peut jamais lire.

- [[tp5]] : la saisie 0 arrête la boucle `do … while` du programme 5.2.
- [[tp6]] : une valeur 0 arrête les boucles de 6.2 et 6.3 ; le triplet qui la contient est quand même traité, le test étant en fin de boucle.
- [[td listes chaînées]] : le [[Pointeur NULL|pointeur `NULL`]] du dernier chaînon marque la fin de la [[Liste chaînée|liste]] ; le parcours s'arrête sur `actuel != NULL`.

Résumés : [[4 - Cours complet]]
