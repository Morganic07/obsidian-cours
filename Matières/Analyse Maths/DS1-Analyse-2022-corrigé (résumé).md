---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé]] (7 pages, texte), dans [[Analyse Maths (matière)]]. Devoir surveillé n° 1 d'Analyse I (PréING1), 1 h 30, sans appareil électronique, 6 exercices. Le barème est sur 24 points. Il porte sur [[Chap0-Rappels-etc (résumé)]] et [[Chap1-reels (résumé)]]. Voir aussi [[DS1-correction-2021 (résumé)]] pour la version précédente, de même forme.

## Les 6 exercices et leurs méthodes

1. **Équations trigonométriques** (4 pts) : $\tan x = 2\sin x$ et $\cos x + \sin x = 1 + \tan x$. Méthode : donner d'abord l'ensemble de définition ($x \ne \pi/2 + k\pi$), puis se ramener à $\sin a = \sin b$ ou à une factorisation $(\cos x - 1)(\cos x + \sin x) = 0$. Solutions : $\{2k\pi,\ \pi/3 + 2k\pi/3\}$ et $\{2k\pi,\ -\pi/4 + k\pi\}$.
2. **Partie entière** (4 pts) : démontrer $E(-x) = -E(x) - 1$ si $x \notin \mathbb{Z}$, et $E(2x) = 2E(x)$ ou $2E(x)+1$ selon que la partie fractionnaire est $< 1/2$ ou $\ge 1/2$ ; résoudre $E(2x) = 5 + E(-x)$. Méthode : distinguer trois cas (entier, partie fractionnaire $< 1/2$, $\ge 1/2$), poser $E(x)$ comme inconnue entière. Solution : $[3/2, 2[$.
3. **Inéquations** (4 pts) : $|x-1| \le |2x+1| + 1$ (cas selon le signe de $2x+1$) et $\sqrt{|x+2|} \le |x-4|$ (élever au carré). Solutions : $]-\infty,-1] \cup [-1/3,+\infty[$ et $]-\infty,2] \cup [7,+\infty[$.
4. **Sommes et produits** (4 pts) : $\sum (1/k - 1/(n+1-k)) = 0$ (changement d'indice $j = n+1-k$), $\sum (-1)^k\binom nk / 2^{2k+1} = 3^n/2^{2n+1}$ (binôme), $\prod_{k=2}^n (1 - 1/k^2) = (n+1)/(2n)$ (télescopage après $k^2 - 1 = (k-1)(k+1)$).
5. **Bornes d'ensembles** (6 pts) : pour $A = \{x \ne 1 : \frac{2}{x-1} \le 2x-5 < 11\}$ et $B = \{(-1)^n/n + 2/n\}$, dire s'ils sont majorés, minorés, puis donner sup, inf, max, min. Méthode : tableau de signe pour écrire $A = [1/2, 1[\,\cup [3, 8[$ ; pour $B$ séparer $n$ pair et impair, puis trouver l'inf par passage à la limite. Résultats : $\sup A = 8$ (sans maximum), $\min A = 1/2$ ; $\max B = \sup B = 3/2$, $\inf B = 0$ non atteint.
6. **Sup d'un translaté** (3 pts) : $\sup(x + A) = x + \sup A$. Méthode : double inégalité, avec la définition du sup comme plus petit majorant.

## Pièges et points de méthode

- Toujours donner l'ensemble de définition avant de transformer une équation avec $\tan$ ou une fraction.
- Un $\sup$ qui n'appartient pas à l'ensemble n'est pas un maximum (cas de $A$ avec $8$ et de $B$ avec $0$).
- Pour un inf non atteint, la preuve classique est : un minorant évident (ici $0$), puis une suite d'éléments de l'ensemble qui tend vers lui. Voir [[Borne supérieure]].

## Points à vérifier

Coquilles du corrigé, sans effet sur les résultats :
- Ex. 6 : l'énoncé écrit $x + A = \{x + a : x \in A\}$ au lieu de $a \in A$, et la dernière ligne écrit $\sup(A+B)$ au lieu de $\sup(A+x)$.
- Ex. 5 : la phrase « $A$ est majorée par tout réel supérieur ou égal à $8$ » est correcte, mais l'écriture de $A$ dans le texte extrait a perdu un crochet : l'ensemble est bien $[1/2, 1[ \cup [3, 8[$, ce qui est cohérent avec $\min A = 1/2$.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Récurrence]], [[Dénombrement]] (binôme).
