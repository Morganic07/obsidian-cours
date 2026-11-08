---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]] (« Chp7 - Processes »), dans [[Cours/Informatique/OS/_index|Operating System]].
## Idée générale

Les processus : ce qu'ils sont, leur mémoire, leurs états, leur bloc de contrôle, leur ordonnancement, le changement de contexte, le multitâche sur mobile, leur création et leur fin, l'exemple de Chrome.

## Concept de processus

- Un OS exécute des programmes variés, qui tournent sous forme de processus.
- Un **[[Processus]]** est un programme en exécution. Un programme est statique, un processus est une tâche en cours.
- Un programme est un fichier exécutable **passif** stocké sur le disque ; un processus est **actif**. Un programme chargé en mémoire devient un processus.
- L'[[Interface graphique]] (GUI) et la [[Interface en ligne de commande|ligne de commande]] (CLI) sont deux façons de lancer un programme.
- Un programme peut donner plusieurs processus (exemple : Chrome, un processus par onglet).
- **Pas d'exécution parallèle des instructions d'un même processus** : un processus exécute une instruction à la fois, dans l'ordre séquentiel. Le parallélisme passe par plusieurs processus ou plusieurs [[Thread|threads]] ; dans un seul processus, il n'y a en général qu'un flux d'exécution, le *thread principal*.
- Les threads d'un même processus partagent son code, ses données et ses fichiers ouverts, mais chacun a sa propre pile, ses registres et son compteur de programme ; deux processus, eux, ont chacun leur mémoire. Créer un thread coûte donc moins cher que créer un processus, mais une erreur dans un thread peut corrompre tout le processus. [[Complément hors du cours|ⓘ]]
- Sous Linux, `ps aux` liste tous les processus du système avec leur PID, leur utilisateur et leur consommation, et `top` (ou `htop`) les affiche en continu ([[Commande ps]]). [[Complément hors du cours|ⓘ]]

## Le processus en mémoire

Voir [[Espace mémoire d'un processus]]. Un processus contient :
- la **section text** : le code du programme ;
- la **pile** (*stack*) : données temporaires (variables locales, adresses de retour, paramètres de fonctions), voir [[Pile d'exécution]] ;
- la **section data** : variables globales ;
- le **tas** (*heap*) : mémoire allouée dynamiquement pendant l'exécution ([[Allocation dynamique]]).

![[OS - chp7 - image11.png]]
*Figure : espace mémoire d'un processus, de l'adresse 0 à max : text, data, heap, zone libre, stack ; la pile et le tas croissent l'un vers l'autre.*

Annotations de l'étudiante sur le dessin : « Memory length allocated inside the [[Mémoire vive|RAM]] » ; « Dynamic memory (can expand / shrink) » ; zones marquées « Dynamic ; fixed ; fixed ; Dynamic » (vraisemblablement stack et heap dynamiques, data et text fixes).

Text et data ont une taille connue dès la compilation ; la pile et le tas varient pendant l'exécution, d'où leur placement aux deux bouts de la zone libre, qu'ils se partagent en croissant l'un vers l'autre. Si la pile grandit trop (récursion sans condition d'arrêt, très grand tableau local), elle dépasse sa limite : c'est le **débordement de pile** (*stack overflow*), qui fait planter le programme ([[Pile d'exécution]]). [[Complément hors du cours|ⓘ]]

Les adresses de 0 à max sont des adresses **virtuelles** ([[Mémoire virtuelle]]) : chaque processus croit disposer de tout l'espace d'adressage, et l'OS, avec l'aide du matériel (la MMU), les traduit en adresses physiques de la RAM. Deux processus peuvent ainsi utiliser la même adresse sans se gêner, et aucun ne peut lire la mémoire d'un autre. [[Complément hors du cours|ⓘ]]

### Disposition mémoire d'un programme C

![[OS - chp7 - image1.png]]
*Figure : disposition mémoire d'un programme C, de la mémoire haute à la basse : argc/argv, stack, zone libre, heap, uninitialized data, initialized data, text ; chaque ligne du code est reliée à sa zone.*

