---
type: concept
tags: [year2]
aliases: [BEGIN block, END block, bloc BEGIN, bloc END]
sources: ["[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]", "[[Séance TP5 (résumé)|Cours TP5]]"]
maj: 2026-11-06
---

En [[AWK]], le bloc `BEGIN` s'exécute avant la lecture de toute ligne : initialiser des variables, afficher un en-tête, fixer `FS`. Le bloc `END` s'exécute après le traitement de toutes les lignes : bilans, calculs finaux.

Exemple du TP5 : en-tête « The list of manufacturers and the car powers they produced », puis fin « The file is finished. ».

Notion parente : [[AWK]]. Voir aussi : [[Variables intégrées d'AWK]].

## À vérifier

- Question h : la commande du rendu affiche `$0` au lieu de l'ID, du constructeur et de la puissance (signalé par les résumés).

Résumés : [[TP5-AWK Command (résumé)]], [[Séance TP5 (résumé)]]
