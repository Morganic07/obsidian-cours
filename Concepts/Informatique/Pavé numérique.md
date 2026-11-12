---
type: concept
tags: [year4]
aliases: [numeric keypad, numpad, pavé num, verrouillage numérique]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.12.c|3.12.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : le pavé numérique est le bloc de touches, en général à droite d'un clavier d'ordinateur de bureau, disposé comme une calculatrice : 7, 8, 9 sur la rangée du haut, 4, 5, 6 au milieu, 1, 2, 3 en bas, 0 sur la dernière rangée, avec les opérateurs (`/`, `*`, `-`, `+`), le séparateur décimal et une touche Entrée. Il accélère la saisie de chiffres. Les claviers de téléphone suivent la disposition inverse (1, 2, 3 en haut).

La touche **Verr Num** (*Num Lock*) en bascule le rôle. Verrouillage désactivé, les touches servent à la navigation : 8, 2, 4 et 6 deviennent les flèches haut, bas, gauche et droite (la croix du milieu du pavé), 7 et 1 Début et Fin, 9 et 3 Page précédente et Page suivante. Cette disposition en croix explique l'usage de 8, 2, 4, 6 pour les déplacements dans les anciens jeux en mode texte, comme les flèches ou ZQSD (WASD sur un clavier QWERTY, voir [[Disposition du clavier]]) aujourd'hui.

Pour un programme, la touche enfoncée n'arrive que comme un caractère (`'8'`) ou un nombre (`8`) lu par `scanf` ; c'est la convention du programme qui lui donne un sens de direction.

## Dans le cours

- [[tp3]] : le programme 3.12 traduit avec un `switch` les chiffres 8, 2, 4 et 6 en nord, sud, ouest et est, d'après la disposition du pavé numérique.

Voir aussi : [[Disposition du clavier]], [[Jeu vidéo]], [[Structure conditionnelle]].
