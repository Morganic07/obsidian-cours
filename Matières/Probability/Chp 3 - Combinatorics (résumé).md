---
type: source
tags: [year2]
sources: ["[[Chp 3 - Combinatorics]]"]
maj: 2026-11-05
---

Résumé de [[Chp 3 - Combinatorics]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Compter les issues d'une expérience, pour calculer $P(A) = |A|/|S|$ dans le cas équiprobable. Voir [[Dénombrement]].

## Contenu, dans l'ordre du cours

- **Arbre de décision** : sans sélection, on a des permutations ($n!$ si les objets sont distincts, $n!/(n_1!\cdots n_i!)$ sinon). Avec sélection, un échantillon ordonné donne $n!/(n-k)!$ (distincts) ou $n^k$ (non distincts), un échantillon non ordonné donne $\binom{n}{k}$ (distincts) ou $\binom{n+k-1}{k}$ (non distincts).
- **Principe fondamental** : $k$ choix successifs de $m_1, \dots, m_k$ possibilités donnent $m_1 \cdot m_2 \cdots m_k$ $k$-uplets.
- **Avec remise** : $k$ choix parmi $n$ objets donnent $n^k$ issues.
- **Sans remise** : une suite ordonnée de $k$ objets distincts est une permutation de taille $k$, et il y en a ${}_nP_k = n(n-1)\cdots(n-k+1) = n!/(n-k)!$.
- **Combinaisons** : une combinaison est un sous-ensemble non ordonné de taille $k$. Chaque combinaison correspond à $k!$ permutations, donc ${}_nC_k = {}_nP_k / k! = \binom{n}{k} = n!/(k!(n-k)!)$ (coefficient binomial). Exemple : $\{a,b,c,d,e\}$, 3 éléments : $60/6 = 10$.
- **Cas particuliers** : $\binom{n}{n} = \binom{n}{0} = 1$ et $\binom{n}{1} = n$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **$n^k$ écrit « n » indice « k »** : dans le texte, « 𝒏<sub>𝒌</sub> » devrait se lire $n^k$, comme dans l'arbre de décision (complément).
2. **Cas non distincts de l'arbre** : l'arbre donne $n^k$ pour un arrangement non distinct et $\binom{n+k-1}{k}$ pour une combinaison non distincte, mais le cours ne développe que le cas « avec remise, ordonné ». La formule $\binom{n+k-1}{k}$ n'est pas démontrée dans la note.
3. **Faute de transcription** : « chose » et « éléments » dans la dernière image sont recopiés tels quels. Fausse alerte sur le fond, rien à corriger.
