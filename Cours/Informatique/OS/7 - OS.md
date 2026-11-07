---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]] (« Chp7 - Processes »), dans [[Cours/Informatique/OS/_index|Operating System]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les processus : ce qu'ils sont, leur mémoire, leurs états, leur bloc de contrôle, leur ordonnancement, le changement de contexte, le multitâche sur mobile, leur création et leur fin, l'exemple de Chrome.

## Concept de processus

- Un OS exécute des programmes variés, qui tournent sous forme de processus.
- Un **[[Processus]]** est un programme en exécution. Un programme est statique, un processus est une tâche en cours.
- Un programme est un fichier exécutable **passif** stocké sur le disque ; un processus est **actif**. Un programme chargé en mémoire devient un processus.
- L'[[Interface graphique]] (GUI) et la [[Interface en ligne de commande|ligne de commande]] (CLI) sont deux façons de lancer un programme.
- Un programme peut donner plusieurs processus (exemple : Chrome, un processus par onglet).
- **Pas d'exécution parallèle des instructions d'un même processus** : un processus exécute une instruction à la fois, dans l'ordre séquentiel. Le parallélisme passe par plusieurs processus ou plusieurs [[Thread|threads]] ; dans un seul processus, il n'y a en général qu'un flux d'exécution, le *thread principal*.

## Le processus en mémoire

Voir [[Espace mémoire d'un processus]]. Un processus contient :
- la **section text** : le code du programme ;
- la **pile** (*stack*) : données temporaires (variables locales, adresses de retour, paramètres de fonctions), voir [[Pile d'exécution]] ;
- la **section data** : variables globales ;
- le **tas** (*heap*) : mémoire allouée dynamiquement pendant l'exécution ([[Allocation dynamique]]).

![[OS - chp7 - image11.png]]
*Figure : espace mémoire d'un processus, de l'adresse 0 à max : text, data, heap, zone libre, stack ; la pile et le tas croissent l'un vers l'autre.*

Annotations de l'étudiante sur le dessin : « Memory length allocated inside the [[Mémoire vive|RAM]] » ; « Dynamic memory (can expand / shrink) » ; zones marquées « Dynamic ; fixed ; fixed ; Dynamic » (vraisemblablement stack et heap dynamiques, data et text fixes).

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

## États d'un processus

Voir [[États d'un processus]]. En s'exécutant, un processus change d'état :
- **New** : en cours de création ;
- **Ready** : attend d'être affecté à un processeur ;
- **Running** : ses instructions s'exécutent ;
- **Waiting** : attend un événement ;
- **Terminated** : a fini son exécution.

![[OS - chp7 - image14.png]]
*Figure : diagramme des états : new → ready (admitted), ready → running (scheduler dispatch), running → ready (interrupt), running → waiting (I/O or event wait), waiting → ready (I/O or event completion), running → terminated (exit).*

Annotation de l'étudiante sur le diagramme : « Storage ; RAM ; RAM ; [[Processeur|CPU]] ; LT scheduler » (mots sans leurs flèches ; sans doute le trajet disque → RAM → CPU, l'ordonnanceur à long terme gérant new → ready).

- Les processus **I/O bound** (Word, Chrome) sont la plupart du temps en *waiting* ; les **CPU bound** (jeu, programme Python) en *running* ([[Processus limité par les entrées-sorties ou par le processeur]]).
- Le **[[Dispatcher]]** est le composant qui effectue la [[Changement de contexte|commutation de contexte]] entre processus. Quand l'ordonnanceur choisit un processus *ready* pour passer en *running*, le dispatcher donne le CPU au processus choisi, ce qui inclut le chargement de son contexte (valeurs des registres et autres informations) depuis le PCB. Il est donc **directement impliqué dans le passage de ready à running**.

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

## Changement de contexte (*Context switch*)

Voir [[Changement de contexte]].

- Il a lieu quand le CPU passe d'un processus à un autre.
- Le système doit **sauvegarder l'état** de l'ancien processus et **charger l'état sauvegardé** du nouveau.
- Le contexte d'un processus est représenté dans son PCB.
- Le système ne fait aucun travail utile pendant le changement de contexte.
- Plus l'OS et le PCB sont complexes, plus le changement est long.
- La durée dépend du support matériel : certains matériels chargent plusieurs contextes à la fois.

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
- Certains OS n'autorisent pas un fils à exister si son parent est terminé : tous ses fils doivent l'être aussi. Quand un parent s'arrête, l'OS applique la **[[Terminaison en cascade]]** (*cascading termination*) : fils, petits-fils, etc. sont terminés.
- Le parent peut attendre la fin d'un fils par `wait()` ([[Appels wait() et waitpid()]]), qui renvoie des informations d'état (succès ou échec du fils) et le pid du processus terminé.
- **PID** (*Process ID*) : unique pour chaque processus.

```c
pid = wait(&status);
```

- `status` contient des informations sur la façon dont le fils s'est terminé ;
- `wait()` renvoie le PID du fils terminé ;
- `wait(&status)` permet au parent d'attendre la fin d'un fils et d'obtenir des informations sur cette fin.

### Zombie et orphelin

Voir [[Processus zombie et orphelin]].

- **Zombie** : aucun parent n'attend (pas d'appel à `wait()`). Un fils devient zombie quand il a fini mais que son parent n'a pas encore appelé `wait()` ; c'est un processus terminé dont les informations de terminaison n'ont pas été récupérées. « Le zombie occupe la mémoire inutilement ».
- **Orphelin** : le parent s'est terminé sans appeler `wait()`. C'est un processus qui continue de s'exécuter alors que son parent est terminé. L'OS le prend en charge : il le rattache généralement au processus système spécial `init` ([[Processus init]]) ou équivalent, qui devient son nouveau parent et se charge de nettoyer les orphelins.

## Un arbre de processus

Exemple de programme qui crée un processus séparé :

```c
#include <sys/types.h>
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

![[OS - chp7 - image12.png]]
*Figure : exemple d'arbre de processus : A crée B et C ; B crée D, E et F ; C crée G ; D crée H ; H crée I.*

## Architecture multiprocessus : le navigateur Chrome

Voir [[Architecture multiprocessus de Chrome]].

- Beaucoup de navigateurs tournent en un seul processus (certains encore) : si un site pose problème, tout le navigateur peut planter.
- Google Chrome est multiprocessus, avec trois types de processus :
  - **Browser process** : gère l'interface utilisateur et les E/S disque et réseau ;
  - **Renderer process** : affiche les pages web, traite HTML et JavaScript ; un nouveau *renderer* est créé pour chaque site ouvert ; il tourne dans un *sandbox* qui restreint les E/S disque et réseau, ce qui limite l'effet des failles de sécurité ;
  - **Plug-in process** : un par type de plug-in.
- Une vidéo est donnée en lien : https://www.youtube.com/watch?v=TguLnogR1NM&list=WL&index=44

## Annotations de l'étudiante

Annotations du dessin sur la mémoire : taille allouée dans la RAM, mémoire dynamique (peut grandir ou rétrécir), zones fixes ou dynamiques. Annotation sur les états : « Storage ; RAM ; RAM ; CPU ; LT scheduler », mots sans leurs flèches, donc sans doute le trajet disque vers RAM vers CPU de l'ordonnanceur à long terme. Sur les files : une tranche de temps expirée renvoie le processus en ready queue ; il emprunte l'une des quatre files.

## Erreurs du cours

- L'exemple C avec `fork()` de [[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]] inclut seulement `<sys/types.h>`, `<stdio.h>` et `<unistd.h>` mais appelle `wait(NULL)` ; il faut ajouter `#include <sys/wait.h>`, qui déclare `wait`.
