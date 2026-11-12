---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.1.c|2.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.2.c|2.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.3.c|2.3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.4.c|2.4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.5.c|2.5.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.6.c|2.6.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.7.c|2.7.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.8.c|2.8.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.9.c|2.9.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp2/2.10.c|2.10.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 2 de [[Langage C|C]] (dossier `programmes C/tp2`, 10 fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils mettent en pratique le chapitre [[1 - basiques]] : [[Type primitif|types de base]] (`int`, `float`), [[Variable (programmation)|variables]], [[Affectation|affectation]], lecture au clavier et affichage avec les [[Fonctions printf et scanf|fonctions `printf` et `scanf`]], [[Opérateurs arithmétiques|opérateurs arithmétiques]] ; le dernier programme utilise déjà la [[Boucle (programmation)|boucle]] `for` de [[2 - structures code]]. Les fichiers n'ont pas de commentaires : l'énoncé de chaque exercice est reconstitué d'après le code. Chaque programme a été compilé avec [[GCC]] (`gcc -std=c17 -Wall -Wextra`) et exécuté ; trois ne compilaient pas et sont corrigés ci-dessous.

## 2.1.c

D'après le code, l'exercice demande d'écrire le premier programme : afficher `Hello, World!`.

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");

    return 0;
}
```

C'est le [[Programme Hello world|programme « Hello world »]] traditionnel. La [[Directive include|directive `#include <stdio.h>`]], traitée par le [[Préprocesseur|préprocesseur]], insère le [[Fichier d'en-tête|fichier d'en-tête]] qui déclare `printf`. L'exécution commence par la [[Fonction main (C et C++)|fonction `main`]] ; son `return 0;` renvoie au système un [[Code de retour|code de retour]] nul, qui signifie « tout s'est bien passé ». Le `\n` est une [[Caractère d'échappement|séquence d'échappement]] : le retour à la ligne. Sortie : `Hello, World!`.

Depuis C99, `main` renvoie implicitement 0 si l'exécution atteint sa dernière accolade sans `return` ; l'écrire reste une bonne habitude. En C avant la norme C23, `int main()` signifie « paramètres non précisés », et `int main(void)` « aucun paramètre » ; C23 aligne le sens de `()` sur celui de `(void)`, comme en [[Langage C++|C++]] (voir [[Norme du C]]). [[Complément hors du cours|ⓘ]]

## 2.2.c

D'après le code, l'exercice demande de lire un entier et un réel au clavier, puis de les afficher.

```c
#include <stdio.h>

int main() {
    int nb1;
    float nb2;

    scanf("%d", &nb1);
    scanf("%f", &nb2);

    printf("nb1 vaut %d ; nb2 vaut %f\n", nb1, nb2);

    return 0;
}
```

