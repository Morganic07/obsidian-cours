---
type: concept
tags: [year1]
aliases: [ordre total, ordre partiel, ensemble ordonné, ensemble partiellement ordonné, ensemble totalement ordonné, ordre strict, ordre lexicographique, order relation, partial order, total order, lexicographic order]
matieres: [Outil Maths, Analyse Maths]
sources: ["[[3 - Relation binaire|Chapitre 3 - Relation binaire]]", "[[Raw/Year 1/Outil Maths/Cours/Chapitre 3 - Relation binaire.docx|Chapitre 3 - Relation binaire]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]", "[[Raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TDRelations.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]"]
maj: 2026-11-08
---

**Relation d'ordre** : réflexive, antisymétrique ($(xRy$ et $yRx) \Rightarrow x = y$), transitive. [[Erreurs du cours#^e-relation-d-ordre|✎]] Elle est **totale** si deux éléments sont toujours comparables, **partielle** sinon. $\le$ et $\ge$ sont des ordres sur $\mathbb{R}$ ; $<$ et $>$ n'en sont pas, faute de réflexivité. On parle d'ensemble **totalement** ou **partiellement ordonné**. Autres exemples du cours : la [[Divisibilité]] sur $\mathbb{N}^*$ et l'inclusion sur $\mathcal{P}(E)$, qui ne sont pas totales.

Dans $(E, \preceq)$, pour $A \subseteq E$ : [[Élément maximal|élément maximal]], [[Majorant et minorant|majorant]], [[Plus grand élément|plus grand élément]] $\max(A)$, borne supérieure $\sup(A)$ (plus petit des majorants). Définitions symétriques pour minimal, minorant, $\min(A)$ et borne inférieure $\inf(A)$.

Le cours en PDF ajoute minimum, maximum, borne inférieure et borne supérieure, ainsi que les fonctions croissantes entre ensembles ordonnés ([[Application monotone]]). La propriété de la [[Borne supérieure]] distingue $\mathbb{R}$ de $\mathbb{Q}$.

**Analyse Maths** (chapitre 1, nombres réels) : majorant, minorant et partie bornée ($\exists K,\ \forall a \in A,\ |a| \le K$). Un majorant n'est jamais « le » majorant. Plus grand et plus petit élément sont uniques s'ils existent, mais peuvent ne pas exister. Les TD traduisent majoré, non minoré, borné, non borné en [[Quantificateur|quantificateurs]].

## Compléments (complément, hors du cours)

Ajoutés dans [[3 - Relation binaire]].

- **Ordre strict associé** : à un ordre $\preceq$ on associe $x \prec y \iff (x \preceq y \text{ et } x \ne y)$. Cette relation est irréflexive et transitive (donc aussi antisymétrique, par vacuité). $<$ est l'ordre strict associé à $\le$ : c'est pourquoi il n'est pas une relation d'ordre au sens du cours, qui exige la réflexivité.
- **Ordre lexicographique** sur $\mathbb{R}^2$ : $(a, b) \preceq (a', b')$ si $a < a'$, ou si $a = a'$ et $b \le b'$. C'est l'ordre du dictionnaire ; il est total.
- **Maximum, élément maximal, borne supérieure** : si $\max(A)$ existe, c'est aussi $\sup(A)$ et l'unique élément maximal de $A$. La réciproque est fausse dans un ordre partiel : dans $\mathcal{P}(\{1,2\})$ ordonné par l'inclusion, $A = \{\{1\},\{2\}\}$ a deux éléments maximaux, pas de maximum, et sa borne supérieure est $\{1,2\}$, qui n'appartient pas à $A$. Dans un ordre total, élément maximal et plus grand élément coïncident.
- **Représentation** : un ordre sur un ensemble fini se dessine par un [[Diagramme de Hasse]].

Notion parente : [[Relation binaire]]. Liens : [[Relation réflexive]], [[Relation antisymétrique]], [[Relation transitive]], [[Relation d'équivalence]], [[Majorant et minorant]], [[Borne supérieure]]

Résumés : [[3 - Relation binaire]], [[3 - pdf]], [[1 - Ensemble des Reels]]
