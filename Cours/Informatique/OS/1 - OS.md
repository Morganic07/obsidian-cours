---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]] (« Chp 1 - Introduction »), dans [[Cours/Informatique/OS/_index|Operating System]]. Notes de cours de l'étudiante, en français et en anglais, avec les figures des diapositives.
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

Ces quatre temps forment le **cycle d'instruction** (*fetch–decode–execute*). Le CPU sait quelle instruction chercher grâce au [[Compteur de programme]] (*program counter*), un [[Registre du processeur|registre]] qui contient l'adresse de la prochaine instruction et avance après chaque lecture ; les opérandes et résultats intermédiaires sont gardés dans d'autres registres, les mémoires les plus rapides de la machine. Le rythme du cycle est donné par l'**horloge** du processeur, exprimée en GHz (milliards de cycles par seconde). [[Complément hors du cours|ⓘ]]

Il **met aussi en relation** les composants de l'ordinateur ([[Disque dur]], mémoire vive, carte graphique…).

- **Cœur** (*core*) : unité qui lit et exécute des instructions ; un cœur = une tâche à la fois ; multicœur = plusieurs tâches ([[Cœur de processeur]]).
- **Multithreading / [[Hyperthreading]]** : transforme les cœurs physiques en plusieurs cœurs virtuels, pour qu'un seul cœur physique exécute plusieurs tâches en parallèle. Seules certaines applications en ont besoin : jeux vidéo, montage vidéo, pas YouTube ni Google.

![[OS - chp 1 - image5.png]]
*Figure : processeur à 4 cœurs, chacun divisé en deux [[Thread|threads]] (8 threads au total).*

L'hyperthreading (nom commercial d'Intel pour le *simultaneous multithreading*, SMT) ne double pas la puissance : les deux threads matériels d'un cœur partagent ses unités de calcul et ses caches, et le second profite surtout des moments où le premier attend une donnée de la mémoire. Le gain est donc partiel et dépend du programme. L'OS voit chaque thread matériel comme un processeur logique, auquel il peut confier un [[Thread|thread]] ou un [[Processus|processus]] (voir [[Commande lscpu]] : *Thread(s) per core*). Les navigateurs aussi répartissent leur travail sur plusieurs processus et threads ([[Architecture multiprocessus de Chrome]]). [[Complément hors du cours|ⓘ]]

## Qu'est-ce qu'un système d'exploitation ?

L'OS sert d'intermédiaire entre l'utilisateur et le matériel. Objectifs :
- exécuter les programmes de l'utilisateur ;
- rendre l'ordinateur plus facile à utiliser ;
- gérer le matériel.

Autrefois les OS étaient en [[Interface en ligne de commande|CLI]] (*command line interface*) ; aujourd'hui on a des [[Interface graphique|GUI]] (*graphical user interface*).

On décrit classiquement l'OS sous deux angles : comme **allocateur de ressources** (il répartit temps processeur, mémoire, espace disque et périphériques entre des demandes concurrentes, de façon efficace et équitable) et comme **programme de contrôle** (il surveille l'exécution des programmes pour éviter erreurs et usages abusifs). Le seul programme qui tourne en permanence est le [[Noyau|noyau]] ; le reste est fait de programmes système et d'applications. [[Complément hors du cours|ⓘ]]

Pour ce contrôle, le processeur a au moins deux modes d'exécution, indiqués par un bit de mode : le **mode noyau** (*kernel mode*), où toutes les instructions sont permises (accès direct au matériel, gestion des interruptions et de la mémoire), et le **mode utilisateur** (*user mode*), où les instructions privilégiées sont interdites. Une application qui a besoin du matériel passe par un [[Appel système]] : le CPU bascule en mode noyau, l'OS fait le travail, puis rend la main en mode utilisateur. Voir [[Mode noyau et mode utilisateur]]. [[Complément hors du cours|ⓘ]]

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

