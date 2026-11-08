---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du PDF OS - chp 4 ([[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]) (4 pages, en anglais), dans [[Cours/Informatique/OS/_index|Operating System]]. C'est le chapitre 4, absent jusqu'ici du coffre : la matière passe du chapitre 3 au chapitre 5.

## Idée générale

Organisation hiérarchique des fichiers de Linux, rôle du répertoire racine, et partitions usuelles. Voir [[Système de fichiers]], [[Arborescence des répertoires Linux]] et [[Distribution Linux]].

## Structure des répertoires Linux (*Linux Directory Structure*)

![[OS - chp 4 - p1.jpg]]
*Figure : la racine `/` et ses sous-répertoires /bin, /etc, /home, /opt, /tmp, /usr, /var.*

La structure des répertoires de Linux est **hiérarchique** : chaque répertoire est un sous-répertoire d'un autre. Le répertoire de plus haut niveau est la **racine** (*root directory*), notée `/` ; tous les autres sont situés en dessous.

Contrairement à Windows, qui a une arborescence par lecteur (`C:\`, `D:\`), Linux n'a **qu'un seul arbre** : un autre disque, une clé USB ou une partition ne forme pas un nouvel arbre, il est « accroché » à un répertoire de cet arbre, son [[Point de montage|point de montage]]. [[Complément hors du cours|ⓘ]]

Le caractère `/` sert aussi de séparateur dans un [[Chemin de fichier|chemin]]. Un chemin **absolu** part de la racine et désigne le même fichier quel que soit l'endroit où l'on se trouve (`/home/user/notes.txt`) ; un chemin **relatif** part du répertoire courant (`notes.txt`, `../photos`). [[Complément hors du cours|ⓘ]]

Cette organisation n'est pas propre à une distribution : elle suit le *Filesystem Hierarchy Standard* (FHS), norme maintenue par la Linux Foundation (version 3.0 en 2015), que respectent dans les grandes lignes Debian, Ubuntu, Fedora, etc. C'est pourquoi on retrouve les mêmes répertoires d'une [[Distribution Linux|distribution]] à l'autre. [[Complément hors du cours|ⓘ]]

Principaux répertoires :

| Répertoire | Contenu |
|---|---|
| `/bin` | fichiers binaires : programmes exécutables directement par le [[Noyau]] Linux |
| `/boot` | fichiers nécessaires au démarrage : le noyau lui-même et l'`initrd` (*initial RAM disk*, [[Image initrd]]) |
| `/dev` | [[Fichier de périphérique\|fichiers de périphériques]] : fichiers spéciaux qui représentent le matériel (disques durs, interfaces réseau, imprimantes) |
| `/etc` | fichiers de configuration du système, par exemple `passwd` (qui contient les comptes des utilisateurs, les mots de passe hachés étant dans `/etc/shadow`, voir [[Fichiers de mots de passe]]) et `fstab` (qui indique quelles partitions monter) [[Erreurs du cours#^e-4-os\|✎]] |
| `/home` | répertoires personnels des utilisateurs ; chacun a le sien, avec ses fichiers et réglages ([[Répertoire personnel]]) |
| `/lib` | [[Bibliothèque partagée\|bibliothèques partagées]] : fichiers utilisés par plusieurs programmes ; elles économisent la mémoire, car partagées au lieu d'être chargées plusieurs fois |
| `/sbin` | binaires système, semblables aux binaires mais servant surtout à l'administration |
| `/tmp` | fichiers temporaires, en général supprimés au redémarrage |
| `/var` | fichiers de données variables : journaux (*log files*, [[Fichier journal]]) et fichiers de file d'attente (*spool files*) |
| `/usr` | fichiers partagés par tous les utilisateurs, comme les applications et les bibliothèques [[Erreurs du cours#^e-4-os\|✎]] |

`/usr` contient les programmes et bibliothèques **partagés par tous les utilisateurs** et installés par le gestionnaire de paquets ([[APT]]) : `/usr/bin` pour les commandes, `/usr/lib` pour les bibliothèques, `/usr/share` pour les données indépendantes de l'architecture (documentation, pages de manuel, icônes), `/usr/local` pour ce que l'administrateur compile lui-même. Les fichiers propres à chaque utilisateur sont dans `/home`. [[Complément hors du cours|ⓘ]]

Répertoires que la figure ou le tableau ne détaillent pas : [[Complément hors du cours|ⓘ]]
- `/opt` : logiciels tiers installés « en bloc », hors du gestionnaire de paquets (chacun dans son sous-dossier, par exemple `/opt/google/chrome`) ; il figure sur la figure du cours sans être décrit. [[Complément hors du cours|ⓘ]]
- `/root` : répertoire personnel du [[Super-utilisateur root|super-utilisateur root]], placé hors de `/home` pour rester accessible même si `/home` n'est pas monté. À ne pas confondre avec la racine `/`. [[Complément hors du cours|ⓘ]]
- `/mnt` et `/media` : points de montage, `/mnt` pour un montage temporaire fait à la main, `/media` pour les supports amovibles (clés USB, CD) montés automatiquement. [[Complément hors du cours|ⓘ]]
- `/proc` et `/sys` : **pseudo-systèmes de fichiers**, sans aucun fichier sur le disque ; le [[Noyau|noyau]] les fabrique à la volée pour exposer son état. `/proc/<pid>/` décrit chaque [[Processus|processus]], `/proc/cpuinfo` et `/proc/meminfo` le processeur et la mémoire ; `/sys` décrit les périphériques et pilotes. [[Complément hors du cours|ⓘ]]
- `/run` : données d'exécution (fichiers de PID, sockets) créées depuis le démarrage, en mémoire, effacées à l'arrêt. [[Complément hors du cours|ⓘ]]

Sur les installations récentes de Debian (par défaut pour les nouvelles installations depuis Debian 10, en 2019, et obligatoire depuis Debian 12, en 2023) et d'Ubuntu (depuis la 19.04), `/bin`, `/sbin` et `/lib` ne sont plus des répertoires distincts mais des [[Lien symbolique|liens symboliques]] vers `/usr/bin`, `/usr/sbin` et `/usr/lib` (fusion dite *usrmerge*). C'est pour cela que `cat /etc/shells` affiche chaque shell en double, sous `/bin` et sous `/usr/bin` (voir [[5 - OS]]). [[Complément hors du cours|ⓘ]]

La présence de `/dev` illustre un principe d'Unix : « **tout est fichier** ». Disques (`/dev/sda`, `/dev/nvme0n1`), terminaux, et même des pseudo-périphériques comme `/dev/null` (qui avale tout ce qu'on y écrit) ou `/dev/random` se lisent et s'écrivent avec les mêmes appels que des fichiers ordinaires. [[Complément hors du cours|ⓘ]]

## Le répertoire racine (*Root Directory*)

Voir [[Répertoire racine]]. Dans un système de fichiers, c'est le répertoire le plus haut de la hiérarchie, noté `/`, point de départ de tous les autres répertoires et fichiers. Il contient les composants essentiels au fonctionnement du système :

1. **Binaires système** : exécutables qui assurent les fonctions essentielles (démarrer le système, gérer les processus, traiter les saisies). Exemples : le noyau, l'initrd, les shells.
2. **Bibliothèques essentielles** : bibliothèques partagées qui fournissent des fonctions communes à diverses applications ; leur code sert à plusieurs programmes, ce qui évite de le dupliquer et économise la mémoire.
3. **Fichiers de configuration** : réglages et paramètres qui contrôlent le comportement du système ; ils servent à personnaliser son fonctionnement, définir la configuration réseau et gérer les comptes utilisateurs.
4. **Fichiers de périphériques** : fichiers spéciaux qui représentent le matériel et offrent aux programmes une interface standard pour interagir avec lui.
5. **Points de montage** ([[Point de montage]]) : répertoires spéciaux où sont montées les partitions ; ils donnent accès aux différents volumes depuis la racine.
6. **Sous-répertoires** : ils organisent fichiers et répertoires liés en une structure hiérarchique, et peuvent contenir d'autres binaires, bibliothèques, fichiers de configuration et données utilisateur.

La racine est un élément crucial : fondation de l'organisation et de la gestion des fichiers et des composants système, elle rend accessibles binaires, bibliothèques et fichiers de configuration essentiels, et facilite l'organisation des données et des applications.

## Les partitions Linux

Voir [[Partitions Linux]] et [[Partition (disque)]].

Une partition est une portion du disque déclarée dans la **table de partitions**, au début du disque. Il en existe deux formats : l'ancien [[MBR]] (4 partitions principales au plus, disques jusqu'à 2 Tio) et [[Table de partitions GPT|GPT]] (*GUID Partition Table*, associée à l'[[BIOS et UEFI|UEFI]] : jusqu'à 128 partitions par défaut, disques bien plus grands). Une fois créée, une partition est **formatée** avec un [[Système de fichiers|système de fichiers]] ([[EXT4|ext4]] par défaut sous Debian et Ubuntu), puis montée sur un répertoire de l'arbre. [[Complément hors du cours|ⓘ]]

| Partition | Rôle | Détails du cours |
|---|---|---|
| **Racine** (`/`) | fondation de la hiérarchie : noyau, programmes de base de l'OS, fichiers de configuration critiques, bibliothèques fondamentales | en général la première créée à l'installation ; montée en lecture-écriture pour que le système puisse modifier et mettre à jour ses composants |
| **`/home`** | données et fichiers personnels des utilisateurs | séparée de la racine pour isoler les fichiers utilisateurs des fichiers système : les mises à jour ne touchent pas aux données ; renforce la sécurité (accès non autorisé aux fichiers système restreint) et la stabilité |
| **`/usr`** (*User Partition*) | installation des applications tierces, bibliothèques et logiciels partagés par tous les utilisateurs [[Erreurs du cours#^e-4-os\|✎]] | séparée de la racine pour distinguer fichiers système et programmes installés ; les changements de la racine n'affectent pas ces applications |
| **`/var`** | données qui changent souvent : journaux, fichiers de file d'attente, cache | séparée pour que ces fichiers dynamiques n'occupent pas l'espace des partitions critiques ; facilite la gestion des journaux |
| **`/boot`** | fichiers de démarrage : noyau, initrd, configuration du [[Chargeur de démarrage]] | petite, environ 100 à 500 Mo ; parfois montée en lecture seule pour protéger son intégrité [[Erreurs du cours#^e-4-os\|✎]] |
| **Swap** | mémoire virtuelle utilisée quand la [[Mémoire vive\|RAM]] physique est pleine ([[Espace d'échange (swap)]]) | extension de la RAM pour les tâches gourmandes ; plus lente que la RAM, donc pas pour les données souvent utilisées |
| **Partition amorçable** (*bootable*) | toute partition qui contient les fichiers nécessaires pour démarrer Linux | en général la racine ou une partition séparée avec la configuration du chargeur ; au démarrage, le système la cherche et y charge le noyau et l'initrd ([[Partition de démarrage]]) |

Seules la racine et, sur une machine UEFI, la [[Partition système EFI|partition système EFI]] (petite partition FAT32 montée sur `/boot/efi`, qui contient le chargeur de démarrage) sont indispensables. Une installation de bureau classique d'Ubuntu se contente souvent de ces deux partitions : `/home`, `/var`, `/usr` et `/boot` séparés relèvent surtout des serveurs ou des installations personnalisées. [[Complément hors du cours|ⓘ]]

Pour `/boot`, le montage en lecture seule reste un choix de durcissement : Debian et Ubuntu le montent par défaut en lecture-écriture (options `defaults`), car chaque mise à jour du noyau y écrit un nouveau noyau et un nouvel initrd. [[Complément hors du cours|ⓘ]]

Le swap n'est pas forcément une partition : Ubuntu utilise par défaut un **fichier d'échange** (`/swap.img` ou `/swapfile`) depuis la version 17.04, plus facile à agrandir. Le swap sert aussi à l'**hibernation**, qui y recopie le contenu de la RAM avant d'éteindre. [[Complément hors du cours|ⓘ]]

Le montage des partitions au démarrage est décrit dans `/etc/fstab`, une ligne par partition : [[Complément hors du cours|ⓘ]]

```
# <périphérique>                           <point de montage> <type> <options>  <dump> <pass>
UUID=3f2a...                                /                  ext4   defaults   0      1
UUID=9c1b...                                /home              ext4   defaults   0      2
UUID=A1B2-C3D4                              /boot/efi          vfat   umask=0077 0      1
/swapfile                                   none               swap   sw         0      0
```

Les partitions y sont désignées par leur **UUID**, identifiant unique du système de fichiers, plutôt que par `/dev/sda1`, dont le nom peut changer si l'on ajoute un disque. Le dernier champ donne l'ordre de vérification par `fsck` au démarrage (1 pour la racine, 2 pour les autres, 0 pour aucune). [[Complément hors du cours|ⓘ]]

Commandes pour observer les partitions : `lsblk` (arbre des disques et partitions avec leurs points de montage), `df -h` (espace utilisé et libre par système de fichiers monté, voir [[Commande df]]), `sudo fdisk -l` (tables de partitions), `mount` / `umount` (monter et démonter à la main), `swapon --show` (swap actif). [[Complément hors du cours|ⓘ]]

**Bilan** : les partitions jouent un rôle crucial dans l'organisation du système de fichiers. Elles isolent les fichiers système des données utilisateurs, renforcent la sécurité, facilitent les mises à jour et optimisent les performances ; chacune a un rôle précis. Voir aussi [[BIOS et UEFI]].