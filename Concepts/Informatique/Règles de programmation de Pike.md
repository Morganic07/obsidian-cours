---
type: concept
tags: [year4]
aliases: [règles de Rob Pike, Rob Pike's rules of programming, Data dominates]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : cinq règles publiées par Rob Pike, chercheur des [[Laboratoires Bell]] et co-auteur du langage Go, dans *Notes on Programming in C* (1989). En substance : 1) on ne sait pas où un programme passera son temps ; 2) mesurer avant d'optimiser ; 3) les algorithmes sophistiqués sont lents quand n est petit, et n est généralement petit ; 4) ils sont plus bogués que les simples : utiliser des algorithmes et des [[Structure de données|structures de données]] simples ; 5) les données dominent : bien choisies, elles rendent les algorithmes évidents.

## Dans le cours

[[4 - Cours complet]] cite la règle n° 5 (« Écrivez du code stupide qui utilise des données futées ! ») au bilan de la deuxième partie, et la règle n° 4, rattachée au [[Principe KISS]], au bilan de la troisième.

Résumés : [[4 - Cours complet]]
