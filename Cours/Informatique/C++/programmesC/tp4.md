---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.1.c|4.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.2.c|4.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.3.c|4.3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.4.c|4.4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.5.c|4.5.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.6.c|4.6.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.7.c|4.7.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.8.c|4.8.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp4/4.9.c|4.9.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 4 de [[Langage C|C]] (dossier `programmes C/tp4`, 9 fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils portent sur la [[Boucle (programmation)|boucle]] `for`, section 4 de [[2 - structures code]] : [[Compteur (programmation)|compteurs]], sortie anticipée avec `break`, [[Accumulateur (programmation)|accumulateurs]], [[Suite numérique|suites]] définies par récurrence, boucles imbriquées pour dessiner des motifs ; 4.4 introduit des [[Fonction et procédure|fonctions]] (section 7 du même chapitre). Les [[Structure conditionnelle|conditions]] viennent du TP 3 ([[tp3]]) et les [[Fonctions printf et scanf|fonctions `printf` et `scanf`]] de [[1 - basiques]]. Les fichiers n'ont pas de commentaires : l'énoncé est reconstitué d'après le code. Les neuf programmes compilent avec [[GCC]] (`gcc -std=c17 -Wall -Wextra`) et donnent le résultat attendu ; aucun n'a demandé de correction.

## 4.1.c

D'après le code, l'exercice demande d'afficher les nombres de 0 à 99, un par ligne.

```c
#include <stdio.h>

int main(){
    int i;

    for (i=0 ; i<100 ; i++){
        printf("%d\n", i);
    }

    return 0;
}
```

Les trois éléments du `for` : initialisation `i=0` (une fois, avant la boucle), condition `i<100` (testée avant chaque tour avec un [[Opérateur de comparaison|opérateur de comparaison]]), incrémentation `i++` (après chaque tour, avec l'[[Opérateur d'incrémentation|opérateur d'incrémentation]]). Le corps s'exécute 100 fois, pour `i` de 0 à 99 ; après la boucle, `i` vaut 100. Sortie : 100 lignes, de `0` à `99`.

La forme `for (i = 0; i < N; i++)` est l'idiome du C pour « répéter N fois » : elle commence à 0 comme les indices d'un [[Tableau (programmation)|tableau]], et `N - 0` donne directement le nombre de tours. Se tromper d'une unité sur une borne (`<=` au lieu de `<`) est l'[[Erreur de décalage d'une unité|erreur de décalage d'une unité]] (*off-by-one*), la plus fréquente avec les boucles. [[Complément hors du cours|ⓘ]]

## 4.2.c

D'après le code, l'exercice demande d'afficher un compte à rebours de 100 à 0.

```c
#include <stdio.h>

int main(){

    int n;

    for (n=0; n<=100; n++){
        printf("%d\n", 100-n);
    }

    return 0;
}
```

La boucle monte de 0 à 100 et affiche l'[[Expression (programmation)|expression]] `100-n`, qui descend de 100 à 0. Avec `<=`, le corps s'exécute 101 fois : de 100 à 0 inclus, il y a 101 nombres. Sortie : 101 lignes, de `100` à `0`.

On peut aussi faire descendre le compteur : `for (n = 100; n >= 0; n--)`. Avec un compteur `unsigned`, cette boucle ne s'arrêterait jamais, car un non-signé est toujours $\geq 0$ et passe de 0 à sa valeur maximale ; c'est une [[1 - basiques#Boucle infinie|boucle infinie]], qui pose un problème de [[Terminaison d'un algorithme|terminaison]]. [[Complément hors du cours|ⓘ]]

## 4.3.c

D'après le code, l'exercice demande de programmer le jeu du nombre secret : l'utilisatrice a 5 essais pour trouver 77, et le programme répond « plus grand » ou « plus petit ».

```c
#include <stdio.h>

int main(){

    int nombre_secret = 77;
    int guess;

    for (int n=1; n<=5; n++){
        printf("Entrez un nombre : ");
        scanf("%d", &guess);

        if (guess == nombre_secret)
        {
            printf("Bravo ! Vous avez trouvé le nombre secret.\n");
            break;
        }

        else if (guess<nombre_secret) printf("Le nombre secret est plus grand \n");

        else if (guess>nombre_secret) printf("Plus petit \n");

    }

    printf("fin du programme (deviné ou 5 tentatives)");

    return 0;
}
```

Le `for` limite le nombre d'essais à 5 ; `break` en sort dès que le nombre est trouvé ([[Instructions break et continue]]), et l'exécution reprend après la boucle. Le compteur `n`, déclaré dans le `for`, n'existe que dans la boucle ([[Portée d'une variable|portée]]). Les `if` sans accolades ne contrôlent qu'une [[Instruction (programmation)|instruction]] (voir [[1 - basiques#Pas besoin d'accolades pour une seule instruction]]). Avec `50 90 77` : « plus grand », « Plus petit », « Bravo ! » puis le message de fin ; avec cinq essais trop petits, cinq « plus grand » puis le message de fin.

