---
type: concept
tags:
  - year1
  - year2
aliases:
  - nombres premiers
  - prime number
  - prime numbers
  - test de primalité
sources:
  - "[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]"
  - ".raw/Year 1/Algo Maths/AlgoID1.pdf"
  - "[[DM Shell Scripting]]"
  - "[[Copy of 08 Processes-TP]]"
maj: 2026-11-06
---

**Algo Maths** : interprétation géométrique avec des billes. Si l'on peut ranger $X$ billes en rectangle, $X$ n'est pas premier ; si la seule disposition est une ligne, il l'est (15 billes : $3 \times 5$ ; 7 billes : une ligne). Exercice Python d'AlgoID1 : compter les nombres premiers inférieurs ou égaux à $n$.

**Operating System** : propriété citée au DM, tout nombre non premier $n > 2$ admet un diviseur premier $p \le \sqrt{n}$ ; donc si $n$ n'a aucun diviseur entre 2 et $\sqrt{n}$, il est premier. D'où le test `for ((i=2; i*i<=n; i++))` pour afficher les 500 premiers nombres premiers, et le test `i*i <= num` du lab 7.

Voir aussi : [[Arithmétique en Bash]], [[Boucle (programmation)]].

## À vérifier

- Version Python du DM : `range(2, int(n**0.5))` exclut la racine, si bien que 4 et 9 seraient jugés premiers (signalé par le résumé).

Résumés : [[Séance 1 - Algo Maths (résumé)|Cours 1 (résumé) (Algo Maths)]], [[AlgoID1 (résumé)]], [[DM Shell Scripting (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[Operating Systems - Semester report (résumé)]]
