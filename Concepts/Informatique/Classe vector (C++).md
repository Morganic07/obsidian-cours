---
type: concept
tags: [year4]
aliases: [std::vector, vector C++, tableau dynamique C++]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : conteneur de la [[Bibliothèque standard du C++|bibliothèque standard]] (en-tête `<vector>`) qui représente un tableau dont la taille peut changer à l'exécution et qui gère seul sa mémoire : `std::vector<int> v{1, 2, 3}; v.push_back(4); v.size();`. Ses éléments sont contigus en mémoire, comme dans un [[Tableau (programmation)|tableau]] C, avec un accès `v[i]` en temps constant ; `v.at(i)` vérifie en plus l'indice. C'est le conteneur à utiliser par défaut en C++ à la place des tableaux C et de l'[[Allocation dynamique|allocation dynamique]] manuelle.

## Dans le cours

Absent de [[4 - Cours complet]] ; ajouté au récapitulatif des évolutions du C++ moderne.

Résumés : [[4 - Cours complet]]
