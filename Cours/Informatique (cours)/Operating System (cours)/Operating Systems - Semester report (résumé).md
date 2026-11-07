---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/DM/Operating Systems - Semester report.docx|Operating Systems - Semester report]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/DM/Operating Systems - Semester report.docx|Operating Systems - Semester report]], dans [[Operating System (index)]]. Rapport de semestre de l'étudiante (classe ID2B) qui rassemble le « Lab 1 Shell scripting » (30 septembre 2024) et le « Lab 2 Processes » (21 octobre 2024), avec ses réponses, son code commenté et les captures des résultats. Ce sont les réponses de l'étudiante, pas un corrigé. Les énoncés, reproduits en captures dans le rapport, sont recopiés ici en texte ; seules les captures de résultats du terminal sont intégrées.

Mêmes questions que [[DM Shell Scripting (résumé)]] pour le Lab 1, mêmes programmes que [[Copy of 08 Processes-TP (résumé)]] pour le Lab 2, mais avec les sorties obtenues et des commentaires.

## Lab 1 : Shell scripting

### Questions simples

**2. Quels shells le système supporte-t-il ?** `cat /etc/shells` ([[Fichier shells]]).

![[Operating Systems - Semester report - image43.png]]
*Figure : sortie de `cat /etc/shells` : sh, bash, rbash et dash, chacun dans `/bin` et `/usr/bin`.*

**3. Où se trouve bash ?** `which bash` ([[Commande which]]).

![[Operating Systems - Semester report - image57.png]]
*Figure : `which bash` renvoie `/usr/bin/bash`.*

**4. Répertoire de travail courant ?** `pwd` ([[Commande pwd]]).

![[Operating Systems - Semester report - image15.png]]
*Figure : `pwd` renvoie `/home/momo`.*

**5. Créer le répertoire `ostasks` dans le répertoire utilisateur et s'y placer** : `cd /home/{user name}`, `mkdir ostasks`, `cd ostasks` ([[Commande mkdir]], [[Commande cd]]).

![[Operating Systems - Semester report - image56.png]]
*Figure : `mkdir ostasks` puis `cd ostasks/` ; l'invite devient `~/ostasks$`.*

**6. Créer `firstprogram.sh`** avec `touch {file name}.sh`, l'ouvrir dans un éditeur ([[Gedit|gedit]], [[Éditeur nano|nano]], [[Vim|vim]]), y afficher « Hello », l'exécuter.

![[Operating Systems - Semester report - image21.png]]
*Figure : `cat firstprogram.sh` montre la ligne `echo "Hello"`.*

**7. Donner la permission d'exécution** : `chmod +x {file name}.extension` ([[Commande chmod]]). L'étudiante utilise `sudo chmod 777`.

![[Operating Systems - Semester report - image32.png]]
*Figure : `sudo chmod 777 firstprogram.sh` puis `./firstprogram.sh` affiche `Hello`.*

**8. Enregistrer puis afficher la date et l'heure** ([[Substitution de commande]]) :

```bash
#!/bin/bash
echo “hello”
current_datetime=$(date)
echo “Current Date and Time: $current_datetime”
```

![[Operating Systems - Semester report - image50.png]]
*Figure : exécution : les guillemets typographiques s'affichent dans la sortie (`“hello”`, `“Current Date and Time: Sat Jan 4 07:40:49 PM CET 2025”`).*

**11. Nom de la variable utilisateur de la question 8** : `current_datetime`.

### DM

#### Tâche 1 : `lshw`

*Énoncé* : lancer `lshw`, expliquer son rôle, trouver une solution s'il ne marche pas.

![[Operating Systems - Semester report - image31.png]]
*Figure : `lshw` → `-bash: lshw: command not found`.*

`lshw` ([[Commande lshw]]) doit être installé avec `sudo apt install lshw` ([[APT]], [[Commande sudo]]). Il liste le matériel de l'ordinateur.

