---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 3, méthode du pivot de Gauss. En cas d'écart, le cours et ses images font foi.

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Opération $L_i \leftarrow \alpha L_i + \beta L_j$** : il faut préciser $\alpha \neq 0$, sinon on perd une équation (complément).
2. **« 1 inconnue = dim 0, 2 inconnues = dim 1, 3 inconnues = dim 2 »** : valable pour une seule équation non triviale, pas en général (complément).
3. **« En fonction d'une inconnue »** : il peut y en avoir plusieurs, selon le nombre de variables libres (complément, l'exemple du cours n'en a qu'une).
