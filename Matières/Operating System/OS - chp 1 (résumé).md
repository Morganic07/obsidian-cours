---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]] (« Chp 1 - Introduction »), dans [[Operating System (matière)]]. Notes de cours de l'étudiante, en français et en anglais, avec les figures des diapositives. En cas d'écart, le cours et ses images font foi.

## Idée générale

Introduction : matériel d'un ordinateur, rôle du [[Système d'exploitation]], communication CPU / mémoire / périphériques, interruptions et démarrage, hiérarchie de stockage, architectures de systèmes et environnements informatiques.

## Matériel d'un ordinateur (*Computer system hardware*)

Tous les ordinateurs ont le même squelette, serveur ou PC : seule la taille change.

![[OS - chp 1 - image4.jpg]]
*Figure : composants d'une [[Carte mère]] : slots d'extension (carte graphique, carte son), connecteurs d'entrée/sortie, socket du CPU, puces North Bridge et South Bridge, slots des barrettes [[Mémoire vive|RAM]], pile CMOS.*

![[OS - chp 1 - image6.png]]
*Figure : carte mère MSI MAG B660 Tomahawk vue de dessus : socket du processeur au centre, quatre slots DIMM à droite, slots PCIe, emplacements M.2 sous dissipateurs, pile BAT1.*

Repères sur la carte mère :
1. **Alimentation du processeur** : 2×8 broches (*pin* = nombre de trous), à côté du processeur.
2. **Alimentation de la carte mère** : toujours située à droite.
3. **Stockage** : deux méthodes de transfert de données, [[SATA]] et [[M.2]] ; les emplacements M.2 sont les plaques avec de petits numéros, souvent vissées.
4. **Port [[PCI Express]]** : slot pour carte graphique, carte Wi-Fi.

**Architecture d'un serveur** : deux alimentations (« batteries » dans la note) ; si l'une tombe, l'autre prend le relais.

![[OS - chp 1 - image7.png]]
*Figure : serveur Dell en rack ouvert : dissipateur du processeur, barrettes mémoire, emplacement CPU2, rangée de ventilateurs, alimentation, baies de disques.*

## Processeurs, cœurs et *hyperthreading*

Le [[Processeur]] (CPU, *Central Processing Unit*) interprète les instructions reçues en quatre temps :
1. recherche de l'instruction ;
2. interprétation des champs opérandes et des codes d'opération ;
3. exécution ;
4. écriture du résultat.

Il **met aussi en relation** les composants de l'ordinateur ([[Disque dur]], mémoire vive, carte graphique…).

- **Cœur** (*core*) : unité qui lit et exécute des instructions ; un cœur = une tâche à la fois ; multicœur = plusieurs tâches ([[Cœur de processeur]]).
- **Multithreading / [[Hyperthreading]]** : transforme les cœurs physiques en plusieurs cœurs virtuels, pour qu'un seul cœur physique exécute plusieurs tâches en parallèle. Seules certaines applications en ont besoin : jeux vidéo, montage vidéo, pas YouTube ni Google.

![[OS - chp 1 - image5.png]]
*Figure : processeur à 4 cœurs, chacun divisé en deux [[Thread|threads]] (8 threads au total).*

## Qu'est-ce qu'un système d'exploitation ?

L'OS sert d'intermédiaire entre l'utilisateur et le matériel. Objectifs :
- exécuter les programmes de l'utilisateur ;
- rendre l'ordinateur plus facile à utiliser ;
- gérer le matériel.

Autrefois les OS étaient en [[Interface en ligne de commande|CLI]] (*command line interface*) ; aujourd'hui on a des [[Interface graphique|GUI]] (*graphical user interface*).

## Structure d'un système informatique (*Computer system structure*)

