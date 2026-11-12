---
type: concept
tags: [year4]
aliases: [options de g++, compiler flags, CXXFLAGS, "-Wall", "-std=c++17", options de compilation]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : une option de compilation est un argument passé au compilateur (ici [[GCC|`g++`]]) pour régler ce qu'il produit : étape où s'arrêter, nom du fichier, avertissements, version du langage, optimisation, débogage. Dans un [[Make (logiciel)|Makefile]], on les regroupe dans la variable `CXXFLAGS`.

| Option | Effet |
|---|---|
| `-c` | compile sans [[Édition de liens\|édition de liens]] : produit un [[Fichier objet\|fichier objet]] `.o` |
| `-o nom` | nomme le fichier produit (sinon `a.out` pour un [[Exécutable\|exécutable]]) |
| `-Wall`, `-Wextra` | active la plupart des [[Avertissement de compilation\|avertissements]], puis d'autres |
| `-Werror` | change les avertissements en erreurs |
| `-std=c++17` | choisit la version de la [[Norme du C++\|norme du C++]] |
| `-g` | ajoute les informations de débogage |
| `-O0` à `-O3` | niveau d'optimisation |
| `-E` | s'arrête après le [[Préprocesseur\|préprocesseur]] |
| `-I dossier` | ajoute un dossier où chercher les en-têtes ([[Directive include]]) |
| `-l nom` | lie une bibliothèque (`-lm`) |

## Dans le cours

- [[4 - Prise de note]] : `g++ monprog.cpp -o monprog -Wall`.
- [[5 - Compilation séparée]] : `-c` et `-o` pour la compilation séparée ; `CXXFLAGS = -Wall -std=c++17` dans le Makefile.

Voir aussi : [[Chaîne de compilation]], [[Compilation séparée]].

- [[4 - Cours complet]] : `-Wall`, `-c` et `-o`.

Résumés : [[4 - Prise de note]], [[5 - Compilation séparée]], [[4 - Cours complet]]
