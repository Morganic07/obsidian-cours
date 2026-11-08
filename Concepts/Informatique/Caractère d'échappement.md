---
type: concept
tags:
  - year2
aliases:
  - escaping
  - escape character
  - échappement
  - antislash
  - backslash
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
  - "[[2 - TP2|Cours TP2]]"
maj: 2026-11-08
---

L'antislash `\` échappe le caractère suivant, qui est alors traité littéralement : `touch My\ File\ With\ Spaces.txt`, `rm file\ name.txt`, ou un fichier nommé `Price$100.txt`. Le sujet du TP2 range aussi les apostrophes inversées parmi les caractères d'échappement.

`rm file\ file2.txt` supprime le fichier nommé `file file2.txt` : l'espace échappé fait partie du nom. [[Erreurs du cours#^e-caractere-d-echappement|✎]]

Notion parente : [[Méta-caractère]]. Voir aussi : [[Guillemets en shell]], [[Substitution de commande]].

Résumés : [[2 - TP2]]
