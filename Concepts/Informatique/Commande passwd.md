---
type: concept
tags:
  - year2
aliases:
  - passwd
  - sudo passwd
matieres:
  - Operating System
sources:
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : `passwd` est la commande qui change le mot de passe d'un compte utilisateur ; elle en enregistre l'empreinte ([[Hachage de mot de passe|hachage]]) dans `/etc/shadow`.

`sudo passwd` change le mot de passe. À ne pas confondre avec le fichier `/etc/passwd` ([[Fichiers de mots de passe]]).

## Les trois usages (complément, hors du cours)

| Commande | Effet |
|---|---|
| `passwd` | change le mot de passe de l'utilisateur courant ; demande d'abord l'ancien |
| `sudo passwd nom` | change celui de l'utilisateur `nom`, sans demander l'ancien (droits de [[Super-utilisateur root\|root]]) |
| `sudo passwd` | sans nom, change celui de root ; sous Ubuntu, où le compte root est verrouillé par défaut, cela l'active |

- `sudo passwd -l nom` verrouille un compte, `sudo passwd -u nom` le déverrouille.
- Le manuel distingue la commande et le fichier : `man passwd` (ou `man 1 passwd`) décrit la commande, `man 5 passwd` le fichier `/etc/passwd` (section 5 = formats de fichiers), voir [[Commande man]].

Voir aussi : [[Fichiers de mots de passe]], [[Hachage de mot de passe]], [[Commande sudo]], [[Super-utilisateur root]].

Résumés : [[1 - TP1]] ; (rapprochement, complément hors du cours) : [[4 - OS]]
