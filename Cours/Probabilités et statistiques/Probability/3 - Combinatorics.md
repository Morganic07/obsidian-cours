---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les images à texte sont recopiées ; l'arbre de décision est intégré.

## Idée générale

Compter les issues d'une expérience, pour calculer $P(A) = |A|/|S|$ dans le cas équiprobable. Voir [[Dénombrement]].

## Arbre de décision du dénombrement

![[Chp 3 - Combinatorics - image6.jpg]]
*Figure : arbre de décision — pas de sélection (permutation) ou sélection (arrangement si l'échantillon est ordonné, combinaison sinon), chaque feuille distinguant objets distincts et non distincts.*

| Situation | Objets distincts | Non distincts |
|---|---|---|
| Pas de sélection : [[Permutation (dénombrement)\|permutation]] de $n$ objets | $n!$ | $\dfrac{n!}{n_1!\, n_2! \cdots n_i!}$ |
| Sélection de $k$, échantillon ordonné : arrangement | $\dfrac{n!}{(n-k)!}$ | $n^k$ |
| Sélection de $k$, échantillon non ordonné : [[Combinaison (dénombrement)\|combinaison]] | $\dbinom{n}{k}$ | $\dbinom{n+k-1}{k}$ |

**Factorielle.** $n! = n \times (n-1) \times \dots \times 2 \times 1$ est le nombre de façons d'ordonner $n$ objets distincts (voir [[Factorielle]]) ; par convention $0! = 1$, ce qui rend justes les formules pour $k = 0$ ou $k = n$. Elle croît plus vite que toute exponentielle : $10! = 3\,628\,800$, et un jeu de 52 cartes peut être mélangé de $52! \approx 8 \times 10^{67}$ façons. La **formule de Stirling** en donne l'ordre de grandeur : $n! \sim \sqrt{2\pi n}\,\left(\frac{n}{e}\right)^n$. [[Complément hors du cours|ⓘ]]

Dans les lignes « sélection », la colonne « non distincts » correspond aux tirages **avec répétition** (un même objet peut être choisi plusieurs fois, comme dans un tirage avec remise) ; la colonne « distincts », aux tirages sans répétition. Un exemple par case : [[Complément hors du cours|ⓘ]]
- **Permutation, objets distincts** : ranger 5 livres différents sur une étagère, $5! = 120$ façons.
- **Permutation, objets non distincts** : les anagrammes du mot ANANAS (3 A, 2 N, 1 S), $\frac{6!}{3!\,2!\,1!} = 60$. On divise par $3!$ et $2!$ car permuter entre eux les A, ou les N, ne change pas le mot. Ce nombre est un **coefficient multinomial**, noté $\binom{n}{n_1, \dots, n_i}$ avec $n_1 + \dots + n_i = n$.
- **Arrangement sans répétition** : le podium (or, argent, bronze) d'une course de 8 coureurs, $\frac{8!}{5!} = 8 \times 7 \times 6 = 336$.
- **Arrangement avec répétition** : les codes de carte bancaire à 4 chiffres, $10^4 = 10\,000$.
- **Combinaison sans répétition** : choisir 2 délégués dans une classe de 30, $\binom{30}{2} = 435$.
- **Combinaison avec répétition** : prendre 3 boules de glace parmi 5 parfums, un parfum pouvant être répété, $\binom{5+3-1}{3} = \binom{7}{3} = 35$.

**D'où vient $\binom{n+k-1}{k}$ (méthode des étoiles et des barres).** Un choix non ordonné avec répétition de $k$ objets parmi $n$ types est décrit par le nombre d'exemplaires de chaque type. On le code par une suite de $k$ étoiles (les objets) et $n - 1$ barres (les séparations entre types) : avec 5 parfums et 3 boules, « ★★||★|| » signifie 2 boules du 1ᵉʳ parfum et 1 du 3ᵉ. Chaque choix correspond à une seule suite de $n + k - 1$ symboles, et une suite est déterminée par la place des $k$ étoiles, d'où $\binom{n+k-1}{k}$. [[Complément hors du cours|ⓘ]]

**Notations françaises.** Les manuels français notent $A_n^k = \frac{n!}{(n-k)!}$ le nombre d'**arrangements** (le $_nP_k$ du cours) et, plus anciennement, $C_n^k$ le nombre de combinaisons, aujourd'hui écrit $\binom{n}{k}$ et lu « $k$ parmi $n$ ». Attention à l'ordre des indices : $C_n^k = \binom{n}{k} = {}_nC_k$. [[Complément hors du cours|ⓘ]]

## Principe fondamental de dénombrement (*fundamental counting principle, product rule*)

- Un **$k$-uplet** (*k-tuple*) est une suite **ordonnée** de $k$ objets.
- On fait $k$ choix (on cherche des $k$-uplets), avec $m_1$ possibilités pour le 1ᵉʳ choix, $m_2$ pour le 2ᵉ, …, $m_k$ pour le $k$-ième. Si ces choix se combinent sans restriction, le nombre total de possibilités est :
$$m_1 \cdot m_2 \cdot \ldots \cdot m_k$$

Exemple : un menu à 3 entrées, 4 plats et 2 desserts offre $3 \times 4 \times 2 = 24$ repas différents. En termes d'ensembles, c'est le cardinal d'un [[Produit cartésien|produit cartésien]] : $|E_1 \times \dots \times E_k| = |E_1| \cdots |E_k|$. Il se visualise par un arbre dont chaque niveau est un choix. [[Complément hors du cours|ⓘ]]

Le principe a un pendant, le **principe additif** (*sum rule*) : si les issues se répartissent en cas **disjoints** (qui ne peuvent pas se produire ensemble), leur nombre total est la somme des nombres de chaque cas, $|A \cup B| = |A| + |B|$ si $A \cap B = \emptyset$. Si les cas se chevauchent, on retranche ce qui est compté deux fois : $|A \cup B| = |A| + |B| - |A \cap B|$, la [[Formule du crible|formule du crible]] du [[1 - Sample space,events, proba|chapitre 1]]. On multiplie pour des choix successifs (« et »), on additionne pour des cas qui s'excluent (« ou »). [[Complément hors du cours|ⓘ]]

Le **passage au complémentaire** simplifie souvent les comptes : pour « au moins un… », on compte les cas où il n'y en a aucun et on retranche du total. Exemple : parmi les $6^4 = 1296$ résultats de quatre lancers de dé, $5^4 = 625$ ne contiennent aucun 6, donc $1296 - 625 = 671$ contiennent au moins un 6 (probabilité $671/1296 \approx 0{,}52$). [[Complément hors du cours|ⓘ]]

## Expériences avec et sans remise (*with and without replacement*)

- **Avec remise** ([[Tirage avec et sans remise]]) : $k$ choix parmi $n$ objets distincts. Le principe fondamental s'applique avec $m_1 = m_2 = \dots = m_k = n$, d'où $n^k$ issues possibles. [[Erreurs du cours#^e-3-combinatorics|✎]]
- **Sans remise** : toute suite ordonnée de $k$ objets tirés sans remise parmi $n$ objets distincts est une **permutation de taille $k$** (*k-permutation*). Leur nombre est :
$$_nP_k = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$

## Combinaisons (*combinations*)

**Définition.** Étant donné $n$ objets distincts, tout **sous-ensemble non ordonné** de taille $k$ est une **combinaison**.

**Exemple du cours.** Ensemble $\{a,b,c,d,e\}$ à cinq éléments. De combien de façons peut-on choisir 3 éléments ?
1. En tenant compte de l'ordre : $_5P_3 = 5 \cdot 4 \cdot 3 = 60$ façons (60 permutations de taille 3).
2. Parmi elles, combien sont formées de $a, b, c$ ? Il y a $3! = 6$ permutations de $a, b, c$ ; sans l'ordre, elles sont toutes équivalentes à la seule combinaison $\{a,b,c\}$.
3. Chaque combinaison de taille 3 correspond à $3!$ permutations (ordres différents du même ensemble), donc
$$_5P_3 = 60 = (\text{nombre de combinaisons de taille } 3) \cdot 3! \;\Rightarrow\; \text{nombre de combinaisons} = \frac{_5P_3}{3!} = 10$$
4. Le raisonnement vaut pour toute taille $k$.

## Nombre de combinaisons

- Avec $n$ objets distincts, toute permutation de taille $k$ s'obtient en ordonnant, de l'une des $k!$ façons possibles, les $k$ objets d'une combinaison :
$$\text{nombre de permutations} = k! \cdot (\text{nombre de combinaisons})$$
- Dans une combinaison, on s'intéresse aux $k$-uplets non ordonnés.

**Formule.** Le nombre de combinaisons de taille $k$ formées à partir de $n$ objets distincts est
$$_nC_k = \frac{n!}{k!\,(n-k)!} =: \binom{n}{k}$$
Le symbole $\binom{n}{k}$ est le **[[Coefficient binomial|coefficient binomial]]** (*binomial coefficient*).

**Cas particuliers.**
- $\binom{n}{n} = \binom{n}{0} = 1$ : il n'y a qu'une façon de choisir $n$ éléments parmi $n$, et qu'une façon de n'en choisir aucun.
- $\binom{n}{1} = n$ : il y a $n$ ensembles de taille 1.

**Propriétés du coefficient binomial.** [[Complément hors du cours|ⓘ]]
- **Symétrie** : $\binom{n}{k} = \binom{n}{n-k}$, car choisir les $k$ éléments qu'on garde revient à choisir les $n - k$ qu'on laisse.
- **[[Formule de Pascal]]** : $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ pour $1 \le k \le n - 1$. On fixe un élément : soit il est dans la combinaison (il reste $k - 1$ éléments à choisir parmi $n - 1$), soit il n'y est pas ($k$ parmi $n - 1$). Elle permet de construire de proche en proche le **triangle de Pascal**.
- **[[Formule du binôme de Newton]]** : $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$, d'où le nom de « coefficient binomial ». Avec $a = b = 1$ : $\sum_{k=0}^{n} \binom{n}{k} = 2^n$, le nombre total de parties d'un ensemble à $n$ éléments ($|\mathcal{P}(S)|$, chapitre 1).

**Du dénombrement aux probabilités.** Dans le cas [[Équiprobabilité|équiprobable]], on compte $|A|$ et $|S|$ avec le **même** modèle (ordonné ou non, avec ou sans remise) ; mélanger les deux est l'erreur la plus fréquente. Exemple : une urne contient 4 boules rouges et 6 noires, on en tire 3 simultanément (sans ordre). La probabilité d'obtenir exactement 2 rouges est [[Complément hors du cours|ⓘ]]
$$P = \frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \frac{6 \times 6}{120} = \frac{3}{10}$$
(choisir 2 rouges parmi 4 et 1 noire parmi 6, sur toutes les façons de choisir 3 boules parmi 10). Ce calcul est celui de la [[Loi hypergéométrique|loi hypergéométrique]] ; avec remise, on obtiendrait la [[Loi binomiale|loi binomiale]]. [[Complément hors du cours|ⓘ]]

**Le paradoxe des anniversaires.** Dans un groupe de $k$ personnes (anniversaires équiprobables sur 365 jours, années bissextiles ignorées), la probabilité que deux au moins partagent le même jour d'anniversaire s'obtient par le complémentaire : les $k$ dates toutes différentes forment un arrangement sans répétition, d'où [[Complément hors du cours|ⓘ]]
$$P(\text{au moins deux identiques}) = 1 - \frac{365 \times 364 \times \dots \times (365 - k + 1)}{365^k} = 1 - \frac{365!}{(365-k)!\,365^k}$$
Elle dépasse $1/2$ dès $k = 23$ (environ $0{,}507$) et vaut environ $0{,}97$ pour $k = 50$, bien plus que ce que l'intuition suggère : le nombre de **paires** de personnes, $\binom{23}{2} = 253$, est grand. Voir [[Paradoxe des anniversaires]]. [[Complément hors du cours|ⓘ]]

Le chapitre ne contient pas d'exercice.
