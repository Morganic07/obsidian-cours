---
type: concept
tags: [year4]
aliases: [logarithmes, logarithme népérien, logarithme binaire, logarithme décimal, logarithme en base b, logarithm]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : pour une base $b > 0$, $b \ne 1$, le **logarithme en base $b$** d'un réel $x > 0$ est l'exposant $y = \log_b x$ tel que $b^y = x$ : c'est la réciproque de $y \mapsto b^y$ (voir [[Puissance (mathématiques)]]). Le **logarithme népérien** $\ln$ a pour base $e$, le **logarithme décimal** la base 10, le **logarithme binaire** $\log_2$ la base 2. Règles : $\log_b(xy) = \log_b x + \log_b y$, $\log_b(x^k) = k \log_b x$, et le changement de base $\log_b x = \frac{\ln x}{\ln b}$ : deux logarithmes ne diffèrent que d'un facteur constant, d'où l'écriture $O(\log n)$ sans base en [[Complexité algorithmique|complexité]].

**Sens pratique.** $\log_2 n$ est à peu près le nombre de fois qu'on peut diviser $n$ par 2 avant d'arriver à 1 : $\log_2 1\,000 \approx 10$, $\log_2 10^6 \approx 20$, $\log_2 10^9 \approx 30$. C'est pourquoi une [[Recherche dichotomique|recherche dichotomique]] ou une recherche dans un [[Arbre équilibré|arbre équilibré]] d'un milliard d'éléments ne demande qu'une trentaine de comparaisons. $\lfloor \log_2 n \rfloor + 1$ est le nombre de chiffres de $n$ en [[Numération binaire|binaire]].

## Dans le cours

[[2 - tree revisions années précédentes]] donne la hauteur minimale d'un arbre $k$-aire de taille $n$ par un logarithme en base $k$, $\lceil \log_k((k-1)n+1) \rceil - 1$ (soit $\lfloor \log_2 n \rfloor$ pour un arbre binaire), et la complexité $O(\log n)$ de la recherche dans un arbre binaire de recherche équilibré.

Voir aussi : [[Échelle logarithmique]], [[Classe de complexité]], [[Hauteur d'un arbre]], [[Partie entière]].

Résumés : [[2 - tree revisions années précédentes]]
