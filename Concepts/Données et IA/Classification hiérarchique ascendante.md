---
type: concept
tags: [year4]
aliases: [classification hiérarchique, hierarchical clustering, dendrogramme, dendrogram, saut minimal, saut maximal, minimal jump]
matieres: [data mining]
sources: [".raw/Year 4/data mining/cours data mining du prof.pdf", "[[Chp1 - intro to data mining]]"]
maj: 2026-11-06
---

Approche ascendante du [[Clustering]] : on part de $N$ groupes (un par exemple) et on fusionne jusqu'à n'en avoir qu'un, ce qui donne un arbre, le **dendrogramme**. Une coupe horizontale du dendrogramme donne $K$ groupes.

Choix des groupes à fusionner :

- **saut minimal** : la plus petite distance entre les deux groupes est minimale ;
- **saut maximal** : la plus grande distance est minimale ;
- **saut moyen** : la distance entre [[Centroïde|centroïdes]] est minimale ;
- **[[Méthode de Ward]]**.

Exercice du cours : saut minimal sur les points 1, 2, 9, 12, 20.

Notion parente : [[Clustering]]. Voir aussi : [[Méthode de Ward]], [[Centroïde]], [[K-moyennes]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
