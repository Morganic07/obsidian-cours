---
type: concept
tags:
  - year2
aliases:
  - sudoers
  - visudo
  - NOPASSWD
  - timestamp_timeout
  - sudo sans mot de passe
  - sudo passwordless
  - groupe sudo
  - groupe wheel
matieres:
  - Operating System
sources:
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : `/etc/sudoers` est le fichier de configuration de [[Commande sudo|sudo]] : il dit quels utilisateurs ou groupes peuvent lancer quelles commandes, en se faisant passer pour quel compte, et avec ou sans mot de passe. Une règle s'écrit `qui hôtes=(comme_qui) commandes`, par exemple `nom ALL=(ALL) ALL`.

Le fichier sudoers s'ouvre avec `sudo visudo` (tâche 2 du TP6).

- Pour supprimer la demande de mot de passe : ajouter en fin de fichier `username ALL=(ALL) NOPASSWD:ALL`.
- Pour régler le délai avant une nouvelle demande : `Defaults timestamp_timeout=15` (pas de nouvelle demande de mot de passe pendant 15 minutes après la première commande `sudo` réussie). [[Erreurs du cours#^e-fichier-sudoers|✎]]

## Précisions (complément, hors du cours)

- **Pourquoi `visudo`** : il édite une copie du fichier et en vérifie la syntaxe avant de l'enregistrer. Une erreur dans `/etc/sudoers` modifié directement peut rendre `sudo` inutilisable, et donc empêcher de la corriger sans accès root. Les règles supplémentaires se placent de préférence dans un fichier de `/etc/sudoers.d/` (`sudo visudo -f /etc/sudoers.d/nom`).
- **Valeurs de `timestamp_timeout`** (en minutes, 15 par défaut) : `0` redemande le mot de passe à chaque commande ; une valeur négative ne le redemande plus jusqu'au redémarrage ou à la fin de la session. `sudo -k` invalide le délai en cours.
- **`NOPASSWD:ALL`** : toute personne ou tout programme qui obtient la session de l'utilisateur devient root sans obstacle ; à réserver à une machine de test.
- **Droits par groupe** : une ligne commençant par `%` désigne un groupe. Debian et Ubuntu contiennent `%sudo ALL=(ALL:ALL) ALL`, Fedora, Red Hat et Arch utilisent `%wheel`. Donner les droits sudo revient donc à ajouter l'utilisateur au groupe : `sudo usermod -aG sudo nom` (`-a` ajoute sans retirer des autres groupes), effectif à la connexion suivante.

Notion parente : [[Commande sudo]]. Voir aussi : [[Super-utilisateur root]].

Résumés : [[1 - TP1]] ; (rapprochement, complément hors du cours) : [[8 - OS commandes sh]]