![[Operating Systems - Semester report - image54.png]]
*Figure : `lshw` sans droits : avertissement « you should run this program as super-user », puis description de la machine (64 bits, mémoire système 6912 MiB, CPU Intel Celeron N3350).*

Pour une vue complète : `sudo lshw` (sortie trop longue pour une seule capture).

![[Operating Systems - Semester report - image41.png]]
*Figure : début de la sortie de `sudo lshw`, sans l'avertissement.*

#### Tâche 2 : les 500 premiers nombres premiers

Démarche : écrire d'abord le script en Python, puis le « traduire » en Bash. Justification mathématique :
- **Propriété** : tout nombre non premier $n > 2$ admet un diviseur premier $p$ avec $p \le \sqrt{n}$ ;
- **Lemme** : si $n$ n'a aucun diviseur entre $2$ et $\sqrt{n}$, alors $n$ est [[Nombre premier|premier]].

```python
NombreActuel = 2
NombreActuelPremier = 0
CompteurNombrePremier = 0
while True:
    NombreActuelPremier = 1           # on suppose le nombre premier
    for i in range(2, int(NombreActuel**0.5)):
        if NombreActuel % i == 0:
            NombreActuelPremier = 0   # i divise : pas premier
            break
    if NombreActuelPremier == 1:      # le nombre a passé la boucle : premier
        print(NombreActuel)
        CompteurNombrePremier += 1
    if CompteurNombrePremier == 500:  # 500 premiers trouvés : arrêt
        break
    NombreActuel += 1
```

En Bash, on ne peut pas utiliser `sqrt` ni `**0.5` dans la condition ; or $i \le \sqrt{n} \iff i^2 \le n$ pour des entiers positifs. Pour les comparaisons arithmétiques on utilise `(( condition ))` et non `[ condition ]` ([[Arithmétique en Bash]]).

```bash
#!/bin/bash
NombreActuel=2
CompteurNombrePremier=0
while true
do
  NombreActuelPremier=1
  for ((i=2; i*i<=NombreActuel; i++))
  do
    if ((NombreActuel%i==0))
    then
      NombreActuelPremier=0
      break
    fi
  done
  if ((NombreActuelPremier == 1))
  then
    echo $NombreActuel
    ((CompteurNombrePremier++))
  fi
  if ((CompteurNombrePremier==500))
  then
    break
  fi
  ((NombreActuel++))
done
```

![[Operating Systems - Semester report - image20.png]]
*Figure : début de la sortie de `./primenumber.sh` : 2, 3, 5, 7, 11… 97.*

![[Operating Systems - Semester report - image53.png]]
*Figure : fin de la sortie : … 3557, 3559, 3571. Le dernier nombre affiché est 3571, le 500e nombre premier.*

#### Tâche 3 : nombre de cœurs

```bash
#! /bin/bash
echo "There is $(nproc --all) cores on my machine"
```

`nproc --all` ([[Commande nproc]]) donne le nombre de cœurs de l'ordinateur ([[Cœur de processeur]]).

![[Operating Systems - Semester report - image10.png]]
*Figure : `./core.sh` affiche « There is 2 cores on my machine ».*

#### Tâche 4 : état des cœurs

*Énoncé* : par défaut tous les cœurs sont en ligne (*online* = actif, [[Cœur en ligne et hors ligne]]) ; trouver la commande qui donne leur état.

Réponse : [[Commande lscpu|lscpu]].

![[Operating Systems - Semester report - image28.png]]
*Figure : sortie de `lscpu` : x86_64, 2 CPU, « On-line CPU(s) list: 0,1 », Intel Celeron N3350.*

La ligne « On-line CPU(s) list » donne les [[Processeur|CPU]] en ligne, indexés par un numéro (ici 0 et 1). S'il y avait des CPU hors ligne, une ligne « Off-line CPU(s) list » apparaîtrait. Pour n'extraire que l'état ([[Commande grep]]) :

