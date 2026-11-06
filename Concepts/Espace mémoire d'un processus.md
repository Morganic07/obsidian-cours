---
type: concept
aliases: [process in memory, memory layout, text section, data section, section de texte, section de données]
sources: ["[[OS - chp7]]"]
maj: 2026-11-06
---

En mémoire, un [[Processus]] contient :

- la section **text** : le code ;
- la **pile** (stack) : variables locales, adresses de retour, paramètres ;
- la section **data** : variables globales ;
- le **tas** (heap) : mémoire allouée dynamiquement à l'exécution.

Le schéma du cours va de 0 à max : text, data, heap, zone libre, stack. La pile et le tas peuvent grandir ou rétrécir. Exemple en C avec `int x;`, `int y = 15;`, un `malloc`, et `argc`, `argv` tout en haut.

Notion parente : [[Processus]]. Voir aussi : [[Pointeur et adresse mémoire]].

## À vérifier

- Le schéma écrit « agrv » pour `argv` (faute sans conséquence).

Résumés : [[OS - chp7 (résumé)]]
