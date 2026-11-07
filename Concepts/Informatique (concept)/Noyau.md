---
type: concept
tags:
  - year2
aliases:
  - kernel
  - noyau du système
  - Linux kernel
  - noyau Linux
matieres:
  - Operating System
sources:
  - "[[1 - OS (résumé)|OS - chp 1]]"
  - "[[3 - OS (résumé)|OS - chp 3]]"
  - "[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
maj: 2026-11-06
---

Cœur du [[Système d'exploitation]] (« le cœur de l'OS »). Les processus s'exécutent au-dessus du noyau, qui lui-même repose sur le matériel. En environnement virtuel, chaque machine virtuelle a son propre noyau (voir [[Machine virtuelle]]).

**[[Linux]]** désigne ici le noyau ; le mot nomme aussi la famille de systèmes libres fondés sur lui. Pour obtenir un système complet, il faut y ajouter d'autres composants (système de fenêtres, environnement de bureau, applications) : c'est le rôle d'une [[Distribution Linux]]. Le cours précise que `uname -r` donne la version du noyau ([[Commande uname]]). Le noyau et l'initrd se trouvent dans `/boot` ([[4 - OS (résumé)]]).

**À corriger avant un examen.** La note du chapitre 3 affirme que macOS est construit sur le noyau Linux. C'est faux : macOS repose sur un noyau d'origine BSD/Mach (complément).

Notion parente : [[Système d'exploitation]].

Liens : [[Distribution Linux]], [[Appel système]]

Résumés : [[1 - OS (résumé)]], [[3 - OS (résumé)]], [[4 - OS (résumé)]]
