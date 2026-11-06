---
type: concept
tags: [year2]
aliases: [Advanced Package Tool, apt update, apt upgrade, apt full-upgrade, apt install, apt-get]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[cours TP1]]", "[[TP1]]"]
maj: 2026-11-06
---

Outil pour installer, supprimer et mettre à jour les paquets d'une distribution Linux.

- `apt update` télécharge seulement la liste des nouvelles versions ;
- `apt upgrade` installe les nouvelles versions des paquets installés, sans installer ni supprimer de paquet ;
- `apt full-upgrade` peut en supprimer et en installer.

`sudo` est nécessaire, à cause des verrous placés sous `/var`.

Notion parente : [[Distribution Linux]]. Voir aussi : [[Commande sudo]].

Résumés : [[OS - chp 5 (résumé)]], [[cours TP1 (résumé)]], [[TP1 (résumé)]], [[Commandes Shell + explications (résumé)]]
