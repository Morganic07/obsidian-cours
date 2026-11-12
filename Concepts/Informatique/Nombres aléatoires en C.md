---
type: concept
tags: [year2, year4]
aliases: ["rand()", "srand()", "srand(time(NULL))"]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"]
maj: 2026-11-12
---

La fonction `rand()`, déclarée dans `stdlib.h`, génère des entiers aléatoires (TP6, tâche 5). Dans le rendu, `srand(time(NULL))` est ajouté car sans lui le nombre est le même à chaque lancement.

Voir aussi : [[Appel fork()]].

## Dans le cours

- [[tp4]] : le nombre secret du jeu (4.3), écrit en dur (77), se tirerait par `srand(time(NULL)); nombre_secret = rand() % 100 + 1;`, entier entre 1 et 100.
- [[tp5]] : même remarque pour le nombre mystère de 5.3 (77 aussi) ; en ajoutant les réponses « plus grand » ou « plus petit », le jeu se résout par [[Recherche dichotomique|recherche dichotomique]].

Résumés (rapprochement, complément hors du cours) : [[4 - TP4]]
