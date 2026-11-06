---
type: concept
tags: [year2]
aliases: [multiprocess architecture, browser process, renderer process, plug-in process, processus de rendu]
sources: ["[[OS - chp7]]"]
maj: 2026-11-06
---

Beaucoup de navigateurs tournent en un seul processus : un site qui pose problème fait alors tomber tout le navigateur. Chrome utilise trois types de processus :

- **browser** : interface, entrées-sorties disque et réseau ;
- **renderer** : rendu des pages (HTML, JavaScript), un par site ouvert, dans une *sandbox* qui limite les entrées-sorties et l'effet des failles ;
- **plug-in** : un par type de plug-in.

Notion parente : [[Processus]].

Résumés : [[OS - chp7 (résumé)]]
