---
type: concept
tags:
  - year1
  - year2
aliases:
  - subspace
  - subspaces
  - sous-espace
  - sous-espaces
  - sous-espaces vectoriels
sources:
  - "[[Chp 0d - Vector Space]]"
  - "[[chp1|chp1 (Algèbre)]]"
  - "[[chp2|chp2 (Algèbre)]]"
  - "[[chp3|chp3 (Algèbre)]]"
  - ".raw/Year 1/Contrôles.pdf"
maj: 2026-11-06
---

Partie $H$ d'un espace vectoriel qui contient le vecteur nul et qui est stable par addition et par multiplication par un scalaire. En 1re année : $F$ est un sev de $E$ si $0_E \in F$, $x + y \in F$ pour $x, y \in F$, et $\lambda x \in F$.

- Tout sous-espace est un espace vectoriel, et $\{\mathbf{0}\}$ est toujours un sous-espace.
- Dans $\mathbb{R}^3$ : un plan et une droite passant par l'origine, ainsi que le point $\{\mathbf{0}\}$. Une droite qui ne passe pas par l'origine n'en est pas un.
- $\mathbb{R}^2$ n'est pas un sous-espace de $\mathbb{R}^3$, car ses vecteurs n'ont que 2 coordonnées.
- Span$\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$ est toujours un sous-espace ([[Espace engendré]]).
- Pour deux sous-espaces $F$ et $G$ (abrégés sev) : $F \cap G$ en est un, $F \cup G$ pas forcément.
- **Dimension** : si $\dim E = n$ et $\dim F = p$, alors $p \leq n$, et $p = n$ donne $E = F$ (voir [[Dimension (algèbre linéaire)]]).
- $\mathrm{Im}(f)$, $\mathrm{Ker}(f)$ et l'ensemble des solutions d'un [[Système linéaire homogène]] sont des sev ([[chp2 (résumé)|chp2]], [[chp3 (résumé)|chp3]]).

Les évaluations 2 et 3 d'algèbre linéaire ([[Contrôles (résumé)|Contrôles]]) demandent bases et dimensions de sous-espaces de $\mathbb{R}^3$ et $\mathbb{R}^4$, une [[Base (algèbre linéaire)|base]] de $F + G$ et de $E \cap F$, et le sous-espace des polynômes de degré $\le 3$ annulés en $-1$ et $1$.

Notion parente : [[Espace vectoriel]]. Voir aussi : [[Espace engendré]], [[Sous-espaces fondamentaux]], [[Espace des colonnes]], [[Espace nul]], [[Somme directe]], [[Base (algèbre linéaire)]], [[Dimension (algèbre linéaire)]], [[Système linéaire homogène]]

## À vérifier

- [[chp1|chp1 (Algèbre)]] écrit « $p < n$ » au lieu de $p \leq n$ (le cas $p = n$ est traité juste après).
- Il écrit aussi « F\E jamais sev », sans doute pour $E \setminus F$.

Résumés : [[Chp 0d - Vector Space (résumé)]], [[chp1 (résumé)|chp1 (résumé)]], [[chp2 (résumé)|chp2 (résumé)]], [[chp3 (résumé)|chp3 (résumé)]], [[Contrôles (résumé)|Contrôles (résumé)]]
