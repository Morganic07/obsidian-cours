---
type: concept
tags: [year2]
aliases: [birthday paradox, problème des anniversaires, birthday problem]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : résultat de dénombrement selon lequel, dans un groupe de 23 personnes seulement, il y a plus d'une chance sur deux que deux au moins aient le même jour d'anniversaire.

**Hypothèses** : $k$ personnes, anniversaires [[Équiprobabilité|équiprobables]] et indépendants sur 365 jours, années bissextiles ignorées.

**Calcul par le complémentaire** : les $365^k$ suites de dates sont équiprobables ; celles où les $k$ dates sont toutes différentes forment un arrangement sans répétition de $k$ jours parmi 365, au nombre de $365 \times 364 \times \dots \times (365 - k + 1) = \dfrac{365!}{(365-k)!}$. D'où

$$P(\text{au moins deux anniversaires identiques}) = 1 - \frac{365 \times 364 \times \dots \times (365 - k + 1)}{365^k} = 1 - \frac{365!}{(365-k)!\,365^k}$$

**Valeurs** : environ 0,507 pour $k = 23$, premier $k$ où l'on dépasse $1/2$ ; environ 0,97 pour $k = 50$.

**Pourquoi c'est contre-intuitif** : on pense à la probabilité qu'une personne donnée partage son anniversaire avec une autre, alors que l'on compare toutes les **paires** : 23 personnes forment $\binom{23}{2} = 253$ paires, chacune ayant une chance sur 365 de coïncider.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[3 - Combinatorics]], comme application des arrangements sans répétition.

Voir aussi : [[Dénombrement]], [[Permutation (dénombrement)]], [[Équiprobabilité]], [[Coefficient binomial]]

Résumés : [[3 - Combinatorics]]
