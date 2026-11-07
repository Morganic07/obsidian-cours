---
type: concept
tags: [year2]
aliases: [interrupt, interrupts, interruption matérielle, ISR, interrupt service routine, vecteur d'interruption, interrupt request]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]"]
maj: 2026-11-06
---

Signal envoyé par le matériel au CPU, qui force le processeur à suspendre ce qu'il fait pour traiter un événement urgent. Un contrôleur de périphérique en émet une quand une opération d'entrée/sortie est terminée : le CPU peut ainsi faire autre chose pendant l'attente.

Réponse du CPU, en cinq temps selon le cours :
1. un événement externe (entrée utilisateur, périphérique, erreur) émet le signal ;
2. le CPU arrête le traitement courant et sauvegarde son état (par exemple l'adresse de l'instruction suivante) ;
3. il consulte le **vecteur d'interruption**, table qui associe chaque type d'interruption à l'adresse de sa routine ;
4. il exécute l'**ISR** (Interrupt Service Routine), le code propre à cette interruption ;
5. il restaure son état et reprend le travail d'origine.

Exemple du cours : l'imprimante interrompt le CPU, puis une seconde interruption signale la fin de l'impression.

Un [[Appel système]] est aussi un moyen de déclencher une interruption, côté logiciel. Pour accéder à la mémoire sans solliciter le CPU, un périphérique peut utiliser le **DMA** (Direct Memory Access).

Voir aussi : [[Appel système]], [[Contrôleur de périphérique]], [[Bus système]], [[Changement de contexte]], [[Hiérarchie de stockage]].

Résumé : [[1 - OS]]