La **largeur du bus d'adresses** fixe la quantité de mémoire adressable : avec $n$ lignes d'adresse, le CPU peut désigner $2^n$ adresses. Avec 32 bits et une adresse par octet, $2^{32}$ octets = 4 Gio, d'où la limite de 4 Go de RAM des anciens systèmes 32 bits ; les processeurs 64 bits dépassent largement ce plafond. La largeur du bus de données, elle, fixe combien de bits passent en un transfert. [[Complément hors du cours|ⓘ]]

![[OS - chp 1 - image3.png]]
*Figure : CPU, contrôleur de disque (disques), contrôleur USB (souris, clavier, imprimante) et adaptateur graphique (moniteur) reliés à la mémoire par un bus système commun.*

- **CPU** : cerveau de l'ordinateur ; exécute les instructions, traite les données, communique avec les périphériques par le bus système.
- **Bus système** : canal de communication entre périphériques.
- **RAM** : espace où stocker et transférer les données entre périphériques ; le CPU traite ces données. Les périphériques peuvent accéder à la RAM en même temps, le bus système régule les accès pour éviter les conflits.
- Un programme ne peut pas être « chargé sur le [[SSD]] directement » : ses données doivent être transférées en RAM pour que le CPU les traite vite.

**Traitement des instructions** :
- **[[Mémoire cache|Cache du CPU]]** : mémoire très rapide dans le CPU, qui stocke données et instructions fréquentes ; le CPU vérifie ses caches avant d'aller en RAM.
- **SSD** : si les données ne sont pas en RAM, on va les chercher sur le SSD, puis on les copie en RAM et éventuellement dans le cache.

$$\text{vitesse SSD} \ll \text{vitesse RAM} \ll \text{vitesse caches}$$

