---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TDRelations.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du corrigé TD Relations (PDF) ([[Raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TDRelations.pdf]]) (42 diapositives, TD Algèbre CY Tech, premier semestre 2025-2026), dans [[Outil Maths (index)]]. 10 exercices, dont les 8 à 10 « à faire chez soi », corrigés (sauf l'exercice 2.3, voir « Points à vérifier »). Cours : [[chp 3 - Relation binaire (résumé)]], [[Chapitre3-Relation binaire (résumé)]], [[Relation d'équivalence]], [[Relation d'ordre]].

Rappel des propriétés étudiées (voir [[Relation binaire]]) : [[Relation réflexive|réflexive]] ($\forall x,\ xRx$), [[Relation symétrique|symétrique]] ($xRy \Rightarrow yRx$), [[Relation antisymétrique|antisymétrique]] ($xRy$ et $yRx \Rightarrow x = y$), [[Relation transitive|transitive]] ($xRy$ et $yRz \Rightarrow xRz$). Équivalence = réflexive + symétrique + transitive ; ordre = réflexive + antisymétrique + transitive.

## Synthèse

| Exercice | Thème | Résultat et méthode |
|---|---|---|
| 1 | Réflexive, symétrique, transitive pour sept relations (égalité, $<$, $\leq$, même carré, même sinus, parallélisme, orthogonalité) | $<$ seulement transitive ; $\leq$ réflexive et transitive ; orthogonalité seulement symétrique ; les autres sont des équivalences |
| 2 | Six relations à étudier : classes pour une équivalence, caractère total et extrema pour un ordre | Voir ci-dessous |
| 3 | Produit de deux équivalences sur $E \times F$ | Les trois propriétés se vérifient composante par composante |
| 4 | Trois ordres : $y = x^n$ sur $\mathbb{R}_+^*$ ; ordre sur $\{(x,y) : x \leq y\}$ ; ordre induit par une application injective vers $\mathbb{R}$ | Réflexivité, antisymétrie, transitivité ; l'injectivité sert à l'antisymétrie du dernier |
| 5 | Ordre $\|x - x'\| \leq y' - y$ sur $\mathbb{R}^2$ | Transitivité par l'inégalité triangulaire ; majorants et minorants d'un point : deux demi-droites formant un « cône » ; ordre non total (points de même ordonnée) |
| 6 | Congruence modulo $n$ | Équivalence, $n$ classes, représentants $\{0, \ldots, n-1\}$, ensemble $\mathbb{Z}/n\mathbb{Z}$ ; compatible avec $+$ et $\times$ (« pour aller plus loin ») |
| 7 | Propriétés des classes : $x \in [x]$ et $x \in [y] \iff y \in [x] \iff [x] = [y] \iff [x] \cap [y] \neq \emptyset$ | Chaîne d'implications circulaire |
| 8 | « Égales à partir d'un certain rang » sur les fonctions de $\mathbb{R}$ dans $\mathbb{R}$ | Équivalence ; pas antisymétrique (fonctions différentes en 0 seulement) ; transitivité avec $A = \max(A_1, A_2)$ |
| 9 | $xSy \iff (xRy \text{ et } yRx)$ pour $R$ réflexive et transitive | $S$ est une équivalence |
| 10 | Fermeture par chemins d'une relation réflexive et symétrique | Équivalence : chemin constant, chemin renversé, chemins mis bout à bout |

## Exercice 1

**Énoncé** : les relations suivantes sont-elles symétriques, réflexives, transitives ?

| Relation | Réflexive | Symétrique | Transitive |
|---|---|---|---|
| Sur $\mathbb R$, l'égalité | oui | oui | oui |
| Sur $\mathbb R$, l'ordre strict $<$ | non | non | oui |
| Sur $\mathbb R$, l'ordre $\le$ | oui | non | oui |
| Sur $\mathbb R$, « avoir le même carré » | oui | oui | oui |
| Sur $\mathbb R$, « avoir le même sinus » | oui | oui | oui |
| Droites du plan, parallélisme | oui | oui | oui |
| Droites du plan, orthogonalité | non | oui | non |

Le corrigé donne seulement les conclusions, sans justification.

## Exercice 2

**Énoncé** : étudier les propriétés des relations suivantes. Pour une relation d'équivalence, préciser les classes. Pour une relation d'ordre, préciser si elle est totale et si l'ensemble admet un plus petit ou un plus grand élément.
1. Sur $\mathcal P(E)$ : $ARB \iff A \subset B$.
2. Sur $\mathcal P(E)$ : $ARB \iff A \cap B = \emptyset$.
3. Sur $\mathbb Z$ : $aRb \iff a$ et $b$ ont la même parité.
4. Sur $\mathbb Z$ : $aRb \iff \exists n \in \mathbb N,\ a - b = 3n$.
5. Sur $\mathbb Z$ : $aRb \iff a - b$ est divisible par 3.
6. Sur $\mathbb R$ : $xRy \iff x^2 - y^2 = x - y$.

### 2.1 Inclusion sur $\mathcal P(E)$

- Réflexive : $A \subset A$.
- Symétrique : non, $A \subset B$ n'implique pas $B \subset A$ (sauf si $A = B$).
- Antisymétrique : $A \subset B$ et $B \subset A \Rightarrow A = B$ ([[Double inclusion]]).
- Transitive : $A \subset B \subset C \Rightarrow A \subset C$.

C'est une relation d'ordre, **partiel** sauf si $E = \emptyset$ ou $E$ est un singleton : si $a \ne b$ dans $E$, $\{a\}$ et $\{b\}$ ne sont pas comparables. Plus petit élément : $\emptyset$ ; plus grand : $E$ (voir [[Inclusion (ensembles)]]).

### 2.2 $A \cap B = \emptyset$ sur $\mathcal P(E)$

- Réflexive : non, pour $A$ non vide, $A \cap A = A \ne \emptyset$.
- Symétrique : oui, $A \cap B = B \cap A$.
- Antisymétrique : non, $A \cap B = \emptyset = B \cap A$ sans que $A = B$.
- Transitive : non, $A \cap B = \emptyset$ et $B \cap C = \emptyset$ n'impliquent pas $A \cap C = \emptyset$.

Ni équivalence, ni ordre. Voir [[Ensembles disjoints]].

### 2.3 Même parité sur $\mathbb Z$

Pas de corrigé dans le document. *Complément (non donné par le TD)* : c'est une équivalence à deux classes, les pairs et les impairs (voir [[Parité d'un entier]]).

