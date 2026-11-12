---
type: concept
tags: [year4]
aliases: [extension de fichier, file extension, extensions de fichier]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : suffixe du nom d'un fichier, après le dernier point, qui indique par convention son type : `.cpp`, `.h`, `.o`, `.exe`. Sous [[Microsoft Windows|Windows]], il détermine le programme d'ouverture et le caractère exécutable ; sous [[Linux]], ce n'est qu'une convention : l'exécutabilité vient des [[Permissions Unix|permissions]], et le contenu se reconnaît à ses premiers octets (commande `file`). Les outils de compilation, eux, s'y fient : g++ traite `.c` comme du C et `.cpp` comme du C++.

## Dans le cours

[[4 - Cours complet]] donne les extensions de la chaîne de fabrication : `.cpp` ou `.cc` (source C++), `.c` (source C), `.h` (en-tête), `.o` ou `.obj` (objet), `.exe` ou aucune (exécutable), `.so` ou `.dll` (bibliothèque dynamique).

Résumés : [[4 - Cours complet]]
