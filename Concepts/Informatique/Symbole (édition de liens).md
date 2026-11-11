---
type: concept
tags: [year4]
aliases: [table des symboles, symbol table, symbole non défini, undefined symbol, décoration de noms, name mangling]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : un symbole est le nom, dans un [[Fichier objet|fichier objet]], d'une fonction ou d'une variable globale. Chaque fichier objet porte une **table des symboles** : ceux qu'il définit, avec leur adresse dans son code, et ceux qu'il utilise sans les définir. L'[[Édition de liens|édition de liens]] associe chaque symbole utilisé à sa définition ; un symbole introuvable donne `undefined reference`, un symbole défini deux fois `multiple definition` ([[Règle de la définition unique]]).

```bash
$ nm -C main.o
                 U Point::Point(int, int)      # U : utilisé, non défini ici
0000000000000000 T main                        # T : défini dans ce fichier (code)
```

En C++, plusieurs fonctions peuvent porter le même nom (surcharge, méthodes de classes différentes) : le compilateur encode donc les types des paramètres et la classe dans le nom du symbole (*name mangling*) ; `Point::Point(int, int)` devient par exemple `_ZN5PointC1Eii`. L'option `-C` de `nm` les rend lisibles.

## Dans le cours

Pas nommé : cité dans les compléments de [[5 - Compilation séparée]] (erreur `undefined reference to 'Point::Point(int, int)'`).

Voir aussi : [[Chaîne de compilation]], [[Surcharge d'opérateurs]].

Résumés : [[5 - Compilation séparée]]
