---
type: concept
tags: [year4]
aliases: [instruction break, instruction continue, break et continue, sortie de boucle, fall-through]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.10.c|3.10.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : `break` et `continue` sont deux instructions de rupture de séquence du [[Langage C|C]], reprises par le [[Langage C++|C++]], le [[Langage Java|Java]] et le [[Langage Python|Python]]. Elles modifient le déroulement d'une [[Boucle (programmation)|boucle]] depuis son corps :

- **`break`** termine immédiatement la boucle (`for`, `while`, `do … while`) ou le `switch` le plus proche ; l'exécution reprend à l'instruction qui suit ;
- **`continue`** abandonne le reste de l'itération en cours et passe à la suivante : dans un `while`, on retourne au test ; dans un `for`, l'incrémentation est exécutée avant le test.

```c
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;   // saute les pairs
    if (i > 7) break;           // arrête tout à 9
    printf("%d ", i);           // affiche 1 3 5 7
}
```

**Dans un `switch`** ([[Structure conditionnelle]]), `break` termine chaque `case`. Sans lui, l'exécution « tombe » dans le `case` suivant (*fall-through*) : c'est l'erreur la plus fréquente, que [[GCC]] signale avec `-Wimplicit-fallthrough` (activé par `-Wextra`). Le regroupement voulu de plusieurs valeurs (`case 'o': case 'O':`) utilise justement cette chute. `continue` n'a pas de sens dans un `switch` seul : dans un `switch` placé dans une boucle, il agit sur la boucle.

Précautions :

- dans des [[Boucle imbriquée|boucles imbriquées]], `break` et `continue` n'agissent que sur la boucle la plus intérieure ; pour sortir de plusieurs niveaux, on utilise un [[Drapeau (programmation)|drapeau]] testé par chaque boucle, ou l'on place les boucles dans une fonction et l'on en sort par `return` ([[Instruction return]]) ;
- après un `break`, on ne sait plus pourquoi la boucle s'est arrêtée (condition devenue fausse ou sortie anticipée) : un drapeau ou un test sur le [[Compteur (programmation)|compteur]] le dit ;
- abusés, ils rendent le flot de contrôle difficile à suivre ; une condition de boucle bien écrite les rend souvent inutiles ([[Théorème de Böhm-Jacopini]] : séquence, choix et boucle suffisent).

## Dans le cours

- [[2 - structures code]] : `break` termine chaque `case` du `switch`, et le chapitre explique la chute dans le `case` suivant ; un complément y présente `break` et `continue` dans les boucles.
- [[tp3]] : `break` à la fin de chaque `case` des programmes 3.10 à 3.12 (chiffre, magnitude, touche du pavé numérique).
- [[tp4]] : `break` arrête le jeu du nombre secret (4.3) dès que le nombre est trouvé.
- [[4 - Cours complet]] : l'oubli d'un `break` à la fin d'un `case` est présenté comme l'erreur la plus fréquente.

Voir aussi : [[Boucle (programmation)]], [[Structure conditionnelle]], [[Table de sauts]].
