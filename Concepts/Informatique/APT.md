---
type: concept
tags:
  - year2
aliases:
  - Advanced Package Tool
  - apt update
  - apt upgrade
  - apt full-upgrade
  - apt install
  - apt-get
  - apt remove
  - apt purge
  - apt search
  - dpkg
matieres:
  - Operating System
sources:
  - "[[5 - OS|OS - chp 5]]"
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]]"
maj: 2026-11-08
---

Outil pour installer, supprimer et mettre à jour les paquets d'une distribution Linux.

- `apt update` télécharge seulement la liste des nouvelles versions ;
- `apt upgrade` installe les nouvelles versions des paquets installés sans jamais en supprimer ; il installe seulement les nouveaux paquets exigés par les dépendances (c'est `apt-get upgrade` qui n'en installe aucun) [[Erreurs du cours#^e-apt|✎]] ;
- `apt full-upgrade` peut en supprimer et en installer.

`sudo` est nécessaire, à cause des verrous placés sous `/var`.

## Compléments (hors du cours)

**Paquets et dépôts.** Un paquet `.deb` (format de Debian et d'Ubuntu) contient les fichiers du logiciel, sa configuration par défaut et la liste de ses dépendances. APT télécharge les paquets depuis des dépôts listés dans `/etc/apt/sources.list` et `/etc/apt/sources.list.d/`, et résout les dépendances (il installe aussi les paquets requis) ; c'est `dpkg`, l'outil de bas niveau, qui installe chaque `.deb` (`dpkg -i paquet.deb` installe un fichier local sans résoudre ses dépendances).

| Commande | Effet |
|---|---|
| `apt install <paquet>` | installe le paquet et ses dépendances |
| `apt remove <paquet>` | désinstalle, en gardant les fichiers de configuration |
| `apt purge <paquet>` | désinstalle et supprime la configuration |
| `apt autoremove` | supprime les dépendances devenues inutiles |
| `apt search <mot>` | cherche un paquet |
| `apt show <paquet>` | décrit un paquet (version, dépendances, taille) |

`apt` est pensé pour un usage interactif (barre de progression, couleurs) ; dans les scripts, on conseille `apt-get` et `apt-cache`, dont la sortie est stable d'une version à l'autre.

Notion parente : [[Distribution Linux]]. Voir aussi : [[Commande sudo]].

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
