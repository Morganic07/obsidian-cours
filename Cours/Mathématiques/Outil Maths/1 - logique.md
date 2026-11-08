---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 1 logique .docx|Chapitre 1 logique]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 1 logique .docx|Chapitre 1 logique]] (séance du 07/10/23), dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]. Les images de la note ne contiennent que des tables, des définitions et des formules : leur contenu est recopié ci-dessous, sans les intégrer. Les passages ajoutés finissent par ⓘ.

## Idée générale

Le chapitre pose le langage des propositions (connecteurs, tables de vérité, équivalences, arguments, quantificateurs) puis les grands types de preuve, illustrés par des théorèmes d'arithmétique. Voir [[Logique propositionnelle]].

## 1. Interprétations et tables de vérité

**Nombre d'interprétations** : avec $n$ variables propositionnelles, il y a $2^n$ interprétations possibles (lignes de la table de vérité).

Tables de vérité des connecteurs (V = vrai, F = faux) :

| $p$ | $q$ | $\neg p$ | $p \wedge q$ | $p \vee q$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ |
|---|---|---|---|---|---|---|
| V | V | F | V | V | V | V |
| V | F | F | F | V | F | F |
| F | V | V | F | V | V | F |
| F | F | V | F | F | V | V |

Le « ou » logique est **inclusif** : $p \vee q$ est vrai aussi quand $p$ et $q$ sont vraies toutes les deux. Le « ou » du langage courant (« fromage ou dessert ») est souvent **exclusif** : c'est un autre connecteur, le [[Ou exclusif|ou exclusif]] (XOR), noté $p \oplus q$, vrai quand exactement une des deux propositions est vraie : $p \oplus q \equiv (p \vee q) \wedge \neg(p \wedge q) \equiv \neg(p \Leftrightarrow q)$. Dans l'ordre des lignes du tableau (VV, VF, FV, FF), sa colonne est F, V, V, F : l'inverse de celle de $p \Leftrightarrow q$. [[Complément hors du cours|ⓘ]]

À retenir sur l'[[Implication logique|implication]] :

$$p \Rightarrow q \;\equiv\; \neg p \vee q \;\equiv\; \neg q \Rightarrow \neg p.$$

L'implication n'est fausse que lorsque $p$ est vraie et $q$ fausse.

Les deux dernières lignes surprennent souvent : quand $p$ est fausse, $p \Rightarrow q$ est vraie quelle que soit $q$. L'implication est une promesse (« si $p$, alors $q$ ») : elle n'est rompue que si $p$ se produit sans $q$ ; quand $p$ ne se produit pas, la promesse n'est pas trahie. C'est pour cela qu'une affirmation sur les éléments d'un ensemble vide (« tout élément de $\emptyset$ est pair ») est vraie. [[Complément hors du cours|ⓘ]]

Trois implications à ne pas confondre, à partir de $p \Rightarrow q$ : la **contraposée** $\neg q \Rightarrow \neg p$, qui lui est équivalente ; la **réciproque** $q \Rightarrow p$ et la **contraire** (ou inverse) $\neg p \Rightarrow \neg q$, qui ne lui sont pas équivalentes (mais sont équivalentes entre elles, l'une étant la contraposée de l'autre). Avec le fil rouge ci-dessous : « tout carré est un rectangle » est vrai, sa réciproque « tout rectangle est un carré » est fausse. Voir [[Implication logique]]. [[Complément hors du cours|ⓘ]]

Exemple qui sert de fil rouge : $p$ : « $A$ est un carré », $q$ : « $A$ est un rectangle ». On a $p \Rightarrow q$.

## 2. Conditions nécessaire, suffisante, nécessaire et suffisante

Voir [[Condition nécessaire et suffisante]].

- **Condition suffisante** : soient $p$ et $q$ deux propositions. $p$ est suffisante pour $q$ si savoir que $p$ est vraie permet de conclure que $q$ est vraie. En revanche, savoir que $p$ est fausse ne permet pas de conclure que $q$ est fausse. On écrit « si $p$, alors $q$ », ou $p \Rightarrow q$.
- **Condition nécessaire** : si $p \Rightarrow q$, on dit que $q$ est une condition nécessaire pour $p$ : si $q$ n'est pas vraie, $p$ ne peut pas être vraie. On dit aussi « $p$ seulement si $q$ ». Exemple : être un rectangle est une condition nécessaire pour être un carré, car si $A$ n'est pas un rectangle, $A$ ne peut pas être un carré.
- **Condition nécessaire et suffisante** : $p$ est une condition nécessaire et suffisante pour $q$ si $p$ est nécessaire pour $q$ ($q \Rightarrow p$) et suffisante pour $q$ ($p \Rightarrow q$), c'est-à-dire $p \Leftrightarrow q$.

