---
type: concept
tags: [year4]
aliases: [make, Makefile, GNU make, makefile, cible factice, .PHONY, variables automatiques de make]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : make automatise la [[Compilation séparée|compilation séparée]] à partir d'un fichier `Makefile`, fait de **règles** :

```makefile
cible: dépendances
	commande
```

- la **cible** est le fichier à produire ; les **dépendances** sont les fichiers dont elle dépend ;
- la ligne de commande commence obligatoirement par une **tabulation**, pas par des espaces ;
- variables : `CXX = g++`, `CXXFLAGS = -Wall -std=c++17`, employées avec `$(CXX)` ;
- variables automatiques : `$@` la cible, `$<` la 1re dépendance, `$^` toutes les dépendances ;
- `clean: rm -f *.o programme` efface les produits de la compilation.

## Compléments (hors du cours)

- make **compare les dates de modification** : une cible est refaite si elle manque ou si une dépendance est plus récente ; les dépendances sont d'abord mises à jour, récursivement. Il ne recompile ainsi que le nécessaire. Un en-tête oublié dans les dépendances laisse des [[Fichier objet|fichiers objets]] périmés.
- `make` construit la première cible du fichier, `make clean` la cible `clean`. `.PHONY: clean` déclare que `clean` n'est pas un fichier (cible factice).
- Des espaces au lieu de la [[Caractère de tabulation|tabulation]] : `*** missing separator.  Stop.`
- Écrit en 1976 aux Bell Labs pour Unix ; GNU make est la version courante sous [[Linux]]. Les projets importants génèrent leur Makefile avec [[CMake]].

Voir aussi : [[Chaîne de compilation]], [[GCC]], [[Option de compilation]].

## Dans [[4 - Cours complet]]

Un Makefile à trois règles (`main`, `main.o`, `somme.o`) avec leurs dépendances, la tabulation obligatoire devant les commandes, et la question 53 sur l'intérêt de `make` en programmation modulaire.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
