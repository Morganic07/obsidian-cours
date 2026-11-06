---
type: concept
aliases: [pointer arithmetic]
sources: ["[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

Ajouter 1 à une adresse la décale de la taille du type pointé : `effectifs + i` est l'adresse de la case `i`, et `t[i]` équivaut à `*(t + i)`. Pour un `unsigned char *`, `pb++` avance d'un octet. On peut ajouter ou retrancher un entier à un pointeur.

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Tableau (programmation)]], [[Notation hexadécimale]].

## À vérifier

- Le nom « arithmétique des pointeurs » n'est pas dans le cours.
- Le cours donne la taille d'un entier comme « 8 octets sur système 64 bits » : à corriger avant un examen (relevé du résumé, image 13 ouverte).

Résumés : [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
