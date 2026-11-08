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
  - crible d'Ératosthène
  - sieve of Eratosthenes
  - théorème fondamental de l'arithmétique
  - décomposition en facteurs premiers
  - prime factorization
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un entier naturel $p \ge 2$ est **premier** s'il a exactement deux diviseurs positifs, $1$ et $p$. Un entier $n \ge 2$ non premier est dit **composé**. $1$ n'est pas premier (il n'a qu'un diviseur positif) ; $2$ est le seul nombre premier pair. Premiers nombres premiers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29…

## Dans le cours

**Algo Maths** : interprétation géométrique avec des billes. Si l'on peut ranger $X$ billes en rectangle, $X$ n'est pas premier ; si la seule disposition est une ligne, il l'est (15 billes : $3 \times 5$ ; 7 billes : une ligne). Exercice Python d'AlgoID1 : compter les nombres premiers inférieurs ou égaux à $n$.

**Operating System** : propriété citée au DM, tout nombre non premier $n > 2$ admet un diviseur premier $p \le \sqrt{n}$ ; donc si $n$ n'a aucun diviseur entre 2 et $\sqrt{n}$, il est premier. D'où le test `for ((i=2; i*i<=n; i++))` pour afficher les 500 premiers nombres premiers, et le test `i*i <= num` du lab 7. En Python, la même boucle s'écrit `for i in range(2, int(n**0.5) + 1)` : la borne de fin de `range` étant exclue, le `+ 1` est nécessaire pour tester $\sqrt{n}$ lui-même (sans lui, 4 et 9 seraient jugés premiers). [[Erreurs du cours#^e-nombre-premier|✎]]

## Compléments (hors du cours)

- **Lien avec les billes et $\sqrt{X}$** : si $X = a \times b$ avec $a \le b$, alors $a^2 \le a b = X$, donc le côté le plus court du rectangle vaut au plus $\sqrt{X}$. Il suffit donc de chercher un diviseur entre 2 et $\sqrt{X}$ : c'est la justification du test `i*i <= n` ci-dessus.
- **Crible d'Ératosthène** (IIIe siècle av. J.-C.) : pour lister tous les nombres premiers jusqu'à $n$, écrire les entiers de 2 à $n$ ; prendre le plus petit non barré (il est premier) et barrer tous ses multiples à partir de son carré ; recommencer jusqu'à dépasser $\sqrt{n}$. Les nombres restants sont premiers. Complexité $O(n \log \log n)$.

  ```python
  def crible(n):
      est_premier = [True] * (n + 1)
      est_premier[0] = est_premier[1] = False
      i = 2
      while i * i <= n:
          if est_premier[i]:
              for k in range(i * i, n + 1, i):
                  est_premier[k] = False
          i += 1
      return [k for k in range(n + 1) if est_premier[k]]
  ```

- **Infinité des nombres premiers** (Euclide, *Éléments*, livre IX) : supposons qu'il n'y en ait qu'un nombre fini $p_1, \dots, p_k$ et posons $N = p_1 p_2 \cdots p_k + 1$. Aucun $p_i$ ne divise $N$ (la division laisse un reste 1) ; or $N \ge 2$ admet un diviseur premier, qui n'est donc pas dans la liste : contradiction.
- **Théorème fondamental de l'arithmétique** : tout entier $n \ge 2$ s'écrit comme produit de nombres premiers, $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_r^{\alpha_r}$, et cette décomposition est unique à l'ordre des facteurs près. Exemple : $60 = 2^2 \times 3 \times 5$. C'est pour préserver cette unicité qu'on exclut 1 des nombres premiers.
- **Cryptographie RSA** (Rivest, Shamir, Adleman, 1977) : la clé publique contient le produit $n = pq$ de deux grands nombres premiers secrets. Multiplier $p$ et $q$ est rapide, mais retrouver $p$ et $q$ à partir de $n$ (factoriser) est, avec les algorithmes connus, hors de portée pour des nombres de plusieurs centaines de chiffres : la sécurité repose sur cette asymétrie.

Voir aussi : [[Arithmétique en Bash]], [[Boucle (programmation)]], [[Divisibilité]], [[Division euclidienne]], [[Algorithme d'Euclide]], [[Racine carrée]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[0 - diapo prof]]
