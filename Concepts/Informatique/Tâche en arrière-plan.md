---
type: concept
tags: [year2]
aliases: [background job, background task, tâche de fond, tâches de fond, background and job control, job control, commandes en arrière-plan]
sources: ["[[raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands]]", "[[Cours TP2]]", "[[raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2)]]"]
maj: 2026-11-06
---

`&` lance une commande en arrière-plan (`cp file1.txt ./backup.txt &`, `./time.sh &`) ; `;` sépare des commandes exécutées à la suite (`mkdir new_folder; cd new_folder`). On suit les tâches de fond avec `jobs` et on les ramène au premier plan avec `fg`.

Notion parente : [[Méta-caractère]]. Voir aussi : [[Commande jobs]], [[Commandes fg et bg]], [[Commande kill]], [[Processus]].

Résumés : [[Copy of TP2-Commands (résumé)]], [[Cours TP2 (résumé)]], [[TP3-Commands (2) (résumé)]]