## 3. Tautologie, contradiction, équivalence logique

- Une proposition est une **[[Tautologie]]** si elle est toujours vraie dans sa table de vérité.
- C'est une **contradiction** si elle est toujours fausse.
- **[[Équivalence logique]]** : deux propositions $P(p_1, \ldots, p_k)$ et $Q(p_1, \ldots, p_k)$ sont dites logiquement équivalentes (ou équivalentes) si elles ont la même table de vérité. On note $P(p_1, \ldots, p_k) \equiv Q(p_1, \ldots, p_k)$.

Exemples classiques : $p \vee \neg p$ est une tautologie (principe du **tiers exclu** : une proposition est vraie ou fausse, il n'y a pas de troisième possibilité) ; $p \wedge \neg p$ est une contradiction (principe de **non-contradiction**). Lien entre les deux notions : $P \equiv Q$ si, et seulement si, $P \Leftrightarrow Q$ est une tautologie. Le signe $\equiv$ n'est pas un connecteur : il énonce un fait sur deux formules, alors que $\Leftrightarrow$ fabrique une nouvelle formule. [[Complément hors du cours|ⓘ]]

## 4. Propriétés des connecteurs logiques

[[Propriétés des connecteurs logiques]] ($T$ = toujours vrai, $F$ = toujours faux) :

| Propriété | Disjonction | Conjonction |
|---|---|---|
| Idempotence | $p \vee p \equiv p$ | $p \wedge p \equiv p$ |
| Associativité | $(p \vee q) \vee r \equiv p \vee (q \vee r)$ | $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$ |
| Commutativité | $p \vee q \equiv q \vee p$ | $p \wedge q \equiv q \wedge p$ |
| Distributivité | $p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$ | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ |
| Identité | $p \vee F \equiv p$ ; $p \vee T \equiv T$ | $p \wedge T \equiv p$ ; $p \wedge F \equiv F$ |
| Involution | $\neg\neg p \equiv p$ | |
| Complément | $p \vee \neg p \equiv T$ ; $\neg T \equiv F$ | $p \wedge \neg p \equiv F$ ; $\neg F \equiv T$ |
| [[Lois de De Morgan]] | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ | $\neg(p \wedge q) \equiv \neg p \vee \neg q$ |

Deux équivalences très utilisées en pratique découlent de $p \Rightarrow q \equiv \neg p \vee q$ et de De Morgan. [[Complément hors du cours|ⓘ]]

- **Négation d'une implication** : $\neg(p \Rightarrow q) \equiv \neg(\neg p \vee q) \equiv p \wedge \neg q$. Ce n'est pas une implication : nier « s'il pleut, je prends mon parapluie », c'est dire « il pleut et je ne prends pas mon parapluie ». [[Complément hors du cours|ⓘ]]
- **Équivalence comme double implication** : $p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)$, d'où la démonstration d'une équivalence en deux sens (même idée que la [[Double inclusion|double inclusion]] pour les ensembles). [[Complément hors du cours|ⓘ]]

## 5. Précédence des connecteurs

[[Priorité des connecteurs logiques]], du plus prioritaire au moins prioritaire :

1. négation ;
2. conjonction ;
3. disjonction ;
4. implication et équivalence.

À priorité égale, le connecteur de droite est prioritaire.

Exemple de lecture : $\neg p \wedge q \vee r \Rightarrow s$ se lit $\big(((\neg p) \wedge q) \vee r\big) \Rightarrow s$ ; et, la règle de droite s'appliquant, $p \Rightarrow q \Rightarrow r$ se lit $p \Rightarrow (q \Rightarrow r)$, qui n'est pas équivalent à $(p \Rightarrow q) \Rightarrow r$ (prendre $p$, $q$, $r$ fausses : la première vaut V, la seconde F). Dans le doute, mettre les parenthèses. [[Complément hors du cours|ⓘ]]

## 6. Arguments

**Définition** : un argument est une suite de propositions $p_1, \ldots, p_k$, appelées **prémisses**, se terminant par une proposition $q$ appelée **conclusion**. On note $p_1, \ldots, p_k \vdash q$. Un argument est **valide** si, dès que les prémisses sont vraies, la conclusion est vraie. Un argument non valide est dit **fallacieux**. Voir [[Argument valide]].

