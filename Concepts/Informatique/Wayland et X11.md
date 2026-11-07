---
type: concept
tags: [year2]
aliases: [Wayland, XWayland, X11]
matieres: [Operating System]
sources: ["[[TP1 (résumé)|TP1]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : X11 (X Window System) et Wayland sont deux systèmes de fenêtrage pour Linux et Unix : ils gèrent l'affichage des fenêtres des applications et transmettent à celles-ci les entrées du clavier et de la souris. X11, datant des années 1980, repose sur un serveur X distinct auquel les applications envoient leurs ordres de dessin ; Wayland, plus récent, est un protocole plus simple où le compositeur de l'[[Environnement de bureau|environnement de bureau]] fait directement office de serveur d'affichage. XWayland est un serveur X qui tourne sous Wayland pour faire fonctionner les anciennes applications X11 ; c'est pourquoi des outils propres à X11, comme `setxkbmap`, n'y ont qu'un effet limité.

## Dans le cours

Notion seulement rencontrée dans le rendu de l'étudiante au TP1, sans explication d'un cours : `setxkbmap` y avertit « Running setxkbmap against an XWayland server », et l'étudiante tente de passer de Wayland à X11 via `/etc/gdm3/custom.conf`, absent de sa machine.

Notion parente : [[Environnement de bureau]]. Voir aussi : [[Disposition du clavier]].

Résumés : [[TP1 (résumé)]]
