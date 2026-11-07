---
type: concept
tags: [year2]
aliases: [process scheduling, scheduler, ordonnanceur, ordonnancement, long term scheduler, short term scheduler, mid term scheduler, ready queue, wait queue, wait queues, scheduling queues, swapper]
matieres: [Operating System]
sources: ["[[7 - OS (résumé)|OS - chp7]]"]
maj: 2026-11-06
---

L'ordonnanceur (*scheduler*) décide quel processus *ready* passe ensuite sur le CPU. Objectif du cours : maximiser l'usage du CPU et changer vite de processus.

**Files d'attente** : la *ready queue* (processus en mémoire principale, prêts à s'exécuter) et les *wait queues* (processus qui attendent un événement, comme une E/S). Les processus migrent d'une file à l'autre. Depuis le CPU, un processus peut : faire une requête d'E/S (file d'attente d'E/S), épuiser sa tranche de temps (retour en ready queue), créer un fils et l'attendre, ou attendre une interruption.

**Trois ordonnanceurs** :
- long terme (*LTS*) : choisit les processus qui passent de *new* à *ready* ;
- court terme (*STS*) : choisit ceux qui passent de *ready* à *running* ;
- moyen terme (*MTS*, ou *swapper*) : peut déplacer un processus de la RAM vers le stockage (voir [[Espace d'échange (swap)]]).

Le cours ne présente pas d'algorithme d'ordonnancement (FCFS, Round Robin…), seulement la notion de tranche de temps ([[Quantum de temps]]).

Liens : [[Processus]], [[États d'un processus]], [[Changement de contexte]], [[Interruption]], [[Quantum de temps]], [[Espace d'échange (swap)]]

Résumé : [[7 - OS (résumé)]]
