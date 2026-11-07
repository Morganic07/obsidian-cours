---
type: concept
tags: [year2]
aliases: [online core, offline core, On-line CPU(s) list, cœur en ligne, cœur hors ligne]
sources: ["[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]", "[[Raw/Year 2/Operating System/DM/Operating Systems - Semester report.docx|Operating Systems - Semester report]]"]
maj: 2026-11-07
---

Un cœur en ligne est actif. Par défaut, tous les cœurs le sont, et le cœur par défaut est le 0. On met le cœur X hors ligne avec `echo 0 | sudo tee /sys/devices/system/cpu/cpuX/online`, et en ligne avec `echo 1`. Le rapport vérifie la sortie `0` avec `cat online`.

Notion parente : [[Cœur de processeur]]. Voir aussi : [[Commande lscpu]], [[Commande tee]], [[Commande nproc]].

## À vérifier

- Le script de la tâche 7 remet aussi le cœur 0 en ligne, contrairement à l'énoncé (signalé par le résumé).

Résumés (rapprochement, complément hors du cours) : [[1 - OS (résumé)]]
