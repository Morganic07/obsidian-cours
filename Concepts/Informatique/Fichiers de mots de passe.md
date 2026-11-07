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
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
maj: 2026-11-07
---

Selon le chp 4, `/etc` contient le fichier `passwd`, « qui contient les mots de passe des utilisateurs ». Selon le cours TP1, les mots de passe sont stockés hachés ([[Hachage de mot de passe]]) dans `/etc/shadow`, lisible seulement par root ; on ne peut donc pas relire son mot de passe.

Notion parente : [[Arborescence des répertoires Linux]]. Voir aussi : [[Commande passwd]], [[Super-utilisateur root]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]] écrit que `/etc` contient « the passwd file (which contains the user passwords) » ; il faut « the passwd file (which contains the user accounts) » : les mots de passe hachés sont dans `/etc/shadow`, comme le dit le [[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]] ; `/etc/passwd` ne garde qu'un `x` à leur place.

Résumés : [[4 - OS]]
