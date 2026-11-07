---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF OS - chp 4 ([[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]) (4 pages, en anglais), dans [[Operating System (index)]]. C'est le chapitre 4, absent jusqu'ici du coffre : la matière passe du chapitre 3 au chapitre 5.

## Idée générale

Organisation hiérarchique des fichiers de Linux, rôle du répertoire racine, et partitions usuelles. Voir [[Système de fichiers]], [[Arborescence des répertoires Linux]] et [[Distribution Linux]].

## Structure des répertoires Linux (*Linux Directory Structure*)

![[OS - chp 4 - p1.jpg]]
*Figure : la racine `/` et ses sous-répertoires /bin, /etc, /home, /opt, /tmp, /usr, /var.*

La structure des répertoires de Linux est **hiérarchique** : chaque répertoire est un sous-répertoire d'un autre. Le répertoire de plus haut niveau est la **racine** (*root directory*), notée `/` ; tous les autres sont situés en dessous.

Principaux répertoires :

| Répertoire | Contenu |
|---|---|
| `/bin` | fichiers binaires : programmes exécutables directement par le [[Noyau]] Linux |
| `/boot` | fichiers nécessaires au démarrage : le noyau lui-même et l'`initrd` (*initial RAM disk*, [[Image initrd]]) |
| `/dev` | [[Fichier de périphérique\|fichiers de périphériques]] : fichiers spéciaux qui représentent le matériel (disques durs, interfaces réseau, imprimantes) |
| `/etc` | fichiers de configuration du système, par exemple `passwd` (« qui contient les mots de passe des utilisateurs », voir point à vérifier 1) et `fstab` (qui indique quelles partitions monter) |
| `/home` | répertoires personnels des utilisateurs ; chacun a le sien, avec ses fichiers et réglages ([[Répertoire personnel]]) |
| `/lib` | [[Bibliothèque partagée\|bibliothèques partagées]] : fichiers utilisés par plusieurs programmes ; elles économisent la mémoire, car partagées au lieu d'être chargées plusieurs fois |
| `/sbin` | binaires système, semblables aux binaires mais servant surtout à l'administration |
| `/tmp` | fichiers temporaires, en général supprimés au redémarrage |
| `/var` | fichiers de données variables : journaux (*log files*, [[Fichier journal]]) et fichiers de file d'attente (*spool files*) |
| `/usr` | « fichiers propres à l'utilisateur », comme les applications et les bibliothèques (voir point à vérifier 2) |

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

| Partition | Rôle | Détails du cours |
|---|---|---|
| **Racine** (`/`) | fondation de la hiérarchie : noyau, programmes de base de l'OS, fichiers de configuration critiques, bibliothèques fondamentales | en général la première créée à l'installation ; montée en lecture-écriture pour que le système puisse modifier et mettre à jour ses composants |
| **`/home`** | données et fichiers personnels des utilisateurs | séparée de la racine pour isoler les fichiers utilisateurs des fichiers système : les mises à jour ne touchent pas aux données ; renforce la sécurité (accès non autorisé aux fichiers système restreint) et la stabilité |
| **`/usr`** (*User Partition*) | installation des applications tierces, bibliothèques et logiciels propres à l'utilisateur | séparée de la racine pour distinguer fichiers système et programmes installés ; les changements de la racine n'affectent pas ces applications |
| **`/var`** | données qui changent souvent : journaux, fichiers de file d'attente, cache | séparée pour que ces fichiers dynamiques n'occupent pas l'espace des partitions critiques ; facilite la gestion des journaux |
| **`/boot`** | fichiers de démarrage : noyau, initrd, configuration du [[Chargeur de démarrage]] | petite, environ 100 à 500 Mo ; en général montée en lecture seule pour protéger son intégrité |
| **Swap** | mémoire virtuelle utilisée quand la [[Mémoire vive\|RAM]] physique est pleine ([[Espace d'échange (swap)]]) | extension de la RAM pour les tâches gourmandes ; plus lente que la RAM, donc pas pour les données souvent utilisées |
| **Partition amorçable** (*bootable*) | toute partition qui contient les fichiers nécessaires pour démarrer Linux | en général la racine ou une partition séparée avec la configuration du chargeur ; au démarrage, le système la cherche et y charge le noyau et l'initrd ([[Partition de démarrage]]) |

**Bilan** : les partitions jouent un rôle crucial dans l'organisation du système de fichiers. Elles isolent les fichiers système des données utilisateurs, renforcent la sécurité, facilitent les mises à jour et optimisent les performances ; chacune a un rôle précis. Voir aussi [[BIOS et UEFI]].

## Points à vérifier

1. **`/etc/passwd`** est décrit comme contenant « les mots de passe des utilisateurs ». Dans un système Linux actuel, les mots de passe hachés sont dans `/etc/shadow` (complément, voir [[Fichiers de mots de passe]]).
2. **`/usr`** est décrit comme « fichiers propres à l'utilisateur » et la partition `/usr` comme destinée aux logiciels tiers. `/usr` contient la majorité des programmes et bibliothèques du système lui-même (complément : usage courant).
3. **`/boot` « montée en lecture seule »** et swap qui permettrait de faire plus « sans ralentir » : affirmations du cours, à nuancer ; en pratique `/boot` est souvent montée en lecture-écriture pour les mises à jour du noyau, et le recours au swap ralentit le système (complément).
4. **Binaires système « le noyau, l'initrd et les shells »** : le noyau et l'initrd sont dans `/boot`, pas dans `/bin` ; la liste mélange les emplacements (complément).
