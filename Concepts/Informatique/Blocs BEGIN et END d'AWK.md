---
type: concept
tags:
  - year2
aliases:
  - BEGIN block
  - END block
  - bloc BEGIN
  - bloc END
sources:
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[5 - TP5|Cours TP5]]"
maj: 2026-11-07
---

En [[AWK]], le bloc `BEGIN` s'exécute avant la lecture de toute ligne : initialiser des variables, afficher un en-tête, fixer `FS`. Le bloc `END` s'exécute après le traitement de toutes les lignes : bilans, calculs finaux.

Exemple du TP5 : en-tête « The list of manufacturers and the car powers they produced », puis fin « The file is finished. ».

Notion parente : [[AWK]]. Voir aussi : [[Variables intégrées d'AWK]].

## Erreurs du cours

- [[5 - TP5|Cours TP5]] (rendu, question h) écrit « {print $0} » ; il faut « {print $1, $2, $4} » (ou les colonnes voulues) : la question demande l'ID, le constructeur et la puissance, et `$0` affiche toute la ligne, modèle compris.

Résumés : [[5 - TP5]]
