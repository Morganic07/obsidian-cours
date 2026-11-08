---
type: concept
tags: [year4]
aliases: [classification hiérarchique, hierarchical clustering, dendrogramme, dendrogram, saut minimal, saut maximal, minimal jump, CAH, single linkage, complete linkage, average linkage, effet de chaîne]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

Approche ascendante du [[Clustering]] : on part de $N$ groupes (un par exemple) et on fusionne jusqu'à n'en avoir qu'un, ce qui donne un arbre, le **dendrogramme**. Une coupe horizontale du dendrogramme donne $K$ groupes.

Choix des groupes à fusionner :

- **saut minimal** : la plus petite distance entre les deux groupes est minimale ;
- **saut maximal** : la plus grande distance est minimale ;
- **saut moyen** : la distance entre [[Centroïde|centroïdes]] est minimale ;
- **[[Méthode de Ward]]**.

Exercice du cours : saut minimal sur les points 1, 2, 9, 12, 20.

**Corrigé de l'exercice (complément, hors du cours)** : fusions {1, 2} à la hauteur 1, {9, 12} à 3, {1, 2, 9, 12} à 7 (distance 2–9), puis tout à 8 (distance 12–20). Couper le dendrogramme entre 3 et 7 donne {1, 2}, {9, 12}, {20}.

## Compléments (hors du cours)

**Noms usuels** : saut minimal = *single linkage*, saut maximal = *complete linkage*, Ward = *ward*. Les manuels et logiciels distinguent le **lien moyen** (*average linkage*, moyenne des distances entre toutes les paires de points des deux groupes) de la **méthode des centroïdes** (distance entre centroïdes, ce que le cours appelle saut moyen).

**Forme des groupes** : le saut minimal produit un **effet de chaîne** (deux groupes reliés par une suite de points proches fusionnent, même s'ils sont loin dans l'ensemble) ; le saut maximal et Ward donnent des groupes compacts.

**Ward et l'inertie** : le critère de Ward est exactement la hausse de $I_W$ causée par la fusion ([[Inertie (clustering)]]), d'où sa parenté avec les [[K-moyennes]].

**Où couper** : on coupe le dendrogramme juste avant un grand saut de hauteur, signe qu'on fusionnerait des groupes éloignés.

**Coût** : la matrice des distances entre paires prend une mémoire de l'ordre de $N^2$. Sur de grandes bases, on fait d'abord des k-moyennes avec beaucoup de groupes, puis une CAH sur leurs centroïdes.

Notion parente : [[Clustering]]. Voir aussi : [[Méthode de Ward]], [[Centroïde]], [[K-moyennes]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
