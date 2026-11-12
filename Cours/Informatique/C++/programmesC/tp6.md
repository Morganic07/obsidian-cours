---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp6/6.1.c|6.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp6/6.2.c|6.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp6/6.3.c|6.3.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 6 de [[Langage C|C]] (dossier `programmes C/tp6`, trois fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils appliquent le § 7 de [[2 - structures code]] : écrire ses propres [[Fonction et procédure|fonctions]], les déclarer par un **prototype** avant la [[Fonction main (C et C++)|fonction `main`]], les définir après, et récupérer leur résultat avec `return`. Les trois programmes contenaient une erreur, corrigée ci-dessous (✎). Ils ont été compilés avec [[GCC|`gcc`]] `-std=c17 -Wall -Wextra`.

## 6.1

D'après le code, l'exercice demande d'écrire une fonction `puissance(valeur, exposant)` qui calcule $valeur^{exposant}$ par une boucle, puis de l'appeler sur deux entiers saisis.

Dans le programme d'origine, `main` lit d'abord `e` puis `v` et appelle `puissance(e,v)` : l'exposant `e` était passé à la place de la valeur, et inversement (la saisie de `2` puis `10` affichait `1024`, soit $2^{10}$, au lieu de $10^2 = 100$). L'appel est corrigé en `puissance(v,e)`. [[Erreurs du cours#^e-tp6|✎]]

```c
#include <stdio.h>

int puissance(int valeur, int exposant);

int main(){
    int e, v;
    scanf("%d", &e);
    scanf("%d", &v);

    printf("%d", puissance(v,e));
    return 0;
}

int puissance(int valeur, int exposant){
    int resultat = 1;

    for (int i = 1; i <=exposant ; i++){
        resultat *= valeur;
    }

    return resultat;
}
```

Explications :

- **Prototype** : `int puissance(int valeur, int exposant);` annonce au [[Compilateur|compilateur]] le nom, le type de retour et les types des [[Argument et paramètre|paramètres]], ce qui permet d'appeler la fonction dans `main` avant sa définition (voir [[Déclaration et définition]]).
- **Correspondance par position** : à l'[[Appel de fonction|appel]], les arguments sont affectés aux paramètres **dans l'ordre**, quel que soit leur nom. `puissance(e, v)` met `e` dans `valeur` : c'est ce qui causait l'erreur. Chaque paramètre reçoit une copie de l'argument ([[Passage par valeur|passage par valeur]]).
- **Calcul** : `resultat` part de 1, élément neutre de la multiplication, et est multiplié `exposant` fois par `valeur` (`resultat *= valeur`, [[Opérateur d'affectation composée|affectation composée]]) : c'est un [[Accumulateur (programmation)|accumulateur]] multiplicatif. Pour `exposant = 0`, la boucle ne tourne pas et la fonction renvoie 1, conformément à $a^0 = 1$ ([[Exponentiation|exponentiation]]).
- **`return`** : l'[[Instruction return|instruction `return`]] renvoie la valeur à l'appelant ; l'appel `puissance(v,e)` est une [[Expression (programmation)|expression]] dont la valeur est passée directement à `printf`.

Limites de cette version : un exposant négatif renvoie 1 (la boucle ne tourne pas), alors que $a^{-n} = 1/a^n$ n'est pas un entier ; et le résultat déborde vite, puisqu'un `int` sur 32 bits ne dépasse pas $2^{31} - 1 \approx 2{,}1 \times 10^9$ : $10^{10}$ ou $2^{31}$ provoquent un [[Dépassement d'entier|dépassement d'entier]], [[Comportement indéfini|comportement indéfini]] pour un type signé. Le type `long long` (au moins 64 bits) repousse la limite à $\approx 9{,}2 \times 10^{18}$ (voir [[Type entier]]). [[Complément hors du cours|ⓘ]]

La boucle fait `exposant` multiplications. L'[[Exponentiation rapide|exponentiation rapide]] n'en fait qu'environ $2\log_2(exposant)$ en utilisant $a^{2k} = (a^k)^2$ et $a^{2k+1} = a \cdot (a^k)^2$, en version itérative ou [[Récursivité|récursive]]. Pour des réels, la [[Bibliothèque cmath|bibliothèque mathématique]] fournit `pow(x, y)` (`#include <math.h>`, option `-lm` à l'[[Édition de liens|édition de liens]] sous Linux), qui travaille en `double`. [[Complément hors du cours|ⓘ]]

Les deux `scanf` s'exécutent sans message : l'utilisateur ne sait pas quoi taper ni dans quel ordre. Un `printf("exposant puis valeur : ");` avant la saisie aurait évité la confusion. [[Complément hors du cours|ⓘ]]

## 6.2

D'après le code, l'exercice demande une fonction `NombreOrdonnes(a, b, c)` qui renvoie 1 si $a \leq b \leq c$ et 0 sinon, et un `main` qui la teste sur des triplets saisis jusqu'à ce qu'une des valeurs soit 0.

La fonction d'origine ne renvoyait rien quand une des valeurs était nulle (`if (a != 0 && b != 0 && c != 0) return (a<=b && b<=c);` sans autre `return`), alors que `main` affiche ce résultat : la valeur affichée était alors indéterminée. Le test est retiré et la fonction renvoie toujours la comparaison. [[Erreurs du cours#^e-tp6|✎]]

```c
#include <stdio.h>

int NombreOrdonnes(int a,int b, int c);

int main(){
    int a1 ;
    int a2;
    int a3;

    do{
        printf("Entrez 3 valeurs : \n");
        scanf("%d", &a1);
        scanf("%d", &a2);
        scanf("%d", &a3);
        printf("%d \n", NombreOrdonnes(a1, a2, a3));
    }while (a1 != 0 && a2 != 0 && a3 != 0);

    return 0;
}

int NombreOrdonnes(int a,int b, int c){
    return (a<=b && b<=c);
}
```

Sortie pour `1 2 3`, `3 2 1`, `0 1 2` : `1`, `0`, `1`, puis le programme s'arrête.

Explications :

- **Une condition est une valeur.** En C, une comparaison vaut 1 si elle est vraie, 0 sinon ([[Booléen]]) : `return (a<=b && b<=c);` renvoie directement 1 ou 0, sans `if`. L'[[Opérateur logique|opérateur logique]] `&&` combine les deux [[Opérateur de comparaison|comparaisons]] ; c'est l'écriture correcte de l'encadrement que `a <= b <= c` ne fait pas (voir [[tp5]], 5.3).
- **Fonction qui ne renvoie rien sur un chemin.** Une fonction déclarée `int` doit exécuter un `return` avec une valeur sur tous ses chemins. En C, sortir par l'accolade finale sans `return` n'est pas une [[Erreur de compilation|erreur de compilation]], mais utiliser ensuite la valeur renvoyée (ici, dans le `printf`) est un [[Comportement indéfini|comportement indéfini]] (norme C17, § 6.9.1, al. 12). `gcc -Wall` le signale : `warning: control reaches end of non-void function`.
- **Arrêt** : la boucle `do … while` s'arrête dès qu'une des trois valeurs vaut 0 ; le triplet qui contient le 0 est quand même évalué et affiché, puisque le test est en fin de boucle. Le 0 joue le rôle de [[Valeur sentinelle|valeur sentinelle]].

`&&` est évalué en court-circuit ([[Évaluation en court-circuit]]) : si `a <= b` est faux, `b <= c` n'est pas évalué. Le nom `NombreOrdonnes` suit la convention de [[Casse chameau|casse chameau]] avec une majuscule initiale, d'habitude réservée aux types ; `nombresOrdonnes` ou `nombres_ordonnes` sont plus courants pour une fonction en C (voir [[Règle de codage]]). [[Complément hors du cours|ⓘ]]

Pour ne pas afficher de résultat pour le triplet d'arrêt, on teste la sentinelle juste après la saisie : `if (a1 == 0 || a2 == 0 || a3 == 0) break;`, puis `while (1)` comme condition. [[Complément hors du cours|ⓘ]]

## 6.3

D'après le code, l'exercice demande trois fonctions de calcul de [[Volume (géométrie)|volume]] (cube, cylindre, sphère) et une fonction `volume(type, valeur)` qui choisit la bonne selon le type saisi (1 cube, 2 cylindre, 3 sphère), dans une boucle arrêtée par le type 0.

Trois erreurs sont corrigées dans le code ci-dessous. [[Erreurs du cours#^e-tp6|✎]]

- La formule du cylindre était $\pi h r$ ; elle devient $\pi r^2 h$ (`*hauteur*rayon*rayon`).
- La formule de la sphère était $\frac{3}{4}\pi r^3$ ; elle devient $\frac{4}{3}\pi r^3$ (`(4.0/3.0)`).
- `volume` ne renvoyait rien pour un type autre que 1, 2 ou 3 (en particulier pour le type 0 qui arrête la boucle, dont le résultat est affiché) ; un `return 0;` final est ajouté. Son prototype `int volume();` devient `int volume(int type, int valeur);`.

```c
#include <stdio.h>
#include <math.h>

int volumeCube(int arete);
float volumeCylindre(int hauteur, int rayon);
float volumeSphere(int rayon);
int volume(int type, int valeur);

int main(){
    int type;
    int valeur;

    do{
        printf("\nrentrez un type\n");
        scanf("%d", &type);
        printf("rentrez une valeur\n");
        scanf("%d", &valeur);
        printf("%d",volume(type, valeur));
    }while (type !=0);

    return 0;
}

int volumeCube(int arete){
    return arete*arete*arete;
}

float volumeCylindre(int hauteur, int rayon){
    return 3.14159265358979323846*hauteur*rayon*rayon;
}

float volumeSphere(int rayon){
    return (4.0/3.0)*3.14159265358979323846*rayon*rayon*rayon;
}

int volume(int type, int valeur){
    if (type ==1) return volumeCube(valeur);
    else if (type ==2) {
        int rayon;
        printf("rentrer le rayon : \n");
        scanf("%d", &rayon);
        return volumeCylindre(valeur, rayon);
    }
    else if (type == 3) return volumeSphere(valeur);

    return 0;
}
```

Sortie corrigée : cube d'arête 3 → `27` ; cylindre de hauteur 2 et de rayon 3 → `56` ($18\pi \approx 56{,}5$, contre `18` avant correction) ; sphère de rayon 3 → `113` ($36\pi \approx 113{,}1$, contre `63` avant).

Explications :

- **Formules** ([[Volume (géométrie)]]) : cube $a^3$, cylindre $\pi r^2 h$ (aire du disque de base fois la hauteur), sphère $\frac{4}{3}\pi r^3$. $\pi$ ([[Nombre pi]]) est écrit en [[Valeur littérale|littéral]] avec 20 décimales, bien plus que les 15 à 17 chiffres significatifs d'un `double` ([[Norme IEEE 754]]) : les décimales en trop sont simplement arrondies.
- **`4.0/3.0` et non `4/3`** : entre deux entiers, `/` est une division entière, et `4/3` vaut 1 ([[Division euclidienne]]). Écrire au moins un des opérandes en `double` (`4.0`) force la division réelle ; le code d'origine l'avait bien fait avec `3.0/4.0`.
- **Prototype vide** : en C17, `int volume();` déclare une fonction **sans préciser ses paramètres** (déclaration à l'ancienne, non prototypée) : le [[Compilateur|compilateur]] ne vérifie alors ni leur nombre ni leur type à l'appel. Depuis C23, `()` signifie « aucun paramètre » comme en [[Langage C++|C++]], et `gcc -std=c23` refuse ce programme (`too many arguments to function 'volume'`). Le prototype complet est la forme correcte dans toutes les versions de la [[Norme du C|norme]] ; pour une fonction sans paramètre, on écrit `(void)` (voir [[Déclaration et définition]]).
- **Conversions** : `volumeCylindre` calcule en `double`, renvoie un `float`, que `volume` convertit en `int` en renvoyant : la partie décimale est tronquée vers zéro (56,5 → 56, voir [[Partie entière]]). Ces conversions implicites ([[Transtypage]]) d'un [[Nombre à virgule flottante|réel]] vers un [[Type entier|entier]] font perdre de la précision sans message, sauf avec l'[[Option de compilation|option]] `-Wconversion`.
- **Fonction qui ne renvoie rien** : même défaut ([[Comportement indéfini|comportement indéfini]]) et même [[Avertissement de compilation|avertissement]] qu'en 6.2.

Pour garder les décimales, `volume` devrait renvoyer un `double` et `main` l'afficher avec `printf("%.2f", …)` ([[Fonctions printf et scanf]]). `math.h` est inclus mais pas utilisé : il fournirait `pow(rayon, 3)` et, sous [[Linux]] avec la glibc ([[Bibliothèque standard du C|bibliothèque standard du C]] de GNU), la [[Macro (préprocesseur)|macro]] `M_PI`, qui n'appartient pas à la norme C (elle vient de la norme [[POSIX]]) ; le plus portable reste de définir sa propre [[Constante (programmation)|constante]], `#define PI 3.14159265358979323846` ou `const double PI = …;`. [[Complément hors du cours|ⓘ]]

Le choix entre les types s'écrit plus lisiblement avec un `switch (type) { case 1: … case 2: … default: return 0; }` ([[Structure conditionnelle]], § 3 de [[2 - structures code]]), le `default` traitant tous les types inconnus. [[Complément hors du cours|ⓘ]]

`volume` fait deux choses : elle choisit le calcul et, pour le cylindre, elle demande le rayon à l'utilisateur. Cette saisie cachée dans une fonction de calcul est un [[Effet de bord|effet de bord]] qui rend la fonction impossible à réutiliser ou à tester sans clavier ; il vaut mieux lire toutes les valeurs dans `main` et passer le rayon en paramètre ([[Principe de responsabilité unique|principe de responsabilité unique]], [[Décomposition fonctionnelle|décomposition fonctionnelle]]). [[Complément hors du cours|ⓘ]]

## À retenir

- Une [[Fonction et procédure|fonction]] se **déclare** (prototype, terminé par `;`) avant son premier appel et se **définit** une fois ([[Déclaration et définition]]) ; le prototype doit lister les types des paramètres, `(void)` s'il n'y en a pas.
- Les [[Argument et paramètre|arguments]] sont associés aux paramètres **par position**, jamais par nom.
- Une fonction non `void` doit exécuter [[Instruction return|`return valeur;`]] sur **tous** ses chemins ; `warning: control reaches end of non-void function` signale un oubli.
- Une [[Opérateur de comparaison|comparaison]] vaut 0 ou 1 ([[Booléen]]) : `return (a <= b && b <= c);` suffit.
- `4/3` vaut 1 ([[Division euclidienne|division entière]]) : écrire `4.0/3.0` pour une division réelle.
- Un résultat réel renvoyé dans un `int` est tronqué sans avertissement ([[Transtypage|conversion implicite]]). [[Complément hors du cours|ⓘ]]
- Une fonction de calcul ne fait ni saisie ni affichage ([[Effet de bord|effets de bord]]) : elle reçoit ses données en paramètres et renvoie son résultat. [[Complément hors du cours|ⓘ]]
