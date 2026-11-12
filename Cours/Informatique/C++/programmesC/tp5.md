---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.1.c|5.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.2.c|5.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.3.c|5.3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.4.c|5.4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.5.c|5.5.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.6.c|5.6.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.7.c|5.7.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp5/5.8.c|5.8.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 5 de [[Langage C|C]] (dossier `programmes C/tp5`, huit fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils mettent en pratique les [[Boucle (programmation)|boucles]] `while` et `do … while` de [[2 - structures code]] (§ 5 et 6) sur des problèmes d'arithmétique ([[Divisibilité|divisibilité]], [[Division euclidienne|division euclidienne]]) : [[Nombre premier|nombres premiers]], [[Nombre parfait|nombres parfaits]], [[Conjecture de Syracuse|suite de Syracuse]]. On y retrouve les réflexes du [[Compteur (programmation)|compteur]], de l'[[Accumulateur (programmation)|accumulateur]] et de la variable [[Drapeau (programmation)|drapeau]], et les [[Fonctions printf et scanf|fonctions `printf` et `scanf`]] de [[1 - basiques]]. Plusieurs fichiers contenaient une erreur, corrigée ci-dessous (✎). Tous ont été compilés avec [[GCC|`gcc`]] `-std=c17 -Wall -Wextra`.

## 5.1

D'après le code, l'exercice demande d'afficher les itérations d'une boucle `while` qui compte de 0 à 9, puis la valeur de la [[Variable (programmation)|variable]] de boucle après la sortie.

```c
#include <stdio.h>
int main () {
    int i = 0 ;

    while ( i < 10 ) {
        printf ("iteration %d \n", i) ;
        i = i+1;
    }

    printf ("valeur de i apres la boucle : %d \n", i) ;
    return 0 ;
}
```

Sortie : `iteration 0` à `iteration 9`, puis `valeur de i apres la boucle : 10`.

C'est la traduction en `while` de la boucle `for (i = 0 ; i < 10 ; i = i + 1)` de [[2 - structures code]] : l'[[Initialisation (programmation)|initialisation]] `i = 0` se fait avant la boucle, la condition `i < 10` est testée **avant** chaque tour, l'[[Affectation|affectation]] `i = i+1` termine chaque tour. Après le dernier tour, `i` vaut 10, la condition devient fausse et la boucle s'arrête : **après la boucle, `i` vaut 10**, comme dans le cours. `%d` est le [[Fonctions printf et scanf|spécificateur de format]] d'un `int`, `\n` le [[Caractère d'échappement|caractère d'échappement]] du saut de ligne.

`i = i+1` s'écrit plus souvent `i++` ([[Opérateur d'incrémentation|opérateur d'incrémentation]]) ou `i += 1` ([[Opérateur d'affectation composée|affectation composée]]) ; les trois sont équivalents ici. Oublier cette ligne donne une [[Boucle (programmation)|boucle infinie]] : la condition ne change jamais. Montrer qu'une boucle s'arrête, c'est exhiber une quantité entière qui décroît strictement à chaque tour (ici $10 - i$) : voir [[Terminaison d'un algorithme]]. [[Complément hors du cours|ⓘ]]

## 5.2

D'après le code, l'exercice demande de redemander « voulez-vous continuer ? » tant que l'utilisateur ne tape pas 0.

```c
#include <stdio.h>

int main(){
    int choix ;

    do {
        printf("voulez-vous continuer ? \n");
        scanf("%d", &choix);
    } while (choix !=0);

    return 0;
}
```