```bash
lscpu | grep "On-line CPU(s) list"
lscpu | grep "Off-line CPU(s) list"
```

![[Operating Systems - Semester report - image58.png]]
*Figure : les deux commandes enchaînées par `;` n'affichent que « On-line CPU(s) list: 0,1 ».*

#### Tâche 5 : cœur par défaut

Les cœurs sont numérotés de 0 à n ; le cœur par défaut est le **cœur 0**.

#### Tâche 6 : mettre hors ligne tous les cœurs sauf le défaut

Pour activer ou désactiver un cœur, on écrit dans le fichier `/sys/devices/system/cpu/cpuX/online` (X = numéro du cœur) : `1` = en ligne, `0` = hors ligne. On pourrait l'ouvrir avec nano et remplacer 1 par 0.

![[Operating Systems - Semester report - image9.png]]
*Figure : `cat online` dans `/sys/devices/system/cpu/cpu1` affiche `1`.*

```bash
#!/bin/bash
total_cores=$(nproc)
default_core=0                       # cœur par défaut
for ((i=0; i<total_cores; i++))      # pour chaque cœur
do
  if [ $i -ne $default_core ]        # si ce n'est pas le cœur par défaut
  then
    echo 0 | sudo tee /sys/devices/system/cpu/cpu$i/online   # on écrit 0 à la place de 1
  fi
done
```

Voir [[Commande tee]].

![[Operating Systems - Semester report - image3.png]]
*Figure : `./core.sh` affiche `0` (sortie de `tee`).*

![[Operating Systems - Semester report - image52.png]]
*Figure : vérification : `cat online` dans `cpu1` affiche désormais `0`.*

#### Tâche 7 : remettre en ligne tous les cœurs sauf le défaut

Même programme, en écrivant `1` au lieu de `0` :

```bash
#!/bin/bash
total_cores=$(nproc)
default_core=0
for ((i=0; i<total_cores; i++))
do
  if [ $i -ne $default_core ]
  then
    echo 1 | sudo tee /sys/devices/system/cpu/cpu$i/online
  fi
done
```

#### Tâche 8 : créer cinq fichiers texte

```bash
#!/bin/bash
echo "Entrez le nom des fichiers"
for ((i=1; i<=5; i++))               # la boucle tourne 5 fois
do
  read -p "Entrez le nom du fichier $i : " nomfichier   # l'utilisateur saisit le nom
  touch "$nomfichier".txt            # création du fichier
done
```

![[Operating Systems - Semester report - image12.png]]
*Figure : `./file.sh` demande cinq noms (file1 à file5) ; `ls` montre `file1.txt` à `file5.txt` et `file.sh`.*

#### Tâche 9 : supprimer ces fichiers

```bash
#!/bin/bash
for ((i=1; i<=5; i++))
do
  echo "entrez le nom du fichier $i à supprimer"
  read fichier                       # nom du fichier à supprimer
  rm "$fichier".txt                  # suppression
done
echo "les fichiers ont été supprimés"
```

![[Operating Systems - Semester report - image36.png]]
*Figure : `./deletefile.sh` supprime file1 à file5 ; `ls` ne montre plus que `deletefile.sh` et `file.sh`.*

#### Tâche 10 : afficher la date `n` fois toutes les 2 secondes

```bash
#! /bin/bash
echo "entrez le nombre de récursion : "
read n                               # l'utilisateur saisit un entier n
for ((i = 1; i <=n; i++))            # la boucle s'exécute n fois
do
  date                               # affiche la date
  sleep 2
done
```

Voir [[Commande date]] et [[Commande sleep]].

![[Operating Systems - Semester report - image8.png]]
*Figure : `./time.sh` avec n = 3 : trois dates espacées de 2 secondes (10:46:26, 10:46:28, 10:46:30).*

#### Tâche 11 : comparer deux chaînes