```c
#include <stdio.h>
#include <stdlib.h>

int x;          // uninitialized data
int y = 15;     // initialized data

int main(int argc, char *argv[])   // argc, argv : tout en haut
{
    int *values;                   // stack
    int i;                         // stack

    values = (int *)malloc(sizeof(int)*5);   // heap

    for(i = 0; i < 5; i++)
        values[i] = i;

    return 0;
}
```

La zone des données non initialisées s'appelle traditionnellement **BSS** : elle n'occupe pas de place dans le fichier exécutable, l'OS la remplit de zéros au chargement, si bien que `x` vaut 0 au démarrage. La commande `size` affiche la taille des sections text, data et bss d'un exécutable. Le tableau `values`, lui, est dans le tas : il doit être rendu par `free(values)` quand il ne sert plus, sinon la mémoire reste réservée jusqu'à la fin du processus (fuite mémoire, [[Allocation dynamique]]). [[Complément hors du cours|ⓘ]]

## États d'un processus

Voir [[États d'un processus]]. En s'exécutant, un processus change d'état :
- **New** : en cours de création ;
- **Ready** : attend d'être affecté à un processeur ;
- **Running** : ses instructions s'exécutent ;
- **Waiting** : attend un événement ;
- **Terminated** : a fini son exécution.

Sur un cœur, **un seul** processus est *running* à un instant donné ; tous les autres sont *ready* ou *waiting*. Une machine à quatre cœurs a donc au plus quatre processus *running* en même temps, même si des centaines sont lancés ([[Cœur de processeur]]). [[Complément hors du cours|ⓘ]]

Sous Linux, la colonne `STAT` de `ps` donne l'état avec une lettre : `R` (*running* ou prêt), `S` (endormi, en attente d'un événement), `D` (attente non interruptible, souvent une E/S disque), `T` (stoppé, par exemple par Ctrl+Z), `Z` (zombie, voir plus bas). Linux ne distingue donc pas *ready* et *running* dans cet affichage. [[Complément hors du cours|ⓘ]]

![[OS - chp7 - image14.png]]
*Figure : diagramme des états : new → ready (admitted), ready → running (scheduler dispatch), running → ready (interrupt), running → waiting (I/O or event wait), waiting → ready (I/O or event completion), running → terminated (exit).*

Annotation de l'étudiante sur le diagramme : « Storage ; RAM ; RAM ; [[Processeur|CPU]] ; LT scheduler » (mots sans leurs flèches ; sans doute le trajet disque → RAM → CPU, l'ordonnanceur à long terme gérant new → ready).

- Les processus **I/O bound** (Word, Chrome) sont la plupart du temps en *waiting* ; les **CPU bound** (jeu, programme Python) en *running* ([[Processus limité par les entrées-sorties ou par le processeur]]).
- Le **[[Dispatcher]]** est le composant qui effectue la [[Changement de contexte|commutation de contexte]] entre processus. Quand l'ordonnanceur choisit un processus *ready* pour passer en *running*, le dispatcher donne le CPU au processus choisi, ce qui inclut le chargement de son contexte (valeurs des registres et autres informations) depuis le PCB. Il est donc **directement impliqué dans le passage de ready à running**.
- Le temps que met le dispatcher à arrêter un processus et à en lancer un autre s'appelle la **latence de répartition** (*dispatch latency*) : c'est du temps perdu pour le travail utile, que l'OS cherche à rendre le plus court possible. Son travail comprend aussi le retour en mode utilisateur et le saut à l'instruction où le processus choisi s'était arrêté. [[Complément hors du cours|ⓘ]]

## Bloc de contrôle de processus (PCB)

- Le [[Bloc de contrôle de processus|PCB]] (*Process Control Block*) est une structure de données qui stocke toutes les informations essentielles d'un processus : état courant, [[Compteur de programme]], [[Registre du processeur|registres CPU]], et ce qu'il faut pour sauvegarder et restaurer son état.
- Chaque processus a son PCB, mis à jour à chaque changement d'état (par exemple *running* → *waiting*).

