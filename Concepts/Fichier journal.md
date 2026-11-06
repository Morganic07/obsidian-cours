---
type: concept
aliases: [log files, log file, fichiers journaux, auth.log]
matieres: [Operating System]
sources: ["[[raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4]]", "[[TP1]]"]
maj: 2026-11-06
---

Le répertoire `/var` contient les données variables, comme les journaux et les fichiers de spool. Au TP1, l'historique de `sudo` se trouve dans `/var/log/auth.log` ; faute de ce fichier, l'étudiante utilise `sudo journalctl _COMM=sudo` ([[Commande journalctl]]).

Notion parente : [[Arborescence des répertoires Linux]].

Résumés : [[OS - chp 4 (résumé)]], [[TP1 (résumé)]]