**Exemples** : $p \wedge q \vdash p$ est valide ; $q,\ p \Rightarrow q \vdash p$ est fallacieux.

Pour montrer qu'un argument est fallacieux, il suffit d'une ligne de la table où toutes les prémisses sont vraies et la conclusion fausse. Ici, $p$ fausse et $q$ vraie : $q$ et $p \Rightarrow q$ sont vraies, $p$ est fausse. Avec le fil rouge : « $A$ est un rectangle ; tout carré est un rectangle ; donc $A$ est un carré » est faux pour un rectangle non carré. Ce sophisme s'appelle l'**affirmation du conséquent** ; son voisin, la **négation de l'antécédent** ($\neg p,\ p \Rightarrow q \vdash \neg q$), est fallacieux pour la même raison. Ce sont les deux erreurs qui imitent le modus ponens et le modus tollens ci-dessous. [[Complément hors du cours|ⓘ]]

**Théorème** : un argument $p_1, \ldots, p_k \vdash q$ est valide si, et seulement si, $p_1 \wedge p_2 \wedge \ldots \wedge p_k \Rightarrow q$ est une tautologie.

## 7. Règles d'inférence

**Définition** : les [[Règle d'inférence|règles d'inférence]] sont des arguments valides, briques de base dans la construction d'arguments valides.

| Règle | Argument |
|---|---|
| Introduction de la disjonction | $p \vdash p \vee q$ |
| Introduction de la conjonction | $p, q \vdash p \wedge q$ |
| Élimination de la conjonction | $p \wedge q \vdash p$ |
| [[Règle de résolution]] (règle de Robinson) | $p \vee q,\ \neg p \vee r \vdash q \vee r$ |
| [[Modus ponens et modus tollens\|Modus ponens]] | $p,\ p \Rightarrow q \vdash q$ |
| Modus tollens | $\neg q,\ p \Rightarrow q \vdash \neg p$ |
| Syllogisme disjonctif | $p \vee q,\ \neg q \vdash p$ |
| Syllogisme hypothétique | $p \Rightarrow q,\ q \Rightarrow r \vdash p \Rightarrow r$ |

### Preuve du modus ponens

Pour montrer que $p,\ p \Rightarrow q \vdash q$ est valide, on montre que $A \equiv (p \wedge (p \Rightarrow q)) \Rightarrow q$ est une tautologie, par sa table de vérité :

| $p$ | $q$ | $p \Rightarrow q$ | $p \wedge (p \Rightarrow q)$ | $A$ |
|---|---|---|---|---|
| V | V | V | V | V |
| V | F | F | F | V |
| F | V | V | F | V |
| F | F | V | F | V |

La colonne $A$ ne contient que des V : l'argument est valide.

## 8. Quantificateurs

[[Quantificateur|Quantificateurs]] :

- existentiel : $\exists a \in A,\ p(a)$ (« il existe un $a$ de $A$ tel que $p(a)$ ») ;
- universel : $\forall a \in A,\ p(a)$ (« pour tout $a$ de $A$, $p(a)$ »).

**Distributivité** de $\forall$ sur $\wedge$ :
$$\forall x\,(p(x) \wedge q(x)) \;\equiv\; (\forall x\, p(x)) \wedge (\forall x\, q(x)).$$

**Négation** (règle de De Morgan pour les quantificateurs) :
$$\neg\,[(\forall x \in A)\ p(x)] \;\equiv\; (\exists x \in A)\ \neg p(x).$$
(et symétriquement, $\neg[\exists x\, p(x)] \equiv \forall x\, \neg p(x)$).

La distributivité ne vaut que dans deux cas : $\forall$ sur $\wedge$ (ci-dessus) et $\exists$ sur $\vee$ : $\exists x\,(p(x) \vee q(x)) \equiv (\exists x\, p(x)) \vee (\exists x\, q(x))$. Les deux autres sont fausses en général. Dans $\mathbb{N}$, « tout entier est pair ou impair » est vrai, mais « tout entier est pair, ou tout entier est impair » est faux : $\forall$ ne se distribue pas sur $\vee$. De même, « il existe un entier pair et il existe un entier impair » est vrai, mais « il existe un entier à la fois pair et impair » est faux : $\exists$ ne se distribue pas sur $\wedge$. Seules les implications $(\forall x\, p(x)) \vee (\forall x\, q(x)) \Rightarrow \forall x\,(p(x) \vee q(x))$ et $\exists x\,(p(x) \wedge q(x)) \Rightarrow (\exists x\, p(x)) \wedge (\exists x\, q(x))$ restent vraies. [[Complément hors du cours|ⓘ]]

