---
type: concept
tags: [year3]
aliases: [integer overflow, dépassement de capacité, débordement d'entier]
sources: ["[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un dépassement d'entier (*integer overflow*) se produit quand le résultat d'un calcul sort de l'intervalle que le type entier peut représenter.

En Java, les entiers signés sont codés en [[Complément à deux|complément à deux]] sur $n$ bits : ils vont de $-2^{n-1}$ à $2^{n-1}-1$. Le résultat d'une opération est pris modulo $2^n$ : il « reboucle » de l'autre côté de l'intervalle, sans erreur ni exception.

- Exemple : `Integer.MAX_VALUE + 1 == Integer.MIN_VALUE`, soit $2^{31}-1+1 \to -2^{31}$.
- Même mécanisme pour un [[Transtypage|cast]] rétrécissant, qui ne garde que les bits de poids faible : `(byte) 200` vaut $200 - 256 = -56$.
- Parades : utiliser un type plus large (`long` au lieu de `int`), ou les méthodes `Math.addExact`, `Math.multiplyExact`, etc., qui lèvent une `ArithmeticException` en cas de dépassement.
- En C, le dépassement d'un entier **signé** est un comportement indéfini (le compilateur peut supposer qu'il n'arrive jamais) ; pour un entier non signé, le résultat est défini modulo $2^n$.

## Dans le cours

Le cours ne la nomme pas. La fiche [[1 - Intro Java]] donne les intervalles des types entiers (`int` de $-2^{31}$ à $2^{31}-1$, `long` de $-2^{63}$ à $2^{63}-1$), et le dépassement apparaît dans ses compléments.

Voir aussi : [[Complément à deux]], [[Type primitif]], [[Transtypage]], [[Langage Java]].

Résumés : [[1 - Intro Java]]
