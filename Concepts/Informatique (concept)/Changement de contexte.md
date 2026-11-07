---
type: concept
tags: [year2]
aliases: [context switch, context switching, commutation de contexte]
matieres: [Operating System]
sources: ["[[OS - chp 7 (résumé)|OS - chp7]]"]
maj: 2026-11-06
---

Le CPU passe d'un [[Processus]] à un autre : le système sauvegarde l'état de l'ancien dans son [[Bloc de contrôle de processus]] et charge l'état sauvegardé du nouveau. Le déclencheur est une [[Interruption]] ou un [[Appel système]].

Points du cours :
- pendant le changement, le système ne fait aucun travail utile ;
- plus le système et le PCB sont complexes, plus il dure ;
- sa durée dépend du matériel : certains permettent de charger plusieurs contextes à la fois.

Le contexte est représenté dans le PCB. Le [[Dispatcher]] est le composant qui l'effectue lors du passage de ready à running (voir [[États d'un processus]]).

Liens : [[Processus]], [[Ordonnancement des processus]], [[Bloc de contrôle de processus]]

Résumé : [[OS - chp 7 (résumé)]]
