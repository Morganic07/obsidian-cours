---
type: concept
tags: [year4]
aliases: [contrôle de saisie, input validation, contrôle des saisies]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : vérification, avant de les utiliser, que les données reçues de l'extérieur (clavier, fichier, réseau) sont du bon type et dans le domaine attendu, avec rejet ou nouvelle demande sinon. Le compilateur ne vérifie que les types, pas le sens des valeurs. En C++, on teste aussi la réussite de la lecture (`if (!(cin >> x))`), puis on remet le flux en état (`cin.clear()`) et on jette la saisie fautive (`cin.ignore(…)`). En sécurité, l'absence de validation est à l'origine d'attaques comme l'[[Injection SQL|injection SQL]].

## Dans le cours

[[4 - Cours complet]] fait contrôler les notes (question 34 : entre 0 et 20, ou −1, sinon redemander) et rappelle que le compilateur accepte `int age = -100;` sans broncher. Voir [[Robustesse (informatique)]].

Résumés : [[4 - Cours complet]]
