---
type: concept
tags: [year4]
aliases: [off-by-one, off-by-one error, erreur du poteau de clôture, fencepost error, erreur de borne de boucle]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp4/4.1.c|4.1.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une erreur de décalage d'une unité (*off-by-one error*) est un [[Bogue (informatique)|bogue]] où une [[Boucle (programmation)|boucle]] ou un indice va une fois de trop ou une fois de moins. Formes typiques :

- `i <= n` au lieu de `i < n` (ou l'inverse) dans la condition d'une boucle ;
- un [[Tableau (programmation)|tableau]] de `n` cases parcouru jusqu'à l'indice `n`, alors que ses indices vont de `0` à `n - 1` ;
- une [[Chaîne de caractères|chaîne]] de `n` lettres rangée dans un tableau de `n` cases, sans place pour le `'\0'` final.

Elle vient souvent de la confusion entre le nombre d'éléments et le nombre d'intervalles, d'où son autre nom d'**erreur du poteau de clôture** : pour une clôture de 10 m avec un poteau tous les mètres, il faut 11 poteaux, pas 10. De même, l'intervalle d'entiers $[a, b]$ contient $b - a + 1$ éléments.

Le [[Langage C|C]] fixe un idiome qui l'évite : indices de `0` à `n - 1` et intervalles semi-ouverts $[0, n[$, écrits `for (i = 0; i < n; i++)`, qui tourne exactement `n` fois (`n - 0` tours). Sortir d'une case d'un tableau est un [[Dépassement de tampon|dépassement de tampon]], [[Comportement indéfini|comportement indéfini]] que le C ne signale pas ; [[AddressSanitizer]] le détecte à l'exécution. Pour s'en prémunir : vérifier les deux bornes extrêmes à la main (premier et dernier tour), écrire des [[Test unitaire|tests]] sur les cas limites (tableau vide, un seul élément), et en [[Langage C++|C++]] préférer la boucle `for (int v : tab)` qui ne manipule pas d'indice.

## Dans le cours

- [[tp4]] : le programme 4.1 affiche 100 nombres avec `i < 100`, le programme 4.2 en affiche 101 avec `n <= 100` ; la fiche rappelle que `for (i = 0; i <= N; i++)` tourne N + 1 fois.

Voir aussi : [[Boucle (programmation)]], [[Compteur (programmation)]], [[Invariant de boucle]], [[Dépassement de tampon]].
