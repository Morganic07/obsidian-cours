---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 3.docx|OS - chp 3]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 3.docx|OS - chp 3]] (« Course 3 »), dans [[Cours/Informatique/OS/_index|Operating System]].
## Idée générale

Linux, ses distributions, Ubuntu et l'installation d'un système (sur PC ou en machine virtuelle).

## Qu'est-ce que Linux ?

- [[Linux]] est une famille de systèmes d'exploitation libres (*open source*) fondés sur le [[Noyau]] Linux (*Linux kernel*).
- Linux n'est pas un système complet à lui seul : sur le noyau il faut ajouter une distribution ([[Ubuntu]], Debian…). Mac OS, lui, n'est pas construit sur le noyau Linux. [[Erreurs du cours#^e-3-os|✎]]
- Chaque distribution a ses propres logiciels : par exemple, le lecteur vidéo d'Ubuntu diffère de celui de Debian.
- Le noyau doit être complété par d'autres composants : systèmes de fenêtrage, [[Environnement de bureau|environnements de bureau]], logiciels d'application. Ils peuvent être fournis par la distribution ou installés à part.
- Le noyau Linux a été lancé en 1991 par Linus Torvalds, alors étudiant à Helsinki, et il est distribué sous licence GNU GPL. Les outils de base qui l'entourent (shell, compilateur [[GCC]], bibliothèque C, utilitaires) viennent en grande partie du projet GNU, lancé en 1983 par Richard Stallman pour écrire un système libre de type Unix : d'où l'appellation « GNU/Linux » que l'on rencontre aussi. [[Complément hors du cours|ⓘ]]
- macOS ne repose pas sur Linux : son noyau, XNU, combine le micronoyau Mach et du code issu de BSD, une autre lignée de systèmes Unix ; Linux et macOS sont donc deux systèmes **de type Unix** distincts, ce qui explique leurs commandes très proches. Android, en revanche, repose bien sur le noyau Linux. [[Complément hors du cours|ⓘ]]

## Les distributions Linux

- Une **[[Distribution Linux]]** (*distro*) est un ensemble de paquets logiciels regroupés pour être installés sur un ordinateur (« en gros, c'est Debian ou Ubuntu »).
- Son cœur est le noyau Linux, le cœur du système.
- Elle comprend aussi d'autres composants : système de fenêtrage, environnement de bureau, logiciels d'application.
- Ce qui distingue surtout les distributions, c'est leur [[Gestionnaire de paquets|gestionnaire de paquets]] et leur dépôt de logiciels : `apt` et les paquets `.deb` pour Debian et Ubuntu ([[APT]]), `dnf` et les paquets `.rpm` pour Fedora (et la famille Red Hat, dont CentOS), `pacman` pour Arch Linux, `zypper` pour openSUSE. Elles diffèrent aussi par leur rythme de publication : versions figées et stables (Debian), versions à date fixe (Ubuntu, Fedora) ou mise à jour continue, dite *rolling release* (Arch Linux). Ubuntu est elle-même dérivée de Debian. [[Complément hors du cours|ⓘ]]

![[OS - chp 3 - image2.png]]
*Figure : logos de distributions populaires : Ubuntu, Fedora, Arch Linux, Debian, CentOS, openSUSE.*

## Qu'est-ce qu'Ubuntu ?

- Système libre fondé sur le noyau Linux, la distribution la plus populaire.
- Apprécié parce qu'il est convivial, stable et riche en fonctionnalités.
- Deux versions :
  - **Ubuntu Desktop**, avec [[Interface graphique|GUI]] ;
  - **Ubuntu Server**, en ligne de commande ([[Interface en ligne de commande|CLI]]).
- Deux types de publication ([[Version LTS et version intermédiaire]]) :
  - **LTS** (*Long Term Support*) : version majeure, stable, supportée longtemps (5 ans de mises à jour standard), idéale pour un système fiable ; [[Erreurs du cours#^e-3-os|✎]]
  - **Interim release** : moins stable, pour tester de nouvelles fonctionnalités, support court (9 mois).
- Ubuntu est éditée par l'entreprise Canonical. Une version sort tous les six mois, en avril et en octobre, et porte le numéro *année.mois* : 24.04 est sortie en avril 2024. Les LTS sortent tous les deux ans, en avril des années paires (20.04, 22.04, 24.04). Depuis la 12.04, Canonical annonce 5 ans de mises à jour standard pour une LTS, Desktop comme Server, prolongeables par l'abonnement Ubuntu Pro ; avant la 12.04, les LTS Desktop n'avaient que 3 ans (Canonical, annonce de 2011). [[Complément hors du cours|ⓘ]]

## Installer Ubuntu

- Il faut le fichier `Ubuntu.iso`.
- Une **[[Image ISO]]** est un fichier qui contient une copie complète et exacte d'un disque optique (CD, DVD, [[Disque optique|Blu-ray]]). Elle sert à distribuer des logiciels, installer des systèmes, faire des sauvegardes.
- Le nom vient de la norme ISO 9660, qui définit le système de fichiers des CD-ROM. L'ISO d'Ubuntu est une image dite *live* : démarrée depuis une clé, elle lance un Ubuntu complet en mémoire, qu'on peut essayer sans rien installer, et qui propose l'installation sur le disque. Avant de l'utiliser, on peut vérifier son intégrité en comparant son empreinte SHA-256 (`sha256sum ubuntu.iso`) à celle publiée sur le site officiel. [[Complément hors du cours|ⓘ]]
- [[Partition (disque)|Partitions]] nécessaires à Ubuntu (voir [[Partitions Linux]]) :
  - **zone d'échange** ([[Espace d'échange (swap)|swap area]]) : espace du [[Disque dur]] que Linux utilise quand la [[Mémoire vive|RAM]] est pleine ;
  - **racine** `/` (*root*, [[Répertoire racine]]) ;
  - **[[Partition système EFI]]** (*EFI system partition*) ;
  - **zone de démarrage BIOS réservée** (*reserved BIOS boot area*) ;
  - **`/home`** ([[Répertoire personnel]]).
- La partition EFI et la zone de démarrage BIOS ne servent pas en même temps : elles dépendent du micrologiciel de la machine ([[BIOS et UEFI]]). Un PC récent démarre en **UEFI** : son micrologiciel lit la partition système EFI, une petite partition [[FAT32]] (quelques centaines de Mo, montée sur `/boot/efi`) qui contient le [[Chargeur de démarrage|chargeur de démarrage]] (GRUB pour Ubuntu). Un PC ancien démarre en **BIOS** : sur un disque partitionné en GPT, GRUB a alors besoin d'une petite partition de 1 Mo environ, sans système de fichiers, la *BIOS boot partition*, pour y loger son code ; sur un disque à table [[MBR]], ce code se place juste après le MBR. [[Complément hors du cours|ⓘ]]
- **MBR et GPT** sont les deux tables de partitionnement d'un disque. MBR, l'ancienne, limite à 4 partitions principales et à des disques de 2 To environ ; GPT (*GUID Partition Table*), qui fait partie de la norme UEFI, admet par défaut 128 partitions et des disques bien plus grands. [[Complément hors du cours|ⓘ]]
- `/` et le swap sont les seules partitions indispensables : sans partition `/home` séparée, `/home` est un simple dossier de la racine. Le swap peut aussi être un fichier (`/swap.img`), ce que fait l'installateur d'Ubuntu par défaut depuis la 17.04 ; il sert de plus à l'hibernation, qui y copie le contenu de la RAM. [[Complément hors du cours|ⓘ]]
- Sous Windows, il y a plusieurs racines (C:, D:, E:…) ; sous Linux, une seule (`/`). Voir [[Arborescence des répertoires Linux]].
- Sous Linux, chaque partition ou périphérique (seconde partition, clé USB, disque réseau) est rattaché à un dossier de cette arborescence unique, son [[Point de montage|point de montage]] : `/home` peut être une autre partition, une clé USB apparaît par exemple sous `/media/<utilisateur>/<nom>`. Le montage se fait avec `mount`, et le fichier `/etc/fstab` liste les partitions montées au démarrage. [[Complément hors du cours|ⓘ]]

## Arbre de décision de l'installation

![[OS - chp 3 - image1.png]]
*Figure : organigramme « Operating System Installation » : branche PC/portable (ISO, clé USB bootable avec Rufus, démarrage, installation) et branche machine virtuelle (logiciel selon l'OS hôte, création de la VM, ISO, installation).*

**Sur PC ou portable** :
1. obtenir l'image ISO de Windows ou d'Ubuntu ;
2. créer une [[Clé USB amorçable]] avec Rufus (le télécharger d'abord) ;
3. démarrer le PC sur la clé ;
4. lancer l'installation de Windows ou d'Ubuntu.

Pour démarrer sur la clé, il faut en général appuyer au démarrage sur la touche du menu de démarrage ou du réglage du micrologiciel (souvent F12, F2, Échap ou Suppr, selon le fabricant) et choisir la clé dans la liste. Rufus fonctionne sous Windows ; depuis Linux, des outils comme le créateur de disque de démarrage d'Ubuntu ou balenaEtcher font la même chose. L'écriture efface tout le contenu de la clé. Installer Ubuntu à côté de Windows sur le même disque s'appelle un *dual boot* : l'installateur réduit la partition Windows, et GRUB propose au démarrage de choisir le système. [[Complément hors du cours|ⓘ]]

**Sur [[Machine virtuelle]]** :
1. selon l'OS hôte : Windows → installer VirtualBox ; Ubuntu → installer KVM ;
2. créer une machine virtuelle ;
3. obtenir l'image ISO ;
4. lancer l'installation sur la machine virtuelle.

Note de la diapositive : la clé USB bootable n'est pas nécessaire pour une installation en machine virtuelle.

**KVM** = *Kernel Virtual Machine*.

Le nom officiel est *Kernel-based Virtual Machine* : KVM est un module du noyau Linux qui fait du noyau lui-même un **hyperviseur**, le logiciel qui crée et fait tourner les machines virtuelles ([[Machine virtuelle]]). On distingue l'hyperviseur de **type 1** (*bare metal*), qui tourne directement sur le matériel (KVM, VMware ESXi, Hyper-V), et celui de **type 2** (*hébergé*), qui est une application d'un système hôte (VirtualBox, VMware Workstation). En pratique, KVM s'utilise sous Ubuntu avec QEMU et une interface comme virt-manager. [[Complément hors du cours|ⓘ]]

La virtualisation demande que le processeur offre des instructions dédiées (Intel VT-x ou AMD-V), activées dans le réglage du micrologiciel ; sans elles, VirtualBox et KVM refusent de lancer une machine 64 bits ou deviennent très lents. On réserve à la VM une part de la RAM, des cœurs et un disque virtuel, qui n'est qu'un fichier sur le disque de l'hôte (`.vdi` pour VirtualBox, `.qcow2` pour KVM). [[Complément hors du cours|ⓘ]]