```bash
#! /bin/bash
read -p "Entrez chaine 1 :" chaine1   # l'utilisateur saisit les deux chaînes
read -p "Entrez chaine 2 :" chaine2
if [ “$chaine1” == “$chaine2” ]        # si elles sont égales
then
  echo "same"
else
  echo "not same"
fi
```

![[Operating Systems - Semester report - image11.png]]
*Figure : `hello` / `hola` → « not same » ; `hello` / `hello` → « same ».*

## Lab 2 : Processes

### Énoncés

Mêmes énoncés que [[Copy of 08 Processes-TP (résumé)]] :
- **Lab 1** : lire deux entiers, ranger leur somme dans une troisième variable, l'afficher ; compiler avec [[GCC]].
- **Lab 2** : lire un entier et afficher les nombres impairs de 1 jusqu'à cette borne.
- **Lab 3** : lire une borne et une raison (*common difference*, [[Suite arithmétique]]), afficher la suite partant de 1 jusqu'à atteindre ou dépasser la borne.
- **Lab 4** : avec `fork()`, créer un fils ; parent et fils affichent leur [[Identifiant de processus|PID]] et un message ; les deux se terminent proprement.
- **Lab 5** : créer l'[[Arbre de processus]] : A crée B et C ; B crée D, E ; E crée F ; C crée K ; K crée L ; L crée M.
- **Lab 6** : deux processus, l'un affiche la table de 5, l'autre celle de 7.
- **Lab 7** : le parent lit une saisie et affiche les nombres premiers ; le fils lit une saisie et affiche la [[Factorielle]] ; le fils s'exécute d'abord, le parent attend.
- **Lab 8** : mettre à jour le Lab 3 pour que fils et parent s'exécutent simultanément.

### Labs 1 à 3 : un seul fichier, une fonction par lab

```c
#include <stdio.h>

int lab1(void){
    int a = 0;
    int b = 0;
    printf("Entrez le premier nombre : ");
    scanf("%d", &a);          // la saisie est rangée dans a
    printf("Entrez le deuxième nombre : ");
    scanf("%d", &b);
    int c = b + a;
    printf("La somme est %d\n", c);
    return 0;
}

int lab2(void){
    int lim = 0;
    printf("ENter a limit : ");
    scanf("%d", &lim);
    for(int i = 1; i<=lim; i+=2){   // i part de 1 et augmente de 2 : il reste impair
        printf("%d ", i); }
    return 0;}

int lab3(void){
    int range = 0;
    int increment = 0;
    int sum = 0;
    printf("Enter the range : ");
    scanf("%d", &range);
    printf("Enter the increment : ");
    scanf("%d", &increment);
    while (sum<= range){
        printf("%d ", sum);
        sum = sum + increment;}
    return 0;}

int main(){
    lab1();
    lab2();
    lab3();
    return 0;
}
```

Voir [[Fonctions printf et scanf]].

![[Operating Systems - Semester report - image17.png]]
*Figure : `gcc -o test lab123.c` puis `./test` : 2 + 5 → « La somme est 7 ».*

![[Operating Systems - Semester report - image45.png]]
*Figure : lab 2 avec la limite 21 : `1 3 5 … 21`.*

![[Operating Systems - Semester report - image2.png]]
*Figure : lab 3 avec range 50 et increment 3 : `0 3 6 … 48`.*

### Lab 4 : `fork()` et `wait()`

