---
type: concept
tags: [year2]
aliases: [device controller, contrôleurs de périphériques, disk controller, USB controller]
sources: ["[[1 - OS|OS - chp 1]]"]
maj: 2026-11-06
---

Chaque périphérique est relié à son contrôleur (un adaptateur pour l'affichage), qui gère la communication avec le CPU. Chaque périphérique a un buffer, un driver et un contrôleur. Une fois l'opération finie, le contrôleur envoie une [[Interruption]] au CPU.

Exemple du cours : le clavier contient un petit processeur local qui convertit la touche en ASCII, puis en binaire.

Voir aussi : [[Pilote de périphérique]], [[Tampon (buffer)]], [[Interruption]], [[Accès direct à la mémoire]].

Résumés : [[1 - OS]]
