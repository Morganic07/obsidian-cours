---
type: concept
tags: [year2]
aliases: [mode noyau, mode utilisateur, kernel mode, user mode, dual-mode, mode privilégié, mode superviseur]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le processeur a au moins deux modes d'exécution, indiqués par un **bit de mode**.

- En **mode noyau** (*kernel mode*, mode superviseur ou privilégié), toutes les instructions sont permises : accès direct au matériel, gestion de la mémoire et des [[Interruption|interruptions]]. C'est le mode du [[Noyau|noyau]].
- En **mode utilisateur** (*user mode*), les instructions privilégiées sont interdites. Si une application en tente une, le matériel déclenche une exception et le [[Système d'exploitation|système d'exploitation]] reprend la main (en général pour arrêter le programme).
- Une application qui a besoin du matériel passe par un [[Appel système|appel système]] : une instruction de *trap* fait basculer le CPU en mode noyau, l'OS exécute le service demandé, puis revient en mode utilisateur. Exemple : `read()` pour lire un fichier.
- Cette séparation protège l'OS et les autres programmes des erreurs ou des abus d'un programme.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - OS]], à propos de l'OS comme programme de contrôle.

Voir aussi : [[Appel système]], [[Interruption]], [[Noyau]], [[Système d'exploitation]].

Résumés : [[1 - OS]]
