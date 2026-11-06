---
type: concept
aliases: [image réciproque, images réciproques, antécédent, antécédents, image directe, preimage, inverse image]
matieres: [Outil Maths]
sources: ["[[Chapitre4-Fonctions (1) (résumé)]]", "[[TD4Applications-Solutions (résumé)]]"]
maj: 2026-11-06
---

Pour une application $f : E \to F$ :

- **Antécédent** de $y \in F$ : un $x \in E$ tel que $f(x) = y$. Un $y$ a 0, 1 ou plusieurs antécédents.
- **Image d'une partie** $A \subset E$ : $f(A) = \{f(x) \mid x \in A\}$. Pour $A = E$, c'est l'ensemble image $\mathrm{Im}(f)$.
- **Image réciproque d'une partie** $B \subset F$ : $f^{-1}(B) = \{x \in E \mid f(x) \in B\}$. Elle est définie même si $f$ n'est pas bijective. La notation $f^{-1}$ ne suppose donc pas que la fonction réciproque existe. Quand $f$ est bijective, $f^{-1}(B)$ est aussi l'image de $B$ par la bijection réciproque.

## Propriétés

Pour $A, A' \subset E$ et $B, B' \subset F$ ([[Chapitre4-Fonctions (1) (résumé)]]) :

- $f(A \cup A') = f(A) \cup f(A')$.
- $f(A \cap A') \subset f(A) \cap f(A')$, avec égalité (pour tous $A$, $A'$) si et seulement si $f$ est injective.
- $f^{-1}(B \cup B') = f^{-1}(B) \cup f^{-1}(B')$, $f^{-1}(B \cap B') = f^{-1}(B) \cap f^{-1}(B')$, et $f^{-1}$ du complémentaire est le complémentaire de $f^{-1}$.

D'après le TD ([[TD4Applications-Solutions (résumé)]]) :

- $A \subset f^{-1}(f(A))$, avec égalité pour tout $A$ si et seulement si $f$ est injective.
- $f(f^{-1}(B)) = f(E) \cap B$, donc $f(f^{-1}(B)) = B$ pour tout $B$ si et seulement si $f$ est surjective.

Les propriétés d'injectivité et de surjectivité sont dans [[Injectivité et surjectivité]]. Les opérations sur les parties utilisées ici sont dans [[Opérations sur les ensembles]].

## Exemple

Pour $f(x) = x^2$ sur $\mathbb{R}$ : $f([-2, 1]) = [0, 4]$ et $f^{-1}([0, 4]) = [-2, 2]$. Les deux ensembles ne sont pas égaux, ce qui illustre $A \subsetneq f^{-1}(f(A))$ quand $f$ n'est pas injective.
