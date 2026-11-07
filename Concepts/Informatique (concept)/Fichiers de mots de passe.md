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
  - "[[chp 1 - séance TP1 (résumé)|cours TP1]]"
maj: 2026-11-06
---

Selon le chp 4, `/etc` contient le fichier `passwd`, « qui contient les mots de passe des utilisateurs ». Selon le cours TP1, les mots de passe sont stockés hachés ([[Hachage de mot de passe]]) dans `/etc/shadow`, lisible seulement par root ; on ne peut donc pas relire son mot de passe.

Notion parente : [[Arborescence des répertoires Linux]]. Voir aussi : [[Commande passwd]], [[Super-utilisateur root]].

## À vérifier

- Désaccord entre sources : OS - chp 4 ([[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]) place les mots de passe dans `/etc/passwd`, le [[chp 1 - séance TP1 (résumé)|cours TP1]] dans `/etc/shadow`.

Résumés : [[4 - OS (résumé)]], [[chp 1 - séance TP1 (résumé)]]
