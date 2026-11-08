---
type: concept
tags: [year2]
aliases: [online core, offline core, On-line CPU(s) list, cœur en ligne, cœur hors ligne]
sources: ["[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]", "[[Raw/Year 2/Operating System/DM/Operating Systems - Semester report.docx|Operating Systems - Semester report]]"]
maj: 2026-11-08
---

Un cœur en ligne est actif. Par défaut, tous les cœurs le sont, et le cœur par défaut est le 0. On met le cœur X hors ligne avec `echo 0 | sudo tee /sys/devices/system/cpu/cpuX/online`, et en ligne avec `echo 1`. Le rapport vérifie la sortie `0` avec `cat online`.

Pour traiter tous les cœurs sauf le cœur par défaut (tâches 6 et 7 du DM), la boucle de 0 à `nproc` - 1 exclut ce cœur par le test `if [ $i -ne $default_core ]`. [[Erreurs du cours#^e-cur-en-ligne-et-hors-ligne|✎]]

Notion parente : [[Cœur de processeur]]. Voir aussi : [[Commande lscpu]], [[Commande tee]], [[Commande nproc]].

Résumés (rapprochement, complément hors du cours) : [[1 - OS]]