![[OS - chp7 - image8.png]]
*Figure : PCB en pile de cases : process state, process number, program counter, registers, memory limits, list of open files, …*

Contenu du PCB (annotations) :

| Champ | Contenu |
|---|---|
| *Process state* | running, waiting, etc. |
| *Program counter* | adresse de la prochaine instruction à exécuter |
| *CPU registers* | informations utilisées par le CPU pendant l'exécution (variables temporaires, données intermédiaires) |
| *CPU scheduling information* | priorités, pointeurs vers les files d'ordonnancement |
| *Memory-management information* | mémoire allouée au processus |
| *Accounting information* | CPU utilisé, temps écoulé depuis le démarrage, limites de temps |
| *I/O status information* | périphériques d'E/S alloués, liste des fichiers ouverts |

Le PCB est rangé dans la mémoire du [[Noyau]], hors de portée du processus lui-même ; l'ensemble des PCB forme la **table des processus**. Sous Linux, le PCB est une structure C du noyau, `task_struct`, qui contient aussi le PID, un pointeur vers le parent et la liste des fils. Le répertoire `/proc/<pid>/` en montre une partie (`cat /proc/self/status`). [[Complément hors du cours|ⓘ]]

## Ordonnancement des processus (*Process scheduling*)

Voir [[Ordonnancement des processus]].

- L'**ordonnanceur** (*scheduler*) décide quel processus *ready* accède ensuite au CPU pour passer en *running*.
- But : maximiser l'usage du CPU, faire passer vite les processus sur un cœur.
- Il tient des **files d'ordonnancement** :
  - **ready queue** : les processus en [[Hiérarchie de stockage|mémoire principale]], prêts et en attente d'exécution ;
  - **wait queues** : les processus qui attendent un événement (E/S…) ;
  - les processus migrent entre les files.

![[OS - chp7 - image13.png]]
*Figure : files d'attente : ready queue → CPU ; depuis le CPU, quatre chemins ramènent à la ready queue : I/O request (I/O wait queue, puis I/O), time slice expired, create child process (child termination wait queue, puis child terminates), wait for an interrupt (interrupt wait queue, puis interrupt occurs).*

Annotations de l'étudiante : chaque processus a une tranche de temps ([[Quantum de temps]]) ; si elle expire, il revient dans la ready queue. Le processus emprunte l'une de ces quatre files.

**Types d'ordonnanceurs** :

