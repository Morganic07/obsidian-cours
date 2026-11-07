---
type: concept
tags: [year4]
aliases: [ID3]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
---

Algorithme de construction d'[[Arbre de décision]] : une fonction récursive `construct-tree` choisit à chaque nœud le test de plus grand [[Gain d'information]], calculé à partir de l'[[Entropie (théorie de l'information)|entropie]].

Sur l'exemple PlayTennis : gain(OUTLOOK) $= 0{,}246$, gain(HUMI.) $= 0{,}151$, gain(WIND) $= 0{,}048$, gain(TEMP.) $= 0{,}029$ bits, donc Outlook est placé à la racine.

Notion parente : [[Arbre de décision]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Gain d'information]], [[Algorithme C4.5]].

Résumés : [[chp 1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