C'est le cas d'usage du `do … while` ([[2 - structures code]], § 5) : la question doit être posée **au moins une fois**, et la condition n'est testée qu'à la fin. `choix` n'a pas besoin d'être initialisé, puisqu'il est lu avant le premier test. `scanf("%d", &choix)` reçoit l'**adresse** de `choix` ([[Opérateur d'adresse|opérateur `&`]]) pour pouvoir écrire dedans. La valeur 0 qui arrête la boucle est une [[Valeur sentinelle|valeur sentinelle]].

Si l'utilisateur tape une lettre, `scanf` échoue, laisse la lettre dans le [[Tampon (buffer)|tampon]] de l'[[Flux standard|entrée standard]] et ne modifie pas `choix` : la boucle tourne alors sans fin, en reposant la question sans jamais attendre de saisie (constaté en tapant `a`). En [[Fin de fichier|fin de fichier]] (`Ctrl+D`), même effet. La parade est de tester la valeur renvoyée par `scanf`, le nombre de valeurs lues : `if (scanf("%d", &choix) != 1) break;`. C'est le principe de la [[Validation des entrées|validation des entrées]]. [[Complément hors du cours|ⓘ]]

## 5.3

D'après le code, l'exercice demande un jeu du nombre mystère : l'utilisateur a 10 essais pour trouver 77, et le message final dépend du nombre de tours (« bravo tricheur » au premier, « bravo » du 2e au 5e, « presque bravo » du 6e au 9e, « mouais » au 10e, « tié nul » en cas d'échec).

Deux erreurs sont corrigées dans le code ci-dessous : `guess` est initialisé (`int guess = 0;` au lieu de `int guess;`), et les doubles comparaisons `2<=nombre_tour<=5` et `6<=nombre_tour<=9` sont réécrites avec `&&`. [[Erreurs du cours#^e-tp5|✎]]

```c
#include <stdio.h>

int main(){
    int nombre = 77;
    int guess = 0;
    int nombre_tour = 0;

    while (guess != nombre && nombre_tour <10){
        nombre_tour +=1;
        printf("tour %d , devinez \n", nombre_tour);
        scanf("%d", & guess);

        if (guess == nombre && nombre_tour==1) printf("bravo tricheur");
        else if (guess == nombre && nombre_tour >= 2 && nombre_tour <= 5) printf("bravo");
        else if (guess == nombre && nombre_tour >= 6 && nombre_tour <= 9) printf("presque bravo");
        else if (guess == nombre && nombre_tour==10) printf("mouais");
        else if (nombre_tour >= 10) printf("tié nul");
    }

    return 0;
}
```

Pourquoi ces corrections :

- **`guess` non initialisé.** Au premier test `guess != nombre`, `guess` n'a encore reçu aucune valeur : lire une [[Variable non initialisée|variable non initialisée]] est un [[Comportement indéfini|comportement indéfini]]. Si la mémoire contenait justement 77, la boucle ne s'exécuterait pas du tout. `gcc -Wall -O2` le signale : `warning: 'guess' is used uninitialized`. Il suffit d'une valeur différente de 77 (ici 0) ; un `do … while` éviterait aussi le problème, puisque la saisie précède le test.
- **`2<=nombre_tour<=5` ne teste pas un encadrement.** Les [[Opérateur de comparaison|opérateurs de comparaison]] s'évaluent de gauche à droite ([[Associativité et ordre d'évaluation|associativité]]) : `(2 <= nombre_tour)` vaut 0 ou 1, puis on teste `0 <= 5` ou `1 <= 5`, **toujours vrai**. Dans le programme d'origine, une bonne réponse au tour 7 ou au tour 10 affichait donc `bravo` (vérifié à l'exécution) : `presque bravo` et `mouais` n'apparaissaient jamais. `gcc -Wall` prévient : `comparisons like 'X<=Y<=Z' do not have their mathematical meaning`. C'est le même piège que `a == b == c` dans [[1 - basiques]]. L'encadrement s'écrit avec l'[[Opérateur logique|opérateur logique]] `&&`.

Le test `guess == nombre` est répété dans chaque branche de la [[Structure conditionnelle|structure conditionnelle]] ; on peut l'écrire une seule fois, `if (guess == nombre) { … } else if (nombre_tour >= 10) …`. Les `printf` finaux sans `\n` collent leur message à l'invite du [[Interface en ligne de commande|terminal]] : ajouter `\n`. Les nombres 77 et 10 gagneraient à être des [[Constante (programmation)|constantes]] nommées (`#define MYSTERE 77`, voir [[Macro (préprocesseur)]]) plutôt que des [[Nombre magique (programmation)|nombres magiques]]. [[Complément hors du cours|ⓘ]]

Pour un vrai jeu, le nombre mystère se tire au hasard : `srand(time(NULL)); int nombre = rand() % 100 + 1;` (voir [[Nombres aléatoires en C]]), et le programme répond « plus grand » ou « plus petit ». La meilleure stratégie est alors la [[Recherche dichotomique|recherche dichotomique]] : couper l'intervalle en deux à chaque essai trouve un nombre entre 1 et 100 en au plus 7 essais, car $2^7 = 128 \geq 100$. [[Complément hors du cours|ⓘ]]

## 5.4

D'après le code, l'exercice demande de dire si un entier (ici 7) est premier et, sinon, d'afficher un de ses diviseurs.