Le cache est organisé en niveaux : **L1** (le plus petit et le plus rapide, propre à chaque cœur, souvent séparé en cache d'instructions et cache de données), **L2**, puis **L3** (plus grand, partagé entre les cœurs). Trouver la donnée dans le cache s'appelle un *cache hit*, ne pas la trouver un *cache miss*. Le cache est efficace grâce au **principe de localité** : un programme réutilise vite ce qu'il vient d'utiliser (localité temporelle, par exemple une variable de boucle) et utilise ce qui est voisin en mémoire (localité spatiale, par exemple les cases suivantes d'un tableau) ; c'est pourquoi le cache charge des blocs entiers (lignes de cache) et non des octets isolés. [[Complément hors du cours|ⓘ]]

**[[Cycle mémoire]]** (*memory cycle*) : processus complet d'interaction entre CPU et RAM pour accéder à des données : demande d'adresse, lecture ou écriture, transmission des données, délais associés. Le CPU émet une requête à la RAM via une adresse mémoire. Si les données sont dans le cache, le CPU les utilise sans aller en RAM ; si elles sont sur le SSD et pas en RAM, l'OS les charge d'abord en RAM.

## Fonctionnement d'un système informatique (*Computer system operation*)

- Le CPU et les périphériques peuvent fonctionner simultanément.
- Chaque périphérique est relié à son propre **contrôleur** ([[Contrôleur de périphérique]], ou *adapter* pour le graphique), qui gère les communications avec le CPU.
- Chaque périphérique a un **[[Tampon (buffer)|buffer]]** : petite mémoire intermédiaire qui stocke temporairement les données avant leur transfert vers le CPU ou le périphérique. « Le buffer se vide dès que la tâche est accomplie ».
- Chaque contrôleur fonctionne grâce à un **pilote** (*driver*, [[Pilote de périphérique]]), programme propre à chaque type de périphérique, intermédiaire entre l'OS et le matériel.
- Le CPU déplace les données entre la mémoire principale (RAM) et les buffers locaux des contrôleurs. Exemple : à une lecture sur disque, le contrôleur place les données dans son buffer avant que le CPU ne les transfère en RAM.

Un dessin illustre ce passage ; seuls ses mots subsistent dans la note : RAM, *Device controller*, *Buffer*, CPU (disposition et flèches perdues).

- Les données des périphériques passent d'abord par le buffer local du contrôleur ; les buffers servent surtout aux E/S, pour que le CPU ne soit pas ralenti par les périphériques lents. Les opérations internes CPU/RAM n'y passent pas.
- La RAM reste l'endroit central où les données sont stockées avant traitement par le CPU.
- Quand un contrôleur a fini une opération (lecture de fichier, impression), il envoie une **interruption** au CPU, ce qui permet au CPU de faire autre chose pendant l'E/S.
- À retenir : *each device comes with a buffer, a driver and a controller*.

**Exemple du clavier** : comment le CPU comprend-il que j'ai appuyé sur « A » ? Chaque touche a un code de touche (*scan code*), et le caractère obtenu a un [[Code ASCII]] (*American Standard Code for Information Interchange*). Le CPU ne gère pas le clavier, il serait trop occupé : un CPU local dans le clavier fait touche pressée → code de touche → envoi en binaire au CPU principal, dont le pilote convertit le code en caractère. [[Erreurs du cours#^e-1-os|✎]]

Le code de touche (*scan code*, ou code d'usage en USB, défini par la spécification USB HID) désigne la position de la touche, pas un caractère. C'est le [[Pilote de périphérique|pilote]] de l'OS qui le traduit en caractère selon la [[Disposition du clavier|disposition]] choisie (AZERTY, QWERTY) : la même touche donne « A » en AZERTY et « Q » en QWERTY. Aujourd'hui le caractère obtenu est codé en [[Unicode]] (souvent en UTF-8), dont l'ASCII forme les 128 premiers codes. [[Complément hors du cours|ⓘ]]

## Termes importants

- **Programme d'amorçage** (*Bootstrap program*, *firmware*) : premier programme lancé à la mise sous tension ou au redémarrage, appelé **BIOS** (*Basic Input/Output System*, voir [[BIOS et UEFI]]). Il est stocké en [[Mémoire morte|ROM]] (*Read-Only Memory*), mémoire non modifiable qui conserve ses données hors tension. Étapes :
  - **POST** (*Power On Self-Test*) : vérifie l'alimentation, la RAM et le matériel ;
  - **localisation de l'OS** : le BIOS va à l'emplacement du disque qui contient l'OS et le copie du stockage vers la RAM. L'ordinateur est alors utilisable.
  - En pratique, le *firmware* ne charge pas tout l'OS d'un coup : il lance un [[Chargeur de démarrage]] (GRUB sous Linux, Windows Boot Manager), qui charge le [[Noyau|noyau]] en RAM ; le noyau initialise le matériel puis lance le premier processus ([[Processus init|init]], `systemd` sur les distributions récentes), qui démarre les services. Sur les cartes actuelles, le *firmware* est stocké en mémoire flash, réinscriptible pour les mises à jour, plutôt qu'en ROM au sens strict. [[Complément hors du cours|ⓘ]]
- **[[Interruption]]** (*interrupt*) : signal envoyé par le matériel au CPU, qui le force à suspendre ce qu'il fait pour traiter l'interruption. Le matériel peut l'envoyer à tout moment via le bus système. Exemple : le CPU est occupé et je lance une impression ; l'imprimante interrompt le CPU, qui sauvegarde son opération en mémoire et traite la requête ; une nouvelle interruption signale la fin de l'impression, et le CPU reprend.
- **[[Appel système]]** (*system call*) : méthode par laquelle un logiciel déclenche une interruption du CPU pour lui demander une action précise.
- Les interruptions provoquées par le logiciel s'appellent **déroutements** (*traps*) ou **exceptions** : elles sont déclenchées soit volontairement (un appel système, par exemple `read()` pour lire un fichier), soit par une erreur du programme (division par zéro, accès mémoire interdit, qui donne une [[Erreur de segmentation]]). On dit qu'un OS moderne est **piloté par les interruptions** (*interrupt-driven*) : sans interruption ni appel système, il n'a rien à faire. [[Complément hors du cours|ⓘ]]
- L'alternative à l'interruption est la **scrutation** (*polling*) : le CPU interroge le contrôleur en boucle pour savoir s'il a fini. C'est simple, mais le CPU perd son temps à attendre un périphérique lent ; l'interruption le libère jusqu'à ce que le périphérique se signale. [[Complément hors du cours|ⓘ]]

## Réponse du CPU à une interruption

1. **Interruption** : un événement externe (saisie de l'utilisateur, requête d'un périphérique, erreur) envoie un signal au CPU.
2. **Arrêt du traitement courant** : le CPU s'interrompt et sauvegarde son état (par exemple l'adresse de l'instruction suivante).
3. **Transfert d'exécution** : le CPU consulte le **vecteur d'interruption**, table qui associe à chaque type d'interruption l'adresse mémoire de l'ISR correspondante (la table d'adresses est la liste de ces adresses).
4. **Exécution de l'ISR** (*Interrupt Service Routine*) : code exécuté en réponse à une interruption ; chaque ISR gère une interruption particulière.
5. **Retour au traitement d'origine** : le CPU restaure son état et reprend.

Les interruptions ont des **priorités** : pendant une opération critique, le CPU peut **masquer** (ignorer temporairement) les interruptions de faible priorité, tandis que les interruptions non masquables (*NMI*) sont réservées aux événements graves, comme une erreur mémoire matérielle. Une interruption urgente peut ainsi en interrompre une moins urgente. [[Complément hors du cours|ⓘ]]

## Structure de stockage

![[OS - chp 1 - image16.png]]
*Figure : [[Hiérarchie de stockage]] en pyramide : registres, cache, mémoire principale (stockage volatil, primaire), mémoire non volatile, disques durs (secondaire), disque optique, bandes magnétiques (tertiaire). Capacité croissante et temps d'accès croissant vers le bas.*

Annotation de l'étudiante sur le dessin : « Located in the CPU ».

| Niveau | Contenu | Caractéristiques |
|---|---|---|
| **Mémoire principale** (*main memory*) | RAM, cache, registres | seule mémoire à laquelle le processeur accède directement ; accès aléatoire (n'importe quelle adresse) ; **volatile** (perd tout hors tension) ; sous forme de DRAM (*Dynamic Random Access Memory*) |
| **Stockage secondaire** | SSD (mémoire non volatile, flash, bien plus rapide que les HDD), HDD (disque magnétique) | extension de la mémoire principale, grande capacité non volatile ; un ordinateur peut avoir un SSD et/ou un HDD |
| **Stockage tertiaire** | [[Disque optique]] (CD, DVD, Blu-ray), [[Bande magnétique\|bandes magnétiques]] | archivage ; les bandes vont jusqu'à plusieurs To par cartouche, lecture séquentielle ; data centers, entreprises |

Voir [[Mémoire volatile et non volatile]].

Ordres de grandeur des temps d'accès, qui expliquent la pyramide : on passe d'environ un cycle d'horloge pour un registre à quelques nanosecondes pour le cache, une centaine de nanosecondes pour la RAM, des dizaines de microsecondes pour un SSD et plusieurs millisecondes pour un HDD. Entre la RAM et le HDD, le rapport est donc de l'ordre de $10^4$ à $10^5$. Les registres et les caches sont faits de **SRAM** (*Static RAM*, rapide mais chère et encombrante), la mémoire principale de **DRAM** (moins chère, mais à rafraîchir en permanence, d'où le « dynamique »). [[Complément hors du cours|ⓘ]]

Quand la RAM manque, l'OS peut déplacer sur le disque les pages de mémoire peu utilisées : c'est la **mémoire virtuelle**, qui donne à chaque processus l'illusion d'une mémoire plus grande que la RAM, au prix d'une forte baisse de vitesse quand le disque est sollicité (voir [[Espace d'échange (swap)]]). [[Complément hors du cours|ⓘ]]

## Fonctionnement d'une opération d'E/S (*Working of an I/O operation*)

Section marquée « A COMPRENDRE » par l'étudiante.

![[OS - chp 1 - image10.png]]
*Figure : le CPU (thread d'exécution, cache) échange instructions et données avec la mémoire ; il envoie une requête d'E/S à un périphérique, qui renvoie des données et une interruption ; le périphérique accède aussi directement à la mémoire par DMA.*

Une [[Opération d'entrée-sortie]] suit trois temps :
1. requête d'E/S (*I/O request*) ;
2. transfert de données (image, PDF…) ;
3. interruption.

**DMA** (*Direct Memory Access*, [[Accès direct à la mémoire]]) : permet d'accéder à la RAM sans interrompre le CPU.

Le schéma se lit ainsi. Sans DMA, pour un gros transfert (lire un fichier de plusieurs mégaoctets), le CPU devrait copier chaque mot du buffer du contrôleur vers la RAM, et recevoir une interruption à chaque petit morceau. Avec DMA : [[Complément hors du cours|ⓘ]]
1. le CPU programme le **contrôleur DMA** : adresse de départ en RAM, nombre d'octets, sens du transfert ;
2. le contrôleur du périphérique transfère tout le bloc directement entre son buffer et la RAM, par le bus, pendant que le CPU exécute autre chose ;
3. une **seule interruption** signale la fin du bloc, au lieu d'une par octet.

Le CPU et le contrôleur DMA se partagent le bus : quand le contrôleur l'utilise, le CPU peut être brièvement ralenti dans ses accès à la RAM (*cycle stealing*), mais il continue de travailler, en particulier sur les données déjà dans ses caches. [[Complément hors du cours|ⓘ]]

## Architecture des systèmes (*Computer system architecture*)

On classe les systèmes selon le nombre de CPU.

- **[[Système monoprocesseur]]** (*single processor systems*) : PC, téléphone. Un processeur pour les tâches générales, et d'autres processeurs locaux pour des tâches spécifiques (le CPU du clavier…).
- **[[Système multiprocesseur]]** (*multi-processor systems*, ou *parallel systems*) : serveurs. Les processeurs généraux communiquent et partagent le bus système, la mémoire et les périphériques.
  - **multiprocesseur symétrique** (SMP) : chaque processeur traite un travail à la fois ;
  - **multiprocesseur asymétrique** : le processeur maître donne des tâches précises à ses esclaves.
  - Un processeur **multicœur** est un système multiprocesseur sur une seule puce : plusieurs cœurs qui communiquent plus vite entre eux que des processeurs séparés et consomment moins. Les PC et téléphones actuels sont donc le plus souvent des systèmes multiprocesseurs symétriques, et c'est le modèle SMP qui domine aujourd'hui. Intérêts : plus de débit (*throughput*), économie d'échelle (bus, alimentation et périphériques partagés), meilleure tolérance aux pannes. Le gain reste inférieur au nombre de processeurs, à cause de la coordination et des parties d'un programme qui ne se parallélisent pas. [[Complément hors du cours|ⓘ]]

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

Le VMM s'appelle aussi **hyperviseur**. Le *bare metal* est dit de **type 1** (exemples : VMware ESXi, Microsoft Hyper-V, Xen ; c'est le cas des serveurs et du cloud), le *hosted* de **type 2** (VirtualBox, VMware Workstation ; usage sur un poste personnel, pour tester un autre système). Le type 1 est plus performant, faute d'OS intermédiaire ; le type 2 est plus simple à installer. Les processeurs actuels ont des instructions dédiées à la virtualisation (Intel VT-x, AMD-V), à activer dans le *firmware*. [[Complément hors du cours|ⓘ]]

Une alternative plus légère à la VM est le **conteneur** (Docker, par exemple) : il isole une application et ses dépendances, mais **partage le noyau** du système hôte au lieu d'embarquer son propre OS. Il démarre en quelques secondes et prend peu de place, mais ne peut faire tourner qu'un système compatible avec le noyau hôte (des conteneurs Linux sur un noyau Linux). Voir [[Conteneur (informatique)]]. [[Complément hors du cours|ⓘ]]

- **Client-serveur** ([[Modèle client-serveur]]) :

![[OS - chp 1 - image11.png]]
*Figure : un serveur relié par un réseau à trois clients (ordinateur de bureau, portable, smartphone).*

Deux types :
- **serveur de calcul** (*compute server*) : fournit une interface pour demander un service. Exemple : une application web de base de données (MySQL, [[PostgreSQL]]) ; je demande des informations sur un client, le serveur traite la requête (recherche dans la table des clients) et renvoie le résultat ;
- **serveur de fichiers** (*file-server system*) : interface pour stocker et récupérer des fichiers (exemple : Google Drive).

- **[[Cloud computing]]** : fournit calcul, stockage et même applications comme un service à travers un réseau ; extension logique de la virtualisation, sur laquelle il repose. Exemples : Shadow, Amazon EC2.

On distingue trois modèles de service, selon ce que le fournisseur gère à la place du client : [[Complément hors du cours|ⓘ]]

| Modèle | Ce qui est fourni | Exemple |
|---|---|---|
| **IaaS** (*Infrastructure as a Service*) | machines virtuelles, stockage, réseau ; le client installe et gère l'OS et les logiciels | Amazon EC2, Shadow (un PC Windows distant) |
| **PaaS** (*Platform as a Service*) | une plateforme prête pour déployer son code, sans gérer l'OS | Google App Engine, Heroku |
| **SaaS** (*Software as a Service*) | une application complète, utilisée depuis un navigateur | Google Drive, Gmail, Microsoft 365 |

On distingue aussi le **cloud public** (fournisseur partagé entre clients), le **cloud privé** (réservé à une organisation) et le **cloud hybride** (les deux combinés). [[Complément hors du cours|ⓘ]]

## Systèmes distribués

![[OS - chp 1 - image1.png]]
*Figure : diapositive « Distributed Systems » : réseau de centre de données en arbre (core switches, aggregate switches, ToR switches au-dessus des racks de serveurs).*

- **[[Système distribué]]** : ensemble de systèmes séparés, éventuellement hétérogènes, reliés en réseau.
- Un **Network Operating System** fournit des fonctions entre les systèmes du réseau et donne l'**illusion d'un seul système**.

L'étudiante note qu'il lui reste à comprendre l'explication et le schéma de cette diapositive.

Le schéma est celui d'un **centre de données en arbre**, sur trois niveaux de [[Commutateur|commutateurs]] (*switches*) : [[Complément hors du cours|ⓘ]]
1. **ToR** (*Top of Rack*) : un commutateur en haut de chaque baie (*rack*), qui relie entre eux les serveurs de cette baie ;
2. **aggregate** (agrégation) : chaque commutateur d'agrégation regroupe plusieurs ToR ;
3. **core** (cœur) : les commutateurs de cœur relient les commutateurs d'agrégation entre eux et à l'extérieur (Internet).

Deux serveurs d'une même baie communiquent par leur seul ToR ; deux serveurs éloignés remontent jusqu'au cœur puis redescendent. Chaque niveau est en général relié à deux commutateurs du niveau supérieur, pour qu'une panne de lien ou de commutateur n'isole pas une baie. C'est sur ce réseau que des milliers de serveurs collaborent comme un seul système distribué. [[Complément hors du cours|ⓘ]]

Intérêts d'un système distribué : partage des ressources, calcul plus rapide (le travail est réparti), fiabilité (une machine en panne ne bloque pas l'ensemble), communication entre utilisateurs. Variante sans serveur central : le **pair-à-pair** (*peer-to-peer*, P2P), où chaque machine est à la fois client et serveur, comme dans BitTorrent ; il s'oppose au [[Modèle client-serveur]]. [[Complément hors du cours|ⓘ]]

## Annotations de l'étudiante

Le dessin de la section « Computer system operation » ne donne que des mots (RAM, Device controller, Buffer, CPU) : la disposition et les flèches sont perdues. Sur la diapositive des systèmes distribués, l'étudiante écrit qu'elle doit encore comprendre l'explication et le schéma. La section « Working of an I/O operation » est marquée « A COMPRENDRE ».
