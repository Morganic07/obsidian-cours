---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp3.docx|chp3 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 3, méthode du pivot de Gauss.
## Méthode du pivot de Gauss

### Méthode

1. Sélectionner une ligne qui sera le pivot. On la « sanctuarise » : on ne la touche plus.
2. À l'aide de [[Combinaison linéaire|combinaisons linéaires]], éliminer les inconnues une par une pour obtenir un système en cascade ([[Forme échelonnée]]).
3. À la fin, la dernière ligne contient une seule inconnue avec sa valeur. On remonte la cascade pour retrouver une à une les valeurs des autres inconnues.

### Opérations autorisées

([[Opérations élémentaires sur les lignes]])

- Changer l'ordre des lignes : $L_i \leftrightarrow L_j$ ;
- multiplier une équation par un scalaire non nul : $L_i \leftarrow \lambda L_i$, $\lambda \neq 0$ ;
- ajouter à une ligne une combinaison linéaire des autres : $L_i \leftarrow \alpha L_i + \beta L_j$, avec $\alpha \neq 0$ et $j \neq i$ (sinon on perd une équation). [[Erreurs du cours#^e-3-algebre-lineaire|✎]]

N'utiliser que celles-là, sinon on perd de l'information.

Ces opérations sont **réversibles** (on peut revenir au système de départ), donc elles transforment un système en un système **équivalent**, qui a exactement les mêmes solutions. Le **pivot** est le coefficient, non nul, de l'inconnue qu'on élimine dans la ligne choisie ; s'il est nul, on échange d'abord deux lignes. On écrit souvent le calcul sur la seule [[Matrice augmentée|matrice augmentée]] du système (les coefficients, suivis de la colonne du second membre), sans recopier les inconnues. [[Complément hors du cours|ⓘ]]

**Exemple complet** (système carré, solution unique) : [[Complément hors du cours|ⓘ]]
$$\begin{cases} x + y + z = 6 & (L_1) \\ 2x + y - z = 1 & (L_2) \\ x - y + z = 2 & (L_3) \end{cases} \xrightarrow[L_3 \leftarrow L_3 - L_1]{L_2 \leftarrow L_2 - 2L_1} \begin{cases} x + y + z = 6 \\ -y - 3z = -11 \\ -2y = -4 \end{cases} \xrightarrow{L_3 \leftarrow L_3 - 2L_2} \begin{cases} x + y + z = 6 \\ -y - 3z = -11 \\ 6z = 18 \end{cases}$$
En remontant : $z = 3$, puis $-y - 9 = -11$ donne $y = 2$, puis $x = 6 - 2 - 3 = 1$. Solution unique $(1, 2, 3)$, qu'on vérifie dans les trois équations de départ.

Si l'on poursuit l'élimination vers le haut, jusqu'à n'avoir qu'une inconnue par ligne avec des pivots égaux à 1, on obtient la [[Forme échelonnée|forme échelonnée réduite]] : c'est la **méthode de Gauss-Jordan**, qui sert aussi à calculer l'inverse d'une [[Matrice inversible|matrice]]. [[Complément hors du cours|ⓘ]]

Pour $n$ équations à $n$ inconnues, la méthode demande de l'ordre de $n^3$ opérations, ce qui en fait l'algorithme de base des logiciels de calcul. Le principe est très ancien : il figure déjà dans *Les Neuf Chapitres sur l'art mathématique*, ouvrage chinois compilé autour du début de notre ère ; il porte le nom de Gauss, qui l'a employé au début du XIXe siècle. [[Complément hors du cours|ⓘ]]

### Compatibilité

- Un [[Système linéaire|système]] $(S)$ est **compatible** s'il admet au moins une solution ; sinon il est **incompatible**.
- $(S)$ est incompatible si l'on obtient une équation du type $0 = \lambda$ avec $\lambda \neq 0$.
- Quand il y a plus d'inconnues que d'équations, la solution s'écrit en fonction d'une inconnue.

Plus généralement, le nombre $r$ de pivots du système échelonné (après suppression des lignes $0 = 0$) s'appelle le **rang** du système ([[Rang d'une matrice]]). Les inconnues qui portent un pivot sont les **inconnues principales** ; les $n - r$ autres sont des **paramètres** ([[Variable libre|variables libres]]), qu'on fait passer au second membre et qui peuvent prendre n'importe quelle valeur. Un système linéaire a donc soit **aucune** solution, soit **une seule** (compatible et $r = n$), soit **une infinité** (compatible et $r < n$, solutions décrites par $n - r$ paramètres) ; il ne peut jamais en avoir exactement deux. Dans l'exemple ci-dessous, $n = 3$, $r = 2$, et il y a un paramètre, $x_3$. [[Complément hors du cours|ⓘ]]

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