```c
#include <stdio.h>

int main(){
    int nombre = 7;
    int i = 2;
    int est_premier = 1;

    while (est_premier ==1 && i < nombre) {
        if (nombre%i == 0) {
            est_premier = 0;
        }
        i++;
    }

    if (est_premier == 1) {
        printf("Le nombre %d est premier\n", nombre);
    }
    else if (est_premier == 0) {
        printf("Le nombre %d n'est pas premier, divisible par %d\n", nombre, i-1);
    }

    return 0;
}
```

Sortie : `Le nombre 7 est premier` ; avec `nombre = 91`, `Le nombre 91 n'est pas premier, divisible par 7`.

Méthode : on essaie tous les diviseurs $i$ de 2 à $n-1$ ([[Recherche exhaustive|recherche exhaustive]], ou divisions successives). `nombre%i` est le reste de la [[Division euclidienne|division euclidienne]] de `nombre` par `i` (opérateur modulo `%`, voir [[Opérateurs arithmétiques]]) : il vaut 0 quand `i` divise `nombre` ([[Divisibilité|divisibilité]]). `est_premier` est un **drapeau** ([[Drapeau (programmation)|flag]]) : il vaut 1 tant qu'aucun diviseur n'est trouvé et passe à 0 au premier diviseur, ce qui arrête la boucle grâce à la condition `est_premier == 1`. Comme `i++` s'exécute encore après la découverte du diviseur, celui-ci vaut `i-1` à la sortie : d'où le `i-1` du dernier `printf`.

Le C n'a pas de type booléen natif avant C99 ; on utilise un `int` qui vaut 0 (faux) ou 1 (vrai). Depuis C99, `<stdbool.h>` fournit `bool`, `true` et `false` (voir [[Booléen]]), et la condition s'écrit simplement `while (est_premier && i < nombre)`. Le `else if (est_premier == 0)` peut devenir un simple `else`. [[Complément hors du cours|ⓘ]]

Deux améliorations classiques. D'abord, 0 et 1 ne sont pas premiers, or le programme répond « premier » pour 1 (la boucle ne s'exécute pas) : il faut traiter à part `nombre < 2`. Ensuite, il suffit de tester les diviseurs jusqu'à $\sqrt{n}$ ([[Racine carrée|racine carrée]] de $n$) : si $n = a \times b$ avec $a \leq b$, alors $a \leq \sqrt{n}$. La condition devient `i * i <= nombre` (plutôt que `i <= sqrt(nombre)`, qui demanderait la [[Bibliothèque cmath|bibliothèque mathématique]] et des calculs en [[Nombre à virgule flottante|virgule flottante]]). La [[Complexité algorithmique|complexité]] passe de $O(n)$ à $O(\sqrt{n})$ divisions : pour un nombre premier proche d'un milliard, environ 31 600 divisions au lieu d'un milliard. [[Complément hors du cours|ⓘ]]

## 5.5

D'après le code, l'exercice demande de dire si un entier (ici 11) est parfait, c'est-à-dire égal à la somme de ses diviseurs autres que lui-même.

Le test d'origine était faux : la boucle allait jusqu'à `i<=nombre` (elle ajoutait donc `nombre` lui-même à la somme) et le test final était `nombre%compteur == 0`. Corrigé ci-dessous : la boucle s'arrête à `i < nombre` et le test devient `compteur == nombre`. [[Erreurs du cours#^e-tp5|✎]]

```c
#include <stdio.h>

int main(){
    int nombre = 11;
    int est_parfait = 0;
    int i = 1;
    int compteur = 0;

    while (est_parfait == 0 && i < nombre) {
        if (nombre%i==0){
            compteur +=i;
        }
        i++;
    }

    if (compteur == nombre) printf("le nombre %d est parfait", nombre);
    else printf("le nombre %d n'est pas parfait", nombre);

    return 0;
}
```

Un [[Nombre parfait|nombre parfait]] est égal à la somme de ses **diviseurs propres** (tous ses diviseurs sauf lui-même) : $6 = 1 + 2 + 3$, $28 = 1 + 2 + 4 + 7 + 14$. Avec l'ancienne version, la somme incluait `nombre` et valait donc $2n$ pour un nombre parfait ; or $n$ n'est jamais divisible par $2n$ : le programme répondait « n'est pas parfait » pour 6 et 28 (vérifié), et « est parfait » pour 1. Pour 11, la réponse était juste par hasard. La version corrigée répond « parfait » pour 6 et 28, « pas parfait » pour 1, 11 et 12.

