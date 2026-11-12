---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.1.c|3.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.2.c|3.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.3.c|3.3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.4.c|3.4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.5.c|3.5.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.6.c|3.6.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.7.c|3.7.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.8.c|3.8.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.9.c|3.9.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.10.c|3.10.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.11.c|3.11.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp3/3.12.c|3.12.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 3 de [[Langage C|C]] (dossier `programmes C/tp3`, 12 fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils portent sur les conditions, sujet des sections 1 à 3 de [[2 - structures code]] : [[Opérateur de comparaison|opérateurs de comparaison]], [[Opérateur logique|opérateurs logiques]] `&&`, `||`, `!`, [[Structure conditionnelle|structure conditionnelle]] `if … else if … else`, puis `switch … case` ; ils réutilisent les [[Fonctions printf et scanf|fonctions `printf` et `scanf`]] de [[1 - basiques]] et l'opérateur modulo `%`. Les fichiers n'ont pas de commentaires : l'énoncé est reconstitué d'après le code. Chaque programme a été compilé avec [[GCC]] (`gcc -std=c17 -Wall -Wextra`) et exécuté ; trois ne compilaient pas et sont corrigés ci-dessous.

## 3.1.c

D'après le code, l'exercice demande d'afficher le plus petit de deux nombres.

```c
#include <stdio.h>

int main(){
    int a = 1;
    int b = 2;
    int nbmin;

    if (a>b) {
        nbmin = b;
    }
    else {
        nbmin = a;
    }

    printf("le plus petit est %d\n", nbmin);

    return 0;
}
```

C'est la [[Recherche du minimum et du maximum|recherche du minimum]] la plus simple : un `if … else` à deux branches, deux [[Bloc d'instructions|blocs d'instructions]] dont un seul s'exécute. Sortie : `le plus petit est 1`. En cas d'égalité, `a>b` est faux et `nbmin` reçoit `a`, ce qui est juste puisque les deux valeurs sont égales.

L'[[Opérateur conditionnel|opérateur ternaire]] écrit le même calcul en une [[Expression (programmation)|expression]] : `int nbmin = (a > b) ? b : a;`. [[Complément hors du cours|ⓘ]]

## 3.2.c

D'après le code, l'exercice demande d'afficher le plus petit de trois nombres.

```c
#include <stdio.h>

int main(){
    int a = 1;
    int b = 2;
    int c = 3;
    int nbmin;

    if (a>=b && c>=b) {
        nbmin = b;
    }
    else if (a>=c && b>=c) {
        nbmin = c;
    }
    else {
        nbmin = a;
    }

    printf("le plus petit est %d\n", nbmin);

    return 0;
}
```

`b` est le minimum s'il est inférieur ou égal aux deux autres : les deux comparaisons sont reliées par le ET logique `&&`. La chaîne `else if` ne teste la condition suivante que si la précédente est fausse ; le dernier `else` couvre le cas restant, où `a` est forcément le minimum. Sortie : `le plus petit est 1`. Les `>=` (et non `>`) garantissent qu'une égalité ne laisse aucun cas sans réponse.

Une version qui passe mieux à l'échelle garde un minimum provisoire : `nbmin = a; if (b < nbmin) nbmin = b; if (c < nbmin) nbmin = c;`. Elle fait $n-1$ comparaisons pour $n$ valeurs et se généralise à un [[Tableau (programmation)|tableau]] avec une [[Boucle (programmation)|boucle]]. [[Complément hors du cours|ⓘ]]

## 3.3.c

D'après le code, l'exercice demande d'afficher le plus grand de trois nombres. Le fichier d'origine ne compilait pas : le `;` manquait après `int nbmax` ([[GCC]] signale `expected '=', ',', ';', 'asm' or '__attribute__' before 'if'`, à la ligne **suivante**). De plus, `a`, `b` et `c` étaient comparés sans avoir reçu de valeur, et le résultat n'était pas affiché. Le `;`, une lecture des trois nombres et l'affichage sont ajoutés : [[Erreurs du cours#^e-tp3|✎]]

```c
#include <stdio.h>

int main(){
    int a,b,c;
    int nbmax;

    scanf("%d %d %d", &a, &b, &c);

    if (a>=b && a >= c) {
        nbmax = a;
    }
    else if (b>=a && b>=c) {
        nbmax = b;
    }
    else {
        nbmax = c;
    }

    printf("le plus grand est %d\n", nbmax);

    return 0;
}
```

Même structure que 3.2, comparaisons inversées. Avec `4 9 2`, la sortie est `le plus grand est 9`.

Lire une [[Variable non initialisée|variable non initialisée]] est un [[Comportement indéfini|comportement indéfini]] : une variable locale contient ce qui traînait dans la [[Pile d'exécution|pile]], et le résultat peut changer d'une exécution à l'autre (voir [[1 - basiques#Afficher une variable non initialisée]]). Une [[Erreur de compilation|erreur de compilation]] est souvent signalée sur la ligne qui suit l'oubli : le compilateur ne s'aperçoit qu'il manque un `;` qu'en lisant le mot suivant. [[Complément hors du cours|ⓘ]]

## 3.4.c

D'après le code, l'exercice demande d'afficher le signe du produit de deux nombres sans forcément le calculer ; la fonction `alternative` le fait en calculant `a*b`. Le fichier d'origine ne compilait pas : `else if (a>0 && b<0)||(a<0 && b>0)` met entre parenthèses la première moitié de la condition seulement, et le `||` se retrouve hors du `if` (`expected expression before '||' token`). Toute la condition est remise entre parenthèses ; `return 0;`, qui manquait à la fin d'`alternative`, est ajouté : [[Erreurs du cours#^e-tp3|✎]]

```c
#include <stdio.h>

int main(){

    int a = 1;
    int b = -2;

    if (a>0 && b>0) {
        printf("le produit des deux nombres est positif\n");
    }
    else if (a<0 && b<0) {
        printf("le produit des deux nombres est positif\n");
    }
    else if ((a>0 && b<0)||(a<0 && b>0)) {
        printf("le produit des deux nombres est négatif\n");
    }

    else if (a==0 || b==0) {
        printf("le produit des deux nombres est nul\n");
    }

    return 0;
}

int alternative(){

    int a = 1;
    int b = -2;

    if (a*b>0) {
        printf("le produit des deux nombres est positif\n");
    }
    else if (a*b<0) {
        printf("le produit des deux nombres est négatif\n");
    }
    else {
        printf("le produit des deux nombres est nul\n");
    }

    return 0;
}
```

En C, la condition d'un `if` s'écrit **tout entière** entre parenthèses : `if (condition)`. Pour combiner des conditions, on ajoute des parenthèses à l'intérieur : `if ((A) || (B))`. Sortie : `le produit des deux nombres est négatif`.

La règle des signes du produit : positif si les deux facteurs ont le même signe, négatif s'ils sont de signes contraires, nul si l'un est nul. Le dernier `else if (a==0 || b==0)` pourrait être un simple `else`, puisque c'est le seul cas restant. Les deux premières branches se fusionnent en `(a>0 && b>0) || (a<0 && b<0)`. [[Complément hors du cours|ⓘ]]

`alternative` est plus courte, mais le calcul de `a*b` peut provoquer un [[Dépassement d'entier|dépassement d'entier]] (par exemple `100000 * 100000` dépasse $2^{31}-1$), qui est un comportement indéfini pour les `int` : la version par comparaisons de `main` n'a pas ce défaut. Comme dans le TP 2, la [[Fonction et procédure|fonction]] `alternative` ne fait l'objet d'aucun [[Appel de fonction|appel]] : elle n'est jamais exécutée. [[Complément hors du cours|ⓘ]]

## 3.5.c

D'après le code, l'exercice demande de lire un âge et de dire si la personne peut voter, en écrivant la condition de trois façons.

```c
#include <stdio.h>

int main(){

    int age;
    printf("entrez votre age: ");
    scanf("%d", &age);

    if (age>=18) {
        printf("peut voter\n");
    }
    else {
        printf("ne peut pas voter\n");
    }

    if (age<18) {
        printf("ne peut pas voter\n");
    }
    else {
        printf("peut voter\n");
    }

    if (!(age>=18)) {
        printf("ne peut pas voter\n");
    }
    else {
        printf("peut voter\n");
    }

    return 0;
}
```

Les trois tests sont équivalents, car une comparaison vaut 1 (vrai) ou 0 (faux), comme un [[Booléen|booléen]] : `age >= 18`, sa négation `age < 18` en échangeant les branches, et `!(age >= 18)` avec le NON logique `!`. Avec `17`, chacun affiche `ne peut pas voter`. En France, le [[Droit de vote|droit de vote]] s'acquiert à 18 ans, âge de la majorité depuis la loi du 5 juillet 1974. [[Complément hors du cours|ⓘ]]

La négation d'une comparaison inverse le sens **et** l'inclusion de l'égalité : le contraire de `>=` est `<`, pas `<=`. Pour une condition composée, les [[Lois de De Morgan|lois de De Morgan]] donnent `!(A && B)` = `!A || !B` et `!(A || B)` = `!A && !B`. Le seuil `18` écrit en dur est un [[Nombre magique (programmation)|nombre magique]] : mieux vaut une [[Constante (programmation)|constante]] nommée (`const int AGE_VOTE = 18;`, ou une [[Macro (préprocesseur)|macro]] `#define AGE_VOTE 18`, remplacée par le [[Préprocesseur|préprocesseur]] avant la compilation). [[Complément hors du cours|ⓘ]]

## 3.6.c

D'après le code, l'exercice demande d'afficher la [[Mention (diplôme)|mention]] correspondant à une moyenne sur 20.

```c
#include <stdio.h>

int main(){
    float moyenne = 10;

    if (moyenne < 10) {
        printf("recalé");
    }

    else if (10 <= moyenne && moyenne < 12) {
        printf("passable");
    }

    else if (12 <= moyenne && moyenne < 14){
        printf(" assez bien");
    }

    else if (14 <= moyenne && moyenne < 16){
        printf("bien");
    }

    else if (16 <= moyenne){
        printf("tres bien");
    }

    return 0;
}
```

Chaque intervalle $[10, 12[$, $[12, 14[$… s'écrit avec deux comparaisons reliées par `&&` : en C, `10 <= moyenne < 12` ne teste **pas** l'intervalle (voir [[1 - basiques#Triple égalité `a == b == c`]]). Avec `moyenne = 10`, la sortie est `passable`.

Dans une chaîne `else if`, chaque branche n'est atteinte que si les précédentes ont échoué : la borne basse est déjà acquise, et l'on peut écrire `else if (moyenne < 12)`, `else if (moyenne < 14)`… puis un `else` final. Le programme ne traite pas les valeurs hors de $[0, 20]$, qu'une [[Validation des entrées|validation des entrées]] rejetterait. [[Complément hors du cours|ⓘ]]

## 3.7.c

D'après le code, l'exercice demande de lire un entier et de dire s'il est pair ou impair.

```c
#include <stdio.h>

int main(){

    int chiffre;

    scanf("%d", &chiffre);

    int modulo = chiffre%2;

    if (modulo == 0){
        printf("pair");
    }

    else{
        printf("impair");
    }

    return 0;
}
```

L'[[Opérateurs arithmétiques|opérateur modulo]] `%` donne le reste de la [[Division euclidienne|division entière]] : un entier est pair si son reste dans la division par 2 est nul ([[Parité d'un entier|parité]]). Avec `7`, la sortie est `impair`. Depuis C99, une variable peut être déclarée au milieu d'un bloc, comme `int modulo` ici.

En C, le reste a le signe du dividende : `-7 % 2` vaut `-1`, pas `1`. Le test `n % 2 == 0` reste donc juste pour les négatifs, mais `n % 2 == 1` échouerait sur `-7`. En mathématiques, on dit que $n$ est pair si $n \equiv 0 \pmod 2$ ([[Congruence modulo n|congruence modulo 2]]). [[Complément hors du cours|ⓘ]]

## 3.8.c

D'après le code, l'exercice demande de lire une année et de dire si elle est [[Année bissextile|bissextile]].

```c
#include <stdio.h>

int main(){
    int annee;

    scanf("%d", &annee);

    if (annee%4==0 && annee%100!=0 || annee%400==0){
        printf("bissextile");
    }

    else{
        printf("non bissextile");
    }

    return 0;
}
```

Une année est bissextile si elle est divisible par 4 sans l'être par 100, ou si elle est divisible par 400. Sorties vérifiées : 1900 non bissextile, 2000 bissextile, 2024 bissextile, 2026 non bissextile.

La condition est juste sans parenthèses parce que `&&` a une [[Associativité et ordre d'évaluation|priorité]] plus forte que `||` (comme le ET devant le OU dans la [[Priorité des connecteurs logiques|priorité des connecteurs logiques]]) : elle se lit `(annee%4==0 && annee%100!=0) || annee%400==0`. GCC émet pourtant l'[[Avertissement de compilation|avertissement]] `suggest parentheses around '&&' within '||'` : écrire ces parenthèses rend l'intention lisible. [[Complément hors du cours|ⓘ]]

Cette règle est celle du [[Calendrier grégorien|calendrier grégorien]], instauré en 1582 : 97 années bissextiles tous les 400 ans donnent une année moyenne de 365,2425 jours, proche de l'année tropique (environ 365,2422 jours). Les opérateurs `&&` et `||` pratiquent l'[[Évaluation en court-circuit|évaluation en court-circuit]] : si `annee%4==0` est faux, `annee%100!=0` n'est pas évalué. [[Complément hors du cours|ⓘ]]

## 3.9.c

D'après le code, l'exercice demande de tester la parité **sans** l'opérateur modulo, par la division entière.

```c
#include <stdio.h>

int main(){
    int nombre = 13;

    int div = nombre/2;

    printf("%d", div);

    if (div*2==nombre) {
        printf("pair");
    }

    else{
        printf("impair");
    }

    return 0;
}
```

`13/2` vaut `6` ([[Division euclidienne|division entière]]) et `6*2` vaut `12` ([[Opérateurs arithmétiques|opérateurs arithmétiques]] `/` et `*`), différent de `13` : le nombre est impair. Le `printf("%d", div)`, affichage de contrôle laissé dans le code, colle le quotient au résultat : la sortie est `6impair`. Pour une trace de [[Bogue (informatique)|débogage]], on ajoute une étiquette et un retour à la ligne (`printf("div = %d\n", div);`), puis on la retire.

Plutôt que des `printf` de contrôle, un [[Débogueur|débogueur]] comme `gdb` permet d'arrêter le programme et d'afficher les variables sans modifier le code (compiler avec l'option `-g`). [[Complément hors du cours|ⓘ]]

Le test repose sur l'égalité de la division euclidienne $n = 2q + r$ : $n$ est pair si et seulement si $2q = n$. Une troisième façon, bit à bit, regarde le bit de poids faible : `(nombre & 1) == 0` (voir [[Opérateur bit à bit]]). [[Complément hors du cours|ⓘ]]

## 3.10.c

D'après le code, l'exercice demande d'écrire en toutes lettres un chiffre de 1 à 3, et `autre` sinon, avec un `switch`.

```c
#include <stdio.h>

int main(){
    int chiffre = 8;

    switch(chiffre) {
        case 1:
            printf("un");
            break;
        case 2:
            printf("deux");
            break;
        case 3:
            printf("trois");
            break;
        default:
            printf("autre");
    }

    return 0;
}
```

Le `switch` compare la valeur entière à chaque `case` et saute au premier qui correspond ; `default` s'exécute si aucun ne correspond (voir [[2 - structures code#3. `switch ... case`]]). Le `break` fait sortir du `switch` : sans lui, l'exécution continuerait dans le `case` suivant. Avec `chiffre = 8`, la sortie est `autre`. `switch`, `case`, `default` et `break` sont des [[Mot réservé|mots réservés]] ([[Instructions break et continue]]).

Quand les valeurs sont proches les unes des autres, le compilateur traduit souvent un `switch` en [[Table de sauts|table de sauts]] : l'adresse du code à exécuter est lue directement dans un tableau indexé par la valeur, au lieu de tester les cas un par un. [[Complément hors du cours|ⓘ]]

## 3.11.c

D'après le code, l'exercice demande de lire une magnitude sur l'[[Échelle de Richter|échelle de Richter]] et d'afficher la description des effets du [[Séisme|séisme]]. Le fichier d'origine ne compilait pas : `case richter>9:` n'est pas une constante (`case label does not reduce to an integer constant`). Le test `richter > 9` passe dans le `default` : [[Erreurs du cours#^e-tp3|✎]]

```c
#include <stdio.h>

int main(){
    int richter;

    scanf("%d", &richter);

    switch(richter){
        case 1:
            printf("Micro-séisme impossible à ressentir.");
            break;
        case 2:
            printf("Micro-séisme impossible à ressentir mais enregistrable par les sismomètres.");
            break;
        case 3:
            printf("Ne cause pas de dégats mais commence à pouvoir être légèrement ressenti.");
            break;
        case 4:
            printf("Séisme capable de faire bouger des objets mais ne causant généralement pas de dégats.");
            break;
        case 5:
            printf("Séisme capable d'engendrer des dégats importants sur de vieux bâtiments ou bien des bâtiments présentants des défauts de construction. Peu de dégats sur des bâtiments modernes.");
            break;
        case 6:
            printf("Fort séisme capable d'engendrer des destructions majeures sur une large distance (180 km) autour de l'épicentre.");
            break;
        case 7:
            printf("Séisme capable de destructions majeures à modérées sur une très large zone en fonction de la distance.");
            break;
        case 8:
            printf("Séisme capable de destructions majeures sur une très large zone de plusieurs centaines de kilomètres.");
            break;
        case 9:
            printf("Séisme capable de tout détruire sur une très vaste zone.");
            break;
        default:
            if (richter > 9) printf("apocalypse.");
            else printf("Valeur incorrecte");
    }

    return 0;
}
```

Chaque `case` doit être une [[Expression constante|expression constante]] entière, connue à la compilation (`case 6:`, `case 'a':`, ou une valeur d'[[Énumération (programmation)|énumération]]) : un `switch` ne teste que des égalités, jamais une comparaison ni un intervalle. Sorties vérifiées : `9` donne la dernière description, `10` donne `apocalypse.`, `0` donne `Valeur incorrecte`.

GCC accepte aussi, en extension non standard, des plages `case 10 ... 100:` ; en C standard, un intervalle passe par un `if`. Les messages pourraient aussi être rangés dans un [[Tableau (programmation)|tableau]] de [[Chaîne de caractères|chaînes]] indexé par la magnitude, `messages[richter - 1]` : c'est une [[Table de correspondance|table de correspondance]], qui remplace neuf `case` par une ligne. Les accents des messages s'affichent correctement si le terminal et le fichier source sont tous deux en [[Unicode|UTF-8]]. [[Complément hors du cours|ⓘ]]

La magnitude est un nombre réel (un séisme de magnitude 6,4), que `scanf("%d")` tronque ; l'échelle est ouverte, sans maximum. C'est une [[Échelle logarithmique|échelle logarithmique]] : un degré de plus multiplie par 10 l'amplitude des ondes enregistrées et par environ 32 l'énergie libérée. Pour les forts séismes, les sismologues utilisent aujourd'hui la [[Magnitude de moment|magnitude de moment]] $M_w$, l'échelle de Richter saturant au-delà d'environ 7. [[Complément hors du cours|ⓘ]]

## 3.12.c

D'après le code, l'exercice demande de traduire une touche de déplacement (8, 2, 4, 6) en direction (nord, sud, ouest, est).

```c
#include <stdio.h>

int main(){

    int deplacement;

    scanf("%d", &deplacement);

    switch(deplacement){
        case 6:
            printf("est");
            break;
        case 4:
            printf("ouest");
            break;
        case 2:
            printf("sud");
            break;
        case 8:
            printf("nord");
            break;
        default:
            printf("deplacement non reconnu");
    }
    return 0;
}
```

Les `case` n'ont pas besoin d'être dans l'ordre ; chacun est une [[Valeur littérale|valeur littérale]] entière. Avec `8`, la sortie est `nord`. Les chiffres correspondent à la disposition du [[Pavé numérique|pavé numérique]] : 8 en haut, 2 en bas, 4 à gauche, 6 à droite, une convention de nombreux jeux. [[Complément hors du cours|ⓘ]]

## À retenir

- La condition d'un `if` est **entièrement** entre parenthèses : `if ((A) || (B))` ([[Structure conditionnelle]]).
- Un intervalle s'écrit `10 <= x && x < 12`, jamais `10 <= x < 12` ([[Opérateur de comparaison]]).
- `&&` passe avant `||` ; des parenthèses explicites évitent l'avertissement et les erreurs de lecture ([[Associativité et ordre d'évaluation]]).
- Le contraire de `>=` est `<` ; pour nier une condition composée, appliquer De Morgan ([[Lois de De Morgan]]). [[Complément hors du cours|ⓘ]]
- `n % 2 == 0` teste la parité, y compris pour les négatifs ; `n % 2 == 1` échoue sur un négatif impair ([[Parité d'un entier]]). [[Complément hors du cours|ⓘ]]
- Un `case` est une constante entière ; une comparaison ou un intervalle va dans un `if`, éventuellement placé dans le `default`.
- Ne pas oublier `break` à la fin de chaque `case`, sauf regroupement voulu ([[Instructions break et continue]]).
- Une variable non initialisée n'a pas de valeur utilisable : la lire est un [[Comportement indéfini]].
- Une erreur de compilation est souvent signalée à la ligne qui **suit** l'oubli d'un `;`. [[Complément hors du cours|ⓘ]]
