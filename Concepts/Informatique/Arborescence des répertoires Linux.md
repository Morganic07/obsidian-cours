---
type: concept
tags: [year2]
aliases: [Linux directory structure, directory structure, arborescence Linux, hiérarchie des répertoires]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[5 - OS|OS - chp 5]]"]
maj: 2026-11-08
---

Système hiérarchique dont le sommet est la racine `/`. Répertoires principaux :

| Répertoire | Contenu |
|---|---|
| `/bin` | binaires exécutables |
| `/boot` | noyau, initrd |
| `/dev` | fichiers de périphériques |
| `/etc` | configuration (passwd, fstab) |
| `/home` | répertoires des utilisateurs |
| `/lib` | bibliothèques partagées |
| `/sbin` | binaires d'administration |
| `/tmp` | fichiers temporaires, effacés au redémarrage |
| `/var` | journaux, spool |
| `/usr` | applications et bibliothèques partagées par tous les utilisateurs (les fichiers propres à chacun sont dans `/home`) [[Erreurs du cours#^e-arborescence-des-repertoires-linux\|✎]] |

## Compléments (hors du cours)

**Norme.** L'organisation suit le **Filesystem Hierarchy Standard** (FHS), norme maintenue par la Linux Foundation (version 3.0, 2015). Contrairement à Windows (une lettre par volume : `C:`, `D:`), Linux n'a qu'un seul arbre : les autres volumes y sont montés sur des [[Point de montage|points de montage]].

**Répertoires absents du tableau du cours :**

| Répertoire | Contenu |
|---|---|
| `/opt` | logiciels tiers installés en bloc (un sous-dossier par logiciel) |
| `/root` | répertoire personnel de [[Super-utilisateur root\|root]] (hors de `/home`) |
| `/mnt` | montages manuels temporaires |
| `/media` | supports amovibles (clés USB, CD) |
| `/proc` | pseudo-système de fichiers fabriqué par le noyau : un dossier par [[Processus\|processus]] (`/proc/<PID>`), infos système (`/proc/cpuinfo`, `/proc/meminfo`) |
| `/sys` | pseudo-système de fichiers du noyau décrivant le matériel et les pilotes |
| `/run` | données d'exécution depuis le démarrage (PID, sockets), en mémoire |

`/proc` et `/sys` n'occupent aucune place sur le disque : leur contenu est produit à la lecture par le noyau.

**Sous-dossiers de `/usr`** : `/usr/bin` (commandes des utilisateurs), `/usr/lib` (bibliothèques), `/usr/share` (données indépendantes de l'architecture : documentation, pages de manuel), `/usr/local` (logiciels installés localement par l'administrateur, hors du gestionnaire de paquets).

**Fusion de `/usr` (usrmerge).** Sur Debian (nouvelles installations depuis Debian 10, obligatoire depuis Debian 12) et Ubuntu (depuis 19.04), `/bin`, `/sbin` et `/lib` sont des [[Lien symbolique|liens symboliques]] vers `/usr/bin`, `/usr/sbin` et `/usr/lib`. C'est ce qui explique les doublons de `cat /etc/shells` (`/bin/bash` et `/usr/bin/bash`, voir [[Fichier shells]]).

**« Tout est fichier ».** Principe d'Unix : périphériques et ressources du noyau sont accessibles comme des fichiers, par exemple `/dev/sda` (premier disque), `/dev/null` (fichier qui absorbe tout ce qu'on y écrit) ; voir [[Fichier de périphérique]].

Notion parente : [[Système de fichiers]]. Voir aussi : [[Répertoire racine]], [[Répertoire personnel]], [[Fichier de périphérique]], [[Bibliothèque partagée]], [[Fichier journal]], [[Image initrd]].

Résumés : [[4 - OS]], [[5 - OS]]
