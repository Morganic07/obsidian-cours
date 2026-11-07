---
type: concept
tags: [year1]
aliases: [image réciproque, images réciproques, antécédent, antécédents, image directe, preimage, inverse image, "image d'une partie", ensemble image]
matieres: [Outil Maths]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]", "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-07
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

Les propriétés d'injectivité et de surjectivité sont dans [[Injectivité et surjectivité]]. Les opérations sur les parties utilisées ici sont dans [[Opérations sur les ensembles]].

## Exemple

Pour $f(x) = x^2$ sur $\mathbb{R}$ : $f([-2, 1]) = [0, 4]$ et $f^{-1}([0, 4]) = [-2, 2]$. Les deux ensembles ne sont pas égaux, ce qui illustre $A \subsetneq f^{-1}(f(A))$ quand $f$ n'est pas injective.

Le DS2 d'Outils math (9 déc. 2022) porte sur l'image réciproque d'une intersection et sur $A \subset f^{-1}(f(A))$, avec égalité si et seulement si $f$ est injective ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

Notion parente : [[Application (mathématiques)]]. Voir aussi : [[Injectivité et surjectivité]], [[Double inclusion]].

## Erreurs du cours

- [[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions]], exercice 9 ($f(x) = \frac{3x+1}{x-2} = 3 + \frac{7}{x-2}$, décroissante sur chaque branche), écrit « $f([0,2[ \cup ]2,4]) = [-\infty, -\frac12[ \cup ]\frac{13}{2}, +\infty]$ » ; il faut « $]-\infty, -\frac12] \cup [\frac{13}{2}, +\infty[$ » ($f(0) = -\frac12$ et $f(4) = \frac{13}{2}$ sont atteints). Dans la même question, « $0 \le 3 + \frac{7}{x-2} < 0$ » est à lire « $< 3$ » ; le résultat $f^{-1}([0,3[ \cup ]3,4]) = ]-\infty, -\frac13] \cup [9, +\infty[$ est juste.
- Même corrigé, exercice 19 ($f(z) = \frac1z + z$ sur $\mathbb{C}^*$), écrit « $f^{-1}(i\mathbb{R}) = \{z \in \mathbb{C}^\times : \mathrm{Re}(z) = 0\} = i\mathbb{R}$ » ; il faut « $i\mathbb{R}^*$ » ($0$ n'est pas dans l'ensemble de départ).

Résumés : [[4 - pdf]]
