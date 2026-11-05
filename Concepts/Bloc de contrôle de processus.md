---
type: concept
aliases: [PCB, process control block, Process Control Block, bloc de contrôle de processus]
matieres: [Operating System]
sources: ["[[OS - chp7]]"]
maj: 2026-11-05
---

Structure de données qui stocke l'essentiel sur un [[Processus]] : de quoi sauvegarder puis restaurer son état. Chaque processus a son PCB, mis à jour à chaque changement d'état.

Contenu cité par le cours :
- état du processus (running, waiting…) ;
- numéro du processus ;
- compteur ordinal (*program counter*) : prochaine instruction à exécuter ;
- registres du CPU (variables temporaires, données intermédiaires) ;
- informations d'ordonnancement : priorités, pointeur de file ;
- gestion mémoire : mémoire allouée, limites ;
- état des E/S : périphériques alloués, fichiers ouverts ;
- comptabilité : temps CPU utilisé, temps écoulé depuis le début, limites de temps.

Le contexte d'un processus est représenté dans son PCB : c'est lui que le [[Changement de contexte]] sauvegarde et recharge.

Liens : [[Processus]], [[États d'un processus]], [[Changement de contexte]]

Résumé : [[OS - chp7 (résumé)]]
