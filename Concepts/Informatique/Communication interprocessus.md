---
type: concept
tags: [year2]
aliases: [IPC, inter-process communication, interprocess communication, communication entre processus]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la communication interprocessus (IPC, *inter-process communication*) désigne l'ensemble des mécanismes qui permettent à des [[Processus|processus]], dont les mémoires sont séparées, d'échanger des données ou de se synchroniser.

Deux modèles :

- **mémoire partagée** : une zone de mémoire commune que les processus lisent et écrivent directement ; rapide, car l'OS n'intervient plus après la mise en place, mais les accès doivent être synchronisés (sémaphores, verrous) ;
- **passage de messages** : les processus s'envoient des messages par l'intermédiaire de l'OS (`send` / `receive`) ; plus simple et sans conflit d'accès, mais plus lent, car chaque échange passe par un appel système.

Outils Unix :

- tubes anonymes, créés par `pipe()` entre un parent et ses fils, et `|` dans le shell ([[Redirection et tube]]) ;
- tubes nommés (FIFO, `mkfifo`), utilisables entre processus sans lien de parenté ;
- signaux (`kill`, `SIGTERM`, `SIGKILL`…), simples notifications sans données ([[Commande kill]]) ;
- files de messages, mémoire partagée et sémaphores (System V ou POSIX) ;
- sockets, y compris entre machines différentes.

## Dans le cours

Le cours ne nomme pas la notion, mais elle répond à deux situations de [[7 - OS]] :

- après [[Appel fork()|fork()]], parent et fils ont chacun leur copie des variables : une variable globale ne permet pas de transmettre une valeur de l'un à l'autre, il faut un tube ou un autre mécanisme d'IPC ;
- dans l'[[Architecture multiprocessus de Chrome]], le *renderer*, enfermé dans un *sandbox*, demande au *browser process* les accès au disque et au réseau : les deux communiquent par IPC.

Voir aussi : [[Appel fork()]], [[Redirection et tube]], [[Architecture multiprocessus de Chrome]], [[Processus]].

Résumés : [[7 - OS]]
