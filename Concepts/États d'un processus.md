---
type: concept
aliases: [process states, process state, état d'un processus, états d'un processus]
matieres: [Operating System]
sources: ["[[OS - chp7]]"]
maj: 2026-11-06
---

Un [[Processus]] change d'état pendant son exécution. Cinq états :

| État | Sens |
|---|---|
| *new* | le processus est en cours de création |
| *ready* | il attend qu'on lui affecte un processeur |
| *running* | ses instructions s'exécutent |
| *waiting* | il attend un événement (fin d'une E/S) |
| *terminated* | il a fini |

Transitions du diagramme : new → ready (*admitted*), ready → running (*scheduler dispatch*), running → ready (*interrupt*), running → waiting (*I/O or event wait*), waiting → ready (*I/O or event completion*), running → terminated (*exit*).

Le passage de ready à running est choisi par l'ordonnanceur à court terme et réalisé par le **dispatcher**, qui effectue le [[Changement de contexte]] en rechargeant le contexte depuis le [[Bloc de contrôle de processus]].

Notion parente : [[Processus]]. Voir aussi : [[Ordonnancement des processus]], [[Changement de contexte]], [[Processus limité par les entrées-sorties ou par le processeur]]

Résumé : [[OS - chp7 (résumé)]]
