---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]] (TP « Processes », *Lesson 05*, daté du 11/03/2024 dans la note), dans [[Operating System (index)]]. Il apprend à programmer en [[Langage C|C]] avec les [[Processus]]. Les énoncés sont recopiés, suivis du code de l'étudiante (captures d'écran de code, recopiées ici en texte ; pas d'image à intégrer). Aucun corrigé officiel.

## Énoncés

- **Lab 1** : programme C qui lit deux entiers, range leur somme dans une troisième variable et l'affiche. Compiler avec [[GCC]].
- **Lab 2** : lire un entier et afficher tous les nombres impairs de 1 jusqu'à cette borne. Compiler avec GCC.
- **Lab 3** : lire deux entiers, une borne (*range*) et une raison (*common difference*, voir [[Suite arithmétique]]) ; afficher une suite partant de 1, chaque terme augmentant de la raison, jusqu'à atteindre ou dépasser la borne.
- **Lab 4** : utiliser `fork()` ([[Appel fork()]], [[Création et terminaison de processus]]) pour créer un fils ; parent et fils affichent leur [[Identifiant de processus|PID]] et un message ; vérifier que le fils est bien créé et que les deux processus se terminent proprement.
- **Lab 5** : créer avec `fork()` l'[[Arbre de processus]] suivant : A crée B et C ; B crée D et E ; E crée F ; C crée K ; K crée L ; L crée M.
- **Lab 6** : créer deux processus ; l'un affiche la table de multiplication de 5, l'autre celle de 7.
- **Lab 7** : deux processus ; le parent lit une saisie et affiche les [[Nombre premier|nombres premiers]] ; le fils lit une saisie et affiche la [[Factorielle|factorielle]]. Le fils s'exécute d'abord, le parent attend qu'il ait fini.
- **Lab 8** : « mettre à jour le Lab 3 » pour que fils et parent s'exécutent en même temps (*concurrently*). La note ne contient pas de code pour ce lab.

## Lab 1 : somme de deux entiers

Lecture avec `scanf`, affichage avec `printf` ([[Fonctions printf et scanf]]).

```c
#include <stdio.h>

int lab1(void){
    int a = 0;
    int b = 0;
    printf("entrez premier nombre : ");
    scanf("%d",&a);
    printf("Entrez deuxieme nombre : ");
    scanf("%d", &b);
    int c = b+a;
    printf("La somme est %d\n", c);
}
```

## Lab 2 : nombres impairs

Boucle `for` qui part de 1 avec un pas de 2.

```c
int lab2(int lim){
    for (int i = 1; i <= lim; i += 2) {
        printf("%d, ", i);
    }
    printf("\n");
    return 0;
}
```

## Lab 3 : suite arithmétique

```c
void lab3(int lim, int increment){
    int sum = 0;
    while (sum <= lim) {
        printf("%d, ", sum);
        sum += increment;
    }
    printf("\n");
}
```

(La suite part de 0 et non de 1 : voir point à vérifier 5.)

## Lab 4 : `fork()` et attente du fils

Méthode :
1. `fork()` renvoie `-1` en cas d'erreur, `0` dans le fils, et le PID du fils dans le parent ; un `switch` distingue les trois cas.
2. `getpid()` donne le PID du processus courant.
3. Le parent attend le fils avec `wait(&status)` ([[Appels wait() et waitpid()]]), puis lit le code de sortie : `WIFEXITED(status)` vrai si le fils s'est terminé normalement, `WEXITSTATUS(status)` donne son code de sortie.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    int status;

    switch(pid){
        case -1:
            printf("Erreur du processus");
            break;
        case 0:
            printf("Processus enfant, pid : %d, %d\n", pid, getpid());
            break;
        default:
            printf("Processus parent, pid de l'enfant : %d\n", pid);
            printf("Processus parent, pid du parent : %d\n", getpid());
            wait(&status);
            if (WIFEXITED(status)) {
                printf("Le processus enfant s'est terminé avec le code de sortie %d\n", WEXITSTATUS(status));
            }
            else {
                printf("Le processus enfant ne s'est pas terminé correctement.\n");
            }
            printf("Processus parent terminé.\n");
            break;
    }
}
```

## Lab 5 : arbre de processus

Méthode : `fork()` imbriqués. Chaque fils fait son travail (afficher son nom, créer ses propres fils), puis **termine par `exit(0)`** pour ne pas exécuter la suite du code de son parent ; chaque parent attend son fils avec `waitpid(pid, &status, 0)`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    printf("I'm process A\n");
    int status;

    pid_t b = fork();
    if(b==0){
        printf("I'm process B inside process A\n");

        pid_t d = fork();
        if(d==0){
            printf("Im process D inside process B\n");
            exit(0);
        }
        waitpid(d, &status, 0);

        pid_t e = fork();
        if(e==0){
            printf("I'm process E, inside process B\n");

            pid_t f = fork();
            if(f==0){
                printf("I'm process F, inside process E\n");
                exit(0);
            }
            waitpid(f, &status, 0);
            exit(0);
        }
        waitpid(e, &status, 0);
        exit(0);
    }
    waitpid(b, &status, 0);

    pid_t c = fork();
    if(c==0){
        printf("I'm process C, inside process A\n");

        pid_t k = fork();
        if(k==0){
            printf("I'm process K, inside process C\n");

            pid_t l = fork();
            if(l==0){
                printf("I'm process L, inside process K\n");

                pid_t m = fork();
                if(m==0){
                    printf("I'm process M, inside process L\n");
                    exit(0);
                }
                waitpid(m, &status, 0);
                exit(0);
            }
            waitpid(l, &status, 0);
            exit(0);
        }
        waitpid(k, &status, 0);
        exit(0);
    }
    return 0;
}
```

