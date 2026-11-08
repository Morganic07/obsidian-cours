---
type: concept
tags:
  - year2
aliases:
  - hashed password
  - mot de passe haché
  - mots de passe hachés
  - password hashing
  - sel cryptographique
  - salt
matieres:
  - Operating System
sources:
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : hacher un mot de passe, c'est le passer dans une fonction de hachage à sens unique, qui en donne une empreinte (hash) de laquelle on ne peut pas remonter au mot de passe. Ce n'est donc pas un chiffrement : un chiffrement est réversible avec la clé, un hachage ne l'est pas. Le système ne conserve que l'empreinte.

Ubuntu et les systèmes de type Unix ne laissent pas voir le mot de passe actuel : il est stocké sous forme hachée (« hashed (encrypted) »), si bien que même un administrateur ne peut pas le lire.

## Fonctionnement (complément, hors du cours)

- **Vérification à la connexion** : le système hache le mot de passe saisi, avec le même sel et le même algorithme, et compare le résultat à l'empreinte enregistrée ; s'ils sont égaux, le mot de passe est bon.
- **Format dans `/etc/shadow`** : le deuxième champ d'une ligne s'écrit `$id$sel$empreinte`, où `id` désigne l'algorithme : `1` = MD5 (obsolète), `5` = SHA-256, `6` = SHA-512, `y` = yescrypt (défaut des Ubuntu récentes, depuis la 22.04). Un champ `!` ou `*` signale un compte verrouillé ou sans mot de passe utilisable.
- **Sel (salt)** : chaîne aléatoire, propre à chaque compte, ajoutée au mot de passe avant le hachage. Deux comptes au même mot de passe ont ainsi des empreintes différentes, et les tables précalculées d'empreintes (tables arc-en-ciel) deviennent inutilisables.
- **Fonctions lentes** : SHA-512 crypt et yescrypt répètent le calcul de nombreuses fois pour ralentir les attaques par force brute.
- **Mot de passe perdu** : il ne se retrouve pas à partir de l'empreinte ; l'administrateur le remplace par un nouveau avec [[Commande passwd|`sudo passwd nom`]].

Notion parente : [[Fichiers de mots de passe]]. Voir aussi : [[Commande passwd]], [[Table de hachage]] (autre usage d'une fonction de hachage).

Résumés : [[1 - TP1]] ; (rapprochement, complément hors du cours) : [[4 - OS]]