Voir [[Appel fork()]], [[Création et terminaison de processus]] et [[Appels wait() et waitpid()]]. L'étudiante choisit un `switch` plutôt qu'un `if/else`, « pour découvrir une autre façon de séparer les processus ».

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    int status;
    switch(pid){
        case 0:      // pid = 0 : partie exécutée par le fils
            printf("Processus enfant, pid : %d, %d\n", pid, getpid());
            break;
        default:     // cas du parent
            printf("Processus parent, pid de l'enfant : %d\n", pid);
            printf("Processus parent, pid du parent : %d\n", getpid());
            wait(&status);            // attendre la fin du fils
            if (WIFEXITED(status)) {
                printf("Le processus enfant s'est terminé avec le code de sortie %d\n", WEXITSTATUS(status));
            }
            else {
                printf("Le processus enfant ne s'est pas terminé correctement\n");
            }
            printf("Processus parent terminé\n");
            break;
    }
}
```

![[Operating Systems - Semester report - image30.png]]
*Figure : le parent affiche le pid de l'enfant (11015), l'enfant affiche `0, 11015`, le parent son propre pid (11014), puis « code de sortie 0 » et « Processus parent terminé. ».*

### Lab 5 : arbre de processus

Méthode : `fork()` imbriqués ; chaque fils termine par `exit(0)` ; chaque parent attend son fils avec `waitpid` avant de créer le suivant.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    printf("I'm process A\n");
    int status;
    pid_t b = fork();
    if(b==0){                         // exécuté par B
        printf("I'm process B inside process A\n");
        pid_t d = fork();             // B crée D
        if(d==0){
            printf("Im process D inside process B\n");
            exit(0);
        }
        waitpid(d, &status, 0);       // D se termine avant la création de E
        pid_t e = fork();             // E dans B
        if(e==0){
            printf("I'm process E, inside process B\n");
            pid_t f = fork();         // F dans E
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
    waitpid(b, &status, 0);           // B terminé : on peut créer C
    pid_t c = fork();                 // même logique pour C
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
                exit(0); }
            waitpid(l, &status, 0);
            exit(0); }
        waitpid(k, &status, 0);
        exit(0); }
    return 0;}
```

Remarques de l'étudiante : elle a cherché sans succès un outil pour visualiser l'arborescence des processus du programme ; elle constate que son code est lourd et qu'elle aurait pu écrire des fonctions séparées au lieu de tout mettre dans `main`.

![[Operating Systems - Semester report - image6.png]]
*Figure : sortie de `lab5.c` : A, B, D, E, F, C, K, L, M, dans cet ordre.*

### Lab 6 : tables de 5 et de 7

```c
int main(){
    int status;
    pid_t enfant1 = fork();
    if(enfant1 == 0){                 // le fils affiche la table de 5
        int i;
        for(i=1; i<=10; i++){
            printf("%d x 5 = %d\n" ,i , i*5);}
        exit(0);
    }
    waitpid(enfant1, &status, 0);     // attendre le premier fils avant de créer le second
    pid_t enfant2 = fork();
    if(enfant2 == 0){
        int i;
        for(i=1; i<=10; i++){
            printf("%d x 7 = %d\n", i, i*7);
        }
        exit(0);
    }
    waitpid(enfant2, &status, 0);
    return 0;
}
```

Interprétation de l'énoncé : l'étudiante ne sait pas si « deux processus » veut dire deux fils (trois processus en tout) ou un parent et un fils. Elle crée deux fils ; pour un parent et un fils, il suffirait de remplacer le second `fork()` par un `else if (enfant1 > 0)` où le parent affiche la table de 7 ([[Structure conditionnelle]]).

![[Operating Systems - Semester report - image46.png]]
*Figure : sortie : table de 5 (1 x 5 = 5 … 10 x 5 = 50), puis table de 7 (… 10 x 7 = 70), puis « fin ».*

### Lab 7 : factorielle (fils), puis nombres premiers (parent)

Même logique de primalité que la tâche 2 du Lab 1 ($i^2 \le num$).

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>

int primenumber(int range){   // lit la borne et affiche les nombres premiers
    int num;
    int i;
    for(num = 2; num <= range; num++){
        bool isPrime = true;
        for(i = 2; i*i <= num; i++){
            if (num % i == 0) {
                isPrime = false;
                break; }}
        if (isPrime){
            printf("%d ", num);} }}

