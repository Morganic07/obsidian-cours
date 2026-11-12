---
type: concept
tags: [year4]
aliases: [tabulation (caractère), tab, caractère TAB, "\\t"]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : le caractère de tabulation (TAB, code 9 en [[Code ASCII|ASCII]], écrit `\t` dans une [[Chaîne de caractères|chaîne]] C ou C++) fait avancer le texte jusqu'à la prochaine position de tabulation. À l'écran il ressemble à plusieurs espaces, mais c'est un seul caractère, différent de l'espace (code 32). C'est un [[Espace blanc|espace blanc]], ignoré entre les mots du code par le compilateur.

Il ne compte vraiment que là où un outil le distingue de l'espace : dans un [[Make (logiciel)|Makefile]], chaque ligne de commande doit commencer par une tabulation ; des espaces donnent `*** missing separator.  Stop.` Les éditeurs réglés pour « remplacer les tabulations par des espaces » produisent cette erreur ; la plupart font une exception pour les Makefiles.

## Dans le cours

[[5 - Compilation séparée]] : dans le Makefile, « la ligne commence obligatoirement par une tabulation, pas par des espaces ».

Voir aussi : [[Éditeur de texte]].

Résumés : [[5 - Compilation séparée]]
