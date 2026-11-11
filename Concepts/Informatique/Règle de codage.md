---
type: concept
tags: [year4]
aliases: [règles de codage, convention de codage, coding standard, style de codage, convention de nommage]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : règle que le programmeur s'impose au-delà de ce qu'exige le langage, pour augmenter la **lisibilité** des programmes en les rapprochant du langage naturel (et éviter des bugs).

Règles du polycopié :
- initialiser toute variable à sa définition ([[Initialisation (programmation)]]) ;
- variables nommées par un nom, fonctions par un verbe, en [[Casse chameau|casse chameau]] ; `i`, `j`, `k` pour les indices ; pas de nom commençant par `_` ;
- pas de [[Nombre magique (programmation)|constantes magiques]], mais des constantes nommées ; constantes en MAJUSCULES ;
- préfixe `ptr` pour les pointeurs ;
- pas de saisie ni d'affichage dans les fonctions ; une seule action par fonction ; 10 à 15 lignes au maximum ;
- paramètre principal en premier.

Complément, hors du cours : les équipes suivent souvent un guide publié (C++ Core Guidelines, Google C++ Style Guide) et le font respecter par des outils (`clang-format`, `clang-tidy`).

Voir aussi : [[Variable (programmation)]], [[Fonction et procédure]].

Résumés : [[4 - Cours complet]]