Arbre obtenu :

```
A
├── B
│   ├── D
│   └── E
│       └── F
└── C
    └── K
        └── L
            └── M
```

## Lab 6 : tables de 5 et de 7

Deux fils créés l'un après l'autre ; chacun affiche sa table de 1 à 10 puis `exit(0)` ; le parent attend chacun avec `waitpid` et affiche `fin`.

```c
int main(){
    int status;

    pid_t enfant1 = fork();
    if(enfant1 == -1){
        printf("erreur enfant1\n");
    }
    if(enfant1 == 0){
        int i;
        for(i=1; i<=10; i++){
            printf("%d x 5 = %d\n" ,i , i*5);}
        exit(0);
    }
    waitpid(enfant1, &status, 0);

    pid_t enfant2 = fork();
    if(enfant2 == -1){
        printf("erreur enfant2\n");    }
    if(enfant2 == 0){
        int i;
        for(i=1; i<=10; i++){
            printf("%d x 7 = %d\n", i, i*7);
        }
        exit(0);
    }
    waitpid(enfant2, &status, 0);
    printf("fin\n");
    return 0;
}
```

## Lab 7 : factorielle dans le fils, nombres premiers dans le parent

Test de primalité : `num` est premier si aucun `i` tel que $i^2 \le num$ ne le divise (il suffit de tester jusqu'à $\sqrt{num}$).

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>

int primenumber(int range){
    int num;
    int i;
    for(num = 2; num <= range; num++){
        bool isPrime = true;
        for(i = 2; i*i <= num; i++){
            if (num % i == 0) {
                isPrime = false;
                break;
            }}
        if (isPrime){
            printf("%d ", num);
        }
    }
}

int main(){
    int status;
    pid_t child = fork();

    if(child == 0){
        int nb =0;
        int i;
        int factorial = 1;
        printf("Enter factorial : ");
        scanf("%d", &nb);
        for(i=1; i<=nb; i++){
            factorial = factorial*i;
        }
        printf("\nfactorial of %d is %d\n", nb, factorial);
        exit(0);
    }
    waitpid(child, &status, 0);   // le parent attend la fin du fils

    int range;
    printf("Enter a range for prime number : ");
    scanf("%d", &range);
    primenumber(range);
    return 0;
}
```

Le `waitpid` garantit l'ordre demandé : le fils d'abord, puis le parent.

## Lab 8 : exécution simultanée

Pas de code dans la note. L'idée attendue est de retirer l'attente (`wait` / `waitpid`) pour que parent et fils s'exécutent en même temps.

## Points à vérifier dans le cours

1. **Lab 5, processus F** : dans le premier extrait, la transcription automatique avait omis le `exit(0)` du bloc de F. **Vérifié sur l'image** : la ligne 29 contient bien `exit(0);` dans le `if(f==0)`. Le code ci-dessus est conforme à l'image. Sans `exit`, F poursuivrait le code de E (complément).
2. **Lab 6** : l'énoncé demande deux processus ; le parent attend chaque fils avant d'en créer un autre, donc l'exécution n'est pas simultanée.
3. **Fonctions sans `return`** : `int lab1(void)` (lab 1) et `int primenumber` (lab 7) sont déclarées `int` sans renvoyer de valeur (complément) ; sans effet sur le résultat. Au lab 7, l'énoncé voulait que le fils s'exécute en premier : c'est le cas grâce au `waitpid`.
4. **Lab 8 « Update Lab 3 »** : l'énoncé concerne le lab 3, qui n'a pas de processus ; la note ne dit pas lequel est visé.
5. **Lab 3** : l'énoncé demande une suite qui part de 1, le code part de `sum = 0` (complément).
6. **Date** : la note indique « 11/03/2024 » ; l'ancien résumé la lisait comme le 3 novembre 2024 (format américain). À vérifier.
7. **Lab 7, factorielle** : un `int` déborde au-delà de $12!$ (complément).