![[OS - chp 1 - image12.png]]
*Figure : quatre couches reliées par des flèches bidirectionnelles : user, application programs (compilateurs, navigateurs, kits de développement), operating system, computer hardware (CPU, mémoire, périphériques d'E/S).*

- **Matériel** : fournit les ressources de calcul de base.
- **OS** : contrôle et coordonne l'usage du matériel entre applications et utilisateurs.
- **Programmes d'application** : définissent comment les ressources servent à résoudre les problèmes des utilisateurs.
- **Utilisateurs** : personnes, machines, autres ordinateurs.

## Organisation d'un système informatique (*Computer system organization*)

Les bus sont des circuits de la carte mère qui relient le CPU aux autres composants. Trois bus forment ensemble le **[[Bus système]]** (*system bus*) :

![[OS - chp 1 - image2.png]]
*Figure : Data Bus, Address Bus et Control Bus réunis forment le System Bus.*

| Bus | Rôle | Sens |
|---|---|---|
| *Data bus* | transporte données et instructions entre tous les composants | bidirectionnel |
| *Address bus* | envoie des signaux du CPU vers la mémoire principale | unidirectionnel |
| *Control bus* | envoie des signaux de contrôle entre composants (horloge, demandes d'[[Interruption\|interruption]]…) | bidirectionnel |

![[OS - chp 1 - image3.png]]
*Figure : CPU, contrôleur de disque (disques), contrôleur USB (souris, clavier, imprimante) et adaptateur graphique (moniteur) reliés à la mémoire par un bus système commun.*

- **CPU** : cerveau de l'ordinateur ; exécute les instructions, traite les données, communique avec les périphériques par le bus système.
- **Bus système** : canal de communication entre périphériques.
- **RAM** : espace où stocker et transférer les données entre périphériques ; le CPU traite ces données. Les périphériques peuvent accéder à la RAM en même temps, le bus système régule les accès pour éviter les conflits.
- Un programme ne peut pas être « chargé sur le [[SSD]] directement » : ses données doivent être transférées en RAM pour que le CPU les traite vite (voir point à vérifier 2).

**Traitement des instructions** :
- **[[Mémoire cache|Cache du CPU]]** : mémoire très rapide dans le CPU, qui stocke données et instructions fréquentes ; le CPU vérifie ses caches avant d'aller en RAM.
- **SSD** : si les données ne sont pas en RAM, on va les chercher sur le SSD, puis on les copie en RAM et éventuellement dans le cache.

$$\text{vitesse SSD} \ll \text{vitesse RAM} \ll \text{vitesse caches}$$

**[[Cycle mémoire]]** (*memory cycle*) : processus complet d'interaction entre CPU et RAM pour accéder à des données : demande d'adresse, lecture ou écriture, transmission des données, délais associés. Le CPU émet une requête à la RAM via une adresse mémoire. Si les données sont dans le cache, le CPU les utilise sans aller en RAM ; si elles sont sur le SSD et pas en RAM, l'OS les charge d'abord en RAM.

## Fonctionnement d'un système informatique (*Computer system operation*)

- Le CPU et les périphériques peuvent fonctionner simultanément.
- Chaque périphérique est relié à son propre **contrôleur** ([[Contrôleur de périphérique]], ou *adapter* pour le graphique), qui gère les communications avec le CPU.
- Chaque périphérique a un **[[Tampon (buffer)|buffer]]** : petite mémoire intermédiaire qui stocke temporairement les données avant leur transfert vers le CPU ou le périphérique. « Le buffer se vide dès que la tâche est accomplie » (voir point à vérifier 2).
- Chaque contrôleur fonctionne grâce à un **pilote** (*driver*, [[Pilote de périphérique]]), programme propre à chaque type de périphérique, intermédiaire entre l'OS et le matériel.
- Le CPU déplace les données entre la mémoire principale (RAM) et les buffers locaux des contrôleurs. Exemple : à une lecture sur disque, le contrôleur place les données dans son buffer avant que le CPU ne les transfère en RAM.

Un dessin illustre ce passage ; seuls ses mots subsistent dans la note : RAM, *Device controller*, *Buffer*, CPU (disposition et flèches perdues).

- Les données des périphériques passent d'abord par le buffer local du contrôleur ; les buffers servent surtout aux E/S, pour que le CPU ne soit pas ralenti par les périphériques lents. Les opérations internes CPU/RAM n'y passent pas.
- La RAM reste l'endroit central où les données sont stockées avant traitement par le CPU.
- Quand un contrôleur a fini une opération (lecture de fichier, impression), il envoie une **interruption** au CPU, ce qui permet au CPU de faire autre chose pendant l'E/S.
- À retenir : *each device comes with a buffer, a driver and a controller*.

**Exemple du clavier** : comment le CPU comprend-il que j'ai appuyé sur « A » ? Chaque touche a un [[Code ASCII]] (*American Standard Code for Information Interchange*). Le CPU ne gère pas le clavier, il serait trop occupé : un CPU local dans le clavier fait touche pressée → conversion en ASCII → conversion en binaire utilisable par le CPU principal.

## Termes importants

- **Programme d'amorçage** (*Bootstrap program*, *firmware*) : premier programme lancé à la mise sous tension ou au redémarrage, appelé **BIOS** (*Basic Input/Output System*, voir [[BIOS et UEFI]]). Il est stocké en [[Mémoire morte|ROM]] (*Read-Only Memory*), mémoire non modifiable qui conserve ses données hors tension. Étapes :
  - **POST** (*Power On Self-Test*) : vérifie l'alimentation, la RAM et le matériel ;
  - **localisation de l'OS** : le BIOS va à l'emplacement du disque qui contient l'OS et le copie du stockage vers la RAM. L'ordinateur est alors utilisable.
- **[[Interruption]]** (*interrupt*) : signal envoyé par le matériel au CPU, qui le force à suspendre ce qu'il fait pour traiter l'interruption. Le matériel peut l'envoyer à tout moment via le bus système. Exemple : le CPU est occupé et je lance une impression ; l'imprimante interrompt le CPU, qui sauvegarde son opération en mémoire et traite la requête ; une nouvelle interruption signale la fin de l'impression, et le CPU reprend.
- **[[Appel système]]** (*system call*) : méthode par laquelle un logiciel déclenche une interruption du CPU pour lui demander une action précise.

## Réponse du CPU à une interruption

1. **Interruption** : un événement externe (saisie de l'utilisateur, requête d'un périphérique, erreur) envoie un signal au CPU.
2. **Arrêt du traitement courant** : le CPU s'interrompt et sauvegarde son état (par exemple l'adresse de l'instruction suivante).
3. **Transfert d'exécution** : le CPU consulte le **vecteur d'interruption**, table qui associe à chaque type d'interruption l'adresse mémoire de l'ISR correspondante (la table d'adresses est la liste de ces adresses).
4. **Exécution de l'ISR** (*Interrupt Service Routine*) : code exécuté en réponse à une interruption ; chaque ISR gère une interruption particulière.
5. **Retour au traitement d'origine** : le CPU restaure son état et reprend.

## Structure de stockage

![[OS - chp 1 - image16.png]]
*Figure : [[Hiérarchie de stockage]] en pyramide : registres, cache, mémoire principale (stockage volatil, primaire), mémoire non volatile, disques durs (secondaire), disque optique, bandes magnétiques (tertiaire). Capacité croissante et temps d'accès croissant vers le bas.*

Annotation de l'étudiante sur le dessin : « Located in the CPU » (voir point à vérifier 1).

| Niveau | Contenu | Caractéristiques |
|---|---|---|
| **Mémoire principale** (*main memory*) | RAM, cache, registres | seule mémoire à laquelle le processeur accède directement ; accès aléatoire (n'importe quelle adresse) ; **volatile** (perd tout hors tension) ; sous forme de DRAM (*Dynamic Random Access Memory*) |
| **Stockage secondaire** | SSD (mémoire non volatile, flash, bien plus rapide que les HDD), HDD (disque magnétique) | extension de la mémoire principale, grande capacité non volatile ; un ordinateur peut avoir un SSD et/ou un HDD |
| **Stockage tertiaire** | [[Disque optique]] (CD, DVD, Blu-ray), [[Bande magnétique\|bandes magnétiques]] | archivage ; les bandes vont jusqu'à plusieurs To par cartouche, lecture séquentielle ; data centers, entreprises |

Voir [[Mémoire volatile et non volatile]].

## Fonctionnement d'une opération d'E/S (*Working of an I/O operation*)

Section marquée « A COMPRENDRE » par l'étudiante.

![[OS - chp 1 - image10.png]]
*Figure : le CPU (thread d'exécution, cache) échange instructions et données avec la mémoire ; il envoie une requête d'E/S à un périphérique, qui renvoie des données et une interruption ; le périphérique accède aussi directement à la mémoire par DMA.*

Une [[Opération d'entrée-sortie]] suit trois temps :
1. requête d'E/S (*I/O request*) ;
2. transfert de données (image, PDF…) ;
3. interruption.

**DMA** (*Direct Memory Access*, [[Accès direct à la mémoire]]) : permet d'accéder à la RAM sans interrompre le CPU.

## Architecture des systèmes (*Computer system architecture*)

On classe les systèmes selon le nombre de CPU.

- **[[Système monoprocesseur]]** (*single processor systems*) : PC, téléphone. Un processeur pour les tâches générales, et d'autres processeurs locaux pour des tâches spécifiques (le CPU du clavier…).
- **[[Système multiprocesseur]]** (*multi-processor systems*, ou *parallel systems*) : serveurs. Les processeurs généraux communiquent et partagent le bus système, la mémoire et les périphériques.
  - **multiprocesseur symétrique** (SMP) : chaque processeur traite un travail à la fois ;
  - **multiprocesseur asymétrique** : le processeur maître donne des tâches précises à ses esclaves.

![[OS - chp 1 - image8.png]]
*Figure : à gauche, multiprocesseur symétrique (CPU 1 à 3 reliés à un même ensemble de processus P1 à P3) ; à droite, asymétrique (un maître relié à trois esclaves, chacun traitant un processus).*

- **[[Système en grappe (cluster)|Systèmes en grappe]]** (*clustered systems*) : data center, groupe d'ordinateurs.
  - plusieurs ordinateurs qui travaillent ensemble ;
  - stockage centralisé partagé via un [[Réseau de stockage SAN|SAN]] (*Storage Area Network*) ;
  - **haute disponibilité** : si un nœud (un ordinateur) tombe, le cluster continue ;
    - *asymmetric clustering* : un nœud est en veille active (*hot-standby*), inactif en attente d'une panne ; si un nœud actif échoue, il prend le relais ;
    - *symmetric clustering* : tous les nœuds sont actifs et exécutent des applications, chacun surveille les autres ; si l'un échoue, les autres se partagent sa charge ;
  - certains clusters servent au [[Calcul haute performance]] (HPC) : tâches lourdes ; les applications doivent être écrites pour la **parallélisation**, le travail étant divisé entre nœuds ;
  - **DLM** ([[Gestionnaire de verrous distribué]], *Distributed Lock Manager*) : évite les opérations simultanées sur une ressource partagée en gérant des verrous distribués, pour éviter les incohérences de données.

## Environnements informatiques (*Computing environments*)

![[OS - chp 1 - image13.png]]
*Figure : trois couches empilées : processes, kernel, hardware.*

- **Environnement traditionnel** : machine autonome à usage général (PC, portable). Le [[Noyau]] (*kernel*) est le cœur de l'OS.
- **Environnement mobile** : machine autonome à usage général (smartphones). Différences : riche en capteurs (GPS, gyroscope…), nouveaux types d'applications (réalité augmentée…), données cellulaires ; leaders : iOS et Android.
- **Environnement virtuel** :

![[OS - chp 1 - image9.png]]
*Figure : le matériel porte le gestionnaire de machines virtuelles (VMM), qui porte trois VM, chacune avec son noyau et ses processus.*

Le VMM ([[Machine virtuelle]], *virtual machine manager*) crée plusieurs PC virtuels. Deux types :
- **Bare metal** : le VMM est installé directement sur le matériel, sans OS ;
- **Hosted** : le VMM est installé sur une machine qui a déjà un OS (exemple : VirtualBox).

- **Client-serveur** ([[Modèle client-serveur]]) :

![[OS - chp 1 - image11.png]]
*Figure : un serveur relié par un réseau à trois clients (ordinateur de bureau, portable, smartphone).*

Deux types :
- **serveur de calcul** (*compute server*) : fournit une interface pour demander un service. Exemple : une application web de base de données (MySQL, [[PostgreSQL]]) ; je demande des informations sur un client, le serveur traite la requête (recherche dans la table des clients) et renvoie le résultat ;
- **serveur de fichiers** (*file-server system*) : interface pour stocker et récupérer des fichiers (exemple : Google Drive).

- **[[Cloud computing]]** : fournit calcul, stockage et même applications comme un service à travers un réseau ; extension logique de la virtualisation, sur laquelle il repose. Exemples : Shadow, Amazon EC2.

## Systèmes distribués

![[OS - chp 1 - image1.png]]
*Figure : diapositive « Distributed Systems » : réseau de centre de données en arbre (core switches, aggregate switches, ToR switches au-dessus des racks de serveurs).*

- **[[Système distribué]]** : ensemble de systèmes séparés, éventuellement hétérogènes, reliés en réseau.
- Un **Network Operating System** fournit des fonctions entre les systèmes du réseau et donne l'**illusion d'un seul système**.

L'étudiante note qu'il lui reste à comprendre l'explication et le schéma de cette diapositive.

## Annotations de l'étudiante

Le dessin de la section « Computer system operation » ne donne que des mots (RAM, Device controller, Buffer, CPU) : la disposition et les flèches sont perdues. Sur la diapositive des systèmes distribués, l'étudiante écrit qu'elle doit encore comprendre l'explication et le schéma. La section « Working of an I/O operation » est marquée « A COMPRENDRE ».

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Texte du dessin « Located in the CPU »** : la note s'arrête là, sans phrase complète. Elle semble désigner les registres et le cache de la hiérarchie de stockage.
2. **« Le buffer se vide dès que la tâche est accomplie »** et « un programme ne peut pas être chargé sur le SSD directement » : formulations approximatives (complément). Un programme est stocké sur le SSD et copié en RAM pour s'exécuter.
3. **Définition du clavier** : « le CPU converti en binary » est simplifiée ; le code ASCII vient du contrôleur du clavier.
4. **À vérifier de la transcription** (trait noir dépassant à gauche du schéma des machines virtuelles) : sans conséquence, fausse alerte pour le contenu.
5. **Mémoire principale « RAM, cache et registres »** : la note range cache et registres dans la *main memory*, alors que la figure les distingue (trois niveaux du stockage primaire). Le cours dit aussi que la main memory est « la seule mémoire à laquelle le processeur peut accéder directement ». À vérifier.
6. **« Deux batteries » d'un serveur** : il s'agit vraisemblablement de deux alimentations redondantes (complément).
