---
type: concept
tags: [year4]
aliases: [getline, std::getline]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : `std::getline(flux, chaine)` lit toute une ligne d'un flux (jusqu'au retour à la ligne, qu'elle consomme sans le garder) et la range dans une [[Classe string (C++)|`string`]], espaces compris ; elle est déclarée dans `<string>`. Contrairement à `cin >> s`, qui s'arrête au premier [[Espace blanc|espace blanc]], elle permet de lire un nom composé ou une phrase. Piège : après `cin >> n`, le retour à la ligne reste dans le flux, et un `getline` lit alors une ligne vide ; `cin >> std::ws` ou `cin.ignore()` l'évitent.

## Dans le cours

[[4 - Cours complet]] la recommande pour saisir un nom qui contient des espaces (question 16), en renvoyant à sa documentation en ligne.

Voir aussi : [[Flux d'entrée-sortie (C++)]].

Résumés : [[4 - Cours complet]]
