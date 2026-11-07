---
type: concept
tags: [year2]
aliases: [processes, processus en cours, parent process, child process, program in execution, programme en exécution]
matieres: [Operating System]
sources: ["[[OS - chp 7 (résumé)|OS - chp7]]"]
maj: 2026-11-06
---

Un processus est un programme en cours d'exécution. Le programme est un fichier exécutable passif, stocké sur le disque ; il devient processus quand il est chargé en mémoire. Un programme peut donner plusieurs processus (Chrome : un processus par onglet). Chaque processus a un identifiant unique, le **PID**.

Un processus exécute ses instructions l'une après l'autre : un seul flux (le thread principal). Le parallélisme vient de plusieurs processus ou de plusieurs threads.

**Mémoire d'un processus** : section `text` (code), section `data` (variables globales), `heap` (mémoire allouée dynamiquement à l'exécution) et `stack` (variables locales, adresses de retour, paramètres de fonctions). Le tas et la pile grandissent l'un vers l'autre dans la zone libre. Dans un programme C : `int x;` (non initialisée) et `int y = 15;` (initialisée) vont dans les données, `malloc` dans le tas, `argc`/`argv` en haut de la mémoire.

**Types** : un processus *I/O bound* (Word, Chrome) passe l'essentiel du temps en attente, un processus *CPU bound* (jeu, programme Python) en exécution.

**Multiprocessus, exemple de Chrome** : un processus *browser* (interface, E/S disque et réseau), un processus *renderer* par site (dans un sandbox), un processus par type de plug-in. Un navigateur à processus unique plante en entier si un site pose problème.

**Mobile** : les premières versions d'iOS n'autorisaient qu'un processus au premier plan ; Android exécute premier plan et arrière-plan, ce dernier via un *service* sans interface.

Liens : [[États d'un processus]], [[Bloc de contrôle de processus]], [[Ordonnancement des processus]], [[Changement de contexte]], [[Création et terminaison de processus]], [[Processus zombie et orphelin]], [[Espace mémoire d'un processus]], [[Thread]]

Résumés : [[OS - chp 7 (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[TP4-Unix Commands (résumé)]]
