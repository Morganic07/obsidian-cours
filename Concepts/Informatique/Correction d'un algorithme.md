---
type: concept
tags: [year1]
aliases: [algorithme correct, algorithme incorrect, correction partielle, correction totale, correctness]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-08
---

Un algorithme est correct si, pour chaque instance en entrée, il se termine avec la bonne sortie. Un algorithme incorrect risque de ne pas se terminer ou de donner une mauvaise réponse ; il peut quand même servir si son taux d'erreur est contrôlé.

Exemple du coût d'une erreur : le premier vol d'Ariane 5 (1996), avec un programme d'Ariane 4 non reconfiguré.

## Compléments (complément, hors du cours)

- **Correction partielle et correction totale** : un algorithme est partiellement correct si, *lorsqu'il s'arrête*, sa sortie est juste ; il est totalement correct s'il est partiellement correct et qu'il se termine toujours. La correction partielle d'une boucle se prouve par un [[Invariant de boucle|invariant de boucle]], la [[Terminaison d'un algorithme|terminaison]] par un variant (quantité entière positive qui décroît strictement à chaque tour).
- **Cause de l'échec d'Ariane 5** (vol 501, 4 juin 1996) : dans le logiciel des centrales inertielles, repris d'Ariane 4, la conversion d'un flottant 64 bits en entier signé 16 bits a débordé, la valeur étant plus grande sur la trajectoire d'Ariane 5 ; l'erreur n'était pas protégée, les deux centrales se sont arrêtées et le lanceur a été détruit environ 40 secondes après le décollage (rapport de la commission d'enquête, juillet 1996).

Notion parente : [[Algorithme]]. Voir aussi : [[Terminaison d'un algorithme]], [[Invariant de boucle]], [[Algorithme d'approximation]].

Résumés : [[0 - diapo prof]]