`compteur` joue ici le rôle d'un [[Accumulateur (programmation)|accumulateur]] (une somme), plus que d'un [[Compteur (programmation)|compteur]] (un nombre d'occurrences) : `somme_diviseurs` serait un nom plus juste. `compteur += i` est l'[[Opérateur d'affectation composée|affectation composée]] pour `compteur = compteur + i`. La variable `est_parfait` n'est jamais modifiée : la condition `est_parfait == 0` est toujours vraie et peut être supprimée. [[Complément hors du cours|ⓘ]]

L'ancien test `nombre%compteur` avait un autre défaut : si `compteur` avait pu valoir 0, le modulo par zéro est, comme la division par zéro, un [[Comportement indéfini|comportement indéfini]] (en pratique, le programme s'arrête sur une exception arithmétique). [[Complément hors du cours|ⓘ]]

## 5.6

D'après le code, l'exercice demande d'afficher tous les nombres premiers de 1 à 100.

Le programme d'origine commençait à `nombre = 1` et affichait 1 comme nombre premier, ce qui est faux (un nombre premier a exactement deux diviseurs distincts, 1 et lui-même). La boucle commence ici à 2. [[Erreurs du cours#^e-tp5|✎]]

```c
#include <stdio.h>

int main(){
    int nombre = 2;
    int est_premier = 1;

    while (nombre <=100){
        int i = 2;

        while (est_premier ==1 && i < nombre) {
            if (nombre%i == 0) est_premier = 0;
            i++;
        }

        if (est_premier == 1) printf("%d \n", nombre);

        est_premier = 1;
        nombre++;
    }

    return 0;
}
```

Sortie : les 25 [[Nombre premier|nombres premiers]] inférieurs à 100, de 2 à 97.

Le programme reprend le test de 5.4 dans une seconde boucle : ce sont des **boucles imbriquées** ([[Boucle (programmation)]]). Deux points de méthode : `i` est déclaré **dans** la boucle externe, donc remis à 2 à chaque nouveau nombre (sa [[Portée d'une variable|portée]] est le [[Bloc d'instructions|bloc]] de la boucle) ; le drapeau `est_premier`, déclaré dehors, doit être remis à 1 à la main à la fin de chaque tour (`est_premier = 1;`), sinon tous les nombres après le premier nombre composé seraient déclarés non premiers. Le déclarer dans la boucle, comme `i`, rendrait cet oubli impossible.

Pour lister tous les nombres premiers jusqu'à $N$, le [[Crible d'Ératosthène|crible d'Ératosthène]] est bien plus rapide : on part d'un [[Tableau (programmation)|tableau]] de $N+1$ cases marquées « premier », puis, pour chaque $p$ encore marqué avec $p^2 \leq N$, on raye ses multiples $p^2, p^2 + p, \dots$ Sa complexité est $O(N \log \log N)$, contre environ $O(N \sqrt{N})$ pour des tests séparés jusqu'à $\sqrt{n}$. [[Complément hors du cours|ⓘ]]

## 5.7

D'après le code, l'exercice demande d'afficher tous les nombres parfaits de 2 à 10 000.

```c
#include <stdio.h>

int main(){
    int nombre = 2;

    while (nombre <=10000){
        int compteur = 0;
        int i = 1;

        while (i<nombre) {
            if (nombre%i==0) compteur +=i;
            i++;
        }

        if (nombre == compteur) printf("%d\n", nombre);

        nombre++;
    }

    return 0;
}
```

Sortie : `6`, `28`, `496`, `8128`.

Ce programme fait correctement ce que 5.5 faisait mal : la somme des diviseurs s'arrête à `i < nombre` et le test est une égalité. Comme en 5.6, `compteur` et `i` sont déclarés dans la boucle externe, donc réinitialisés pour chaque nombre.

Ces quatre nombres sont les seuls nombres parfaits inférieurs à 10 000 ; le suivant est 33 550 336. Tous les nombres parfaits pairs sont de la forme $2^{p-1}(2^p - 1)$ où $2^p - 1$ est un [[Nombre de Mersenne|nombre premier de Mersenne]] (théorème d'Euclide-Euler) : $p = 2, 3, 5, 7$ donnent 6, 28, 496, 8128. On ne connaît aucun nombre parfait impair, sans savoir s'il en existe. [[Complément hors du cours|ⓘ]]

Le programme fait environ $\sum_{n \leq N} n \approx N^2/2$ divisions, soit 50 millions pour $N = 10\,000$ : instantané, mais [[Complexité algorithmique|quadratique]]. En parcourant les diviseurs par paires ($i$ et $n/i$ pour $i \leq \sqrt{n}$), on descend à environ $N\sqrt{N}$. [[Complément hors du cours|ⓘ]]

## 5.8

D'après le code, l'exercice demande d'afficher la [[Conjecture de Syracuse|suite de Syracuse]] partant de 15 : si $u_n$ est pair, $u_{n+1} = u_n / 2$, sinon $u_{n+1} = 3u_n + 1$, jusqu'à atteindre 1.

Le premier `printf` du programme d'origine, `printf("u0 = %d \n", i , nombre);`, affichait `u0 = 1` (la valeur de `i`) au lieu de `u0 = 15` : le format n'a qu'un `%d` et reçoit deux arguments, seul le premier est utilisé. Corrigé en `printf("u0 = %d \n", nombre);`. [[Erreurs du cours#^e-tp5|✎]]

```c
#include <stdio.h>

int main(){
    int nombre = 15;
    int i = 1;

    printf("u0 = %d \n", nombre);

    while (nombre > 1){
        if (nombre%2==0){
            nombre = nombre/2;
        }
        else nombre = nombre*3+1;

        printf("u%d = %d \n", i , nombre);
        i++;
    }

    return 0;
}
```

Sortie : `u0 = 15`, `u1 = 46`, `u2 = 23`, `u3 = 70`, `u4 = 35`, `u5 = 106`, `u6 = 53`, `u7 = 160`, `u8 = 80`, `u9 = 40`, `u10 = 20`, `u11 = 10`, `u12 = 5`, `u13 = 16`, `u14 = 8`, `u15 = 4`, `u16 = 2`, `u17 = 1`.

`nombre%2==0` teste la [[Parité d'un entier|parité]] ; `nombre/2` est une division entière, exacte ici puisque `nombre` est pair. `i` sert d'indice de la [[Suite numérique|suite]]. `gcc -Wall` signalait l'argument en trop : `warning: too many arguments for format` ; un [[Avertissement de compilation|avertissement]] n'empêche pas de compiler, mais celui-ci révélait une vraie erreur.

La suite partant de 15 atteint 1 en 17 étapes (son « temps de vol ») et culmine à 160. La [[Conjecture de Syracuse|conjecture de Syracuse]] (ou de Collatz, 1937) affirme que c'est vrai quel que soit l'entier de départ ; elle est vérifiée par ordinateur pour d'immenses valeurs mais n'est toujours pas démontrée. Le programme est donc un exemple de boucle dont on ne sait pas prouver la [[Terminaison d'un algorithme|terminaison]] en général. Pour de grands départs, les termes peuvent dépasser la capacité d'un `int` ([[Dépassement d'entier|dépassement d'entier]], lui aussi comportement indéfini pour un entier signé) : on utilise alors `long long` ou `unsigned long long` (voir [[Type entier]]). [[Complément hors du cours|ⓘ]]

## À retenir

- Une [[Variable non initialisée|variable lue avant d'avoir reçu une valeur]] (`guess` en 5.3) est un [[Comportement indéfini|comportement indéfini]] : initialiser à la déclaration, ou utiliser un `do … while` quand la saisie précède le test.
- `a <= x <= b` ne teste pas un encadrement en C ([[Associativité et ordre d'évaluation|associativité]]) : écrire `a <= x && x <= b` ([[Opérateur logique|opérateur logique]] `&&`).
- Compiler avec `-Wall -Wextra` : les [[Avertissement de compilation|avertissements]] de 5.3 et 5.8 désignaient exactement les erreurs.
- [[Nombre parfait]] : somme des diviseurs **propres** (`i < n`) **égale** à $n$ ; 1 n'est pas [[Nombre premier|premier]].
- Un [[Drapeau (programmation)|drapeau]] ou un [[Accumulateur (programmation)|accumulateur]] utilisé dans des boucles imbriquées doit être réinitialisé à chaque tour de la boucle externe : le plus sûr est de le déclarer dans cette boucle.
- Le diviseur trouvé vaut `i-1` à la sortie d'une boucle qui fait `i++` après le test.
- Tester [[Fonctions printf et scanf|`scanf(...)`]] `== 1` avant d'utiliser la valeur lue, sinon une saisie invalide fait boucler le programme ([[Validation des entrées]]). [[Complément hors du cours|ⓘ]]
- Tester les [[Divisibilité|diviseurs]] jusqu'à $\sqrt{n}$ ([[Racine carrée]] ; en code, `i * i <= n`) suffit pour la primalité. [[Complément hors du cours|ⓘ]]
