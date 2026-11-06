---
type: matiere
tags: [year2]
sources: ["[[OS - chp 1]]", "[[OS - chp 2]]", "[[OS - chp 3]]", "[[OS - chp 5]]", "[[OS - chp7]]", "[[Commandes Shell + explications]]", "[[cours TP1]]", "[[Cours TP2]]", "[[Cours TP3]]", "[[Cours TP4]]", "[[Cours TP5]]"]
maj: 2026-11-06
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

- **Environnements informatiques (chp 1)** : [[Système d'exploitation]], [[Environnement informatique]], [[Modèle client-serveur]], [[Cloud computing]], [[Calcul haute performance]], [[Système distribué]], [[Système en grappe (cluster)]], [[Gestionnaire de verrous distribué]], [[Réseau de stockage SAN]], [[Système monoprocesseur]], [[Système multiprocesseur]], [[Machine virtuelle]], [[Interface en ligne de commande]], [[Interface graphique]]
- **Matériel et noyau (chp 1)** : [[Carte mère]], [[Processeur]], [[Cœur de processeur]], [[Hyperthreading]], [[Registre du processeur]], [[Bus système]], [[Contrôleur de périphérique]], [[Pilote de périphérique]], [[Interruption]], [[Accès direct à la mémoire]], [[Opération d'entrée-sortie]], [[Tampon (buffer)]], [[Cycle mémoire]], [[Code ASCII]], [[Noyau]], [[Appel système]]
- **Mémoire et supports de stockage (chp 1 et 2)** : [[Hiérarchie de stockage]], [[Mémoire vive]], [[Mémoire morte]], [[Mémoire cache]], [[Mémoire volatile et non volatile]], [[Disque dur]], [[SSD]], [[Disque optique]], [[Bande magnétique]], [[Secteur défectueux]]
- **Interfaces de stockage (chp 2)** : [[Interface de stockage]], [[IDE (PATA)]], [[SATA]], [[SAS (interface de stockage)]], [[SCSI]], [[PCI Express]], [[M.2]], [[NVMe]]
- **Partitions, systèmes de fichiers et démarrage (chp 2)** : [[Partition (disque)]], [[MBR]], [[Formatage d'un disque]], [[Système de fichiers]], [[FAT32]], [[Système de fichiers exFAT]], [[NTFS]], [[ReFS]], [[EXT4]], [[XFS]], [[NFS]], [[BIOS et UEFI]], [[Démarrage sécurisé]]
- **Linux et installation (chp 3)** : [[Linux]], [[Distribution Linux]], [[Ubuntu]], [[Version LTS et version intermédiaire]], [[Environnement de bureau]], [[Wayland et X11]], [[Image ISO]], [[Clé USB amorçable]], [[Partition système EFI]], [[Espace d'échange (swap)]]
- **Arborescence Linux (chp 4)** : [[Arborescence des répertoires Linux]], [[Répertoire racine]], [[Répertoire personnel]], [[Chemin de fichier]], [[Point de montage]], [[Partitions Linux]], [[Partition de démarrage]], [[Chargeur de démarrage]], [[Image initrd]], [[Bibliothèque partagée]], [[Fichier de périphérique]], [[Fichier journal]], [[Fichiers de mots de passe]], [[Lien symbolique]]
- **Shells, éditeurs et paquets (chp 5)** : [[Shell et Bash]], [[Bourne Shell (sh)]], [[Shell dash]], [[Shell rbash]], [[Fichier shells]], [[Éditeur de texte]], [[Vim]], [[Éditeur nano]], [[Gedit]], [[APT]]
- **Utilisateurs et droits (chp 5, TP1)** : [[Super-utilisateur root]], [[Commande sudo]], [[Fichier sudoers]], [[Commande su]], [[Commande passwd]], [[Hachage de mot de passe]], [[Permissions Unix]], [[Commande chmod]], [[Nom d'hôte]], [[Commande hostname]], [[Disposition du clavier]]
- **Commandes de fichiers** : [[Commande ls]], [[Commande cd]], [[Commande pwd]], [[Commande mkdir]], [[Commande rmdir]], [[Commande touch]], [[Commande cp]], [[Commande mv]], [[Commande rm]], [[Commande cat]], [[Commande tree]], [[Commande echo]]
- **Aide et informations système** : [[Commande man]], [[Commande info]], [[Option --help]], [[Commande which]], [[Commande whoami]], [[Commande uname]], [[Commande date]], [[Commande uptime]], [[Commande df]], [[Commande free]], [[Commande lscpu]], [[Commande lshw]], [[Commande nproc]], [[Cœur en ligne et hors ligne]], [[Commandes shutdown et poweroff]]
- **Traitement de texte en ligne de commande** : [[Commande grep]], [[Commande sort]], [[Commande uniq]], [[Commande wc]], [[Commande shuf]], [[Commande tee]], [[Commande read]]
- **Syntaxe du shell et tâches (TP2)** : [[Joker (wildcard)]], [[Méta-caractère]], [[Expansion d'accolades]], [[Guillemets en shell]], [[Caractère d'échappement]], [[Redirection et tube]], [[Substitution de commande]], [[Groupement de commandes]], [[Sous-shell]], [[Tâche en arrière-plan]], [[Commande jobs]], [[Commandes fg et bg]], [[Commande sleep]], [[Commande kill]]
- **Scripts Bash (fiche de commandes, DM)** : [[Script Bash]], [[Shebang]], [[Exécution d'un script]], [[Commentaire en Bash]], [[Variable Bash]], [[Arithmétique en Bash]], [[Opérateur de comparaison]], [[Opérateur logique]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Tableau (programmation)]], [[Nombre premier]], [[Factorielle]]
- **Réseau et sauvegarde (TP3)** : [[Interface réseau]], [[Adressage IPv4 et CIDR]], [[IPv6]], [[Adresse de bouclage]], [[DHCP]], [[DNS]], [[Fichier hosts]], [[Netplan]], [[YAML]], [[Commande ip]], [[Commande ifconfig]], [[Commande ping]], [[Sauvegarde de fichier]]
- **Processus et ordonnancement (chp 7)** : [[Processus]], [[Espace mémoire d'un processus]], [[Compteur de programme]], [[États d'un processus]], [[Bloc de contrôle de processus]], [[Thread]], [[Ordonnancement des processus]], [[Processus limité par les entrées-sorties ou par le processeur]], [[Quantum de temps]], [[Dispatcher]], [[Changement de contexte]], [[Multitâche sur mobile]], [[Architecture multiprocessus de Chrome]]
- **Création de processus en C (chp 7, TP4)** : [[Création et terminaison de processus]], [[Identifiant de processus]], [[Arbre de processus]], [[Processus init]], [[Appel fork()]], [[Appel exec()]], [[Appels wait() et waitpid()]], [[Processus zombie et orphelin]], [[Terminaison en cascade]], [[GCC]], [[Fonction system() en C]], [[Nombres aléatoires en C]], [[Suite arithmétique]]
- **Services et tâches planifiées (TP4)** : [[Démon (informatique)]], [[Commande systemctl]], [[Commande journalctl]], [[Tâche planifiée cron]]
- **AWK (TP5)** : [[AWK]], [[Fichier CSV]], [[Fichier TSV]], [[Séparateur de champs]], [[Blocs BEGIN et END d'AWK]], [[Variables intégrées d'AWK]], [[Fonctions intégrées d'AWK]], [[Expression régulière]]

## À revoir en priorité avant un examen

- [[OS - chp 3 (résumé)]] : macOS n'est pas construit sur le noyau Linux.
- [[Commandes Shell + explications (résumé)]] : `sh` n'est pas Bash sur Debian/Ubuntu (c'est `dash`).
- [[DM Shell Scripting (résumé)]] : la version Python du test de primalité compte 4 comme premier.
- [[cours TP1 (résumé)]] : `chmod -R 444` retire le droit de traverser les dossiers.
- [[OS - chp 2 (résumé)]] : tableau des vitesses d'interfaces aux unités mélangées.

## Contenu manquant ou à compléter

Le cours ne couvre pas les algorithmes d'ordonnancement (FCFS, Round Robin), les threads en détail, la mémoire virtuelle, la synchronisation ni l'interblocage . Il n'y a pas de chapitre 6 ; le chapitre 4 (arborescence et partitions) est résumé depuis son PDF.

## Liens avec les autres matières

- **[[Computer Network (matière)]]** : le TP3 anticipe ce cours avec l'[[Adressage IPv4 et CIDR]], l'[[IPv6]], l'[[Adresse de bouclage]], l'[[Interface réseau]] et la [[Commande ping]].
- **[[C++ (matière)]]** : la [[Structure conditionnelle]], la [[Boucle (programmation)]], le [[Tableau (programmation)]], l'[[Opérateur de comparaison]] et le [[Code ASCII]] y sont repris en C.
- **[[Algo Maths (matière)]]** et **[[Java (matière)]]** : les mêmes structures de contrôle, en pseudo-code et en Java.
- **[[Algo (matière)]]** : la [[Factorielle]], calculée ici par des processus en C, y sert d'exemple de récursivité.
- **[[Anglais (matière)]]** : « operating system » figure dans le vocabulaire Global Exam ([[Système d'exploitation]]).
