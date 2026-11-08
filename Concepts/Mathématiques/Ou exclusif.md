---
type: concept
tags: [year1]
aliases: [XOR, disjonction exclusive, exclusive or, ou exclusif logique]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 1 logique .docx|Chapitre 1 logique]]", "[[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le **ou exclusif** de deux propositions $p$ et $q$, noté $p \oplus q$ (ou XOR), est vrai quand **exactement une** des deux propositions est vraie.

| $p$ | $q$ | $p \oplus q$ |
|---|---|---|
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |

**Équivalences** :
$$p \oplus q \equiv (p \vee q) \wedge \neg(p \wedge q) \equiv (p \wedge \neg q) \vee (\neg p \wedge q) \equiv \neg(p \Leftrightarrow q).$$
Sa colonne est donc l'inverse de celle de l'équivalence $p \Leftrightarrow q$.

**Différence avec le ou du cours** : le ou logique $p \vee q$ est **inclusif**, vrai aussi quand $p$ et $q$ sont vraies toutes les deux. Le ou exclusif est faux dans ce cas : il correspond au « ou » du langage courant dans « fromage ou dessert ».

**Propriétés** :

- commutatif : $p \oplus q \equiv q \oplus p$ ; associatif : $(p \oplus q) \oplus r \equiv p \oplus (q \oplus r)$ ;
- élément neutre F : $p \oplus F \equiv p$ ; et $p \oplus V \equiv \neg p$ ;
- $p \oplus p \equiv F$ : chaque proposition est son propre inverse, d'où $(p \oplus q) \oplus q \equiv p$.

**Ensembles** : l'analogue ensembliste est la [[Différence symétrique]] : $x \in A \,\Delta\, B \iff (x \in A) \oplus (x \in B)$.

**Informatique** : c'est l'opérateur XOR, noté `^` en C et en Python sur les [[Bit|bits]] des entiers (`5 ^ 3` vaut `6`, car `101 ^ 011 = 110`). La propriété $(a \oplus b) \oplus b = a$ sert à échanger deux variables sans variable temporaire, ou au chiffrement par masque jetable. Il n'existe pas de XOR logique dédié en C : sur des booléens, on écrit `a != b`.

## Dans le cours

Le cours ne le définit pas : il ne présente que le ou inclusif $\vee$. Il apparaît dans les compléments de [[1 - logique]] (à propos du « ou » du langage courant) et, par la différence symétrique, de [[2 - ensembles]].

Notion parente : [[Logique propositionnelle]]. Voir aussi : [[Propriétés des connecteurs logiques]], [[Équivalence logique]], [[Différence symétrique]], [[Opérateur logique]], [[Bit]].

Résumés : [[1 - logique]], [[2 - ensembles]]