Le dernier test `else if (guess>nombre_secret)` est forcément vrai quand on y arrive : un `else` suffit. Pour savoir après la boucle si le nombre a été trouvé, on garde un [[Booléen|booléen]] `trouve` (`int trouve = 0;`, mis à 1 avant le `break`), ou on teste `n <= 5`, à condition d'avoir déclaré `n` avant la boucle. [[Complément hors du cours|ⓘ]]

La stratégie optimale est la [[Recherche dichotomique|recherche dichotomique]] : proposer le milieu de l'intervalle restant, qui est divisé par deux à chaque essai. Avec $k$ essais, on distingue au plus $2^k - 1$ valeurs : 5 essais suffisent pour un nombre entre 1 et 31, et il en faut 7 entre 1 et 100 ($\log_2 100 \approx 6{,}6$). Un nombre secret écrit en dur (un [[Nombre magique (programmation)|nombre magique]]) se remplace par un tirage : `srand(time(NULL)); nombre_secret = rand() % 100 + 1;` (voir [[Nombres aléatoires en C]]). [[Complément hors du cours|ⓘ]]

Le message `Entrez un nombre : ` n'a pas de `\n` : la [[Flux standard|sortie standard]] étant gardée en [[Tampon (buffer)|tampon]] ligne par ligne vers un terminal, la norme ne garantit pas qu'il s'affiche avant la saisie ; `fflush(stdout);` après le `printf` le force. [[Complément hors du cours|ⓘ]]

## 4.4.c

D'après le code, l'exercice demande d'afficher les nombres pairs de 0 à 100 de deux façons, et de laisser l'utilisatrice choisir l'algorithme.

```c
#include <stdio.h>

int algo1(){

    for (int n=0; n<=100; n++){

        if (n%2==0) printf("%d\n", n);
    }

    return 0;
}

int algo2(){

    for (int n=0; n<=100; n+=2) printf("%d\n", n);

    return 0;
}

int main(){

    int nombre = 101;
    int algo;

    printf("algo 1 ou 2 ? \n");
    scanf("%d", &algo);

    if (algo==1) algo1();

    else if (algo ==2) algo2();

    return 0;
}
```