**L'ordre des quantificateurs compte** quand ils sont de nature différente. $\forall x \in \mathbb{N},\ \exists y \in \mathbb{N},\ y > x$ (« pour tout entier, il en existe un plus grand ») est vrai : $y$ peut dépendre de $x$ (prendre $y = x + 1$). $\exists y \in \mathbb{N},\ \forall x \in \mathbb{N},\ y > x$ (« il existe un entier plus grand que tous les autres ») est faux. Deux quantificateurs de même nature, en revanche, s'échangent : $\forall x\, \forall y \equiv \forall y\, \forall x$, et de même pour $\exists$. [[Complément hors du cours|ⓘ]]

**Existence et unicité** : $\exists!\, x \in A,\ p(x)$ (« il existe un unique $x$ ») signifie $\exists x \in A,\ p(x)$ et $\forall x, x' \in A,\ (p(x) \wedge p(x')) \Rightarrow x = x'$. On le démontre donc en deux temps : on exhibe un $x$ qui convient (existence), puis on suppose deux solutions et on montre qu'elles sont égales (unicité). [[Complément hors du cours|ⓘ]]

**Exemple avec plusieurs variables** : on fait entrer la négation de proche en proche, en changeant chaque quantificateur traversé :
$$\neg\,[\forall x \exists y \exists z,\ p(x,y,z)] \equiv \exists x\ \neg[\exists y \exists z,\ p(x,y,z)] \equiv \exists x \forall y\ \neg[\exists z,\ p(x,y,z)] \equiv \exists x \forall y \forall z,\ \neg p(x,y,z).$$

## 9. Types de preuve

### Preuve par contraposition

[[Preuve par contraposition]] : $p \Rightarrow q$ est logiquement équivalent à $\neg q \Rightarrow \neg p$. Pour prouver $p \Rightarrow q$, on suppose $\neg q$ vraie et on en déduit $\neg p$. Une fois cela prouvé, on a démontré $p \Rightarrow q$.

### Preuve par contradiction (par l'absurde)

