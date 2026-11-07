---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]"]
maj: 2026-11-07
complet: true
---

Résumé de Chap1-reels ([[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]) (PDF de 6 pages, « Chapitre 1 : L'ensemble $\mathbb{R}$ »), dans [[Cours/Mathématiques/Analyse Maths/_index|Analyse Maths]]. Scan sans texte (assemblage de captures de plusieurs documents), lu en image. Le document ne contient aucune figure : tout est recopié en texte ci-dessous.

## I. Ensembles de nombres

On utilise les notations classiques des [[Ensembles de nombres|ensembles emboîtés]] $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$.

| Notation | Ensemble | Exemples |
|---|---|---|
| $\mathbb{N}$ | Entiers naturels | $0, 1, 2, 3, \dots$ |
| $\mathbb{Z}$ | Entiers relatifs | $-2, -1, 0, 1, 2, \dots$ |
| $\mathbb{Q}$ | Rationnels | $1.2,\ 1/2,\ 0.0012,\ \frac{355}{113}, \dots$ |
| $\mathbb{R}$ | Réels | $\sqrt{2},\ \pi,\ e, \dots$ |
| $\mathbb{C}$ | Complexes | $1 + 2i,\ 1 + i\sqrt{3},\ 2e^{i\pi/3}, \dots$ |

On peut y ajouter l'ensemble $\mathbb{D}$ des **nombres décimaux** :
$$\mathbb{D} = \left\{ \frac{m}{10^p},\ m \in \mathbb{Z},\ p \in \mathbb{N} \right\}$$
ce sont les nombres dont l'écriture décimale comporte un nombre fini de chiffres, et $\mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q}$. Exemples : $1{,}234 = 1234 \times 10^{-3} = \frac{1234}{1000}$ ; $0{,}00345 = 345 \times 10^{-5} = \frac{345}{100\,000}$.

> **Proposition 1.** Un nombre est [[Nombre rationnel|rationnel]] si et seulement s'il admet une écriture décimale périodique ou finie.

Exemples : $\frac{3}{5} = 0{,}6$ ; $\frac{1}{3} = 0{,}3333\ldots$ ; $1{,}179\,325\,325\,325\ldots$

### Méthode : montrer qu'un développement périodique est rationnel

Exemple : $x = 12{,}34\,2021\,2021\ldots$

1. Faire apparaître la partie périodique juste après la virgule. La période commence deux chiffres après la virgule, donc on multiplie par 100 :
$$100x = 1234{,}2021\,2021\ldots \quad (1)$$
2. Décaler de la longueur d'une période (4 chiffres), donc multiplier encore par $10\,000$ :
$$10\,000 \times 100x = 12\,342\,021{,}2021\ldots \quad (2)$$
3. Les parties décimales de (1) et (2) sont les mêmes ; on fait (2) − (1) :
$$10\,000 \times 100x - 100x = 12\,342\,021 - 1234$$
donc $999\,900\,x = 12\,340\,787$ et
$$x = \frac{12\,340\,787}{999\,900} \in \mathbb{Q}.$$

### Propriétés de $\mathbb{R}$

1. $\mathbb{R}$ est un [[Corps (algèbre)|corps]] : l'addition et la multiplication ont toutes les propriétés « sympathiques » que l'on peut espérer.
2. Il contient l'ensemble des rationnels : $\mathbb{Q} \subset \mathbb{R}$.
3. La relation d'ordre $\le$ y est totale et compatible avec l'addition et la multiplication.
4. La plus importante est la propriété de la borne supérieure (partie III).

## II. Relation d'ordre

Voir [[Relation d'ordre]] et [[Majorant et minorant]].

### 1.1 Majorants et minorants d'une partie de $\mathbb{R}$

> **Définition.**
> - $A$ est **majorée** si $\exists M \in \mathbb{R},\ \forall a \in A,\ a \le M$. Un tel $M$ est appelé **un** majorant de $A$ ; on dit que $A$ est majorée par $M$, ou que $M$ majore $A$.
> - $A$ est **minorée** si $\exists m \in \mathbb{R},\ \forall a \in A,\ m \le a$. Un tel $m$ est **un** minorant de $A$.
> - $A$ est **bornée** si elle est à la fois majorée et minorée, c'est-à-dire si $\exists K \ge 0,\ \forall a \in A,\ |a| \le K$.

**Attention !** On ne parle jamais « du » majorant d'une partie majorée de $\mathbb{R}$, mais toujours d'**un** majorant : une telle partie en possède toujours plein. Si $M$ est un majorant, tout réel supérieur en est aussi un.

**Exemple.** L'intervalle $]-\infty, 1]$ est majoré par 1, mais aussi par $\sqrt{2}$, 10, $e^{100}$… Il n'est pas minoré.

### 1.2 Plus grand et plus petit élément d'une partie de $\mathbb{R}$

Voir [[Plus grand élément]].

> **Définition.**
> - On appelle **plus grand élément** de $A$, ou **maximum** de $A$, tout élément de $A$ qui majore $A$.
> - On appelle **plus petit élément** de $A$, ou **minimum** de $A$, tout élément de $A$ qui minore $A$.

> **Théorème (unicité du plus grand/petit élément).** Si $A$ possède un plus grand (resp. petit) élément, celui-ci est unique. On peut donc l'appeler **le** plus grand (resp. petit) élément de $A$, noté $\max A$ (resp. $\min A$).

**Attention !** Le plus grand/petit élément est unique… **s'il existe** !

*Démonstration.* Soient $M, M'$ deux plus grands éléments de $A$. Alors $M' \le M$ car $M$ majore $A$ et $M' \in A$, et de même $M \le M'$. Donc $M = M'$.

> **Théorème (deux propriétés de $\mathbb{N}$).**
> (i) Toute partie non vide de $\mathbb{N}$ possède un plus petit élément.
> (ii) Toute partie non vide majorée de $\mathbb{N}$ possède un plus grand élément.

*Démonstration.*

(i) Soit $A$ une partie de $\mathbb{N}$. Supposons par contraposition que $A$ n'a pas de plus petit élément : aucun élément de $A$ ne peut alors minorer $A$. On montre par [[Récurrence|récurrence]] que $A$ est minorée par $n$ pour tout $n \in \mathbb{N}$ ; il en découle que $A$ est vide.

- *Initialisation* : $A$ est minorée par 0, car toute partie de $\mathbb{N}$ l'est.
- *Hérédité* : soit $n \in \mathbb{N}$, supposons $A$ minorée par $n$. Comme $A$ n'a pas de plus petit élément, $n \notin A$, donc $a > n$ pour tout $a \in A$. Comme on travaille avec des **entiers**, $a \ge n + 1$ pour tout $a \in A$ : $A$ est minorée par $n + 1$.

(ii) Soit $A$ une partie non vide majorée de $\mathbb{N}$. L'ensemble $\mathcal{M}$ des majorants **entiers** de $A$ est non vide, donc possède un plus petit élément $m$ d'après (i).

- Si $m = 0$ : $a \le m = 0$ pour tout $a \in A$, et comme $a \in \mathbb{N}$, $a = 0$. $A$ étant non vide, $A = \{0\}$, qui admet 0 pour plus grand élément.
- Si $m \ne 0$ : $m - 1 \in \mathbb{N}$. Comme $m = \min \mathcal{M}$, $m - 1$ ne majore pas $A$, donc $m - 1 < a$ pour un certain $a \in A$. Par l'**inégalité d'entiers**, $m - 1 < a \le m$ est en fait une **égalité** : $m = a$, donc $m \in A$. Ainsi $m$ est un élément de $A$ qui majore $A$ : c'est le plus grand élément.

## III. Propriété de la borne supérieure

Voir [[Borne supérieure]].

### 2.1 Définition

$[0, 1[$ n'a pas de plus grand élément, pourtant 1 est « quelque chose de cet ordre ». Ce qui rend 1 si particulier pour $[0, 1[$, c'est que 1 n'est pas n'importe quel majorant : c'est le meilleur majorant, le plus petit possible.

> **Définition (borne supérieure/inférieure d'une partie de $\mathbb{R}$).**
> - **S'il existe**, le plus petit majorant de $A$ est appelé **la borne supérieure** de $A$, notée $\sup A$.
> - **S'il existe**, le plus grand minorant de $A$ est appelé **la borne inférieure** de $A$, notée $\inf A$.

- Différence essentielle avec le plus grand élément : la borne supérieure, quand elle existe, n'appartient pas forcément à l'ensemble considéré.
- Elle n'existe pas toujours, mais quand elle existe elle est unique (en tant que plus petit élément), d'où l'article « la » et la notation.

**Exemple : $[0, 1[$ admet 1 pour borne supérieure.**

*Démonstration.* 1 majore $[0, 1[$ ; reste à montrer qu'aucun réel $x < 1$ ne le majore.

- Si $x < 0$ : comme $0 \in [0, 1[$, $x$ ne majore pas $[0, 1[$.
- Si $x \in [0, 1[$ : $x < \frac{x+1}{2}$ et pourtant $\frac{x+1}{2} \in [0, 1[$, donc $x$ ne majore pas $[0, 1[$.

En résumé, $[0, 1[$ possède une borne supérieure mais **pas** de plus grand élément. Inversement, une partie de $\mathbb{R}$ ne peut pas posséder un plus grand élément sans borne supérieure :

> **Théorème (max/min implique sup/inf).** Si $A$ possède un plus grand (resp. petit) élément, $A$ possède une borne supérieure (resp. inférieure) et $\sup A = \max A$ (resp. $\inf A = \min A$).

*Démonstration.* Il faut montrer que l'ensemble $\mathcal{M}$ des majorants de $A$ a pour plus petit élément $\max A$. Deux choses à vérifier :

- $\max A \in \mathcal{M}$ : par définition, $\max A$ majore $A$ ;
- $\max A$ minore $\mathcal{M}$ : par définition, $\max A \in A$, donc tout majorant de $A$ est $\ge \max A$.

### 2.2 Propriété de la borne supérieure/inférieure

Le résultat qui suit est **une propriété essentielle de l'ensemble des réels**. Sa démonstration dépend de la façon dont on construit $\mathbb{R}$ à partir de $\mathbb{Q}$ ; elle est admise. **Toute l'analyse est dans ce théorème** : on en déduit tous les grands théorèmes d'analyse du programme de MPSI, à savoir [[Théorème de la limite monotone|limite monotone]], [[Suites adjacentes|suites adjacentes]], [[Théorème de Bolzano-Weierstrass|Bolzano-Weierstrass]], [[Théorème des valeurs intermédiaires|valeurs intermédiaires]], [[Théorème des bornes atteintes|bornes atteintes]], [[Théorème de Rolle|Rolle]], [[Inégalité des accroissements finis|accroissements finis]], théorème de Heine et construction de l'[[Intégrale|intégrale]].

> **Théorème (propriété de la borne supérieure/inférieure).**
> - Toute partie non vide majorée de $\mathbb{R}$ possède une borne supérieure.
> - Toute partie non vide minorée de $\mathbb{R}$ possède une borne inférieure.

> **Proposition 5 (caractérisation de la borne supérieure).** Soit $A$ une partie non vide et majorée de $\mathbb{R}$. La borne supérieure de $A$ est l'unique réel $\sup A$ tel que
> (i) si $x \in A$, alors $x \le \sup A$ ;
> (ii) pour tout $y < \sup A$, il existe $x \in A$ tel que $y < x$.

*Démonstration.*

1. $\sup A$ vérifie ces propriétés. C'est un majorant, d'où (i). Pour (ii), soit $y < \sup A$ : comme $\sup A$ est le plus petit des majorants, $y$ n'est pas un majorant de $A$, donc il existe $x \in A$ tel que $y < x$.
2. Réciproquement, si $\alpha$ vérifie (i) et (ii), c'est $\sup A$. Par (i), $\alpha$ majore $A$. Supposons [[Raisonnement par l'absurde|par l'absurde]] que $\alpha$ n'est pas le plus petit des majorants : il existe un majorant $y < \alpha$. Par (ii), il existe $x \in A$ tel que $y < x$, ce qui contredit le fait que $y$ majore $A$. Donc $\alpha = \sup A$.

> **Proposition 6.** Soit $A$ une partie non vide et majorée de $\mathbb{R}$. La borne supérieure de $A$ est l'unique réel $\sup A$ tel que
> (i) $\sup A$ est un majorant de $A$ ;
> (ii) il existe une suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $A$ qui converge vers $\sup A$.

(Caractérisation séquentielle, « anticipée sur la suite » : voir [[Convergence d'une suite]].)

## IV. $\mathbb{R}$ est archimédien, partie entière, approximation décimale

> **Propriété (R3, [[Propriété d'Archimède|propriété d'Archimède]]).** $\mathbb{R}$ est archimédien :
> $$\forall x \in \mathbb{R}\ \exists n \in \mathbb{N}\ \ n > x$$
> « Pour tout réel $x$, il existe un entier naturel $n$ strictement plus grand que $x$. »

Cette propriété semble évidente mais elle est essentielle : elle permet de définir la partie entière.

> **Proposition 3.** Soit $x \in \mathbb{R}$. Il **existe un unique** entier relatif, la **[[Partie entière|partie entière]]** notée $E(x)$, tel que
> $$E(x) \le x < E(x) + 1.$$

**Exemple 1.** $E(2{,}853) = 2$, $E(\pi) = 3$, $E(-3{,}5) = -4$ ; $E(x) = 3 \iff 3 \le x < 4$.

*Démonstration.*

- **Existence.** Supposons $x \ge 0$. Par la propriété d'Archimède, il existe $n \in \mathbb{N}$ tel que $n > x$. L'ensemble $K = \{k \in \mathbb{N} \mid k \le x\}$ est fini (pour tout $k \in K$, $0 \le k < n$). Il admet un plus grand élément $k_{\max} = \max K$. Alors $k_{\max} \le x$ car $k_{\max} \in K$, et $k_{\max} + 1 > x$ car $k_{\max} + 1 \notin K$. Donc $k_{\max} \le x < k_{\max} + 1$ et $E(x) = k_{\max}$.
- **Unicité.** Si $k$ et $\ell$ sont deux entiers vérifiant $k \le x < k + 1$ et $\ell \le x < \ell + 1$, alors $k \le x < \ell + 1$, donc $k < \ell + 1$. En échangeant les rôles, $\ell < k + 1$. Donc $\ell - 1 < k < \ell + 1$, et le seul entier strictement entre $\ell - 1$ et $\ell + 1$ est $\ell$ : $k = \ell$.

> **Définition 1.** Les **nombres décimaux** sont les nombres de la forme $\frac{n}{10^p}$, $(n, p) \in \mathbb{Z} \times \mathbb{N}$.

Autrement dit, un réel $x$ est décimal si et seulement s'il existe un entier naturel $p$ tel que $10^p x$ soit un entier relatif.

> **Théorème 3 ([[Approximation décimale|approximation décimale]]).** Soit $x$ un réel. Pour tout entier naturel $p$, il existe un et un seul entier relatif $n_p$ tel que
> $$\frac{n_p}{10^p} \le x < \frac{n_p}{10^p} + \frac{1}{10^p}.$$
> Le décimal $d_p = \frac{n_p}{10^p}$ est l'**approximation décimale de $x$ à $10^{-p}$ par défaut**, et $d_p + \frac{1}{10^p}$ l'**approximation décimale de $x$ à $10^{-p}$ par excès**.

*Démonstration.* Soit $p \in \mathbb{N}$ et $n \in \mathbb{Z}$ :
$$\frac{n}{10^p} \le x < \frac{n}{10^p} + \frac{1}{10^p} \iff n \le 10^p x < n + 1 \iff n = E(10^p x).$$

Ainsi, l'approximation décimale à $10^{-p}$ près par défaut de $x$ est $\frac{E(10^p x)}{10^p}$. Exemple : puisque $3{,}14159 \le \pi < 3{,}14160$, l'approximation décimale à $10^{-5}$ près par défaut de $\pi$ est $3{,}14159$.

## V. Intervalles de $\mathbb{R}$

La définition suivante décrit tous les intervalles de $\mathbb{R}$ (fermés, ouverts, majorés, minorés…). Voir [[Intervalle réel]].

> **Définition 3.1 (intervalle de $\mathbb{R}$).** On appelle **intervalle** de $\mathbb{R}$ toute partie $I$ de $\mathbb{R}$ vérifiant :
> $$\forall (x, y) \in I^2,\ \forall t \in \mathbb{R},\ x \le t \le y \implies t \in I.$$

> **Proposition 3.1.** Une intersection d'intervalles est un intervalle.

> **Proposition 3.2.** Les intervalles de $\mathbb{R}$ sont les ensembles du type $[a, b]$, $[a, b[$, $]a, b]$ ou $]a, b[$ avec $a, b \in \mathbb{R}$, $a \le b$, et éventuellement $a = -\infty$ ou $b = +\infty$ en position de « borne ouverte ».

**Remarque.** On retrouve donc bien tous les intervalles au sens précédent. L'ensemble vide est un intervalle ouvert de $\mathbb{R}$, puisqu'il est du type $]a, a[$ avec $a \in \mathbb{R}$.

## VI. Densité de $\mathbb{Q}$ dans $\mathbb{R}$

Le théorème suivant montre que $\mathbb{Q}$ et l'ensemble $\mathbb{R} \setminus \mathbb{Q}$ des irrationnels sont enlacés l'un à l'autre « comme deux peignes imbriqués ». Voir [[Densité de ℚ dans ℝ]].

> **Théorème.** Entre deux réels distincts, il existe toujours une infinité de rationnels et une infinité d'irrationnels.

*Démonstration.* Soient $x < y$ deux réels. Comme $y - x > 0$, on peut toujours trouver un entier naturel $n$ tel que
$$10^{-n} < y - x \iff 10^n > \frac{1}{y - x} \iff n \ln(10) > -\ln(y - x) \iff n > \frac{-\ln(y - x)}{\ln(10)}.$$
Notons $r = d_n + 10^{-n}$, avec $d_n$ l'approximation décimale de $x$ à $10^{-n}$ près par défaut. $r$ est rationnel car $d_n + 10^{-n} \in \mathbb{D} \subset \mathbb{Q}$.

- On sait que $d_n \le x < d_n + 10^{-n} = r$.
- De plus, $r = d_n + 10^{-n} \le x + 10^{-n} < x + (y - x) = y$.

On a donc bien $x < r < y$ avec $r \in \mathbb{Q}$.

## Liens

[[Relation d'ordre]], [[Borne supérieure]], [[Récurrence]] (preuves sur $\mathbb{N}$). Les théorèmes cités comme conséquences servent dans [[Limite et continuité]], [[Dérivabilité]] et [[Intégrale]].

## Erreurs du cours

- [[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]] conclut la preuve de densité par « On a donc bien : $x < r < y$ et $y \in \mathbb{Q}$ » ; il faut « $r \in \mathbb{Q}$ » (forme reprise dans cette fiche).
