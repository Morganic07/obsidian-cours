---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 1 logique .docx|Chapitre 1 logique]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 1 logique .docx|Chapitre 1 logique]] (séance du 07/10/23), dans [[Outil Maths (matière)]]. En cas d'écart, le cours et ses images font foi. Les images de la note ne contiennent que des tables, des définitions et des formules : leur contenu est recopié ci-dessous, sans les intégrer.

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

À retenir sur l'[[Implication logique|implication]] :

$$p \Rightarrow q \;\equiv\; \neg p \vee q \;\equiv\; \neg q \Rightarrow \neg p.$$

L'implication n'est fausse que lorsque $p$ est vraie et $q$ fausse.

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

## 5. Précédence des connecteurs

[[Priorité des connecteurs logiques]], du plus prioritaire au moins prioritaire :

1. négation ;
2. conjonction ;
3. disjonction ;
4. implication et équivalence.

À priorité égale, le connecteur de droite est prioritaire.

## 6. Arguments

**Définition** : un argument est une suite de propositions $p_1, \ldots, p_k$, appelées **prémisses**, se terminant par une proposition $q$ appelée **conclusion**. On note $p_1, \ldots, p_k \vdash q$. Un argument est **valide** si, dès que les prémisses sont vraies, la conclusion est vraie. Un argument non valide est dit **fallacieux**. Voir [[Argument valide]].

**Exemples** : $p \wedge q \vdash p$ est valide ; $q,\ p \Rightarrow q \vdash p$ est fallacieux.

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

**Exemple avec plusieurs variables** : on fait entrer la négation de proche en proche, en changeant chaque quantificateur traversé :
$$\neg\,[\forall x \exists y \exists z,\ p(x,y,z)] \equiv \exists x\ \neg[\exists y \exists z,\ p(x,y,z)] \equiv \exists x \forall y\ \neg[\exists z,\ p(x,y,z)] \equiv \exists x \forall y \forall z,\ \neg p(x,y,z).$$

## 9. Types de preuve

### Preuve par contraposition

[[Preuve par contraposition]] : $p \Rightarrow q$ est logiquement équivalent à $\neg q \Rightarrow \neg p$. Pour prouver $p \Rightarrow q$, on suppose $\neg q$ vraie et on en déduit $\neg p$. Une fois cela prouvé, on a démontré $p \Rightarrow q$.

### Preuve par contradiction (par l'absurde)

[[Raisonnement par l'absurde]] : on montre que $p$ est vraie en démontrant que si $p$ est fausse, on aboutit à une conclusion absurde.

### Preuve par contre-exemple

[[Preuve par contre-exemple]] : pour montrer qu'une proposition « pour tout $x$ » est vraie, il faut la montrer pour tout $x$ de l'ensemble de définition ; pour montrer qu'elle est fausse, il suffit d'un seul contre-exemple.

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

## 10. Théorèmes à connaître

Voir [[Parité d'un entier]].

### Somme de deux impairs (preuve directe)

**Théorème** : si $x$ et $y$ sont impairs, alors $x + y$ est pair.

*Preuve* : il existe des entiers $k$ et $l$ tels que $x = 2k + 1$ et $y = 2l + 1$. Alors $x + y = 2k + 2l + 2 = 2(k + l + 1)$, qui est pair.

### Parité d'une somme paire (contraposition)

**Théorème** : soient $x$ et $y$ deux entiers positifs. Si $x + y$ est pair, alors $x$ et $y$ ont la même parité.

*Preuve* : soit $p(x,y)$ : « $x + y$ est pair » et $q(x,y)$ : « $x$ et $y$ ont la même parité » (l'image écrit $q(x,x)$, voir « Points à vérifier »). Par contraposition, on suppose $\neg q(x,y)$ : $x$ et $y$ n'ont pas la même parité. On peut supposer $x$ impair et $y$ pair : $x = 2u + 1$, $y = 2v$. Alors $x + y = 2(u + v) + 1$ est impair, donc $\neg p(x,y)$ est vraie.

### Lemme : carré pair (contraposition)

**Lemme** : soit $a$ un entier positif. Si $a^2$ est pair, alors $a$ est pair.

*Preuve* : supposons $a$ impair : $a = 2u + 1$. Alors $a^2 = 4u^2 + 4u + 1 = 2(2u^2 + 2u) + 1$, donc $a^2$ est impair.

### $\sqrt{2}$ est irrationnel (par l'absurde)

[[Irrationalité de √2]]. Supposons $\sqrt{2}$ rationnel : il existe des entiers $a$ et $b$, $b \ne 0$, sans facteur commun, tels que $\sqrt{2} = \dfrac{a}{b}$.

1. Alors $2 = \dfrac{a^2}{b^2}$, donc $2b^2 = a^2$ (1).
2. $a^2$ est pair, donc par le lemme $a$ est pair : $a = 2u$.
3. En remplaçant dans (1) : $2b^2 = 4u^2$, soit $b^2 = 2u^2$ ; donc $b^2$ est pair, et $b$ aussi.
4. $a$ et $b$ sont tous deux pairs : contradiction avec l'hypothèse qu'ils n'ont pas de facteur commun.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes pour cette note. Exception : l'image de la démonstration de parité, ouverte le 2026-11-06 (point 1).

1. **« $q(x,x)$ »** dans la démonstration de la parité : la transcription le recopie tel quel avec un « À vérifier ». On attendrait $q(x,y)$, d'après le raisonnement. Je n'ai pas ouvert l'image : c'est probablement une coquille du cours, sans conséquence sur la preuve. Mise à jour du 2026-11-06 : image ouverte, elle écrit bien $q(x,x)$ ; la coquille est dans le cours.
2. **Énoncé du lemme** : l'image écrit « Soit $a^2$ un entier positif » ; c'est $a$ qui est l'entier considéré.
3. **Titres de la note** : la formule $\forall x\,(p \wedge q) \equiv \ldots$ est placée sous « Quantificateurs » et la négation sous « Distributivité des quantificateurs » : les intitulés semblent décalés d'un cran par rapport aux formules (la négation $\neg\forall \equiv \exists\neg$ est la règle de De Morgan, la formule avec $\wedge$ la distributivité).
4. **Ligne « P→ q = non(p)U(q) »** : notation de l'étudiant, le « U » désigne la disjonction $\vee$ (pas l'union).
5. **Fin de note** : la ligne « Montrons que rac(2) est irrationnel : » est placée après la démonstration, sans contenu.
