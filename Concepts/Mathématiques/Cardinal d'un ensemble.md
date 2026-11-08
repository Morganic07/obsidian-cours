---
type: concept
tags: [year1, year2]
aliases: [cardinal, ensemble fini, cardinality, Cardinal of a set, formule du crible, inclusion-exclusion, principe d'inclusion-exclusion, inclusion-exclusion principle, principe des tiroirs, pigeonhole principle]
matieres: [Outil Maths, Probability]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre2-Ensemble (4).pdf]]", "[[2 - ensembles|Chapitre 2 ensembles]]", "[[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]", "[[1 - Sample space,events, proba|Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-08
---

Un ensemble $E$ est **fini** s'il est vide ou contient un nombre fini d'éléments. Son **cardinal** $|E|$ est son nombre d'éléments ; $|\emptyset| = 0$.

**Outil Maths** : $|A \cup B| = |A| + |B| - |A \cap B|$, et $|A \cup B| = |A| + |B|$ si $A \cap B = \emptyset$ ([[Ensembles disjoints]]). Le TD Ensembles utilise $|\mathcal{P}(E)| = 2^n$ pour un ensemble $E$ à $n$ éléments.

**Probability** : un ensemble n'a ni ordre ni répétition, donc $\{a,b,b,c,c\} = \{a,b,c\} = \{c,b,a\}$.

## Compléments (complément, hors du cours)

Ajoutés dans [[2 - ensembles]] et [[4 - pdf]].

**Ensemble des parties.** Si $|E| = n$, alors $|\mathcal{P}(E)| = 2^n$ : construire une partie revient à décider, pour chacun des $n$ éléments, s'il y figure ou non, soit $2 \times 2 \times \cdots \times 2 = 2^n$ choix. En comptant les parties par taille ($\binom{n}{k}$ parties à $k$ éléments), on obtient l'identité
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n.$$

**Formule du crible (inclusion-exclusion)** pour trois ensembles :
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$
On retire les éléments comptés deux fois, puis on rajoute ceux de l'intersection triple, retirés une fois de trop. La formule à deux ensembles du cours en est le cas $C = \emptyset$.

**Autres formules** (ensembles finis) :
- complémentaire : pour $A \subset E$, $|\bar A| = |E| - |A|$ ;
- monotonie : $A \subset B \Rightarrow |A| \le |B|$ ;
- produit cartésien : $|A \times B| = |A| \times |B|$.

**Cardinal et applications.** Pour $E$, $F$ finis et $f : E \to F$ ([[Injectivité et surjectivité]], [[Bijection]]) :
- $f$ injective $\Rightarrow |E| \le |F|$ ; $f$ surjective $\Rightarrow |E| \ge |F|$ ; il existe une bijection de $E$ sur $F$ $\iff |E| = |F|$ ;
- si $|E| = |F|$ : $f$ injective $\iff$ $f$ surjective $\iff$ $f$ bijective.

**Principe des tiroirs** : si l'on range $n + 1$ objets dans $n$ tiroirs, un tiroir au moins en contient deux. C'est la contraposée de la première inégalité : une application d'un ensemble à $n+1$ éléments vers un ensemble à $n$ éléments ne peut pas être injective.

**Ensembles infinis.** Deux ensembles quelconques ont « même cardinal » (sont **équipotents**) s'il existe une bijection de l'un sur l'autre. $\mathbb{N}$ et $\mathbb{Z}$ sont équipotents (tous deux [[Ensemble dénombrable|dénombrables]]) ; $\mathbb{N}$ et $\mathbb{R}$ ne le sont pas, ce que Cantor a établi par l'argument diagonal (1891).

Notion parente : [[Ensemble (mathématiques)]]. Voir aussi : [[Équiprobabilité]], [[Dénombrement]], [[Opérations sur les ensembles]], [[Ensemble dénombrable]], [[Injectivité et surjectivité]], [[Bijection]].

Résumés : [[2 - pdf]], [[2 - ensembles]], [[4 - pdf]], [[1 - Sample space,events, proba]]