[[Raisonnement par l'absurde]] : on montre que $p$ est vraie en démontrant que si $p$ est fausse, on aboutit à une conclusion absurde.

Forme logique : $(\neg p \Rightarrow C) \Rightarrow p$, où $C$ est une contradiction, est une tautologie. La « conclusion absurde » est en pratique une proposition et sa négation obtenues en même temps ($r \wedge \neg r$), comme « $a$ et $b$ sont sans facteur commun » et « $a$ et $b$ sont pairs » dans la preuve de l'irrationalité de $\sqrt{2}$ plus bas. Différence avec la contraposition : pour prouver $p \Rightarrow q$ par contraposition, on part de $\neg q$ et on vise précisément $\neg p$ ; par l'absurde, on suppose $p$ et $\neg q$ ensemble et on cherche une contradiction quelconque. [[Complément hors du cours|ⓘ]]

### Preuve par contre-exemple

[[Preuve par contre-exemple]] : pour montrer qu'une proposition « pour tout $x$ » est vraie, il faut la montrer pour tout $x$ de l'ensemble de définition ; pour montrer qu'elle est fausse, il suffit d'un seul contre-exemple.

C'est la négation des quantificateurs vue plus haut : $\neg[\forall x,\ p(x)] \equiv \exists x,\ \neg p(x)$, donc exhiber un seul $x$ tel que $\neg p(x)$ réfute la proposition. Exemple : « pour tout entier $n$, $n^2 + n + 41$ est premier » est vrai pour $n = 0, 1, \ldots, 39$, mais faux pour $n = 40$, car $40^2 + 40 + 41 = 41^2$. Des exemples, même nombreux, ne prouvent donc jamais un « pour tout ». [[Complément hors du cours|ⓘ]]

### Preuve par disjonction des cas

[[Raisonnement par disjonction des cas]] :
$$[(p_1 \vee p_2 \vee \ldots \vee p_n) \Rightarrow q] \;\equiv\; [(p_1 \Rightarrow q) \wedge (p_2 \Rightarrow q) \wedge \ldots \wedge (p_n \Rightarrow q)].$$

### Preuve par récurrence

[[Récurrence]]. Exemple du cours : $P(n) :\ 1 + 2 + \ldots + n = \dfrac{n(n+1)}{2}$ (voir [[Somme des premiers entiers]]).

- **Initialisation** : $P(1)$ : $1 = \dfrac{1 \times 2}{2}$, donc $P(1)$ est vraie.
- **Hérédité** : soit $n \ge 1$ ; supposons $P(n)$ vraie et montrons $P(n+1)$ :
$$1 + 2 + \ldots + n + (n+1) = \frac{n(n+1)}{2} + (n+1) = (n+1)\left[\frac{n}{2} + 1\right] = \frac{(n+1)(n+2)}{2}.$$
Donc $P(n+1)$ est vraie.
- **Conclusion** : $P(1)$ est vraie et $P$ est héréditaire à partir du rang 1, donc par récurrence $P(n)$ est vraie pour tout $n \ge 1$.

Les deux étapes sont indispensables. Sans initialisation, on « prouve » des choses fausses : $P(n)$ : « $n = n + 1$ » est héréditaire (si $n = n+1$, alors $n + 1 = n + 2$), mais n'est vraie pour aucun $n$. Image usuelle : une file de dominos tombe tout entière si le premier tombe (initialisation) et si chaque domino qui tombe fait tomber le suivant (hérédité). [[Complément hors du cours|ⓘ]]

Variante, la **récurrence forte** : si $P(n_0)$ est vraie et si, pour tout $n \ge n_0$, la vérité de $P(n_0), P(n_0 + 1), \ldots, P(n)$ entraîne celle de $P(n+1)$, alors $P(n)$ est vraie pour tout $n \ge n_0$. On s'en sert quand $P(n+1)$ dépend d'un rang antérieur quelconque et pas seulement de $P(n)$ : par exemple pour montrer que tout entier $n \ge 2$ est un produit de nombres premiers (si $n + 1$ n'est pas premier, il s'écrit $a \times b$ avec $2 \le a, b \le n$, et l'on applique l'hypothèse à $a$ et à $b$). [[Complément hors du cours|ⓘ]]

## 10. Théorèmes à connaître

Voir [[Parité d'un entier]].

### Somme de deux impairs (preuve directe)

**Théorème** : si $x$ et $y$ sont impairs, alors $x + y$ est pair.

*Preuve* : il existe des entiers $k$ et $l$ tels que $x = 2k + 1$ et $y = 2l + 1$. Alors $x + y = 2k + 2l + 2 = 2(k + l + 1)$, qui est pair.

### Parité d'une somme paire (contraposition)

**Théorème** : soient $x$ et $y$ deux entiers positifs. Si $x + y$ est pair, alors $x$ et $y$ ont la même parité.

*Preuve* : soit $p(x,y)$ : « $x + y$ est pair » et $q(x,y)$ : « $x$ et $y$ ont la même parité » [[Erreurs du cours#^e-1-logique|✎]]. Par contraposition, on suppose $\neg q(x,y)$ : $x$ et $y$ n'ont pas la même parité. On peut supposer $x$ impair et $y$ pair : $x = 2u + 1$, $y = 2v$. Alors $x + y = 2(u + v) + 1$ est impair, donc $\neg p(x,y)$ est vraie.

### Lemme : carré pair (contraposition)

**Lemme** : soit $a$ un entier positif. Si $a^2$ est pair, alors $a$ est pair. [[Erreurs du cours#^e-1-logique|✎]]

*Preuve* : supposons $a$ impair : $a = 2u + 1$. Alors $a^2 = 4u^2 + 4u + 1 = 2(2u^2 + 2u) + 1$, donc $a^2$ est impair.

### $\sqrt{2}$ est irrationnel (par l'absurde)

[[Irrationalité de √2]]. Supposons $\sqrt{2}$ rationnel : il existe des entiers $a$ et $b$, $b \ne 0$, sans facteur commun, tels que $\sqrt{2} = \dfrac{a}{b}$.

1. Alors $2 = \dfrac{a^2}{b^2}$, donc $2b^2 = a^2$ (1).
2. $a^2$ est pair, donc par le lemme $a$ est pair : $a = 2u$.
3. En remplaçant dans (1) : $2b^2 = 4u^2$, soit $b^2 = 2u^2$ ; donc $b^2$ est pair, et $b$ aussi.
4. $a$ et $b$ sont tous deux pairs : contradiction avec l'hypothèse qu'ils n'ont pas de facteur commun.

L'hypothèse « sans facteur commun » ne restreint rien : tout rationnel non nul s'écrit sous forme de fraction irréductible, en divisant numérateur et dénominateur par leur PGCD. Sans elle, on obtiendrait seulement « $a$ et $b$ sont pairs », ce qui n'a rien de contradictoire en soi. La même méthode montre que $\sqrt{p}$ est irrationnel pour tout nombre premier $p$. [[Complément hors du cours|ⓘ]]
