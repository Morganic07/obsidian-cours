---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]], dans [[Probability (index)]]. En cas d'écart, le cours et ses images font foi. Les images à texte sont recopiées ; l'arbre de décision est intégré.

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

## Principe fondamental de dénombrement (*fundamental counting principle, product rule*)

- Un **$k$-uplet** (*k-tuple*) est une suite **ordonnée** de $k$ objets.
- On fait $k$ choix (on cherche des $k$-uplets), avec $m_1$ possibilités pour le 1ᵉʳ choix, $m_2$ pour le 2ᵉ, …, $m_k$ pour le $k$-ième. Si ces choix se combinent sans restriction, le nombre total de possibilités est :
$$m_1 \cdot m_2 \cdot \ldots \cdot m_k$$

## Expériences avec et sans remise (*with and without replacement*)

- **Avec remise** ([[Tirage avec et sans remise]]) : $k$ choix parmi $n$ objets distincts. Le principe fondamental s'applique avec $m_1 = m_2 = \dots = m_k = n$, d'où $n^k$ issues possibles.
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

Le chapitre ne contient pas d'exercice.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **$n^k$ écrit « n » indice « k »** : dans le texte, « 𝒏<sub>𝒌</sub> » devrait se lire $n^k$, comme dans l'arbre de décision (complément).
2. **Cas non distincts de l'arbre** : l'arbre donne $n^k$ pour un arrangement non distinct et $\binom{n+k-1}{k}$ pour une combinaison non distincte, mais le cours ne développe que le cas « avec remise, ordonné ». La formule $\binom{n+k-1}{k}$ n'est pas démontrée dans la note.
3. **Faute de transcription** : « chose » et « éléments » dans la dernière image sont recopiés tels quels. Fausse alerte sur le fond, rien à corriger.
4. **Vocabulaire « distinct / non distinct »** : dans l'arbre, « non distinct » recouvre deux situations différentes — objets répétés pour les permutations ($n!/(n_1!\cdots n_i!)$), tirage avec remise pour arrangements et combinaisons ($n^k$, $\binom{n+k-1}{k}$). Le cours ne le précise pas (complément).