int main(){
    int status;
    pid_t child = fork();
    if(child == 0){            // le fils calcule la factorielle
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
    else if(child>0){
        wait(NULL);            // attendre la fin du fils
        int range;
        printf("Enter a range for prime number : ");
        scanf("%d", &range);
        primenumber(range);}
    return 0;
}
```

![[Operating Systems - Semester report - image47.png]]
*Figure : « factorial of 6 is 720 », puis avec la borne 19 : `2 3 5 7 11 13 17 19`.*

### Lab 8 : exécution simultanée

L'étudiante ne comprend pas la consigne, puisque le Lab 3 n'a ni parent ni fils. Elle propose deux réponses.

**1. Mise à jour du Lab 7** : il suffit de retirer le `wait(NULL)` du parent ; le code est identique au précédent sans cette ligne (non annoté) :

```c
    else if(child>0){
        int range;
        printf("Enter a range for prime number : ");
        scanf("%d", &range);
        primenumber(range);}
```

**2. Mise à jour du Lab 3 avec un `fork`**. D'abord la version **sans** exécution simultanée :

```c
int lab3_fork(void){
    int range = 0;
    int increment = 0;
    int sum = 0;
    // le parent demande la borne et l'incrément
    printf("Enter the range : ");
    scanf("%d", &range);
    printf("Enter the increment : ");
    scanf("%d", &increment);
    pid_t child = fork();
    if(child==0){             // le fils calcule la suite
        while (sum<= range){
            printf("%d ", sum);
            sum = sum + increment;}
    }
    else if(child>0){
        wait(NULL);           // le parent attend le fils avant le message de fin
        printf("\nL'enfant a fini son execution, fin du programme\n");
    }
    return 0;}
```

![[Operating Systems - Semester report - image23.png]]
*Figure : range 50, increment 4 : `0 4 8 … 48`, puis « L'enfant a fini son execution, fin du programme ».*

Puis la version simultanée, en retirant `wait(NULL)` : le parent s'exécute en même temps que le fils.

```c
    else if(child>0){         // le parent s'exécute en même temps que le fils
        printf("\nL'enfant a fini son execution, fin du programme\n");
    }
```

![[Operating Systems - Semester report - image39.png]]
*Figure : range 40, increment 3 : le message final du parent s'affiche avant la suite `0 3 6 … 39` du fils.*

On voit que le message final s'affiche avant la fin du fils.

## Points à vérifier dans le cours

1. **Lab 8** : au lab 8 version simultanée, le message du parent s'affiche avant la fin de l'enfant ; il porte pourtant « L'enfant a fini » : le message est faux dans ce cas (complément).
2. **Lab 7 simultané** : parent et fils lisent tous deux `scanf` sur le terminal au même moment ; les saisies se mélangent (complément).
3. **Alertes de transcription** (« Cat » en majuscule, « used » pour « user », lignes coupées) : portent sur des captures de l'énoncé, sans effet sur le contenu.
4. **Programme de nombres premiers du lab 1** : voir [[DM Shell Scripting (résumé)]], point 1.
5. **Écarts entre code et captures** : la sortie du lab 6 se termine par « fin », que le code du rapport n'affiche pas ; la sortie du lab 4 affiche « Processus parent terminé. » avec un point, absent du code. Les captures viennent sans doute d'une version antérieure du code (celle de [[Copy of 08 Processes-TP (résumé)]]).
6. **Question simple 8** : les guillemets typographiques `“ ”` du script apparaissent dans la sortie, signe qu'ils ne sont pas compris comme des guillemets par Bash (complément). Même chose pour `[ “$chaine1” == “$chaine2” ]` à la tâche 11, qui fonctionne ici par chance.
7. **Version simultanée du Lab 3** : la ligne commence par `nt lab3_fork(void){` (le `i` de `int` manque) dans le rapport.
8. **Labs 3 et suivants** : la suite part de 0 alors que l'énoncé demande de partir de 1 (complément).
