---
type: concept
tags: [year2]
aliases: [interrupt, interrupts, interruption matérielle, ISR, interrupt service routine, vecteur d'interruption, interrupt request, interruption logicielle, déroutement, trap, NMI, interruption non masquable, interrupt-driven, scrutation, polling]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : signal envoyé par le matériel au CPU, qui force le processeur à suspendre ce qu'il fait pour traiter un événement urgent. Un contrôleur de périphérique en émet une quand une opération d'entrée/sortie est terminée : le CPU peut ainsi faire autre chose pendant l'attente.

Réponse du CPU, en cinq temps selon le cours :
1. un événement externe (entrée utilisateur, périphérique, erreur) émet le signal ;
2. le CPU arrête le traitement courant et sauvegarde son état (par exemple l'adresse de l'instruction suivante) ;
3. il consulte le **vecteur d'interruption**, table qui associe chaque type d'interruption à l'adresse de sa routine ;
4. il exécute l'**ISR** (Interrupt Service Routine), le code propre à cette interruption ;
5. il restaure son état et reprend le travail d'origine.

Exemple du cours : l'imprimante interrompt le CPU, puis une seconde interruption signale la fin de l'impression.

Un [[Appel système]] est aussi un moyen de déclencher une interruption, côté logiciel. Pour accéder à la mémoire sans solliciter le CPU, un périphérique peut utiliser le **DMA** (Direct Memory Access).

## Complément (hors du cours)

**Interruptions logicielles.** Les interruptions provoquées par le programme lui-même s'appellent **déroutements** (*traps*) ou **exceptions**. Elles sont soit volontaires (un [[Appel système]], par exemple `read()` pour lire un fichier, qui fait passer en [[Mode noyau et mode utilisateur|mode noyau]]), soit dues à une erreur : division par zéro, instruction illégale, accès à une adresse mémoire interdite (qui donne une [[Erreur de segmentation]]). À la différence d'une interruption matérielle, qui arrive à n'importe quel moment, une exception est synchrone : elle naît de l'instruction en cours.

**OS piloté par les interruptions.** Un système d'exploitation moderne est dit *interrupt-driven* : il ne travaille qu'en réponse à des événements (interruptions matérielles, exceptions, appels système). L'horloge matérielle envoie aussi des interruptions régulières, qui permettent à l'OS de reprendre la main pour l'[[Ordonnancement des processus|ordonnancement]].

**Alternative : la scrutation (*polling*).** Le CPU interroge le contrôleur en boucle pour savoir s'il a fini. C'est simple, mais le CPU perd son temps à attendre un périphérique lent ; avec les interruptions, il fait autre chose jusqu'à ce que le périphérique se signale.

**Priorités et masquage.** Les interruptions ont des priorités : une interruption urgente peut interrompre le traitement d'une moins urgente. Pendant une opération critique, le CPU peut **masquer** (ignorer temporairement) les interruptions de faible priorité. Les **interruptions non masquables** (*NMI*, *Non-Maskable Interrupt*) ne peuvent pas être ignorées : elles sont réservées aux événements graves, comme une erreur mémoire matérielle.

## Dans le cours

Le cours décrit l'interruption matérielle, sa réponse en cinq temps et l'exemple de l'imprimante ; les interruptions logicielles, la scrutation et les priorités sont des compléments de [[1 - OS]].

Voir aussi : [[Appel système]], [[Contrôleur de périphérique]], [[Bus système]], [[Changement de contexte]], [[Hiérarchie de stockage]], [[Accès direct à la mémoire]], [[Opération d'entrée-sortie]].

Résumé : [[1 - OS]]
