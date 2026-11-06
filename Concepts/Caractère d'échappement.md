---
type: concept
aliases: [escaping, escape character, échappement, antislash, backslash]
matieres: [Operating System]
sources: ["[[raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands]]", "[[Cours TP2]]"]
maj: 2026-11-06
---

L'antislash `\` échappe le caractère suivant, qui est alors traité littéralement : `touch My\ File\ With\ Spaces.txt`, `rm file\ name.txt`, ou un fichier nommé `Price$100.txt`. Le sujet du TP2 range aussi les apostrophes inversées parmi les caractères d'échappement.

Notion parente : [[Méta-caractère]]. Voir aussi : [[Guillemets en shell]], [[Substitution de commande]].

## À vérifier

- Commentaire faux du sujet : `rm file\ file2.txt` supprime « file file2.txt », pas « file2.txt ».

Résumés : [[Copy of TP2-Commands (résumé)]], [[Cours TP2 (résumé)]], [[TP2 (résumé)]]
