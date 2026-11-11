---
type: concept
tags: [year4]
aliases: [ninja build, Ninja build system]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : Ninja est un outil de construction qui joue le même rôle que [[Make (logiciel)|make]] : il ne recompile que les fichiers dont une dépendance a changé. Son fichier `build.ninja` n'est pas fait pour être écrit à la main, mais généré par un outil comme [[CMake]] (`cmake -G Ninja`). Conçu pour la rapidité (il a été écrit pour compiler Chromium), il lance par défaut plusieurs compilations en parallèle.

## Dans le cours

Pas nommé : cité dans les compléments de [[5 - Compilation séparée]].

Voir aussi : [[Compilation séparée]].

Résumés : [[5 - Compilation séparée]]
