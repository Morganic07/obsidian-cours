---
type: source
tags: [year3]
sources: ["[[Chp4 - Series of functions]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp4 - Series of functions]], dans [[Séries (matière)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Les énoncés en image sont recopiés en texte ; seul le schéma des modes de convergence est intégré.

## Idée générale

Une série de fonctions est la suite de ses sommes partielles : on applique les résultats sur les séries numériques (en fixant $x$) et ceux de [[Chp3 - Sequence of function (résumé)|la convergence uniforme]]. Voir [[Convergence uniforme]] et [[Série numérique]].

## Définition d'une série de fonctions

**Définition.** Soit $(f_n)$ une suite de fonctions définies sur $X \subset \mathbb{R}$. La suite des sommes partielles $(S_n)$ est définie par
$$\forall x \in X,\ S_n(x) = \sum_{k=0}^{n} f_k(x).$$
La série de fonctions, notée $\sum_{n\in\mathbb{N}} f_n$ (ou $\sum_{n\ge n_0} f_n$ si elle commence à $n_0$), est la suite des sommes partielles.

## Convergence simple

**Définition.** $\sum f_n$ converge simplement sur $X$ si la suite de fonctions $(S_n)$ converge simplement sur $X$. Sa limite simple est la **somme** de la série :
$$\forall x \in X,\ S(x) = \left(\sum_{n=0}^{+\infty} f_n\right)(x) = \lim_{n\to+\infty} S_n(x) = \lim_{n\to+\infty} \sum_{k=0}^{n} f_k(x).$$
Sinon, la série est divergente.

**Remarques.**
- Pour étudier la convergence simple, on fixe $x$ : on obtient une série numérique, à laquelle s'appliquent toutes les méthodes du chapitre sur les séries numériques ([[Chp1 - Convergent, divergent and positive terms SERIES (résumé)|chapitre 1]], [[Chp2 - Alternating and absolutly convergent series (résumé)|chapitre 2]]).
- Les sommes partielles sont des suites de fonctions : on étudie donc aussi plusieurs types de convergence et des théorèmes d'interversion.
- Ce chapitre utilise donc les définitions, propriétés et théorèmes des deux chapitres précédents.

## Reste d'une série simplement convergente

**Définition.** Si $\sum f_n$ converge simplement vers $S$ sur $X$, le $n$-ième reste est
$$R_n = S - S_n = \sum_{k\ge n+1} f_k, \qquad R_n(x) = S(x) - S_n(x) = \sum_{k\ge n+1} f_k(x).$$
Voir [[Reste d'une série]].

**Proposition.** $(R_n)$ converge simplement vers la fonction nulle.

## Convergence uniforme

**Définition.** $\sum f_n$ converge uniformément sur $X$ si la suite $(S_n)$ converge uniformément sur $X$.

**Proposition.** $\sum f_n$ converge uniformément sur $X$ si et seulement si elle converge simplement sur $X$ **et** la suite des restes $(R_n)$ converge uniformément vers la fonction nulle sur $X$.

**Proposition.** Si $\sum f_n$ converge uniformément sur $X$, alors $(f_n)$ converge uniformément vers la fonction nulle sur $X$.

**Corollaire.** Si $f_n = S_n - S_{n-1}$ ne converge pas uniformément vers 0 sur $X$, alors $\sum f_n$ ne converge pas uniformément sur $X$.
Preuve : contraposée de la proposition précédente.

## Convergence normale

**Définition.** $\sum f_n$ converge normalement sur $X$ si chaque $f_n$ est bornée sur $X$ et si la série numérique $\sum \|f_n\|_\infty$ converge.

**Proposition (critère de Weierstrass, *Weierstrass M-test*) — condition suffisante.** S'il existe une série numérique convergente à termes positifs $\sum a_n$ telle que
$$\forall n,\ \|f_n\|_\infty \le a_n,$$
alors $\sum f_n$ converge normalement sur $X$.

## Convergence absolue

**Définition.** $\sum f_n$ est absolument convergente sur $X$ si, pour tout $x \in X$, la série numérique $\sum f_n(x)$ est absolument convergente, c'est-à-dire si $\sum |f_n(x)|$ converge.

La convergence absolue implique la convergence simple.

## Relations entre les modes de convergence

**Théorème.** Si $\sum f_n$ converge normalement sur $X$, elle converge uniformément, absolument et simplement.

![[Chp4 - Series of functions - image17.png]]

*Figure : la convergence normale implique la convergence uniforme et la convergence absolue, qui impliquent chacune la convergence simple.*

$$\text{normale} \Rightarrow \text{uniforme} \Rightarrow \text{simple}, \qquad \text{normale} \Rightarrow \text{absolue} \Rightarrow \text{simple}.$$

## Interversion somme-limite

**Théorème.** Soit $a$ un [[Point limite]] de $X$. On suppose :
- pour tout $n$, il existe $\ell_n \in \mathbb{R}$ tel que $\lim_{x\to a} f_n(x) = \ell_n$ ;
- $\sum f_n$ converge uniformément sur $X$ vers $S$.

Alors $\sum \ell_n$ converge et $\lim_{x\to a} S(x) = \sum_{n=0}^{+\infty} \ell_n$, soit
$$\lim_{x\to a}\left(\sum_{n=0}^{+\infty} f_n(x)\right) = \sum_{n=0}^{+\infty} \lim_{x\to a} f_n(x).$$
Voir [[Interversion de limites]].

## Continuité en un point et sur un ensemble

**Corollaire.** Soit $x_0 \in X$. Si chaque $f_n$ est continue en $x_0$ et si $\sum f_n$ converge uniformément sur $X$, alors $S = \sum_{n=0}^{+\infty} f_n$ est continue en $x_0$.

**Corollaire.** Si chaque $f_n$ est continue sur $X$ et si $\sum f_n$ converge uniformément sur $X$, alors $S$ est continue sur $X$.

## Interversion somme-intégrale et somme-dérivée

**Théorème (intégration terme à terme).** Soient $a < b$ et des $f_n$ définies sur $[a, b]$. Si
1. chaque $f_n$ est continue sur $[a, b]$,
2. $\sum f_n$ converge uniformément sur $[a, b]$,

alors $S$ est continue sur $[a, b]$, la série $\sum \int_a^b f_n$ converge vers $\int_a^b S$, et
$$\sum_{n=0}^{+\infty} \int_a^b f_n(t)\,dt = \int_a^b \sum_{n=0}^{+\infty} f_n(t)\,dt.$$

**Théorème (dérivation terme à terme).** Soit $(f_n)$ une suite de fonctions dérivables sur un intervalle **borné** $I$, telle que
1. il existe $x_0 \in I$ tel que $\sum f_n(x_0)$ converge,
2. $\sum f_n'$ converge uniformément sur $I$.

Alors $\sum f_n$ converge uniformément sur $I$ vers une fonction $S$ dérivable, et
$$S' = \left(\sum f_n\right)' = \sum f_n'.$$

**Théorème (version $\mathcal{C}^1$).** Mêmes hypothèses avec des $f_n$ de [[Fonction de classe Ck|classe $\mathcal{C}^1$]] : $\sum f_n$ converge uniformément sur $I$ vers une fonction $S$ de classe $\mathcal{C}^1$, et $S' = \sum f_n'$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition des sommes partielles** : « $\forall s \in X$ » au lieu de $x$ et $\sum f_n$ au lieu de $f_k$ (alerte confirmée, coquilles). La dernière phrase de la définition de la convergence simple écrit $\sum_{n\in\mathbb{N}}$ sans terme.
2. **Schéma des convergences** : il ne dit pas que les implications inverses sont fausses (uniforme n'implique pas absolue, ni l'inverse). Le cours ne les justifie pas ici.
3. **Hypothèse « intervalle borné »** pour la dérivation terme à terme : demandée ici, absente du chapitre 3 pour les suites ; sans conséquence pour la logique du chapitre.
4. **« The the », « does not converges »** : fautes d'anglais répétées, sans enjeu.
5. **Notation $\sum_{n\in\mathbb{N}} (f_n)_{n\in\mathbb{N}}$** dans les théorèmes d'interversion, et « converges uniformly $[a,b]$ » sans « on » : coquilles de notation, lues ici comme $\sum f_n$ (alerte de la transcription).
6. **Notation de départ** : la définition écrit $\sum_{n\ge n_0} f_k$ pour une série commençant à $n_0$ ; lire $f_n$ (coquille).
