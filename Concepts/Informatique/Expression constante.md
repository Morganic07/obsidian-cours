---
type: concept
tags: [year4]
aliases: [constant expression, constexpr]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : [[Expression (programmation)|expression]] dont la valeur peut être calculée **à la compilation** : littéraux, constantes initialisées par des littéraux, opérations sur celles-ci (`2 * MAXIMUM`). Elle est exigée là où le compilateur doit connaître la valeur : étiquettes `case`, taille d'un tableau statique, paramètres de templates. Depuis C++11, le mot-clé `constexpr` déclare une variable ou une fonction utilisable dans une expression constante : `constexpr double pi = 3.14159;`.

## Dans le cours

[[4 - Cours complet]] précise que les étiquettes des `case` d'un `switch` doivent être des expressions constantes, et non des variables (voir [[Structure conditionnelle]], [[Constante (programmation)]]).

- [[tp3]] : le programme 3.11 sur l'échelle de Richter ne compilait pas, `case richter>9:` n'étant pas une expression constante entière (`case label does not reduce to an integer constant`) ; le test `richter > 9` est passé dans le `default`.

Résumés : [[4 - Cours complet]]