Chaque variable a un [[Typage statique|type fixé à la déclaration]] : `nb1` est un [[Type entier|entier]] (`int`), `nb2` un [[Nombre à virgule flottante|nombre à virgule flottante]] (`float`). Le format de `scanf` doit correspondre au type : `%d` pour un `int`, `%f` pour un `float`. Le `&` est l'[[Opérateur d'adresse|opérateur d'adresse]] : `scanf` reçoit l'adresse de la variable, car le C passe les arguments [[Passage par valeur|par valeur]] (voir [[1 - basiques#`printf` et `scanf`]]). Avec l'entrée `5 2.5`, la sortie est `nb1 vaut 5 ; nb2 vaut 2.500000` : `%f` affiche six décimales par défaut.

Dans `printf`, un `float` est automatiquement converti en `double` (promotion des arguments d'une fonction variadique), si bien que `%f` affiche indifféremment `float` et `double` ; dans `scanf`, qui reçoit une [[Pointeur et adresse mémoire|adresse]], il faut `%f` pour un `float` et `%lf` pour un `double`. [[Complément hors du cours|ⓘ]]

`scanf` renvoie le nombre de valeurs effectivement lues, ou `EOF` en [[Fin de fichier|fin de fichier]]. Si l'utilisatrice tape une lettre au lieu d'un nombre, `nb1` reste [[Variable non initialisée|non initialisée]] et l'afficher est un [[Comportement indéfini|comportement indéfini]] ; un programme robuste teste ce retour, c'est la [[Validation des entrées|validation des entrées]] : [[Complément hors du cours|ⓘ]]

```c
if (scanf("%d", &nb1) != 1) {
    printf("entrée invalide\n");
    return 1;
}
```

## 2.3.c

D'après le code, l'exercice demande de lire deux notes entières et d'afficher leur [[Mesures de tendance centrale|moyenne]]. Le programme d'origine calculait `(note1 + note2) / 2` : avec `12` et `15`, il affichait `13.000000` au lieu de `13.500000`. Le diviseur `2` devient `2.0` : [[Erreurs du cours#^e-tp2|✎]]

```c
#include <stdio.h>

int main() {
    int note1;
    int note2;
    float moyenne;

    scanf("%d", &note1);
    scanf("%d", &note2);

    moyenne = (note1 + note2) / 2.0;

    printf(("la moyenne de %d et %d est %f\n"), note1, note2, moyenne);

    return 0;
}
```

La cause est la [[Division euclidienne|division entière]] : quand les deux opérandes de `/` sont des `int`, le C calcule le quotient entier et jette le reste (`27 / 2` vaut `13`). La conversion en `float` n'a lieu qu'**après**, à l'[[Affectation|affectation]] : elle ne rattrape pas la partie décimale perdue. Il suffit qu'un des deux opérandes soit réel pour que la division soit réelle : `2.0` est une [[Valeur littérale|constante littérale]] de type `double`, et `note1 + note2` est alors converti en `double` avant la division (conversions arithmétiques usuelles, une forme de [[Transtypage|transtypage]] implicite). Autres écritures équivalentes : `(float)(note1 + note2) / 2`, ou `/ 2.0f` pour rester en `float`. [[Complément hors du cours|ⓘ]]

Les parenthèses autour de la chaîne de format, `printf(("…"), …)`, sont inutiles mais valides : une [[Expression (programmation)|expression]] entre parenthèses garde sa valeur.

## 2.4.c

D'après le code, l'exercice demande de lire les coefficients `a` et `b` d'une [[Équation du premier degré|équation du premier degré]] $ax + b = 0$, de demander la solution à l'utilisatrice, puis de dire si elle est juste.

```c
#include <stdio.h>

int main() {
    int a ;
    int b;
    float x;

    scanf("%d", &a);
    scanf("%d", &b);

    printf("que vaut x dans l'équation %dx+%d=0\n", a, b);
    scanf("%f", &x);
    if (a*x+b==0) {
        printf("la solution est bonne");
    }
    else {
        printf("la solution est fausse");
    }
    return 0;
}
```

Le test utilise la [[Structure conditionnelle|structure conditionnelle]] `if … else` et l'[[Opérateur de comparaison|opérateur de comparaison]] `==` (voir [[2 - structures code#2. `if ... else`]]). Dans `a*x+b`, l'`int` `a` est converti en `float` avant la multiplication. Avec `2`, `-4` puis `2`, le programme affiche `que vaut x dans l'équation 2x+-4=0` et `la solution est bonne` : l'affichage de `b` négatif donne `+-4`.

Piège : comparer des flottants avec `==` est fragile, parce qu'un `float` est stocké en binaire selon la [[Norme IEEE 754|norme IEEE 754]] et que la plupart des décimaux (0,1, 1/3…) n'y sont qu'approchés. Pour $3x + 1 = 0$, la réponse `-0.333333` est déclarée fausse, et aucune saisie ne peut donner exactement $-1/3$. La [[Comparaison de nombres flottants|comparaison de nombres flottants]] se fait avec une tolérance sur la [[Valeur absolue|valeur absolue]] de l'écart, `fabs` venant de `math.h` : [[Complément hors du cours|ⓘ]]

```c
#include <math.h>
if (fabs(a*x + b) < 1e-4) printf("la solution est bonne\n");
```

La solution exacte existe si $a \neq 0$ : $x = -b/a$ ; si $a = 0$, l'équation n'a aucune solution ($b \neq 0$) ou en a une infinité ($b = 0$), cas que le programme ne traite pas. [[Complément hors du cours|ⓘ]]

## 2.5.c

D'après le code, l'exercice demande de lire un réel `x` et d'afficher l'image $f(x) = 3x + 4$ par une [[Fonction affine|fonction affine]]. Le fichier d'origine ne compilait pas : la chaîne de format de `scanf` était coupée par un retour à la ligne (`scanf("` puis `%f", &x);` à la ligne suivante), et [[GCC]] répond `error: missing terminating " character`. La chaîne est remise sur une ligne : [[Erreurs du cours#^e-tp2|✎]]

```c
#include <stdio.h>

int main() {
    float f;
    float x;

    scanf("%f", &x);

    f = 3*x+4;
    printf("f = %f\n", f);

    return 0;
}
```

Une [[Chaîne de caractères|chaîne littérale]] ne peut pas contenir de retour à la ligne brut : c'est une [[Erreur de compilation|erreur de compilation]], détectée avant toute exécution. Avec l'entrée `2`, la sortie est `f = 10.000000`.

Pour couper une chaîne longue, on écrit deux littéraux à la suite (`"abc" "def"`), que le compilateur concatène, ou on termine la ligne par une barre oblique inverse `\`. [[Complément hors du cours|ⓘ]]

## 2.6.c

D'après le code, l'exercice demande de lire la largeur et la longueur d'un rectangle, puis d'afficher son [[Aire (géométrie)|aire]].

```c
#include <stdio.h>

int main() {
    int largeur;
    int longueur;

    scanf("%d", &largeur);
    scanf("%d", &longueur);

    printf("la surface est : %d", largeur*longueur);

    return 0;
}
```

L'argument de `printf` peut être une [[Expression (programmation)|expression]] : `largeur*longueur` est calculé puis affiché, sans variable intermédiaire. Avec `4` et `5`, la sortie est `la surface est : 20`. Faute de `\n` final, l'invite du terminal s'affiche collée au résultat.

Le produit de deux `int` reste un `int` : au-delà de $2^{31}-1$ (environ 2,1 milliards), il y a [[Dépassement d'entier|dépassement d'entier]], qui est un comportement indéfini pour les entiers signés. Un rectangle de 50 000 × 50 000 suffit. [[Complément hors du cours|ⓘ]]

## 2.7.c

D'après le code, l'exercice demande de lire une date (jour, mois, année) en une seule saisie, puis de l'afficher de deux façons.

```c
#include <stdio.h>

int main() {
    int jour;
    int mois;
    int annee;

    scanf("%d %d %d", &jour, &mois, &annee);
    printf("jour : %d\nmois : %d\nannee : %d\n", jour, mois, annee);
    printf("on est le %d/%d/%d", jour, mois, annee);

    return 0;
}
```

Un seul `scanf` peut lire plusieurs valeurs : il y a autant de `%d` que d'adresses. Un [[Espace blanc|espace blanc]] dans le format accepte n'importe quelle suite d'espaces, tabulations ou retours à la ligne entre les nombres. Avec `12 11 2026`, la sortie est `jour : 12`, `mois : 11`, `annee : 2026` sur trois lignes, puis `on est le 12/11/2026`.

Pour lire une date saisie avec des barres obliques, le format reprend le séparateur : `scanf("%d/%d/%d", …)`. Pour afficher `05/03/2026` au lieu de `5/3/2026`, on utilise le modificateur `%02d` (largeur 2 complétée par des zéros). L'ordre jour/mois/année est l'usage français ; la [[Norme ISO 8601|norme ISO 8601]] écrit `2026-11-12` (année, mois, jour), ordre qui trie correctement les dates comme du texte. [[Complément hors du cours|ⓘ]]

## 2.8.c

D'après le code, l'exercice demande d'échanger les valeurs de deux variables `a` et `b`.

```c
#include <stdio.h>

int main() {
    int a = 1;
    int b = 2;
    int c;
    printf("a = %d\nb = %d\n", a, b);

    c = a;
    a = b;
    b = c;

    printf("a = %d\nb = %d\n", a, b);
    return 0;
}
```

L'[[Échange de deux variables|échange de deux variables]] demande une variable temporaire `c` : écrire directement `a = b; b = a;` donnerait 2 aux deux, car la première [[Affectation|affectation]] écrase l'ancienne valeur de `a`. Les déclarations `int a = 1;` combinent déclaration et [[Initialisation (programmation)|initialisation]]. Sortie : `a = 1`, `b = 2`, puis `a = 2`, `b = 1`.

Il existe un échange sans variable temporaire, par le [[Ou exclusif|ou exclusif]] bit à bit (`a ^= b; b ^= a; a ^= b;`, voir [[Opérateur bit à bit]]) : c'est une curiosité, moins lisible, plus lente sur un processeur moderne, et fausse si `a` et `b` désignent la même variable. En [[Langage C++|C++]], on écrit `std::swap(a, b);`. Pour échanger deux variables dans une fonction en C, il faut lui passer leurs adresses (voir [[3 - pointeurs , tableaux, listes chainées, structures]]). [[Complément hors du cours|ⓘ]]

## 2.9.c

D'après le code, l'exercice demande de faire tourner les valeurs de trois variables : `a` prend la valeur de `b`, `b` celle de `c`, `c` celle de `a`.

```c
#include <stdio.h>

int main() {
    int a = 1;
    int b = 2;
    int c = 3;
    int d;
    printf("a = %d\nb = %d\nc = %d\n", a, b, c);

    d = a;
    a = b;
    b = c;
    c = d;

    printf("a = %d\nb = %d\nc = %d\n", a, b, c);
    return 0;
}
```

Même principe que 2.8 : on sauvegarde dans `d` la seule valeur qui va être écrasée en premier, puis chaque variable reçoit la suivante. Sortie : `1 2 3` avant, `2 3 1` après (une permutation circulaire). Une seule variable temporaire suffit, quel que soit le nombre de variables à faire tourner.

## 2.10.c

D'après le code, l'exercice demande de lire le premier terme `a`, la raison `r` et le nombre de termes `nmax` d'une [[Suite arithmétique|suite arithmétique]], puis d'afficher ses termes, le dernier terme et la somme des termes. Une fonction `alternative` calcule la somme directement par la formule.

Deux corrections : le message de `main` annonçait `la suite est %d*n + %d` avec `a` puis `r`, soit `3*n + 2` pour les termes 3, 5, 7, 9, alors que le terme de rang `n` vaut $a + (n-1)r$ (ici $2n + 1$) : le message affiche désormais `u(n) = 3 + (n-1)*2`. La fonction `alternative` ne compilait pas : `;` manquant après le premier `printf`, condition du `if` sans parenthèses ; elle calculait la somme sans l'afficher et ne renvoyait rien. Le `;`, les parenthèses, un `printf` du résultat et `return 0;` sont ajoutés : [[Erreurs du cours#^e-tp2|✎]]

```c
#include <stdio.h>

int main(){
    int a;
    int r;
    int nmax;
    int somme=0;
    int l;

    scanf("%d", &a);
    scanf("%d", &r);
    scanf("%d", &nmax);

    printf("la suite est u(n) = %d + (n-1)*%d\n", a, r);
    printf("le nombre de termes est %d\n", nmax);

    for(int n=1; n<=nmax; n++){
        somme = somme + a+(n-1)*r;
        printf("le terme %d est %d\n", n, a+(n-1)*r);
    }

    l = a + (nmax-1)*r;
    printf("le dernier terme est %d\n", l);

    printf("la somme des termes est %d\n", somme);

    return 0;
}

int alternative(){

    int raison, start;
    int nb_termes;
    int last;
    float somme;

    printf("entrez la raison et la valeur du premier terme de la suite \n");
    scanf("%d", &raison);
    scanf("%d", &start);
    printf("entrez le nombre de termes de la suite \n");
    scanf("%d", &nb_termes);

    if (nb_termes <= 0) {
        printf("le nombre de termes doit être supérieur à 0\n");
        return 1;
    }

    last = start + (nb_termes-1)*raison;
    somme = (start + last) * nb_termes / 2;
    printf("la somme des termes est %f\n", somme);

    return 0;
}
```

**La boucle.** `for(int n=1; n<=nmax; n++)` répète le corps `nmax` fois, `n` allant de 1 à `nmax` (voir [[2 - structures code#4. Boucle `for`]]) ; `n++` utilise l'[[Opérateur d'incrémentation|opérateur d'incrémentation]], et `n`, déclaré dans le `for`, n'existe que dans la boucle ([[Portée d'une variable|portée]]). `somme`, initialisée à 0 avant la boucle et augmentée d'un terme à chaque tour, est un [[Accumulateur (programmation)|accumulateur]]. Avec l'entrée `3 2 4` : termes 3, 5, 7, 9, dernier terme 9, somme 24.

**La formule.** La somme des $n$ premiers termes d'une suite arithmétique vaut $S_n = \dfrac{n\,(u_1 + u_n)}{2}$ : nombre de termes × (premier + dernier) / 2, la même idée que la [[Somme des premiers entiers|somme des premiers entiers]] $1 + 2 + \dots + n = \frac{n(n+1)}{2}$. Ici $4 \times (3 + 9) / 2 = 24$. La boucle fait $n$ additions, la formule un nombre constant d'opérations : en [[Complexité algorithmique|complexité]], $O(n)$ contre $O(1)$. [[Complément hors du cours|ⓘ]]

**Division exacte.** Dans `alternative`, `(start + last) * nb_termes / 2` est une division entière, mais elle tombe toujours juste : si `nb_termes` est impair, `nb_termes - 1` est pair et `start + last` $= 2\,u_1 + (n-1)r$ est pair. Le `float somme` n'apporte donc rien ; un `int` suffirait. [[Complément hors du cours|ⓘ]]

**Une fonction jamais appelée.** `alternative` est une [[Fonction et procédure|fonction]] définie après `main` mais jamais appelée : elle est compilée mais ne s'exécute pas. Pour s'en servir, il faut un [[Appel de fonction|appel]] dans `main` (`alternative();`) et, puisqu'elle est définie après, une [[Déclaration et définition|déclaration]] (prototype `int alternative(void);`) avant `main` (voir [[2 - structures code#Règles pour que la compilation se passe bien]]). Sa valeur de retour, 1 en cas d'erreur, 0 sinon, suit la convention du [[Code de retour|code de retour]]. [[Complément hors du cours|ⓘ]]

## À retenir

- `int / int` est une division entière : `27 / 2` vaut `13`. Écrire `2.0` ou transtyper un opérande **avant** la division ([[Division euclidienne]], [[Transtypage]]).
- `scanf` attend des adresses (`&x`) et un format qui correspond au type : `%d` pour `int`, `%f` pour `float`, `%lf` pour `double` ([[Fonctions printf et scanf]]).
- Tester la valeur de retour de `scanf` évite de travailler sur une [[Variable non initialisée]] ([[Validation des entrées]]). [[Complément hors du cours|ⓘ]]
- Ne pas comparer deux flottants avec `==` : tester `fabs(x - y) < epsilon` ([[Comparaison de nombres flottants]]). [[Complément hors du cours|ⓘ]]
- Une chaîne littérale ne se coupe pas par un retour à la ligne ; un `;` oublié ou un `if` sans parenthèses sont des [[Erreur de compilation|erreurs de compilation]] : lire le premier message de [[GCC]], qui donne fichier, ligne et colonne.
- Échanger deux variables demande une variable temporaire ([[Échange de deux variables]]).
- Une fonction définie mais jamais appelée ne fait rien ; appelée avant sa définition, elle demande un prototype ([[Déclaration et définition]]).
- Compiler avec `-Wall -Wextra` : les [[Avertissement de compilation|avertissements]] signalent variables inutilisées et fonctions sans `return`. [[Complément hors du cours|ⓘ]]
