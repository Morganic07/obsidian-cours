---
type: matiere
tags:
  - year2
sources:
  - "[[1 - OS|OS - chp 1]]"
  - "[[2 - OS|OS - chp 2]]"
  - "[[3 - OS|OS - chp 3]]"
  - "[[5 - OS|OS - chp 5]]"
  - "[[7 - OS|OS - chp7]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[1 - TP1|cours TP1]]"
  - "[[2 - TP2|Cours TP2]]"
  - "[[3 - TP3|Cours TP3]]"
  - "[[4 - TP4|Cours TP4]]"
  - "[[5 - TP5|Cours TP5]]"
maj: 2026-11-08
---

Systèmes d'exploitation : matériel, démarrage, stockage, Linux, processus, et pratique du shell (Bash, cron, AWK). Les 11 notes sont des notes de cours : chapitres 1, 2, 3, 5, 7, fiche de commandes, TP1 à TP5. Il n'y a pas de note pour le chapitre 6, et le chapitre 4 n'existe qu'en PDF (voir « Documents PDF »).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - OS\|OS - chp 1]] | Matériel, bus, interruptions, stockage, architectures | [[1 - OS\|Résumé]] |
| [[2 - OS\|OS - chp 2]] | Disques, partitions, systèmes de fichiers, BIOS et UEFI | [[2 - OS\|Résumé]] |
| [[3 - OS\|OS - chp 3]] | Linux, Ubuntu, installation | [[3 - OS\|Résumé]] |
| [[5 - OS\|OS - chp 5]] | Shell, `cat`, `chmod`, APT, scripts | [[5 - OS\|Résumé]] |
| [[7 - OS\|OS - chp7]] | Processus, ordonnancement, `fork` | [[7 - OS\|Résumé]] |
| [[8 - OS commandes sh\|Commandes Shell + explications]] | Fiche de commandes et de Bash | [[8 - OS commandes sh\|Résumé]] |
| [[1 - TP1\|cours TP1]] | `sudo`, sudoers, clavier, nom d'hôte, `mkdir -p`, `chmod -R` | [[1 - TP1\|Résumé]] |
| [[2 - TP2\|Cours TP2]] | Jokers, redirections, tâches de fond | [[2 - TP2\|Résumé]] |
| [[3 - TP3\|Cours TP3]] | Réseau, `/etc/hosts`, scripts de sauvegarde | [[3 - TP3\|Résumé]] |
| [[4 - TP4\|Cours TP4]] | Programme C `fork`, cron | [[4 - TP4\|Résumé]] |
| [[5 - TP5\|Cours TP5]] | AWK | [[5 - TP5\|Résumé]] |

## Documents PDF

Six PDF complètent les notes : le chapitre 4 du cours et les sujets des TP2 à TP6.

| Document | Contenu | Résumé |
|---|---|---|
| OS - chp 4 ([[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf\|OS - chp 4.pdf]]) | Arborescence Linux, répertoire racine, partitions | [[4 - OS\|Résumé]] |

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
- **Ajoutés par l'enrichissement** : [[Mode noyau et mode utilisateur]], [[Conteneur (informatique)]], [[Table de partitions GPT]], [[Journalisation (système de fichiers)]], [[Flux standard]], [[Gestionnaire de paquets]], [[Masque umask]], [[Tableau associatif]], [[Commande ps]], [[Mémoire virtuelle]], [[Communication interprocessus]], [[Code de retour]]

Les fiches sont enrichies de compléments hors du cours, marqués ⓘ.

## À revoir en priorité avant un examen

- [[3 - OS]] : macOS est un Unix (noyau XNU, héritage BSD), sans noyau Linux.
- [[8 - OS commandes sh]] : sur Debian et Ubuntu, `/bin/sh` est `dash`, pas Bash.
- [[2 - OS]] : dans les vitesses d'interfaces, distinguer bits et octets par seconde.

## Contenu manquant ou à compléter

Le cours ne couvre pas les algorithmes d'ordonnancement (FCFS, Round Robin), les threads en détail, la mémoire virtuelle, la synchronisation ni l'interblocage . Il n'y a pas de chapitre 6 ; le chapitre 4 (arborescence et partitions) est résumé depuis son PDF.

## Liens avec les autres matières

- **[[Cours/Informatique/Computer Network/_index|Computer Network]]** : le TP3 anticipe ce cours avec l'[[Adressage IPv4 et CIDR]], l'[[IPv6]], l'[[Adresse de bouclage]], l'[[Interface réseau]] et la [[Commande ping]].
- **[[Cours/Informatique/C++/_index|C++]]** : la [[Structure conditionnelle]], la [[Boucle (programmation)]], le [[Tableau (programmation)]], l'[[Opérateur de comparaison]] et le [[Code ASCII]] y sont repris en C.
- **[[Cours/Informatique/Algo/_index|Algo]]** et **[[Cours/Informatique/Java/_index|Java]]** : les mêmes structures de contrôle, en pseudo-code et en Java.
- **[[Cours/Informatique/Algo/_index|Algo]]** : la [[Factorielle]], calculée ici par des processus en C, y sert d'exemple de récursivité.
