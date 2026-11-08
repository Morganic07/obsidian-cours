---
type: concept
tags: [year1]
aliases: [image réciproque, images réciproques, antécédent, antécédents, image directe, preimage, inverse image, "image d'une partie", ensemble image]
matieres: [Outil Maths]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]", "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-08
---

Pour une application $f : E \to F$ :

- **Antécédent** de $y \in F$ : un $x \in E$ tel que $f(x) = y$. Un $y$ a 0, 1 ou plusieurs antécédents.
- **Image d'une partie** $A \subset E$ : $f(A) = \{f(x) \mid x \in A\}$. Pour $A = E$, c'est l'ensemble image $\mathrm{Im}(f)$.
- **Image réciproque d'une partie** $B \subset F$ : $f^{-1}(B) = \{x \in E \mid f(x) \in B\}$. Elle est définie même si $f$ n'est pas bijective. La notation $f^{-1}$ ne suppose donc pas que la fonction réciproque existe. Quand $f$ est bijective, $f^{-1}(B)$ est aussi l'image de $B$ par la bijection réciproque.

## Propriétés

Pour $A, A' \subset E$ et $B, B' \subset F$ ([[4 - pdf]]) :

- $f(A \cup A') = f(A) \cup f(A')$.
- $f(A \cap A') \subset f(A) \cap f(A')$, avec égalité (pour tous $A$, $A'$) si et seulement si $f$ est injective.
- $f^{-1}(B \cup B') = f^{-1}(B) \cup f^{-1}(B')$, $f^{-1}(B \cap B') = f^{-1}(B) \cap f^{-1}(B')$, et $f^{-1}$ du complémentaire est le complémentaire de $f^{-1}$.

D'après le TD ([[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions]]) :

- $A \subset f^{-1}(f(A))$, avec égalité pour tout $A$ si et seulement si $f$ est injective.
- $f(f^{-1}(B)) = f(E) \cap B$, donc $f(f^{-1}(B)) = B$ pour tout $B$ si et seulement si $f$ est surjective.
- Exercice 9 : pour $f(x) = \frac{3x+1}{x-2} = 3 + \frac{7}{x-2}$, décroissante sur chaque branche, $f([0,2[ \cup ]2,4]) = ]-\infty, -\frac12] \cup [\frac{13}{2}, +\infty[$ ($f(0) = -\frac12$ et $f(4) = \frac{13}{2}$ sont atteints) ; en résolvant $0 \le 3 + \frac{7}{x-2} < 3$ puis $3 < 3 + \frac{7}{x-2} \le 4$, $f^{-1}([0,3[ \cup ]3,4]) = ]-\infty, -\frac13] \cup [9, +\infty[$. [[Erreurs du cours#^e-image-et-image-reciproque|✎]]
- Exercice 19 : pour $f(z) = \frac1z + z$ sur $\mathbb{C}^*$, $f^{-1}(i\mathbb{R}) = \{z \in \mathbb{C}^* : \mathrm{Re}(z) = 0\} = i\mathbb{R}^*$. [[Erreurs du cours#^e-image-et-image-reciproque|✎]]

Les propriétés d'injectivité et de surjectivité sont dans [[Injectivité et surjectivité]]. Les opérations sur les parties utilisées ici sont dans [[Opérations sur les ensembles]].

## Exemple

Pour $f(x) = x^2$ sur $\mathbb{R}$ : $f([-2, 1]) = [0, 4]$ et $f^{-1}([0, 4]) = [-2, 2]$. Les deux ensembles ne sont pas égaux, ce qui illustre $A \subsetneq f^{-1}(f(A))$ quand $f$ n'est pas injective.

### Exemples supplémentaires (complément, hors du cours)

Ajoutés dans [[4 - pdf]], toujours avec $f(x) = x^2$ sur $\mathbb{R}$ :

- **Image directe et réciproque** : $f([-1, 2]) = [0, 4]$ ; $f^{-1}([-2, 4]) = [-2, 2]$ ; $f^{-1}([-2, -1]) = \emptyset$ (un carré n'est jamais négatif) ; $f^{-1}(]1, +\infty[) = ]-\infty, -1[ \cup ]1, +\infty[$.
- **L'inclusion $f(A \cap B) \subset f(A) \cap f(B)$ peut être stricte** : avec $A = [-1, 0]$ et $B = [0, 1]$, $f(A \cap B) = f(\{0\}) = \{0\}$, alors que $f(A) \cap f(B) = [0, 1] \cap [0, 1] = [0, 1]$. La cause est la non-injectivité : $-x$ et $x$ ont la même image.
- **$A \subset f^{-1}(f(A))$ stricte** : $f^{-1}(f(\{1\})) = f^{-1}(\{1\}) = \{-1, 1\}$.
- **$f(f^{-1}(C)) \subset C$ stricte** : $f(f^{-1}([-1, 1])) = f([-1, 1]) = [0, 1] \subsetneq [-1, 1]$, car $f$ n'est pas surjective sur $\mathbb{R}$. On a toujours $f(f^{-1}(C)) \subset C$, avec égalité pour tout $C$ si $f$ est surjective.

Le DS2 d'Outils math (9 déc. 2022) porte sur l'image réciproque d'une intersection et sur $A \subset f^{-1}(f(A))$, avec égalité si et seulement si $f$ est injective ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

Notion parente : [[Application (mathématiques)]]. Voir aussi : [[Injectivité et surjectivité]], [[Double inclusion]].

Résumés : [[4 - pdf]]
