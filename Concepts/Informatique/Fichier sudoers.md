---
type: concept
tags: [year2]
aliases: [sudoers, visudo, NOPASSWD, timestamp_timeout, sudo sans mot de passe, sudo passwordless]
matieres: [Operating System]
sources: ["[[cours TP1]]", ".raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf"]
maj: 2026-11-06
---

Le fichier sudoers s'ouvre avec `sudo visudo` (tâche 2 du TP6).

- Pour supprimer la demande de mot de passe : ajouter en fin de fichier `username ALL=(ALL) NOPASSWD:ALL`.
- Pour régler le délai avant une nouvelle demande : `Defaults timestamp_timeout=15`.

Notion parente : [[Commande sudo]].

## À vérifier

- Incohérence dans l'image d'origine : 15 minutes dans le texte, 30 minutes dans la parenthèse (signalée par la transcription et le résumé).

Résumés : [[séance TP1 (résumé)]], [[TP1 (résumé)]], [[TP6-Assignment (résumé)]], [[UNIX Commands - Semester report (résumé)]]
