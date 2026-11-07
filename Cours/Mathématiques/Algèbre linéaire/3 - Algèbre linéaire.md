---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]]"
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 3, méthode du pivot de Gauss. En cas d'écart, le cours et ses images font foi.

## Méthode du pivot de Gauss

### Méthode

1. Sélectionner une ligne qui sera le pivot. On la « sanctuarise » : on ne la touche plus.
2. À l'aide de [[Combinaison linéaire|combinaisons linéaires]], éliminer les inconnues une par une pour obtenir un système en cascade ([[Forme échelonnée]]).
3. À la fin, la dernière ligne contient une seule inconnue avec sa valeur. On remonte la cascade pour retrouver une à une les valeurs des autres inconnues.

### Opérations autorisées

([[Opérations élémentaires sur les lignes]])

- Changer l'ordre des lignes : $L_i \leftrightarrow L_j$ ;
- multiplier une équation par un scalaire non nul : $L_i \leftarrow \lambda L_i$, $\lambda \neq 0$ ;
- ajouter à une ligne une combinaison linéaire des autres : $L_i \leftarrow \alpha L_i + \beta L_j$.

N'utiliser que celles-là, sinon on perd de l'information.

### Compatibilité

- Un [[Système linéaire|système]] $(S)$ est **compatible** s'il admet au moins une solution ; sinon il est **incompatible**.
- $(S)$ est incompatible si l'on obtient une équation du type $0 = \lambda$ avec $\lambda \neq 0$.
- Quand il y a plus d'inconnues que d'équations, la solution s'écrit en fonction d'une inconnue.

**Exemple du cours** (images de formules, recopiées d'après leur transcription). Le système échelonné
$$\begin{cases} x_1 + x_2 + 3x_3 = 3 \\ x_2 - 5x_3 = 1 \end{cases}$$
donne, en remontant :
$$\iff \begin{cases} x_1 = 3 - x_2 - 3x_3 = 2 - 8x_3 \\ x_2 = 1 + 5x_3 \\ x_3 \in \mathbb{R} \end{cases}$$
L'ensemble des solutions est $\{(2 - 8x_3;\ 1 + 5x_3;\ x_3) : x_3 \in \mathbb{R}\}$.

## Cas des systèmes linéaires homogènes

- $(S)$ est un [[Système linéaire homogène|système homogène]] si son second membre est nul.
- Un système homogène est **toujours compatible** : il admet le $n$-uplet $(0, \dots, 0)$ comme solution.
- L'ensemble des solutions d'un système homogène à $p$ équations et $n$ inconnues est un **sev de $\mathbb{R}^n$**.
- Un système homogène avec plus d'inconnues que d'équations admet des solutions non nulles.
- Si $s_1$ et $s_2$ sont solutions d'un système linéaire $(S)$, alors $s_1 - s_2$ est solution du système homogène associé $(S_0)$.

## Applications aux familles libres et/ou génératrices

Le cours note : 1 inconnue = dimension 0 (point), 2 inconnues = dimension 1 (droite), 3 inconnues = dimension 2 (plan), etc. La partie s'arrête sur un « Exemple : » sans contenu.

## Erreurs du cours

- [[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]] écrit l'opération « $L_i \leftarrow \alpha L_i + \beta L_j$ » sans condition ; il faut « $L_i \leftarrow \alpha L_i + \beta L_j$, avec $\alpha \neq 0$ et $j \neq i$ », sinon on perd une équation.
- Le cours écrit « 1 inconnue = dim 0 (point), 2 inconnues = dim 1 (droite), 3 inconnues = dim 2 (plan) » ; cela ne vaut que pour une seule équation non triviale : en général, la dimension de l'ensemble des solutions d'un système homogène est le nombre d'inconnues moins le rang du système.
