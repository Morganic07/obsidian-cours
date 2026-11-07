---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TD1-numbres-reels ([[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]) (4 pages, sans corrigé), dans [[Analyse Maths (matière)]]. TD sur les réels (PréING1, Analyse, 2020-2021), en lien avec [[Chap1-reels (résumé)]]. Le document ne donne que les énoncés : les pistes de méthode signalées « Piste » ne viennent pas du TD, sauf mention « Indication (TD) ».

## Énoncés des 19 exercices

### Exercice 1 — rationnels et décimaux

Les nombres suivants sont-ils des [[Nombre rationnel|rationnels]] ? des décimaux ?
$a = 1/3$, $b = 1/15$, $c = 1/25$, $d = 1/125$, $e = 0{,}333\ldots$, $f = \sqrt2$, $g = 0{,}123456789123\ldots$

*Piste* : un rationnel $p/q$ (forme irréductible) est décimal si et seulement si $q$ n'a que 2 et 5 comme facteurs premiers.

### Exercice 2 — développements périodiques

Trouver sous la forme $p/q$ les rationnels $x$ dont les développements décimaux périodiques sont (le chapeau marque la période) :
$$3{,}14\widehat{14}\ldots \qquad 0{,}999\ldots \qquad 3{,}149\widehat{9}\ldots$$

*Piste* : multiplier par $10^k$ ($k$ = longueur de la période) et soustraire. On trouve $0{,}999\ldots = 1$ et $3{,}1499\ldots = 3{,}15$.

### Exercice 3 — irrationalité

Montrer que $\dfrac{\ln 3}{\ln 2}$ est irrationnel.

*Piste* : [[Raisonnement par l'absurde|par l'absurde]], $\ln 3/\ln 2 = p/q$ donne $3^q = 2^p$, impossible par parité.

### Exercice 4 — ensemble défini par une inégalité

Soit $I = \left\{x \in \mathbb R^* : -2 < x + \dfrac{1}{2x} \le 2\right\}$.
1. Montrer que $I$ est la réunion de deux [[Intervalle réel|intervalles]].
2. Déterminer (s'ils existent) : les [[Majorant et minorant|majorants, les minorants]], la [[Borne supérieure|borne supérieure]], la borne inférieure, le [[Plus grand élément|plus grand élément]], le plus petit élément de $I$.

### Exercice 5

On considère l'ensemble des nombres $1 + \frac1n$, $n \in \mathbb N^*$. Est-il majoré ? minoré ? A-t-il un plus petit élément ? un plus grand élément ? Justifier.

### Exercice 6 — quantificateurs

Pour $A \subset \mathbb R$, écrire avec des [[Quantificateur|quantificateurs]] :
1. 10 est un majorant de $A$ ;
2. $m$ est un minorant de $A$ ;
3. $P$ n'est pas un majorant de $A$ ;
4. $A$ est majoré ;
5. $A$ n'est pas minoré ;
6. $A$ est borné ;
7. $A$ n'est pas borné.

*Piste* : par exemple « $A$ majoré » : $\exists M \in \mathbb R,\ \forall x \in A,\ x \le M$ ; la négation échange $\forall$ et $\exists$ et nie la dernière inégalité.

### Exercice 7 — opérations sur les parties

1. $A$ non vide et bornée, $-A = \{-x : x \in A\}$. Montrer que $-A$ est bornée et $\sup(-A) = -\inf(A)$.
2. $A, B$ non vides bornées, $A + B = \{x + y : x \in A,\ y \in B\}$. Montrer que $A+B$ est bornée et que $\sup(A+B) = \sup A + \sup B$, $\inf(A+B) = \inf A + \inf B$.
3. $A\cdot B = \{xy : x \in A,\ y \in B\}$. A-t-on toujours $\sup(A\cdot B) = \sup A \cdot \sup B$ ? Quelle hypothèse ajouter pour que ce soit vrai ?

*Piste* : non en général (par exemple avec des éléments négatifs) ; l'égalité vaut pour des parties à éléments positifs.

### Exercice 8

1. Montrer que $\forall n, m \in \mathbb N^*$, $0 < \dfrac{mn}{(m+n)^2} \le \dfrac14$.
2. En déduire que $A = \left\{\dfrac{mn}{(m+n)^2},\ n, m \in \mathbb N^*\right\}$ admet une borne supérieure et une borne inférieure, à déterminer.

*Piste* : $(m+n)^2 - 4mn = (m-n)^2 \ge 0$ ; $1/4$ est atteint pour $m = n$ ; avec $m = 1$ et $n \to \infty$ on approche 0.

### Exercice 9

$A$ non vide et bornée, $B = \{|x - y|,\ (x,y) \in A^2\}$.
1. Justifier que $B$ est majoré.
2. On note $a = \sup B$. Prouver que $a = \sup(A) - \inf(A)$.

### Exercice 10

Les ensembles suivants sont-ils majorés ? minorés ? Si oui, déterminer leurs bornes inférieure et supérieure :
$$A = \{x \in \mathbb R : x^2 < 2\},\quad B = \left\{\tfrac1n : n \in \mathbb N^*\right\},\quad C = \left\{\tfrac1n - \tfrac1p : n, p \in \mathbb N^*\right\}$$

### Exercice 11

$A$ et $B$ non vides, avec $x \le y$ pour tout $x \in A$ et tout $y \in B$. Démontrer que $\sup(A)$ et $\inf(B)$ existent et que $\sup(A) \le \inf(B)$.

### Exercice 12

$A$ et $B$ bornées. Démontrer :
1. $A \subset B \Rightarrow \sup(A) \le \sup(B)$ ;
2. $A \subset B \Rightarrow \inf(B) \le \inf(A)$ ;
3. $\sup(A \cup B) = \max(\sup A, \sup B)$ ;
4. $\inf(A \cup B) = \min(\inf A, \inf B)$ ;
5. $\sup(A \cap B) \le \min(\sup A, \sup B)$ ;
6. $\inf(A \cap B) \ge \max(\inf A, \inf B)$.

### Exercice 13

Montrer que la fonction [[Partie entière|partie entière]] est croissante.

### Exercice 14 — partie entière

On note $E(x)$ la partie entière de $x$.
1. Montrer que $\forall (x,y) \in \mathbb R^2$, $E(x) + E(y) \le E(x+y) \le E(x) + E(y) + 1$.
2. Calculer $E(x) + E(-x)$ pour tout $x \in \mathbb R$.
3. Montrer que $\forall n \in \mathbb N^*$, $\forall x \in \mathbb R$, $E(x) = E\!\left(\dfrac{E(nx)}{n}\right)$.

*Piste* : partir de $E(x) \le x < E(x) + 1$. Pour 2 : $0$ si $x \in \mathbb Z$, $-1$ sinon.

### Exercice 15

1. Démontrer que si $r \in \mathbb Q$ et $x \notin \mathbb Q$, alors $r + x \notin \mathbb Q$, et si $r \ne 0$, $r x \notin \mathbb Q$.
2. Montrer que $\sqrt2 \notin \mathbb Q$ (voir [[Irrationalité de √2]]).
3. En déduire qu'entre deux rationnels il y a toujours un irrationnel.

*Piste* : pour 3, entre $r < s$, considérer $r + \frac{s-r}{\sqrt2}$.

### Exercice 16 — écriture décimale

Tout entier $n \ge 1$ s'écrit de façon unique $n = a_0 + 10 a_1 + \ldots + 10^p a_p$, avec $a_i \in \{0,\ldots,9\}$ et $a_p \ne 0$. Déterminer $p$ en fonction de $n$.

*Piste* : $10^p \le n < 10^{p+1}$, donc $p = E(\log_{10} n)$.

### Exercice 17 — moyennes et Bernoulli

1. $0 < x \le y$. On pose $A = \dfrac{x+y}{2}$ (moyenne arithmétique), $G = \sqrt{xy}$ (moyenne géométrique), $H = \dfrac{1}{\frac12\left(\frac1x + \frac1y\right)}$ (moyenne harmonique). Montrer que
$$x \le H \le G \le A \le y$$
([[Inégalité arithmético-géométrique]]).
2. $a \ge 0$, $n \in \mathbb N$. Montrer l'[[Inégalité de Bernoulli]] $(1+a)^n \ge 1 + na$.

*Piste* : $(\sqrt x - \sqrt y)^2 \ge 0$ pour $G \le A$ ; [[Récurrence]] pour Bernoulli.

### Exercice 18 — Cauchy-Schwarz

Soit $n \in \mathbb N^*$, $a_1,\ldots,a_n, b_1,\ldots,b_n \in \mathbb R$. Montrer que
$$\sum_{k=1}^n a_k b_k \le \sqrt{\sum_{k=1}^n a_k^2}\ \sqrt{\sum_{k=1}^n b_k^2}.$$
**Indication (TD)** : considérer le polynôme $f(x) = \sum_{k=1}^n (a_k + b_k x)^2$.

*Piste* : $f \ge 0$ sur $\mathbb R$, donc son discriminant est négatif ou nul (voir [[Inégalité de Cauchy-Schwarz]], [[Produit scalaire]]).

### Exercice 19 — identité d'Hermite

But : montrer que $\forall n \in \mathbb N^*$, $\forall x \in \mathbb R$,
$$\sum_{k=0}^{n-1} E\!\left(x + \frac kn\right) = E(nx)$$
([[Identité d'Hermite]]).
1. Soit $f(x) = \sum_{k=0}^{n-1} E\!\left(x + \frac kn\right) - E(nx)$. Montrer que $f$ est [[Fonction périodique|périodique]] de période $\frac1n$.
2. Montrer que $f(x) = 0$ pour tout $x \in [0, \frac1n[$, et conclure.

## À retenir

Pour prouver $\sup A = s$, vérifier deux choses : $s$ majore $A$, et tout réel $y < s$ n'est pas un majorant (voir [[Borne supérieure]]). Les exercices 7, 11 et 12 servent de lemmes pour la suite du cours.

## Points à vérifier

- L'énoncé de l'exercice 18 s'intitule « Cauchy-Schwartz » (orthographe du document ; le nom usuel est Cauchy-Schwarz) et l'exercice 19 contient la coquille « prériode ».
- Exercice 17 : le TD appelle « inégalité arithmético-géométrique » toute la chaîne $x \le H \le G \le A \le y$.

## Liens

[[Borne supérieure]], [[Relation d'ordre]], [[Récurrence]], [[Produit scalaire]] (Cauchy-Schwarz), [[Chap1-reels (résumé)]].