| Ordonnanceur | Rôle |
|---|---|
| *Long term scheduler* (**LTS**) | décide quel processus passe de *new* à *ready* |
| *Short term scheduler* (**STS**) | décide quel processus passe de *ready* à *running* |
| *Mid term scheduler* (**MTS**, ou *swapper*) | peut faire passer (*[[Espace d'échange (swap)\|swap]]*) un processus de la RAM vers le stockage |

Les noms viennent de la fréquence d'intervention. L'ordonnanceur à court terme agit très souvent (à chaque fin de quantum ou blocage), il doit donc être rapide. L'ordonnanceur à long terme agit rarement et règle le **degré de multiprogrammation**, le nombre de processus présents en mémoire ; il cherche un bon mélange de processus I/O bound et CPU bound, pour que ni le processeur ni les périphériques ne restent inoccupés. Sur les systèmes de bureau et les mobiles actuels, il n'y a pratiquement pas d'ordonnanceur à long terme : tout programme lancé est admis aussitôt. [[Complément hors du cours|ⓘ]]

**Algorithmes d'ordonnancement à court terme.** Le cours n'en présente aucun ; les classiques sont : [[Complément hors du cours|ⓘ]]
- **FCFS** (*First Come, First Served*) : le premier arrivé dans la ready queue est servi le premier, jusqu'à ce qu'il se bloque ou finisse ; simple, mais un long processus fait attendre tous les courts (effet de convoi). [[Complément hors du cours|ⓘ]]
- **SJF** (*Shortest Job First*) : le processus dont la prochaine rafale CPU est la plus courte passe d'abord ; il minimise le temps d'attente moyen, mais suppose d'estimer la durée à venir et peut faire attendre indéfiniment les longs processus (famine). [[Complément hors du cours|ⓘ]]
- **Par priorité** : le plus prioritaire passe d'abord ; contre la famine, on augmente peu à peu la priorité de ceux qui attendent (vieillissement, *aging*). Sous Linux, `nice` et `renice` ajustent la priorité d'un processus. [[Complément hors du cours|ⓘ]]
- **Tourniquet** (*Round Robin*) : chaque processus reçoit à son tour un [[Quantum de temps]] ; s'il ne finit pas, il retourne en fin de ready queue. C'est le chemin « time slice expired » de la figure ci-dessus. Un quantum trop long ramène à FCFS, un quantum trop court multiplie les changements de contexte. [[Complément hors du cours|ⓘ]]

Un ordonnancement est **préemptif** quand l'OS peut retirer le CPU à un processus qui ne l'a pas rendu (fin de quantum, arrivée d'un processus plus prioritaire), **non préemptif** quand le processus garde le CPU jusqu'à ce qu'il se bloque ou se termine. Les OS actuels (Linux, Windows, macOS) sont préemptifs ; FCFS est non préemptif, le tourniquet préemptif. [[Complément hors du cours|ⓘ]]

Exemple de calcul, pour trois processus arrivés en même temps dans l'ordre $P_1$, $P_2$, $P_3$, de durées 24, 3 et 3 unités. En FCFS, ils attendent 0, 24 et 27 : temps d'attente moyen $(0+24+27)/3 = 17$. En SJF, l'ordre devient $P_2$, $P_3$, $P_1$, qui attendent 0, 3 et 6 : moyenne $(0+3+6)/3 = 3$. [[Complément hors du cours|ⓘ]]

## Changement de contexte (*Context switch*)

Voir [[Changement de contexte]].

- Il a lieu quand le CPU passe d'un processus à un autre.
- Le système doit **sauvegarder l'état** de l'ancien processus et **charger l'état sauvegardé** du nouveau.
- Le contexte d'un processus est représenté dans son PCB.
- Le système ne fait aucun travail utile pendant le changement de contexte.
- Plus l'OS et le PCB sont complexes, plus le changement est long.
- La durée dépend du support matériel : certains matériels chargent plusieurs contextes à la fois.
- Un changement de contexte est déclenché par une [[Interruption]] (en particulier l'interruption d'horloge qui signale la fin du quantum, ou la fin d'une E/S) ou par un [[Appel système]] qui bloque le processus (lecture sur disque, `wait()`, `sleep`). Il se fait en mode noyau : le processus n'en a pas conscience et reprend plus tard exactement là où il s'était arrêté. [[Complément hors du cours|ⓘ]]
- Les processeurs qui « chargent plusieurs contextes à la fois » ont plusieurs jeux de registres : basculer de l'un à l'autre revient à changer de jeu, sans copie en mémoire. L'[[Hyperthreading]] va plus loin : un cœur garde deux contextes matériels et fait avancer les deux threads en partageant ses unités de calcul. [[Complément hors du cours|ⓘ]]

![[OS - chp7 - image3.png]]
*Figure : changement de contexte entre $P_0$ et $P_1$ : à une interruption ou un [[Appel système]], l'OS sauvegarde l'état dans PCB₀ et recharge PCB₁ ; $P_1$ s'exécute pendant que $P_0$ est inactif, puis l'inverse.*

## Multitâche sur mobile

Voir [[Multitâche sur mobile]].

- Certains systèmes mobiles (premières versions d'iOS) ne laissent tourner qu'un processus, les autres étant suspendus en arrière-plan.
  - À cause de la taille de l'écran, iOS limite le multitâche.
  - iOS ne permettait qu'un processus actif au [[Commandes fg et bg|premier plan]], contrôlé par l'interface ; les processus en arrière-plan restaient en mémoire mais limités (tâches courtes, réception de notifications, lecture audio continue…).
- Android fait tourner premier plan et arrière-plan :
  - un processus d'arrière-plan utilise un **service** pour ses tâches ;
  - le service peut continuer même si le processus d'arrière-plan est suspendu ;
  - le service n'a pas d'interface et utilise peu de mémoire.
- Sur les deux systèmes, quand la mémoire manque, l'OS peut **tuer** des processus d'arrière-plan, en commençant par les moins utiles ; l'application doit donc sauvegarder son état pour pouvoir le restaurer quand l'utilisateur revient. iOS a introduit un multitâche limité pour les applications tierces avec sa version 4, en 2010. [[Complément hors du cours|ⓘ]]

## Opérations sur les processus

### Création

Voir [[Création et terminaison de processus]].

- Un processus parent crée des fils, qui en créent d'autres : on obtient un [[Arbre de processus]].
- Les processus sont identifiés et gérés par un [[Identifiant de processus]] (*pid*).
- **Partage des ressources** : parent et fils partagent toutes les ressources ; ou les fils en partagent une partie ; ou aucune.
- **Exécution** : parent et fils s'exécutent en même temps ; ou le parent attend la fin des fils.
- **Espace d'adressage** :
  - le fils est un **duplicata du parent** : il démarre avec le même code, les mêmes données et le même état mémoire, grâce à `fork()` ([[Appel fork()]]) ;
  - le fils a un **programme chargé** : sous UNIX, après `fork()`, on utilise `exec()` ([[Appel exec()]]) pour charger un nouveau programme dans le fils, qui exécute alors un programme différent du parent.
- **Exemple UNIX** :
  - `fork()` crée un nouveau processus ;
  - `exec()`, appelé après `fork()`, remplace l'espace mémoire du processus par un nouveau programme ;
  - le parent appelle `wait()` pour attendre la fin du fils.
- `fork()` est appelé une fois mais **revient deux fois**, une fois dans chaque processus, avec une valeur différente : le PID du fils (> 0) dans le parent, 0 dans le fils, une valeur négative si la création a échoué (aucun fils n'existe alors). C'est ce qui permet au même code de faire deux choses différentes, comme dans la figure ci-dessous ([[Appel fork()]]). [[Complément hors du cours|ⓘ]]
- Après `fork()`, parent et fils ont chacun **leur copie** de la mémoire : une variable modifiée par l'un ne change pas chez l'autre. Pour ne pas tout recopier inutilement (surtout si le fils fait aussitôt un `exec()`), les systèmes actuels utilisent la **copie sur écriture** (*copy-on-write*) : les pages mémoire sont partagées tant qu'aucun des deux n'écrit, et une page n'est dupliquée qu'au moment où l'un la modifie. Pour échanger des données, ils doivent passer par la [[Communication interprocessus]]. [[Complément hors du cours|ⓘ]]
- Le fils hérite aussi des fichiers ouverts du parent : c'est ainsi qu'un shell relie deux commandes par un tube ([[Redirection et tube]]). [[Complément hors du cours|ⓘ]]

![[OS - chp7 - image2.png]]
*Figure : `pid = fork()` ; le parent (pid > 0) va à `wait()` ; le fils (pid = 0) fait `exec()` puis `exit()` ; ensuite le parent reprend (parent resumes).*

### Terminaison

- Le processus exécute sa dernière instruction et demande à l'OS de le supprimer par l'appel `exit()` :
  - il renvoie des données d'état au parent (via `wait()`) ;
  - l'OS libère ses ressources.
- Le parent peut terminer un fils par l'appel `abort()`, par exemple si :
  - le fils a dépassé les ressources allouées ;
  - sa tâche n'est plus nécessaire ;
  - le parent se termine et l'OS ne permet pas à un fils de continuer sans parent.
- `abort()` désigne ici l'opération générale. Sous UNIX, un processus en arrête un autre en lui envoyant un **signal** avec l'appel `kill(pid, signal)` : `SIGTERM` demande poliment l'arrêt (le processus peut nettoyer avant de finir), `SIGKILL` l'impose sans qu'il puisse s'y opposer. La commande `kill` du shell fait la même chose ([[Commande kill]]). La fonction C `abort()`, elle, fait s'arrêter brutalement le processus **qui l'appelle**. [[Complément hors du cours|ⓘ]]
- Certains OS n'autorisent pas un fils à exister si son parent est terminé : tous ses fils doivent l'être aussi. Quand un parent s'arrête, l'OS applique la **[[Terminaison en cascade]]** (*cascading termination*) : fils, petits-fils, etc. sont terminés.
- Le parent peut attendre la fin d'un fils par `wait()` ([[Appels wait() et waitpid()]]), qui renvoie des informations d'état (succès ou échec du fils) et le pid du processus terminé.
- **PID** (*Process ID*) : unique pour chaque processus.

```c
pid = wait(&status);
```

- `status` contient des informations sur la façon dont le fils s'est terminé ;
- `wait()` renvoie le PID du fils terminé ;
- `wait(&status)` permet au parent d'attendre la fin d'un fils et d'obtenir des informations sur cette fin.

`status` ne se lit pas directement : on le décode avec des macros de `<sys/wait.h>`. `WIFEXITED(status)` est vrai si le fils s'est terminé normalement (par `exit()` ou un `return` de `main`), et `WEXITSTATUS(status)` donne alors la valeur passée à `exit()`, son [[Code de retour]] : par convention 0 pour un succès, une autre valeur pour une erreur. `WIFSIGNALED(status)` indique une fin causée par un signal. Pour attendre un fils précis plutôt que le premier qui finit, on utilise `waitpid(pid, &status, 0)` ([[Appels wait() et waitpid()]]). [[Complément hors du cours|ⓘ]]

```c
int status;
pid_t fils = wait(&status);
if (WIFEXITED(status))
    printf("fils %d fini avec le code %d\n", fils, WEXITSTATUS(status));
```

C'est le même mécanisme que `$?` dans le shell, qui contient le code de retour de la dernière commande. [[Complément hors du cours|ⓘ]]

### Zombie et orphelin

Voir [[Processus zombie et orphelin]].

- **Zombie** : aucun parent n'attend (pas d'appel à `wait()`). Un fils devient zombie quand il a fini mais que son parent n'a pas encore appelé `wait()` ; c'est un processus terminé dont les informations de terminaison n'ont pas été récupérées. « Le zombie occupe la mémoire inutilement ».
- **Orphelin** : le parent s'est terminé sans appeler `wait()`. C'est un processus qui continue de s'exécuter alors que son parent est terminé. L'OS le prend en charge : il le rattache généralement au processus système spécial `init` ([[Processus init]]) ou équivalent, qui devient son nouveau parent et se charge de nettoyer les orphelins.
- Précision sur le zombie : sa mémoire, ses fichiers et ses autres ressources sont déjà libérés ; il ne garde que son entrée dans la table des processus (PID, code de retour, temps CPU consommé), pour que le parent puisse la lire. Un zombie isolé ne coûte presque rien ; le risque vient d'un parent qui en crée sans cesse sans jamais appeler `wait()`, et finit par épuiser les PID disponibles. Il apparaît avec l'état `Z` et la mention `<defunct>` dans `ps`. On ne peut pas le tuer avec `kill` (il est déjà mort) : il disparaît quand son parent appelle `wait()`, ou quand le parent se termine, car `init` l'adopte alors et le nettoie. [[Complément hors du cours|ⓘ]]
- Sur la plupart des distributions Linux actuelles, le processus de PID 1 qui joue le rôle d'`init` est `systemd` ([[Processus init]]). [[Complément hors du cours|ⓘ]]

## Un arbre de processus

Exemple de programme qui crée un processus séparé : [[Erreurs du cours#^e-7-os|✎]]

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
pid_t pid;

    /* fork a child process */
    pid = fork();

    if (pid < 0) { /* error occurred */
      fprintf(stderr, "Fork Failed");
      return 1;
    }
    else if (pid == 0) { /* child process */
      execlp("/bin/ls","ls",NULL);
    }
    else { /* parent process */
      /* parent will wait for the child to complete */
      wait(NULL);
      printf("Child Complete");
    }

    return 0;
}
```

Le fils remplace son programme par `ls` (`execlp`) ; le parent attend sa fin puis affiche « Child Complete ».

Les arguments de `execlp("/bin/ls","ls",NULL)` sont : le programme à lancer (le `p` de `execlp` permet de donner seulement `"ls"`, cherché dans le `PATH`), puis la liste des arguments du nouveau programme, qui commence par son propre nom (il deviendra `argv[0]`), et enfin `NULL` pour marquer la fin. Un `exec()` réussi **ne revient jamais** : le code du fils est entièrement remplacé, donc une ligne écrite après `execlp` ne s'exécute que si l'appel a échoué ; on y met en général un message d'erreur et un `exit(1)` ([[Appel exec()]]). [[Complément hors du cours|ⓘ]]

Le PID, l'utilisateur et les fichiers ouverts sont conservés par `exec()` : le fils garde le même PID, seul le programme change. C'est exactement ce que fait un shell pour chaque commande tapée : `fork()`, puis `exec()` de la commande dans le fils, et `wait()` dans le shell, sauf si la commande est lancée en arrière-plan avec `&`. [[Complément hors du cours|ⓘ]]

**Exercice classique** : combien de processus crée ce code ? [[Complément hors du cours|ⓘ]]

```c
fork();
fork();
fork();
```

Chaque `fork()` est exécuté par tous les processus qui existent à ce moment et double leur nombre : 1 → 2 → 4 → 8. Il y a donc $2^3 = 8$ processus au total, soit 7 créés en plus du processus initial ; avec $n$ appels successifs, $2^n$ processus. [[Complément hors du cours|ⓘ]]

![[OS - chp7 - image12.png]]
*Figure : exemple d'arbre de processus : A crée B et C ; B crée D, E et F ; C crée G ; D crée H ; H crée I.*

Sous Linux, la racine de l'arbre est le processus de PID 1 (`init` ou `systemd`), lancé par le noyau au démarrage ; tous les autres en descendent. La commande `pstree -p` affiche l'arbre réel avec les PID, et `ps -ef` donne pour chaque processus son PID et celui de son parent (colonne `PPID`) ; en C, `getpid()` et `getppid()` renvoient ces deux valeurs ([[Arbre de processus]]). [[Complément hors du cours|ⓘ]]

## Architecture multiprocessus : le navigateur Chrome

Voir [[Architecture multiprocessus de Chrome]].

- Beaucoup de navigateurs tournent en un seul processus (certains encore) : si un site pose problème, tout le navigateur peut planter.
- Google Chrome est multiprocessus, avec trois types de processus :
  - **Browser process** : gère l'interface utilisateur et les E/S disque et réseau ;
  - **Renderer process** : affiche les pages web, traite HTML et JavaScript ; un nouveau *renderer* est créé pour chaque site ouvert ; il tourne dans un *sandbox* qui restreint les E/S disque et réseau, ce qui limite l'effet des failles de sécurité ;
  - **Plug-in process** : un par type de plug-in.
- Le prix de cette architecture est une consommation de mémoire plus élevée (chaque processus a son propre espace d'adressage), et la nécessité de faire dialoguer les processus entre eux : le *renderer*, enfermé dans son *sandbox*, demande au *browser process* de faire pour lui les accès réseau et disque. Ce dialogue relève de la [[Communication interprocessus]]. [[Complément hors du cours|ⓘ]]
- Le gestionnaire de tâches de Chrome (menu « Plus d'outils ») montre ces processus un par un, avec leur mémoire et leur CPU. [[Complément hors du cours|ⓘ]]
- Une vidéo est donnée en lien : https://www.youtube.com/watch?v=TguLnogR1NM&list=WL&index=44

## Annotations de l'étudiante

Annotations du dessin sur la mémoire : taille allouée dans la RAM, mémoire dynamique (peut grandir ou rétrécir), zones fixes ou dynamiques. Annotation sur les états : « Storage ; RAM ; RAM ; CPU ; LT scheduler », mots sans leurs flèches, donc sans doute le trajet disque vers RAM vers CPU de l'ordonnanceur à long terme. Sur les files : une tranche de temps expirée renvoie le processus en ready queue ; il emprunte l'une des quatre files.