Conséquence, la **structure des solutions** : si $(S)$ est compatible et $s_0$ en est une solution particulière, l'ensemble de ses solutions est $\{s_0 + h \mid h \text{ solution de } (S_0)\}$ (« solution générale = solution particulière + solutions de l'homogène »). Ce n'est pas un sev dès que le second membre est non nul (il ne contient pas $0$), mais un sev « translaté », appelé **sous-espace affine**. Dans l'exemple du cours, $(2 - 8x_3;\ 1 + 5x_3;\ x_3) = (2, 1, 0) + x_3(-8, 5, 1)$ : une droite passant par $(2, 1, 0)$, dirigée par $(-8, 5, 1)$, solution de l'homogène. Le même principe régit les équations différentielles linéaires. [[Complément hors du cours|ⓘ]]

Lien avec le chapitre 2 : l'ensemble des solutions de $(S_0)$ est le [[Espace nul|noyau]] de l'application linéaire $x \mapsto (\text{premiers membres})$ de $\mathbb{R}^n$ dans $\mathbb{R}^p$ ; le [[Théorème du rang|théorème du rang]] donne alors sa dimension, $n - r$. [[Complément hors du cours|ⓘ]]

## Applications aux familles libres et/ou génératrices

Pour une seule équation non triviale, l'ensemble des solutions de l'homogène a pour dimension le nombre d'inconnues moins 1 : 1 inconnue = dimension 0 (point), 2 inconnues = dimension 1 (droite), 3 inconnues = dimension 2 (plan), etc. En général, cette dimension est le nombre d'inconnues moins le rang du système. [[Erreurs du cours#^e-3-algebre-lineaire|✎]] La partie s'arrête sur un « Exemple : » sans contenu.

**Le principe.** Pour des vecteurs $v_1, \dots, v_p$ de $\mathbb{R}^n$ : [[Complément hors du cours|ⓘ]]
- la famille est [[Indépendance linéaire|libre]] si et seulement si le système homogène $\lambda_1 v_1 + \dots + \lambda_p v_p = 0$, d'inconnues $\lambda_1, \dots, \lambda_p$, n'a que la solution nulle, c'est-à-dire si son rang vaut $p$ ;
- elle est [[Espace engendré|génératrice]] de $\mathbb{R}^n$ si et seulement si le système $\lambda_1 v_1 + \dots + \lambda_p v_p = b$ est compatible pour tout $b \in \mathbb{R}^n$, c'est-à-dire si son rang vaut $n$ ;
- elle est une [[Base (algèbre linéaire)|base]] si et seulement si ce système a une solution unique pour tout $b$ : rang $p = n$.

**Exemple** : $v_1 = (1, 1, 0)$, $v_2 = (0, 1, 1)$, $v_3 = (1, 0, 1)$ dans $\mathbb{R}^3$. Le système $\lambda_1 v_1 + \lambda_2 v_2 + \lambda_3 v_3 = 0$ s'écrit $\lambda_1 + \lambda_3 = 0$, $\lambda_1 + \lambda_2 = 0$, $\lambda_2 + \lambda_3 = 0$. Les deux premières donnent $\lambda_3 = -\lambda_1$ et $\lambda_2 = -\lambda_1$, et la troisième $-2\lambda_1 = 0$ : $\lambda_1 = \lambda_2 = \lambda_3 = 0$. La famille est libre ; avec 3 vecteurs en dimension 3, c'est une base de $\mathbb{R}^3$. [[Complément hors du cours|ⓘ]]
