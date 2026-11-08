---
type: concept
tags: [year2]
aliases: [package manager, gestionnaires de paquets, paquet logiciel, dépôt de paquets, software repository]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 3.docx|OS - chp 3]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un gestionnaire de paquets est le logiciel qui installe, met à jour et supprime les **paquets** d'une [[Distribution Linux|distribution Linux]]. Un paquet est une archive qui contient les fichiers d'un programme et ses métadonnées : nom, version, description, et liste des **dépendances** (les autres paquets nécessaires à son fonctionnement). Le gestionnaire télécharge les paquets depuis des **dépôts** (serveurs de la distribution), résout automatiquement les dépendances, garde la liste de ce qui est installé et permet de tout mettre à jour d'une seule commande.

Chaque famille de distributions a le sien :

| Famille | Outil de haut niveau | Outil de bas niveau, format |
|---|---|---|
| Debian, Ubuntu | `apt` ([[APT]]) | `dpkg`, paquets `.deb` |
| Fedora, Red Hat, CentOS | `dnf` (anciennement `yum`) | `rpm`, paquets `.rpm` |
| Arch Linux | `pacman` | paquets `.pkg.tar.zst` |
| openSUSE | `zypper` | `rpm`, paquets `.rpm` |

L'outil de bas niveau installe un fichier de paquet déjà présent, sans chercher ses dépendances ; l'outil de haut niveau interroge les dépôts et s'en charge.

- **Sécurité** : les dépôts et les paquets sont signés par la distribution ; le gestionnaire vérifie la signature avant d'installer, ce qui garantit l'origine et l'intégrité des paquets. C'est la raison de préférer les dépôts officiels à un logiciel téléchargé sur un site quelconque.
- **Formats indépendants de la distribution** : Snap (poussé par Canonical, installé par défaut sous [[Ubuntu]]) et Flatpak embarquent leurs propres dépendances et s'exécutent isolés du système, au prix de paquets plus lourds.
- **Ailleurs** : le même principe existe pour les langages (`pip` pour Python, `npm` pour JavaScript, voir [[Module, paquet, bibliothèque et framework]]) et pour d'autres systèmes (Homebrew sous macOS, winget sous Windows).

## Dans le cours

Le chapitre 3 ([[3 - OS]]) définit la distribution comme « un ensemble de paquets logiciels » sans nommer l'outil qui les gère ; la notion apparaît dans les compléments de la fiche.

Voir aussi : [[APT]], [[Distribution Linux]], [[Linux]], [[Ubuntu]], [[Version LTS et version intermédiaire]].

Résumés : [[3 - OS]]
