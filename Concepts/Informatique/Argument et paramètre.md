---
type: concept
tags: [year4]
aliases: [argument, arguments, paramètre formel, paramètre effectif, argument effectif, parameter]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : les entrées d'une partie de programme (une [[Fonction et procédure|fonction]]) s'appellent des **arguments** (ou parfois paramètres), ses sorties des **résultats**.

Complément, hors du cours : on distingue le **paramètre** (formel), variable nommée dans la définition (`x` dans `int carre(int x)`), et l'**argument** (effectif), valeur fournie à l'appel (`2` dans `carre(2)`). À l'appel, l'argument initialise le paramètre : par copie ([[Passage par valeur]]), par adresse ([[Pointeur et adresse mémoire|pointeur]]) ou par [[Référence (C++)|référence]]. Le nombre et le type des arguments doivent correspondre à la déclaration.

## Dans le cours

[[4 - Cours complet]] montre les erreurs d'[[Appel de fonction|appel]] (argument manquant, en trop, de mauvais type) et pose une règle d'ordre : le paramètre principal d'abord, puis les données secondaires.

Voir aussi : [[Passage de paramètres]].

Résumés : [[4 - Cours complet]]
