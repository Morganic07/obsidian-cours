---
type: concept
tags: [year4]
aliases: [code de Huffman, Huffman coding, codage entropique, code préfixe]
sources: ["[[Raw/Year 4/histoire du design et interactions /chp2 - de courrier à courriels.pdf|chp2 - de courrier à courriels.pdf]]"]
maj: 2026-11-10
---

**Définition (complément, hors du cours)** : méthode de [[Compression de données|compression sans perte]] publiée par David Huffman en 1952, alors étudiant au MIT, qui attribue à chaque symbole un mot de code binaire d'autant plus court que le symbole est fréquent. Les codes sont construits en fusionnant répétitivement les deux symboles les moins fréquents dans un [[Arbre (théorie des graphes)|arbre]] binaire ; aucun mot de code n'est le début d'un autre (code préfixe), ce qui permet de décoder sans séparateur. C'est le code optimal parmi ceux qui codent chaque symbole séparément, et sa longueur moyenne approche l'[[Entropie (théorie de l'information)|entropie]] de la source ; il est utilisé dans les formats ZIP, JPEG et MP3. [[Complément hors du cours|ⓘ]]

## Dans le cours

[[2 - De courrier à courriels]] : complément sur la compression selon Shannon (un code efficace donne les mots de code les plus courts aux symboles les plus fréquents).

Voir aussi : [[Théorie de l'information]], [[Code Morse]].

Résumés : [[2 - De courrier à courriels]]
