---
type: concept
tags:
  - year2
aliases:
  - keyboard layout
  - keyboard map
  - setxkbmap
  - XKBLAYOUT
  - /etc/default/keyboard
matieres:
  - Operating System
sources:
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
maj: 2026-11-07
---

Changement temporaire, perdu au redémarrage : `setxkbmap us`. Changement permanent : modifier la ligne `XKBLAYOUT="us"` ou `"fr"` dans `/etc/default/keyboard`. Au TP1, `setxkbmap` manque et s'installe avec le paquet `x11-xkb-utils`.

Voir aussi : [[Wayland et X11]].

Résumés (rapprochement, complément hors du cours) : [[2 - tree]]
