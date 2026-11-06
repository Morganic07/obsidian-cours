---
type: concept
tags: [year2]
aliases: [buffer, buffers, tampon mémoire]
matieres: [Operating System]
sources: ["[[OS - chp 1]]"]
maj: 2026-11-06
---

Petite mémoire intermédiaire propre à chaque périphérique, qui stocke temporairement les données avant leur transfert vers le CPU ou vers le périphérique. Le CPU déplace les données entre la RAM et les buffers locaux des contrôleurs. Les buffers servent surtout aux entrées-sorties, pour que les périphériques lents ne ralentissent pas le CPU ; les opérations internes entre CPU et RAM n'y passent pas.

Notion parente : [[Contrôleur de périphérique]]. Voir aussi : [[Mémoire vive]], [[Opération d'entrée-sortie]].

## À vérifier

- Le cours écrit « le buffer se vide dès que la tâche est accomplie » : formulation approximative relevée par le résumé.

Résumés : [[OS - chp 1 (résumé)]]
