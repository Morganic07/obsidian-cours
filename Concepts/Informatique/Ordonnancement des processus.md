---
type: concept
tags: [year2]
aliases: [process scheduling, scheduler, ordonnanceur, ordonnancement, long term scheduler, short term scheduler, mid term scheduler, ready queue, wait queue, wait queues, scheduling queues, swapper, FCFS, SJF, Round Robin, tourniquet, ordonnancement préemptif, preemptive scheduling, dispatch latency, latence de répartition]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

L'ordonnanceur (*scheduler*) décide quel processus *ready* passe ensuite sur le CPU. Objectif du cours : maximiser l'usage du CPU et changer vite de processus.

**Files d'attente** : la *ready queue* (processus en mémoire principale, prêts à s'exécuter) et les *wait queues* (processus qui attendent un événement, comme une E/S). Les processus migrent d'une file à l'autre. Depuis le CPU, un processus peut : faire une requête d'E/S (file d'attente d'E/S), épuiser sa tranche de temps (retour en ready queue), créer un fils et l'attendre, ou attendre une interruption.

**Trois ordonnanceurs** :
- long terme (*LTS*) : choisit les processus qui passent de *new* à *ready* ;
- court terme (*STS*) : choisit ceux qui passent de *ready* à *running* ;
- moyen terme (*MTS*, ou *swapper*) : peut déplacer un processus de la RAM vers le stockage (voir [[Espace d'échange (swap)]]).

Le cours ne présente pas d'algorithme d'ordonnancement (FCFS, Round Robin…), seulement la notion de tranche de temps ([[Quantum de temps]]).

## Compléments (hors du cours)

**Fréquence d'intervention** : l'ordonnanceur court terme intervient très souvent (toutes les quelques millisecondes), il doit donc être très rapide. L'ordonnanceur long terme intervient rarement ; il règle le **degré de multiprogrammation** (nombre de processus en mémoire) et cherche un bon mélange de processus *I/O bound* (qui passent surtout leur temps en E/S) et *CPU bound* (qui calculent surtout). Il est quasi absent des systèmes de bureau comme Linux ou Windows, où tout processus lancé est admis.

**Latence de répartition** (*dispatch latency*) : temps que met le *dispatcher* pour arrêter un processus et en lancer un autre ([[Changement de contexte]], passage en mode utilisateur, saut à l'instruction à reprendre).

**Préemptif ou non** : un ordonnancement **non préemptif** laisse le processus sur le CPU jusqu'à ce qu'il se termine ou se bloque de lui-même ; un ordonnancement **préemptif** peut le lui retirer (fin de quantum, arrivée d'un processus plus prioritaire). Les systèmes actuels sont préemptifs.

**Algorithmes classiques** :

- **FCFS** (*First Come, First Served*) : premier arrivé, premier servi, non préemptif. Un long processus en tête fait attendre tous les courts derrière lui (**effet de convoi**).
- **SJF** (*Shortest Job First*) : le plus court d'abord. Il donne le temps d'attente moyen minimal, mais suppose de connaître la durée à l'avance, et un long processus peut attendre indéfiniment (**famine**). Sa version préemptive s'appelle SRTF (*Shortest Remaining Time First*).
- **Par priorité** : le processus de plus haute priorité passe d'abord ; risque de famine pour les faibles priorités, corrigé par le **vieillissement** (*aging*), qui augmente la priorité d'un processus à mesure qu'il attend. Sous Linux, `nice -n 10 commande` lance une commande avec une priorité plus faible (de −20, la plus haute, à 19), et `renice` change celle d'un processus en cours.
- **Tourniquet** (*Round Robin*) : chaque processus reçoit à tour de rôle un [[Quantum de temps]], puis retourne en fin de *ready queue*. Un quantum trop long ramène à FCFS ; un quantum trop court multiplie les changements de contexte, qui coûtent du temps CPU.

**Exemple** : trois processus arrivés ensemble, de durées 24, 3 et 3 (dans cet ordre).

- FCFS : temps d'attente 0, 24 et 27, moyenne $\frac{0 + 24 + 27}{3} = 17$ ;
- SJF : ordre 3, 3, 24, temps d'attente 0, 3 et 6, moyenne $\frac{0 + 3 + 6}{3} = 3$.

Liens : [[Processus]], [[États d'un processus]], [[Changement de contexte]], [[Interruption]], [[Quantum de temps]], [[Espace d'échange (swap)]]

Résumé : [[7 - OS]]
