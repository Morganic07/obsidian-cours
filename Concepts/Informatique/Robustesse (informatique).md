---
type: concept
tags: [year4]
aliases: [robustesse, programme robuste, robustness]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : qualité d'un programme qui ne plante pas et se comporte de manière sensée même dans les cas imprévus ou face à des utilisateurs qui ne le sont pas : aucune donnée saisie, valeur hors limites, unité inconnue.

Complément, hors du cours : on l'obtient en traitant les cas limites (liste vide, zéro, valeur maximale), en vérifiant les entrées ([[Validation des entrées]]) et le résultat des opérations qui peuvent échouer (lecture, ouverture de fichier), et en le testant ([[Test unitaire]]). Elle s'oppose à la correction seule : un programme correct pour les entrées prévues peut être fragile face aux autres.

## Dans le cours

[[4 - Cours complet]] la demande explicitement (question 36 : « Un bon programme ne doit pas planter » si l'on tape −1 d'emblée, ce qui provoquerait une division par zéro), l'illustre par le programme de conversion cm/pouce, et la range parmi les qualités d'un programme réutilisable (clair, lisible, fonctionnel, robuste, documenté).

Résumés : [[4 - Cours complet]]
