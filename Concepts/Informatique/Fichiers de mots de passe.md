---
type: concept
tags:
  - year2
aliases:
  - /etc/shadow
  - /etc/passwd
  - fichier shadow
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"
  - "[[1 - TP1|cours TP1]]"
maj: 2026-11-08
---

Selon le chp 4, `/etc` contient le fichier `passwd`, qui décrit les comptes des utilisateurs ; à la place du mot de passe, il ne garde qu'un `x`. [[Erreurs du cours#^e-fichiers-de-mots-de-passe|✎]] Selon le cours TP1, les mots de passe sont stockés hachés ([[Hachage de mot de passe]]) dans `/etc/shadow`, lisible seulement par root ; on ne peut donc pas relire son mot de passe.

Notion parente : [[Arborescence des répertoires Linux]]. Voir aussi : [[Commande passwd]], [[Super-utilisateur root]].

Résumés : [[4 - OS]]
