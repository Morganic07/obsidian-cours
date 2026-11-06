---
type: source
tags: [year2]
sources: ["[[OS - chp 3]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[OS - chp 3]] (« Course 3 »), dans [[Operating System (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Linux, ses distributions, Ubuntu et l'installation d'un système (sur PC ou en machine virtuelle).

## Qu'est-ce que Linux ?

- [[Linux]] est une famille de systèmes d'exploitation libres (*open source*) fondés sur le [[Noyau]] Linux (*Linux kernel*).
- Linux n'est pas un système complet à lui seul : sur le noyau il faut ajouter une distribution ([[Ubuntu]], Debian…). La note ajoute : « Mac OS est construit sur le noyau Linux » (faux, voir point à vérifier 1).
- Chaque distribution a ses propres logiciels : par exemple, le lecteur vidéo d'Ubuntu diffère de celui de Debian.
- Le noyau doit être complété par d'autres composants : systèmes de fenêtrage, [[Environnement de bureau|environnements de bureau]], logiciels d'application. Ils peuvent être fournis par la distribution ou installés à part.

## Les distributions Linux

- Une **[[Distribution Linux]]** (*distro*) est un ensemble de paquets logiciels regroupés pour être installés sur un ordinateur (« en gros, c'est Debian ou Ubuntu »).
- Son cœur est le noyau Linux, le cœur du système.
- Elle comprend aussi d'autres composants : système de fenêtrage, environnement de bureau, logiciels d'application.

![[Cours/Year 2/Operating System/Cours OS/medias/OS - chp 3/image2.png]]
*Figure : logos de distributions populaires : Ubuntu, Fedora, Arch Linux, Debian, CentOS, openSUSE.*

## Qu'est-ce qu'Ubuntu ?

- Système libre fondé sur le noyau Linux, la distribution la plus populaire.
- Apprécié parce qu'il est convivial, stable et riche en fonctionnalités.
- Deux versions :
  - **Ubuntu Desktop**, avec [[Interface graphique|GUI]] ;
  - **Ubuntu Server**, en ligne de commande ([[Interface en ligne de commande|CLI]]).
- Deux types de publication ([[Version LTS et version intermédiaire]]) :
  - **LTS** (*Long Term Support*) : version majeure, stable, supportée longtemps (« 3-4 ans » selon la note), idéale pour un système fiable ;
  - **Interim release** : moins stable, pour tester de nouvelles fonctionnalités, support court (9 mois).

## Installer Ubuntu

- Il faut le fichier `Ubuntu.iso`.
- Une **[[Image ISO]]** est un fichier qui contient une copie complète et exacte d'un disque optique (CD, DVD, [[Disque optique|Blu-ray]]). Elle sert à distribuer des logiciels, installer des systèmes, faire des sauvegardes.
- [[Partition (disque)|Partitions]] nécessaires à Ubuntu (voir [[Partitions Linux]]) :
  - **zone d'échange** ([[Espace d'échange (swap)|swap area]]) : espace du [[Disque dur]] que Linux utilise quand la [[Mémoire vive|RAM]] est pleine ;
  - **racine** `/` (*root*, [[Répertoire racine]]) ;
  - **[[Partition système EFI]]** (*EFI system partition*) ;
  - **zone de démarrage BIOS réservée** (*reserved BIOS boot area*) ;
  - **`/home`** ([[Répertoire personnel]]).
- Sous Windows, il y a plusieurs racines (C:, D:, E:…) ; sous Linux, une seule (`/`). Voir [[Arborescence des répertoires Linux]].

## Arbre de décision de l'installation

![[Cours/Year 2/Operating System/Cours OS/medias/OS - chp 3/image1.png]]
*Figure : organigramme « Operating System Installation » : branche PC/portable (ISO, clé USB bootable avec Rufus, démarrage, installation) et branche machine virtuelle (logiciel selon l'OS hôte, création de la VM, ISO, installation).*

**Sur PC ou portable** :
1. obtenir l'image ISO de Windows ou d'Ubuntu ;
2. créer une [[Clé USB amorçable]] avec Rufus (le télécharger d'abord) ;
3. démarrer le PC sur la clé ;
4. lancer l'installation de Windows ou d'Ubuntu.

**Sur [[Machine virtuelle]]** :
1. selon l'OS hôte : Windows → installer VirtualBox ; Ubuntu → installer KVM ;
2. créer une machine virtuelle ;
3. obtenir l'image ISO ;
4. lancer l'installation sur la machine virtuelle.

Note de la diapositive : la clé USB bootable n'est pas nécessaire pour une installation en machine virtuelle.

**KVM** = *Kernel Virtual Machine*.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Mac OS est construit sur le noyau Linux »** : texte lu dans la note. C'est faux (macOS a un noyau d'origine BSD/Mach), complément. **À corriger avant un examen.**
2. **Durée du support LTS** : « 3-4 ans » ; le cours Ubuntu officiel parle plutôt de 5 ans (complément, non établi par la note).
3. **Interim release** : support de 9 mois selon la note ; à comparer avec le cours.
