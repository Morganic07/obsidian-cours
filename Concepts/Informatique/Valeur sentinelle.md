---
type: concept
tags: [year4]
aliases: [sentinelle, sentinel value, marque de fin]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : valeur particulière, impossible parmi les données réelles, qui signale la fin d'une série ou un état « vide ». Elle permet une [[Boucle (programmation)|boucle]] dont le nombre de tours n'est pas connu d'avance : on lit jusqu'à rencontrer la sentinelle, qui n'est pas traitée comme une donnée. Le `'\0'` qui termine une chaîne C en est un exemple.

## Dans le cours

[[4 - Cours complet]] en donne deux : la note **−1**, « uniquement une marque de fin » de la saisie des notes (exercice 3), et la chaîne `" "` qui initialise `motPrecedent` dans le détecteur de mots répétés, valeur que `cin` ne peut jamais lire.

Résumés : [[4 - Cours complet]]
