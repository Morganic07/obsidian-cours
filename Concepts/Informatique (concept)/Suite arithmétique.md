---
type: concept
tags: [year2, year4]
aliases: [arithmetic series, common difference, "raison d'une suite"]
sources: ["[[Copy of 08 Processes-TP (résumé)|Copy of 08 Processes-TP]]", "[[3 - complexité (résumé)]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une [[Suite numérique|suite]] $(u_n)$ est arithmétique s'il existe un réel $r$, appelé raison (*common difference*), tel que $u_{n+1} = u_n + r$ pour tout $n$. Son terme général est alors $u_n = u_0 + n r$, et la somme de ses termes consécutifs vaut le nombre de termes multiplié par la moyenne du premier et du dernier : $\sum_{k=0}^{n} u_k = (n+1)\dfrac{u_0 + u_n}{2}$ (voir [[Somme des premiers entiers]]). À comparer avec la [[Suite géométrique]], où l'on multiplie par la raison au lieu de l'ajouter.

## Dans le cours

Nommée dans le lab 3 de Operating System sans définition mathématique : un programme C y affiche une suite partant de 1, chaque terme augmentant d'une différence commune (common difference) donnée, jusqu'à atteindre ou dépasser la borne. Le même lab figure dans [[Operating Systems - Semester report (résumé)]].

En Graph theory (Year 4), [[3 - complexité (résumé)]] résout une récurrence de coût en suite arithmétique : $T(n) = 3n + 1$, donc $T(n) = \Theta(n)$, algorithme linéaire.

Notion parente : [[Suite numérique]].

Résumés : [[Copy of 08 Processes-TP (résumé)]], [[Operating Systems - Semester report (résumé)]], [[3 - complexité (résumé)]]
