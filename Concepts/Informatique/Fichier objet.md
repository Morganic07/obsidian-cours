---
type: concept
tags: [year4]
aliases: [object file, fichier .o, code objet, object code]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : `g++ -c Point.cpp` compile un [[Fichier source|fichier source]] sans faire l'[[Édition de liens|édition de liens]] et produit le fichier objet `Point.o`. L'[[Exécutable|exécutable]] est ensuite assemblé à partir des fichiers objets : `g++ Point.o Segment.o main.o -o programme`.

## Compléments (hors du cours)

- Un fichier objet contient le [[Code machine|code machine]] d'une seule [[Unité de compilation|unité de compilation]], encore incomplet : les appels à des fonctions définies ailleurs y restent des trous, à remplir par l'éditeur de liens. Il porte une **table des [[Symbole (édition de liens)|symboles]]** : les noms qu'il définit et ceux qu'il utilise sans les définir (`nm Point.o` l'affiche).
- Format : ELF sous [[Linux]], Mach-O sous macOS, COFF/PE sous Windows (`.obj`).
- Plusieurs `.o` peuvent être regroupés en [[Bibliothèque statique|bibliothèque statique]] (`.a`) ; une [[Bibliothèque partagée|bibliothèque partagée]] (`.so`) est liée au chargement.

Voir aussi : [[Chaîne de compilation]], [[Compilation séparée]], [[GCC]].

## Dans [[4 - Cours complet]]

Le fichier objet est le produit du compilateur (`.o` sous Unix/Linux, `.obj` sous Windows) ; il n'est pas portable d'un système à l'autre. La question 9 demande sa différence avec un fichier source.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