### 2.4 $a - b = 3n$ avec $n \in \mathbb N$

- Réflexive : $a - a = 0 = 3 \cdot 0$.
- Symétrique : non, si $a - b = 3n$ alors $b - a = 3(-n)$ et $-n \notin \mathbb N$ (pour $n \neq 0$).
- Antisymétrique : $a - b = 3n$ et $b - a = 3n'$ avec $n, n' \in \mathbb N$ donnent $3n = -3n'$, donc $n = -n'$ avec les deux dans $\mathbb N$, d'où $n = n' = 0$ et $a = b$.
- Transitive : $a - c = (a-b) + (b-c) = 3(n + n')$.

Relation d'ordre **partiel** : 4 et 5 ne sont pas comparables. Comme $a\,R\,(a+3)$ et $(a-3)\,R\,a$, $\mathbb Z$ n'a ni minorant ni majorant pour $R$ : pas de plus petit ni de plus grand élément.

### 2.5 $a - b$ divisible par 3

$aRb \iff \exists k \in \mathbb Z,\ a - b = 3k$ (voir [[Divisibilité]]).
- Réflexive : $a - a = 3 \cdot 0$.
- Symétrique : $b - a = 3(-k)$.
- Antisymétrique : non, par exemple $-3$ est divisible par 3 et $3$ est divisible par $-3$, mais $3 \ne -3$ (exemple du corrigé, voir « Points à vérifier »).
- Transitive : $a - c = 3(k + k')$.

Relation d'équivalence. Par la [[Division euclidienne]], tout $n = 3k + r$ avec $r \in \{0, 1, 2\}$ : **trois classes**, les multiples de 3 ($3n$), les $3n + 1$ et les $3n + 2$.

### 2.6 $x^2 - y^2 = x - y$ sur $\mathbb R$

On reformule : $xRy \iff x^2 - x = y^2 - y$. Réflexivité, symétrie et transitivité découlent alors de celles de l'égalité : c'est une relation d'équivalence.

Classe de $x$ :
$$[x] = \{y : (x-y)(x+y) - (x-y) = 0\} = \{y : (x-y)(x+y-1) = 0\} = \{x,\ 1 - x\}.$$
Deux éléments, sauf si $x = 1 - x \iff x = \frac12$ : la classe est alors $\{\frac12\}$.

## Exercice 3 (produit cartésien)

**Énoncé** : $R$ équivalence sur $E$, $S$ équivalence sur $F$. Sur $E \times F$ ([[Produit cartésien]]) :
$$(x,y) \sim (x',y') \iff xRx' \text{ et } ySy'.$$
Vérifier que $\sim$ est une relation d'équivalence.

**Corrigé** :
- Réflexive : $xRx$ et $ySy$, donc $(x,y) \sim (x,y)$.
- Symétrique : $xRx' \Rightarrow x'Rx$ et $ySy' \Rightarrow y'Sy$, donc $(x',y') \sim (x,y)$.
- Transitive : $xRx'$ et $x'Rx'' \Rightarrow xRx''$, de même pour $S$, donc $(x,y) \sim (x'',y'')$.

## Exercice 4 — trois relations d'ordre

### 4.1 $x \preccurlyeq y \iff \exists n \in \mathbb N,\ y = x^n$ sur $\mathbb R_+^*$

Montrer que c'est un ordre ; est-il total ?
- Réflexive : $x = x^1$.
- Antisymétrique : $y = x^n$ et $x = y^m$ donnent $y = y^{mn}$. Si $y = 1$, $x = 1^m = 1 = y$. Sinon $\ln y = mn \ln y$ avec $\ln y \neq 0$, donc $mn = 1$, $m = n = 1$ et $x = y$.
- Transitive : $z = y^m = (x^n)^m = x^{mn}$.

Ordre **partiel** : 2 et 3 ne sont pas comparables. Le corrigé raisonne ainsi : si $2^n = 3^m$, alors $n \ln 2 = m \ln 3$, donc $\frac{\ln 2}{\ln 3} = \frac mn$ serait rationnel, contradiction (voir l'exercice 3 de [[TD1-numbres-reels (résumé)]] et « Points à vérifier »).

### 4.2 Sur $E = \{(x,y) \in \mathbb R^2 : x \le y\}$

$$(x,y) \preccurlyeq (x',y') \iff (x,y) = (x',y') \text{ ou } y \le x'.$$
- Réflexive : $(x,y) = (x,y)$.
- Antisymétrique : on se ramène à $(x,y) = (x',y')$ ou ($y \le x'$ et $y' \le x$). Dans le second cas, avec $x \le y$ et $x' \le y'$ : $x \le y \le x' \le y' \le x$, d'où $x = x'$ et $y = y'$.
- Transitive : on développe les quatre cas. Égalité et égalité donnent l'égalité ; $(x,y) = (x',y')$ et $y' \le x''$ donnent $y = y' \le x''$ ; $(x',y') = (x'',y'')$ et $y \le x'$ donnent $y \le x' = x''$ ; $y \le x'$ et $y' \le x''$ donnent $y \le x' \le y' \le x''$. Dans tous les cas $(x,y) = (x'',y'')$ ou $y \le x''$.

### 4.3 Ordre induit par une injection

$f : E \to \mathbb R$ [[Injectivité et surjectivité|injective]], $x \preccurlyeq y \iff f(x) \le f(y)$.
- Réflexive : $f(x) \le f(x)$.
- Antisymétrique : $f(x) \le f(y)$ et $f(y) \le f(x)$ donnent $f(x) = f(y)$, donc $x = y$ par injectivité.
- Transitive : $f(x) \le f(y) \le f(z)$.

## Exercice 5 — un ordre sur $\mathbb R^2$

**Énoncé** : $(x,y) \preceq (x',y') \iff |x - x'| \le y' - y$.
1. Vérifier que c'est une relation d'ordre.
2. Dessiner les ensembles des majorants et des minorants d'un couple $(a,b)$.
3. L'ordre est-il total ?

**Corrigé** :
- Réflexive : $|x - x| = 0 \le 0 = y - y$.
- Antisymétrique : $0 \le |x - x'| \le y' - y$ et $0 \le |x' - x| \le y - y'$ donnent $y' - y = 0$, donc $y = y'$, puis $|x - x'| \le 0$, donc $x = x'$.
- Transitive : par l'[[Inégalité triangulaire]],
$$|x - x''| \le |x - x'| + |x' - x''| \le (y' - y) + (y'' - y') = y'' - y.$$

**Majorants et minorants** de $(a,b)$ : $(a,b) \preceq (x,y) \iff b - y \le x - a \le y - b$, soit
$$y \ge x + b - a \quad\text{et}\quad y \ge -x + a + b.$$
De même, $(x,y) \preceq (a,b) \iff y \le x + b - a$ et $y \le a + b - x$. Les majorants forment le « cône » au-dessus des deux droites de pente $\pm 1$ passant par $(a,b)$, les minorants le cône en dessous (voir [[Majorant et minorant]]).

![[TDRelations - p25.jpg]]
*Figure : majorants (cône bleu, au-dessus) et minorants (cône rose, en dessous) du point $(a,b)$, délimités par les droites $y = \pm(x - a) + b$.*

**Totalité** : non. Deux points de même ordonnée et d'abscisses différentes ne sont pas comparables, par exemple $(2,1)$ et $(5,1)$ : $|2 - 5| = 3 > 1 - 1 = 0$.

## Exercice 6 — congruence modulo $n$

**Énoncé** : $n > 0$ entier, sur $\mathbb Z$, $a \equiv_n b \iff n$ divise $a - b$ (aussi noté $a \equiv b \bmod n$ ou $a \equiv b\ [n]$, voir [[Congruence modulo n]]).
1. Montrer que $\equiv_n$ est une relation d'équivalence.
2. Combien de classes ? Donner un système de représentants.
3. (Pour aller plus loin) Montrer que $\equiv_n$ est compatible avec l'addition et la multiplication de $\mathbb Z$.

**Corrigé** :
1. $a \equiv_n b \iff \exists k \in \mathbb Z,\ a - b = nk$. Réflexive ($a - a = n \cdot 0$), symétrique ($b - a = n(-k)$), transitive ($a - c = n(k + k')$).
2. Par la division euclidienne, tout $m = nk + r$ avec $0 \le r \le n-1$, donc $m \equiv_n r$ pour un unique $r$. Il y a **$n$ classes** : les $nk$ (représentant 0), les $nk + 1$ (représentant 1), …, les $nk + n - 1$ (représentant $n - 1$). Système de représentants : $\{0, 1, \ldots, n-1\}$. L'ensemble des classes se note $\mathbb Z/n\mathbb Z = \{\bar 0, \bar 1, \ldots, \overline{n-1}\}$.
3. Si $a = nk + b$ et $c = nk' + d$ :
   - $a + c = n(k + k') + (b + d)$, donc $a + c \equiv_n b + d$ ;
   - $ac = n(nkk' + kd + k'b) + bd$, donc $ac \equiv_n bd$.

   L'addition et la multiplication ne dépendent donc pas du représentant choisi pour la classe.

## Exercice 7 — propriétés des classes

**Énoncé** : $R$ équivalence sur $X$, $[x]$ la classe de $x$. Montrer :
1. $\forall x \in X$, $x \in [x]$ ;
2. $\forall (x,y) \in X^2$, $x \in [y] \iff y \in [x] \iff [x] = [y] \iff [x] \cap [y] \ne \emptyset$.

**Corrigé** :
1. Par réflexivité, $xRx$, donc $x \in [x]$.
2. Il suffit de montrer la chaîne circulaire $x \in [y] \Rightarrow y \in [x] \Rightarrow [x] = [y] \Rightarrow [x] \cap [y] \ne \emptyset \Rightarrow x \in [y]$.
   - $x \in [y] \iff yRx \Rightarrow xRy$ (symétrie) $\Rightarrow y \in [x]$.
   - $y \in [x] \Rightarrow [x] = [y]$ : si $z \in [x]$, alors $xRz$ et $xRy$, donc $yRx$ et $xRz$, d'où $yRz$ : $[x] \subset [y]$. Si $z \in [y]$, $xRy$ et $yRz$ donnent $xRz$ : $[y] \subset [x]$.
   - $[x] = [y] \Rightarrow [x] \cap [y] = [x] \ni x$, non vide.
   - $z \in [x] \cap [y]$ : $yRz$ et $xRz$, donc $yRz$ et $zRx$ (symétrie), d'où $yRx$ (transitivité) : $x \in [y]$.

## Exercice 8 (à faire chez soi) — égalité « à partir d'un certain rang »

**Énoncé** : sur les applications de $\mathbb R$ dans $\mathbb R$,
$$fRg \iff \exists A > 0,\ \forall x \in \mathbb R,\ |x| > A \Rightarrow f(x) = g(x).$$
$f$ et $g$ sont en relation si elles sont égales « à partir d'un certain moment ».

**Corrigé** :
- Réflexive : n'importe quel $A > 0$ convient.
- Symétrique : $f(x) = g(x) \Rightarrow g(x) = f(x)$ pour $|x| > A$.
- Antisymétrique : non, deux fonctions qui coïncident sur $\mathbb R^*$ mais diffèrent en 0 sont en relation dans les deux sens sans être égales.
- Transitive : avec $A_1$ pour $(f,g)$ et $A_2$ pour $(g,h)$, $A = \max\{A_1, A_2\}$ donne $f(x) = g(x) = h(x)$ pour $|x| > A$.

C'est une relation d'équivalence.

## Exercice 9 (à faire chez soi)

**Énoncé** : $R$ réflexive et transitive sur $E$, $xSy \iff (xRy$ et $yRx)$. $S$ est-elle une relation d'équivalence ?

**Corrigé** : oui.
- Réflexive : $xRx$ et $xRx$.
- Symétrique : la définition est symétrique en $x$ et $y$.
- Transitive : de $(xRy$ et $yRx)$ et $(yRz$ et $zRy)$, on tire par transitivité de $R$ : $xRy$ et $yRz \Rightarrow xRz$ ; $zRy$ et $yRx \Rightarrow zRx$. Donc $xSz$.

## Exercice 10 (à faire chez soi) — fermeture par chemins

**Énoncé** : $R$ symétrique et réflexive sur $X$. On pose
$$xSy \iff \exists n \in \mathbb N,\ \exists z_0, \ldots, z_n \in X,\ z_0 = x,\ z_n = y,\ \forall\, 0 \le i \le n-1,\ z_i R z_{i+1}.$$
Montrer que $S$ est une relation d'équivalence.

**Corrigé** :
- Réflexive : $n = 1$, $z_0 = z_1 = x$ ; $xRx$ par réflexivité de $R$.
- Symétrique : chaque $z_i R z_{i+1}$ donne $z_{i+1} R z_i$ ; le chemin renversé $z'_0 = y, z'_1 = z_{n-1}, \ldots, z'_n = x$ relie $y$ à $x$.
- Transitive : un chemin $z_0 = x, \ldots, z_n = y$ et un chemin $t_0 = y, \ldots, t_m = w$ se mettent bout à bout : $z'_0 = x, \ldots, z'_n = y = t_0, z'_{n+1} = t_1, \ldots, z'_{n+m} = w$.

## Méthodes et pièges

- Pour une propriété de relation, toujours reformuler la relation sous la forme la plus simple (par exemple $x^2 - x = y^2 - y$).
- Un contre-exemple suffit pour réfuter une propriété ; pour l'antisymétrie, chercher deux éléments distincts en relation dans les deux sens.
- « $n \in \mathbb{N}$ » ou « $k \in \mathbb{Z}$ » change tout : la symétrie échoue avec $\mathbb{N}$ (exercice 2.4), elle marche avec $\mathbb{Z}$ (exercice 2.5).
- Ne pas confondre antisymétrique et « non symétrique ».

## Points à vérifier

- **Exercice 4.1, incomparabilité de 2 et 3** : la preuve montre que $2^n = 3^m$ est impossible avec $n, m$ non nuls. Ce n'est pas la même chose que d'établir $3 \neq 2^n$ et $2 \neq 3^m$, qui est ce qu'exige l'incomparabilité. Le résultat est vrai ($\log_2 3$ est irrationnel), mais l'argument écrit ne l'établit pas tel quel (complément).
- **Exercice 2, relations 4 et 5** : « pour tout $a \in \mathbb{R}$ » est une coquille, il s'agit de $a \in \mathbb{Z}$.
- **Exercice 10, symétrie** : « puisque $S$ est symétrique » doit se lire « puisque $R$ est symétrique ».
- **Exercice 2.3 (même parité)** : l'énoncé figure dans le document mais aucune diapositive ne le corrige.
- **Exercice 2.5, antisymétrie** : l'exemple « $-3$ est divisible par 3 et 3 est divisible par $-3$ » parle de divisibilité de nombres et non de couples en relation ; un contre-exemple direct serait $0\,R\,3$ et $3\,R\,0$ avec $0 \ne 3$ (complément).
- **Exercice 10, transitivité** : le corrigé écrit $t_i R y_{i+1}$ au lieu de $t_i R t_{i+1}$, et garde « $\forall\, 0 \le i \le n-1$ » pour le chemin concaténé, qui doit aller jusqu'à $n + m - 1$ (coquilles).
- **Exercice 1** : le corrigé donne les réponses sans justification ; « $\le$ est seulement réflexive et transitive » omet qu'elle est aussi antisymétrique (propriété non demandée dans l'énoncé).
