---
type: concept
tags:
  - year4
aliases:
  - erreurs de compilation
  - erreurs du compilateur
  - undefined reference
  - compilation error
  - avertissement du compilateur
  - compiler warning
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/Chp1 - basiques.docx|Chp1 - basiques]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une erreur de compilation est un défaut du code source détecté avant l'exécution, qui empêche la production de l'exécutable. Les messages viennent d'étapes différentes de la [[Chaîne de compilation]] :

- **préprocesseur** : fichier `.h` introuvable (`fatal error: x.h: Aucun fichier ou dossier de ce type`) ;
- **compilation** proprement dite : syntaxe et types (`;` ou accolade oubliés, variable non déclarée, types incompatibles) ;
- **édition de liens** : `undefined reference to '…'` puis `ld returned 1 exit status`, quand `ld` ne trouve le code d'une fonction dans aucun fichier objet ni aucune bibliothèque (fonction déclarée mais jamais définie, nom mal orthographié, bibliothèque oubliée comme `-lm` pour `math.h`).

Il faut distinguer les **erreurs**, bloquantes, des **avertissements** (*warnings*), qui laissent la compilation aboutir mais signalent un code suspect. `gcc -Wall -Wextra` les active : affectation dans une condition (`if (x = 0)`), [[Variable non initialisée|variable non initialisée]], `;` juste après un `if`, variable inutilisée. L'option `-Werror` les transforme en erreurs.

## Dans le cours

Messages types du compilateur relevés par le cours :

| Message | Cause |
|---|---|
| `expected ';'` | point-virgule oublié |
| `expected declaration or statement at end of input` | accolade oubliée |
| `'nom_variable' undeclared` | variable non déclarée |
| `undefined reference to 'nom_fonction'`, avec `ld returned 1 exit status` | fonction inconnue |
| `fatal error: nom_fichier.h` | fichier d'en-tête mal orthographié |

Notion parente : [[Langage C]]. Voir aussi : [[Typage statique]], [[Fonction et procédure]], [[Chaîne de compilation]], [[GCC]].

Résumés : [[1 - basiques]]
