---
type: matiere
sources: ["[[OS - chp 1]]", "[[OS - chp 2]]", "[[OS - chp 3]]", "[[OS - chp 5]]", "[[OS - chp7]]", "[[Commandes Shell + explications]]", "[[cours TP1]]", "[[Cours TP2]]", "[[Cours TP3]]", "[[Cours TP4]]", "[[Cours TP5]]"]
maj: 2026-11-05
---

Systèmes d'exploitation : matériel, démarrage, stockage, Linux, processus, et pratique du shell (Bash, cron, AWK). Les 21 notes sont intégrées : 11 notes de cours (chapitres 1, 2, 3, 5, 7, fiche de commandes, TP1 à TP5) et 10 notes de rendus (TP, DM, rapports). Il n'y a pas de note pour le chapitre 6, et le chapitre 4 n'existe qu'en PDF (voir « Documents PDF »).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[OS - chp 1]] | Matériel, bus, interruptions, stockage, architectures | [[OS - chp 1 (résumé)\|Résumé]] |
| [[OS - chp 2]] | Disques, partitions, systèmes de fichiers, BIOS et UEFI | [[OS - chp 2 (résumé)\|Résumé]] |
| [[OS - chp 3]] | Linux, Ubuntu, installation | [[OS - chp 3 (résumé)\|Résumé]] |
| [[OS - chp 5]] | Shell, `cat`, `chmod`, APT, scripts | [[OS - chp 5 (résumé)\|Résumé]] |
| [[OS - chp7]] | Processus, ordonnancement, `fork` | [[OS - chp7 (résumé)\|Résumé]] |
| [[Commandes Shell + explications]] | Fiche de commandes et de Bash | [[Commandes Shell + explications (résumé)\|Résumé]] |
| [[cours TP1]] | `sudo`, nom de machine, clavier, droits | [[cours TP1 (résumé)\|Résumé]] |
| [[Cours TP2]] | Jokers, redirections, tâches de fond | [[Cours TP2 (résumé)\|Résumé]] |
| [[Cours TP3]] | Réseau, `/etc/hosts`, scripts de sauvegarde | [[Cours TP3 (résumé)\|Résumé]] |
| [[Cours TP4]] | Programme C `fork`, cron | [[Cours TP4 (résumé)\|Résumé]] |
| [[Cours TP5]] | AWK | [[Cours TP5 (résumé)\|Résumé]] |
| [[DM Shell Scripting]] | Scripts Bash, cœurs, premiers | [[DM Shell Scripting (résumé)\|Résumé]] |
| [[Copy of 08 Processes-TP]] | Programmes C avec `fork` | [[Copy of 08 Processes-TP (résumé)\|Résumé]] |
| [[Operating Systems - Semester report]] | Rapport des labs 1 et 2 | [[Operating Systems - Semester report (résumé)\|Résumé]] |
| [[UNIX Commands - Semester report]] | Rapport des TP1 à TP6 | [[UNIX Commands - Semester report (résumé)\|Résumé]] |
| [[TP1]] | Rendu du TP1 | [[TP1 (résumé)\|Résumé]] |
| Rendu TP2 (dossier DM/TP2) | Rendu du TP2 | [[TP2 (résumé)\|Résumé]] |
| Rendu TP3 (dossier DM/TP3) | Rendu du TP3 | [[TP3 (résumé)\|Résumé]] |
| Rendu TP4 (dossier DM/TP4) | Rendu du TP4 | [[TP4 (résumé)\|Résumé]] |
| [[Cours/Year 2/Operating System/DM/TP5/TP5\|TP5 (DM)]] | Rendu du TP5 | [[TP5 (résumé)\|Résumé]] |
| [[Cours/Year 2/Operating System/DM/TP6/log\|log (TP6)]] | Données pour AWK | [[log (résumé)\|Résumé]] |

## Documents PDF

Six PDF complètent les notes : le chapitre 4 du cours et les sujets des TP2 à TP6.

| Document | Contenu | Résumé |
|---|---|---|
| [[raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf\|OS - chp 4]] | Arborescence Linux, répertoire racine, partitions | [[OS - chp 4 (résumé)\|Résumé]] |
| [[raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf\|Copy of TP2-Commands]] | Sujet du TP2 : jokers, redirections, tâches de fond, guillemets | [[Copy of TP2-Commands (résumé)\|Résumé]] |
| [[raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf\|TP3-Commands (2)]] | Sujet du TP3 : adresse IP, `/etc/hosts`, Netplan, sauvegarde | [[TP3-Commands (2) (résumé)\|Résumé]] |
| [[raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf\|TP4-Unix Commands]] | Sujet du TP4 : `fork` en C, cron | [[TP4-Unix Commands (résumé)\|Résumé]] |
| [[raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf\|TP5-AWK Command]] | Sujet du TP5 : AWK | [[TP5-AWK Command (résumé)\|Résumé]] |
| [[raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf\|TP6-Assignment]] | Sujet du TP6 : informations système, sudo, cron, AWK, `fork` | [[TP6-Assignment (résumé)\|Résumé]] |

## Concepts

- **Système et matériel** : [[Système d'exploitation]], [[Noyau]], [[Interruption]], [[Appel système]], [[Hiérarchie de stockage]], [[Machine virtuelle]]
- **Démarrage et disques** : [[BIOS et UEFI]], [[Système de fichiers]], [[Distribution Linux]]
- **Processus** : [[Processus]], [[États d'un processus]], [[Bloc de contrôle de processus]], [[Ordonnancement des processus]], [[Changement de contexte]], [[Création et terminaison de processus]], [[Processus zombie et orphelin]]
- **Shell** : [[Shell et Bash]], [[Permissions Unix]], [[Redirection et tube]], [[Script Bash]], [[Tâche planifiée cron]], [[AWK]]

## À revoir en priorité avant un examen

- [[OS - chp 3 (résumé)]] : macOS n'est pas construit sur le noyau Linux.
- [[Commandes Shell + explications (résumé)]] : `sh` n'est pas Bash sur Debian/Ubuntu (c'est `dash`).
- [[DM Shell Scripting (résumé)]] : la version Python du test de primalité compte 4 comme premier.
- [[cours TP1 (résumé)]] : `chmod -R 444` retire le droit de traverser les dossiers.
- [[OS - chp 2 (résumé)]] : tableau des vitesses d'interfaces aux unités mélangées.

## Contenu manquant ou à compléter

Le cours ne couvre pas les algorithmes d'ordonnancement (FCFS, Round Robin), les threads en détail, la mémoire virtuelle, la synchronisation ni l'interblocage . Il n'y a pas de chapitre 6 ; le chapitre 4 (arborescence et partitions) est résumé depuis son PDF.

## Liens avec les autres matières

Cette matière est autonome dans le coffre : elle reste à relier aux cours de réseaux ou d'architecture quand ils seront intégrés.
