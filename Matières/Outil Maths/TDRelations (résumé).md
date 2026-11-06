---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TD Relations (PDF)]]"]
maj: 2026-11-06
---

Résumé du corrigé [[raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TD Relations (PDF)]] (42 pages, algèbre, premier semestre 2025-2026), dans [[Outil Maths (matière)]]. 10 exercices, dont les 8 à 10 « à faire chez soi », tous corrigés. Cours : [[Chapitre 3 - Relation binaire (résumé)]], [[Chapitre3-Relation binaire (résumé)]], [[Relation d'équivalence]], [[Relation d'ordre]].

## Thèmes et exercices

| Exercice | Thème | Résultat et méthode |
|---|---|---|
| 1 | Réflexive, symétrique, transitive pour sept relations (égalité, $<$, $\leq$, même carré, même sinus, parallélisme, orthogonalité) | $<$ seulement transitive ; $\leq$ réflexive et transitive ; orthogonalité seulement symétrique ; les autres sont des équivalences |
| 2 | Six relations à étudier : classes pour une équivalence, caractère total et extrema pour un ordre | Voir ci-dessous |
| 3 | Produit de deux équivalences sur $E \times F$ | Les trois propriétés se vérifient composante par composante |
| 4 | Trois ordres : $y = x^n$ sur $\mathbb{R}_+^*$ ; ordre sur $\{(x,y) : x \leq y\}$ ; ordre induit par une application injective vers $\mathbb{R}$ | Réflexivité, antisymétrie, transitivité ; l'injectivité sert à l'antisymétrie du dernier |
| 5 | Ordre $\|x - x'\| \leq y' - y$ sur $\mathbb{R}^2$ | Transitivité par l'inégalité triangulaire ; majorants et minorants d'un point : deux demi-droites formant un « cône » ; ordre non total (points de même ordonnée) |
| 6 | Congruence modulo $n$ | Équivalence, $n$ classes, représentants $\{0, \ldots, n-1\}$, ensemble $\mathbb{Z}/n\mathbb{Z}$ ; compatible avec $+$ et $\times$ (« pour aller plus loin ») |
| 7 | Propriétés des classes : $x \in [x]$ et $x \in [y] \iff y \in [x] \iff [x] = [y] \iff [x] \cap [y] \neq \emptyset$ | Chaîne d'implications circulaire |
| 8 | « Égales à partir d'un certain rang » sur les fonctions de $\mathbb{R}$ dans $\mathbb{R}$ | Équivalence ; pas antisymétrique (fonctions différentes en 0 seulement) ; transitivité avec $A = \max(A_1, A_2)$ |
| 9 | $xSy \iff (xRy \text{ et } yRx)$ pour $R$ réflexive et transitive | $S$ est une équivalence |
| 10 | Fermeture par chemins d'une relation réflexive et symétrique | Équivalence : chemin constant, chemin renversé, chemins mis bout à bout |

### Exercice 2 en détail

- Inclusion sur $\mathcal{P}(E)$ : ordre, partiel dès que $E$ a au moins deux éléments (les singletons $\{a\}$, $\{b\}$ sont incomparables) ; minimum $\emptyset$, maximum $E$.
- $A \cap B = \emptyset$ : symétrique seulement (pas réflexive pour $A$ non vide, pas transitive).
- Même parité sur $\mathbb{Z}$ : équivalence à deux classes (le texte de l'exercice 2.3 est traité à la suite).
- $a - b = 3n$ avec $n \in \mathbb{N}$ : ordre partiel, sans minimum ni maximum ($4$ et $5$ incomparables).
- $a - b$ divisible par $3$ : équivalence à trois classes ($3n$, $3n+1$, $3n+2$).
- $x^2 - y^2 = x - y$ sur $\mathbb{R}$ : équivalence ; la classe de $x$ est $\{x, 1 - x\}$, réduite à $\{1/2\}$ pour $x = 1/2$.

## Méthodes et pièges

- Pour une propriété de relation, toujours reformuler la relation sous la forme la plus simple (par exemple $x^2 - x = y^2 - y$).
- Un contre-exemple suffit pour réfuter une propriété ; pour l'antisymétrie, chercher deux éléments distincts en relation dans les deux sens.
- « $n \in \mathbb{N}$ » ou « $k \in \mathbb{Z}$ » change tout : la symétrie échoue avec $\mathbb{N}$ (exercice 2.4), elle marche avec $\mathbb{Z}$ (exercice 2.5).
- Ne pas confondre antisymétrique et « non symétrique ».

## Points à vérifier

- **Exercice 4.1, incomparabilité de 2 et 3** : la preuve montre que $2^n = 3^m$ est impossible avec $n, m$ non nuls. Ce n'est pas la même chose que d'établir $3 \neq 2^n$ et $2 \neq 3^m$, qui est ce qu'exige l'incomparabilité. Le résultat est vrai ($\log_2 3$ est irrationnel), mais l'argument écrit ne l'établit pas tel quel (complément).
- **Exercice 2, relations 4 et 5** : « pour tout $a \in \mathbb{R}$ » est une coquille, il s'agit de $a \in \mathbb{Z}$.
- **Exercice 10, symétrie** : « puisque $S$ est symétrique » doit se lire « puisque $R$ est symétrique ».
