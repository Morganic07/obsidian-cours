---
type: source
tags: [year1]
sources: [".raw/Year 1/Analyse Maths/contrôles/correction-DS1-analyse-18-11-2021(1)(1).pdf"]
maj: 2026-11-06
---

Résumé de correction-DS1-analyse-18-11-2021 (`.raw/Year 1/Analyse Maths/contrôles/correction-DS1-analyse-18-11-2021(1)(1).pdf`) (5 pages, texte), dans [[Analyse Maths (matière)]]. Corrigé du DS1 d'Analyse du 18 novembre 2021 (PréING1). Même structure que [[DS1-Analyse-2022-corrigé (résumé)]], sur [[Chap0-Rappels-etc (résumé)]] et [[Chap1-reels (résumé)]].

## Les 5 exercices et leurs méthodes

1. **Équations** : $\sin 3x = \cos x$ (écrire $\cos x = \sin(x + \pi/2)$, deux familles de solutions : $\pi/4 + k\pi$ et $\pi/8 + k\pi/2$) ; $\tan^2(3x + \pi/3) - 3 = 0$ (passer à $\tan = \pm\sqrt3$, domaine $x \ne \pi/18 + k\pi/3$, solutions $k\pi/3$ et $-2\pi/9 + k\pi/3$) ; $(5E(x)+2)(3E(x)+6) = 0$ (un facteur donne $E(x) = -2/5$, impossible car $E(x)$ est entier, donc $x \in [-2,-1[$).
2. **Inéquations** : $|1/x + 1| < 1$ (cas $x > 0$ impossible, $x < 0$ donne $x < -1/2$) ; $(2E(x)+1)^2 < 4$ ; $\sqrt{x^2-1} < 2-x$ (domaine puis carré, solution $]-\infty,-1] \cup [1, 5/4[$).
3. **Sommes et produits** : $\sum k/(k+1)! = 1 - 1/(n+1)!$ (écrire $k = (k+1) - 1$, télescopage) ; $\sum (-1)^k\binom nk / 3^{k+1} = \frac13(2/3)^n$ (binôme) ; $\prod (-5)e^k = (-5)^{n+1} e^{n(n+1)/2}$.
4. **Bornes** : $A = \{x : x^2 - 2 \ge 0,\ |x-1| < 3\} = ]-2,-\sqrt2] \cup [\sqrt2, 4[$, donc $\sup A = 4$, $\inf A = -2$, sans max ni min ; $B = \{(-1)^n + 1/n\}$, $\max B = \sup B = 3/2$, $\inf B = -1$ non atteint (suite $u_k = -1 + 1/(2k+1)$ et passage à la limite).
5. **Racine d'une borne inférieure** : pour $A \subset \mathbb{R}_+$ borné non vide, $\inf(\sqrt A) = \sqrt{\inf A}$. Méthode : $\sqrt{\inf A}$ minore $\sqrt A$ par croissance de la racine, puis raisonnement par l'absurde avec un minorant strictement plus grand $\sqrt{\inf A} + \varepsilon$ que l'on élève au carré.

## Points à vérifier

- **Exercice 2, question 2** : le corrigé écrit $-1 \le E(x) \le 0 \Leftrightarrow -1 < x < 1$ et conclut $S_2 = ]-1, 1[$. Or $E(x) = -1$ correspond à $x \in [-1, 0[$, donc $-1$ est solution (pour $x = -1$ : $(2 \cdot (-1) + 1)^2 = 1 < 4$). L'ensemble correct est $[-1, 1[$.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Dénombrement]] (binôme), [[Récurrence]].