`algo1` parcourt tous les entiers et filtre les pairs avec le modulo ([[Parité d'un entier|parité]], [[Opérateurs arithmétiques|opérateur `%`]]) ; `algo2` avance de 2 en 2 grâce à l'[[Opérateur d'affectation composée|opérateur d'affectation composée]] `n+=2`, qui équivaut à `n = n + 2`. Les deux affichent les 51 nombres pairs de 0 à 100 ; `algo1` fait 101 tours et 101 tests, `algo2` 51 tours sans test. Les fonctions sont définies **avant** `main` : aucun prototype n'est nécessaire ([[Déclaration et définition]]), et `main` les invoque par un [[Appel de fonction|appel]] `algo1();`.

Les deux fonctions renvoient `0`, valeur que `main` ignore : ce sont en fait des procédures, qui s'écriraient `void algo1(void)` sans `return` de valeur (voir [[2 - structures code#Procédure]]). La variable `nombre`, jamais utilisée, déclenche l'[[Avertissement de compilation|avertissement]] `unused variable 'nombre'` ; sans doute devait-elle servir de borne (`n < nombre`). Si la saisie n'est ni 1 ni 2, rien ne s'affiche : un `else` pourrait le signaler ; si ce n'est pas un nombre, `algo` reste une [[Variable non initialisée|variable non initialisée]], d'où l'intérêt de la [[Validation des entrées|validation des entrées]]. Ce découpage d'un programme en fonctions courtes et nommées est la [[Décomposition fonctionnelle|décomposition fonctionnelle]]. [[Complément hors du cours|ⓘ]]

Les deux algorithmes ont la même [[Complexité algorithmique|complexité]] linéaire, $O(n)$, mais `algo2` fait deux fois moins de tours : la complexité donne l'ordre de grandeur, pas la constante. [[Complément hors du cours|ⓘ]]

## 4.5.c

D'après le code, l'exercice demande de calculer la [[Puissance (mathématiques)|puissance]] $x^n$ par multiplications successives, en affichant chaque étape.

```c
#include <stdio.h>

int main(){

    int x = 2;

    int n = 3;

    int result =1;

    for (int i=1; i<=n; i+=1){
        result *= x;
        printf("%d \n", result);
    }

    return 0;
}
```

`result` est un accumulateur multiplicatif : il part de 1, l'élément neutre de la multiplication (comme une somme part de 0), et `result *= x` le multiplie par `x` à chaque tour. Après le tour `i`, `result` vaut $x^i$ : c'est l'[[Invariant de boucle|invariant de boucle]] qui prouve, par [[Récurrence|récurrence]] sur le nombre de tours, la [[Correction d'un algorithme|correction]] du calcul : le résultat final est $x^n$. Sortie : `2`, `4`, `8`. Pour $n = 0$, la boucle ne tourne pas et `result` vaut 1, ce qui est juste puisque $x^0 = 1$.

Le calcul fait $n$ multiplications. L'[[Exponentiation rapide|exponentiation rapide]] en fait environ $2\log_2 n$, en utilisant $x^{2k} = (x^k)^2$. La fonction `pow` de `math.h` (voir [[Bibliothèque cmath]] pour son équivalent C++) calcule en `double`, ce qui peut arrondir de grands entiers. Avec des `int`, $2^{31}$ provoque déjà un [[Dépassement d'entier|dépassement d'entier]]. [[Complément hors du cours|ⓘ]]

## 4.6.c

D'après le code, l'exercice demande d'afficher les 21 premiers termes de la suite de Lucas, définie par $u_0 = 2$, $u_1 = 1$ et $u_n = u_{n-1} + u_{n-2}$.

```c
#include <stdio.h>

int main(){

    int u0 = 2;
    int u1 =1;

    int lucas;

    printf("u0 = %d\n", u0);
        printf("u1 = %d\n", u1);

    for (int i =2; i<=20; i++){
        lucas = u0 + u1;
        printf("u%d = %d \n", i, lucas);
        u0 = u1;
        u1 = lucas;
    }

    return 0;
}
```

Une [[Suite numérique|suite]] définie par une relation de récurrence d'ordre 2 se calcule avec deux variables qui gardent les deux derniers termes : on calcule le nouveau terme, puis on décale (`u0` reçoit `u1`, `u1` reçoit le nouveau terme), dans cet ordre, sur le principe de l'[[Échange de deux variables|échange de deux variables]]. Sortie : `u0 = 2`, `u1 = 1`, `u2 = 3`, `u3 = 4`, `u4 = 7`… jusqu'à `u20 = 15127`.

Les [[Nombres de Lucas|nombres de Lucas]] suivent la même récurrence que la [[Suite de Fibonacci|suite de Fibonacci]], avec d'autres termes initiaux (Fibonacci : 0, 1). Ils s'écrivent $L_n = \varphi^n + \psi^n$, où $\varphi = \frac{1+\sqrt5}{2}$ est le [[Nombre d'or|nombre d'or]] et $\psi = \frac{1-\sqrt5}{2}$ ; le rapport de deux termes consécutifs tend vers $\varphi \approx 1{,}618$. La croissance est exponentielle : $L_{44} = 1\,568\,397\,607$ tient dans un `int` 32 bits, mais $L_{45} = 2\,537\,720\,636$ dépasse $2^{31}-1$ ; au-delà, il faut un `long long` ([[Type entier|types entiers]]). Le second `printf` est mal indenté, sans effet sur l'exécution : en C, l'indentation ne compte pas, mais une [[Règle de codage|règle de codage]] l'impose pour la lisibilité. [[Complément hors du cours|ⓘ]]

## 4.7.c

D'après le code, l'exercice demande de dessiner un rectangle plein d'étoiles, de 5 lignes sur 10 colonnes.

```c
#include <stdio.h>

int main(){
    int longueur = 5;
    int largeur = 10;

    for (int i =1; i<=longueur; i++){

        for (int j =1; j<=largeur; j++){

            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
```

Deux [[Boucle imbriquée|boucles imbriquées]] : la boucle externe parcourt les lignes (`i`), la boucle interne les colonnes (`j`), et le `\n` ([[Caractère d'échappement|séquence d'échappement]]) passe à la ligne après chaque ligne complète. Le `printf("* ")` s'exécute $5 \times 10 = 50$ fois. Sortie : 5 lignes de 10 étoiles `* * * * * * * * * * `.

Le nombre total de tours d'une double boucle est le produit des nombres de tours : c'est pourquoi deux boucles imbriquées sur $n$ éléments ont une [[Complexité algorithmique|complexité]] en $O(n^2)$. Ces dessins en caractères relèvent de l'[[Art ASCII|art ASCII]]. [[Complément hors du cours|ⓘ]]

## 4.8.c

D'après le code, l'exercice demande de dessiner un triangle rectangle d'étoiles de 5 lignes.

```c
#include <stdio.h>

int main(){
    int lignes = 5;

    for (int i =1; i <= lignes; i++){

        for(int j=1; j<=i; j++){printf("* ");}

        printf("\n");
    }

    return 0;
}
```

La borne de la boucle interne dépend du compteur externe (`j<=i`) : la ligne `i` contient `i` étoiles. Sortie : 1, 2, 3, 4 puis 5 étoiles.

Le nombre total d'étoiles est $1 + 2 + \dots + 5 = 15$, la [[Somme des premiers entiers|somme des premiers entiers]] $\frac{n(n+1)}{2}$ : une boucle interne bornée par le compteur externe reste en $O(n^2)$. Pour un triangle aligné à droite, on affiche d'abord `lignes - i` paires d'espaces dans une seconde boucle interne. [[Complément hors du cours|ⓘ]]

## 4.9.c

D'après le code, l'exercice demande de dessiner le contour d'un rectangle de 5 lignes sur 10 colonnes : des étoiles sur le bord, des espaces à l'intérieur.

```c
#include <stdio.h>

int main(){
    int longueur = 5;
    int largeur = 10;

    for (int i =1; i<=longueur; i++){

        for (int j =1; j<=largeur; j++){

            if (j!=1 && j!=largeur && i!= 1 && i!=longueur) printf("  ");
            else printf("* ");
        }
        printf("\n");
    }

    return 0;
}
```

Une case est intérieure si elle n'est ni sur la première ni sur la dernière colonne, ni sur la première ni sur la dernière ligne : quatre conditions reliées par `&&` ([[Opérateur logique|opérateurs logiques]]). Chaque case occupe deux caractères (`"* "` ou `"  "`), pour que les colonnes restent alignées. Sortie :

```text
* * * * * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * *
```

Par les [[Lois de De Morgan|lois de De Morgan]], la condition inverse « case du bord » s'écrit `i==1 || i==longueur || j==1 || j==largeur`, souvent plus lisible : `if (bord) printf("* "); else printf("  ");`. [[Complément hors du cours|ⓘ]]

## À retenir

- `for (i = 0; i < N; i++)` tourne N fois ; `for (i = 0; i <= N; i++)` tourne N + 1 fois ([[Erreur de décalage d'une unité]]). [[Complément hors du cours|ⓘ]]
- Un compteur déclaré dans le `for` n'existe plus après la boucle ([[Portée d'une variable]]).
- `break` sort de la boucle la plus proche ; pour savoir ensuite pourquoi on est sorti, garder un drapeau ([[Instructions break et continue]]).
- Un accumulateur s'initialise à l'élément neutre : 0 pour une somme, 1 pour un produit ([[Accumulateur (programmation)]]). [[Complément hors du cours|ⓘ]]
- Pour une récurrence d'ordre 2, calculer le nouveau terme **avant** de décaler les deux variables ([[Suite numérique]]).
- Boucles imbriquées : nombre total de tours = produit des nombres de tours ([[Boucle imbriquée]]). [[Complément hors du cours|ⓘ]]
- Les `int` débordent vite (puissances, suites exponentielles) : prévoir `long long` ([[Dépassement d'entier]]). [[Complément hors du cours|ⓘ]]
- Une fonction qui ne renvoie rien d'utile s'écrit `void` ([[Fonction et procédure]]).
