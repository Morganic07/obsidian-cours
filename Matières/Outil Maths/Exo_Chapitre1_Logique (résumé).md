---
type: source
tags: [year1]
sources: [".raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf"]
maj: 2026-11-06
complet: true
---

Résumé de la feuille Exo Chapitre 1 Logique (PDF) (`.raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf`) (3 pages, 2023-2024), dans [[Outil Maths (matière)]]. Titre de la feuille : « Logique et Calcul propositionnel », Outils Mathématiques, semestre 1. Document scanné, sans couche de texte : lu à partir des images des trois pages. **Énoncés seuls, sans corrigé** : aucune correction n'est donnée par le document. Pas de figure : rien à intégrer. Cours : [[Chapitre 1 logique (résumé)]], [[Logique propositionnelle]], [[Récurrence]]. Les exercices 15 à 19 sortent de la logique pure (inégalités, récurrence, dénombrement).

## Vue d'ensemble : 19 exercices

| Exercices | Thème |
|---|---|
| 1 | Valeur de vérité d'assertions en langage courant |
| 2 à 4 | Négations, traduction formules ↔ phrases |
| 5 | Implication et réciproque |
| 6, 7 | Traduction en formules, équivalence par table de vérité |
| 8, 9 | Tables de vérité, équivalences, formes normales |
| 10 | Modélisation et déduction (parapluies) |
| 11 à 14 | [[Quantificateur\|Quantificateurs]] : vérité, traduction, négation |
| 15, 16 | Inégalités, [[Preuve par contraposition\|contraposée]] |
| 17 | Récurrence et piège de l'hérédité seule |
| 18, 19 | [[Coefficient binomial\|Coefficients binomiaux]], [[Formule du binôme de Newton\|binôme de Newton]] |

## Exercice 1 : vrai ou faux ?

Parmi les assertions suivantes, lesquelles sont vraies, lesquelles sont fausses, et pourquoi ?

1. Si Napoléon était chinois alors $3 - 2 = 2$.
2. Soit Cléopâtre était chinoise, soit les grenouilles aboient.
3. Soit les roses sont des animaux, soit les chiens ont 4 pattes.
4. Si l'homme est un quadrupède, alors il parle.
5. Les roses ne sont ni des animaux, ni des fleurs.
6. Paris est en France ou Madrid est en Chine.
7. La pierre ponce est un homme si et seulement si les femmes sont des sardines.
8. Les poiriers ne donnent pas de melons, et Cléopâtre n'est pas chinoise.

Enjeu : appliquer les tables de vérité de l'[[Implication logique|implication]] (une implication à prémisse fausse est vraie, items 1 et 4), du « soit… soit » (ou exclusif), du « ou », du « et » et de l'équivalence (deux propositions fausses sont équivalentes, item 7).

## Exercice 2 : négations

Soient $(P)$, $(Q)$ et $(R)$ trois propositions. Donner la négation de :

a) $P \wedge (\neg Q \vee R)$ ; b) $(P \wedge Q) \Rightarrow R$.

Outils : [[Lois de De Morgan]] et $\neg(A \Rightarrow B) \equiv A \wedge \neg B$.

## Exercice 3 : écrire la négation

Soient $A$, $B$ et $C$ trois assertions. Pour chacune des assertions suivantes, écrire sa négation (l'énoncé imprime « Ecriresangation », voir « Points à vérifier ») :

- $(A1) \equiv (A \wedge \neg B)$ ; $(A2) \equiv (A \vee \neg B)$ ; $(A3) \equiv (A \vee (B \wedge C))$ ;
- $(A4) \equiv (A \wedge (B \vee C))$ ; $(A5) \equiv (A \Rightarrow \neg B)$ ;
- $(A6) \equiv (A \Rightarrow B)$ ; $(A7) \equiv (\neg(A \vee B) \Rightarrow C)$ ; $(A8) \equiv ((A \wedge B)(C))$.

## Exercice 4 : négation de phrases

Donner la négation mathématique de :

1. Toutes les boules contenues dans l'urne sont rouges.
2. Certains nombres entiers sont pairs.
3. Si un nombre entier est divisible par 4, alors il se termine par 4.

Soit $f : \mathbb{R} \to \mathbb{R}$.

4. $f$ est positive, c'est-à-dire $\forall x \in \mathbb{R},\ f(x) \ge 0$.
5. $f$ est paire sur $\mathbb{R}$, c'est-à-dire $\forall x \in \mathbb{R},\ f(-x) = f(x)$.

Outil : $\neg(\forall x,\ p(x)) \equiv \exists x,\ \neg p(x)$ et réciproquement.

## Exercice 5 : implication et réciproque

Soient $(P)$ « J'ai mon permis de conduire » et $(Q)$ « J'ai plus de 18 ans ». Les propositions $(P) \Rightarrow (Q)$ et $(Q) \Rightarrow (P)$ sont-elles vraies ? Que peut-on conclure ?

Enjeu : distinguer une implication de sa réciproque, et donc condition nécessaire et condition suffisante ([[Condition nécessaire et suffisante]]).

## Exercice 6 : traduire en formules

Écrire chacune des phrases suivantes sous forme de formule logique impliquant $P$, $Q$ et $R$ (la feuille ne définit pas $P$, $Q$, $R$ ; d'après les phrases : « j'ai soif », « mon verre est vide », « il est trois heures ») :

1. J'ai soif mon verre n'est pas vide.
2. Il est trois heures et j'ai soif.
3. S'il est trois heures alors j'ai soif.
4. Si j'ai soif alors mon verre est vide.
5. Si je n'ai pas soif, alors mon verre n'est pas vide.

## Exercice 7 : roses et violettes

$P$ : « les roses sont rouges », $Q$ : « les violettes sont bleues ». Écrire sous forme de formule logique :

1. Si les roses ne sont pas rouges, alors les violettes ne sont pas bleues.
2. Les roses sont rouges ou les violettes ne sont pas bleues.
3. Soit les roses sont rouges, soit les violettes sont bleues (mais pas les deux).

Montrer avec une table de vérité que les propositions 1 et 2 sont équivalentes (c'est-à-dire $\neg P \Rightarrow \neg Q \equiv P \vee \neg Q$, voir [[Équivalence logique]]).

## Exercice 8 : tables de vérité et équivalences

1. Construire la table de vérité de $R = \overline{(P \vee Q)} \vee (\bar P \vee \bar Q)$ (la barre désigne la négation).
2. Démontrer que $P \Rightarrow Q$ et $\bar P \vee Q$ sont logiquement équivalentes.
3. Soient $P$, $Q$, $R$ trois propositions. Démontrer que $P \wedge (Q \vee R)$ et $(P \wedge Q) \vee (P \wedge R)$ sont équivalentes (distributivité).
4. Soient $P$ et $Q$ deux propositions. Montrer que $\neg(P \Rightarrow Q)$ et $P \wedge \neg Q$ sont équivalentes.

## Exercice 9 : formes normales

Écrire sous [[Forme normale conjonctive et disjonctive|forme normale conjonctive et sous forme normale disjonctive]] :

1. $(\neg P \wedge Q) \Rightarrow R$
2. $\neg(P \vee Q) \wedge (S \Rightarrow t)$
3. $\neg(P \wedge Q) \wedge (P \vee Q)$

## Exercice 10 : les parapluies

« S'il pleut, Abel prend un parapluie. Béatrice ne prend jamais de parapluie s'il ne pleut pas et en prend toujours un quand il pleut. » Que peut-on déduire de ces affirmations dans les situations suivantes ? Justifier en introduisant trois propositions logiques $P$, $Q$ et $R$.

- Abel se promène avec un parapluie.
- Abel se promène sans parapluie.
- Béatrice se promène avec un parapluie.
- Béatrice se promène sans parapluie.
- Il ne pleut pas.
- Il pleut.

Pistes (complément, pas dans la feuille) : Abel obéit à une implication (pluie ⇒ parapluie), Béatrice à une équivalence (pluie ⇔ parapluie) ; on raisonne par [[Modus ponens et modus tollens|modus ponens, modus tollens]] ou contraposée.

## Exercice 11 : ordre des quantificateurs

Soient les 4 assertions :

1. $\exists x \in \mathbb{R}\ \forall y \in \mathbb{R}\quad x + y > 0$
2. $\forall x \in \mathbb{R}\ \exists y \in \mathbb{R}\quad x + y > 0$
3. $\forall x \in \mathbb{R}\ \forall y \in \mathbb{R}\quad x + y > 0$
4. $\exists x \in \mathbb{R}\ \forall y \in \mathbb{R}\quad y^2 > x$

Questions : 1. sont-elles vraies ou fausses ? 2. Donner leur négation.

Enjeu : $\exists x\, \forall y$ (un même $x$ pour tous les $y$) n'est pas $\forall x\, \exists y$ ($y$ peut dépendre de $x$).

## Exercice 12 : des quantificateurs aux mots

Soient $I$ un intervalle de $\mathbb{R}$ et $f : I \to \mathbb{R}$. Exprimer verbalement :

1. $\exists C \in \mathbb{R},\ \forall x \in I,\ f(x) = C$
2. $\forall x \in I,\ f(x) = 0 \Rightarrow x = 0$
3. $\forall y \in \mathbb{R},\ \exists x \in I,\ f(x) = y$
4. $\forall x, y \in I,\ x \le y \Rightarrow f(x) \le f(y)$
5. $\forall x, y \in I,\ f(x) = f(y) \Rightarrow x = y$

(Propriétés en jeu : fonction constante, ne s'annulant qu'en 0, surjective, croissante, injective ; voir [[Injectivité et surjectivité]].)

## Exercice 13 : des mots aux quantificateurs

Mêmes $I$ et $f$. Exprimer à l'aide de quantificateurs :

1. La fonction $f$ s'annule.
2. La fonction $f$ est la fonction nulle.
3. $f$ n'est pas une fonction constante.
4. $f$ ne prend jamais deux fois la même valeur.

## Exercice 14 : négations quantifiées

Soient $I$ un intervalle non vide de $\mathbb{R}$ et $f : I \to \mathbb{R}$. Donner la négation de :

1. $\forall x \in I,\ f(x) \ne 0$.
2. $\forall y \in \mathbb{R},\ \exists x \in I,\ y = f(x)$.
3. $\exists M \in \mathbb{R},\ \forall x \in I,\ |f(x)| \le M$.
4. $\forall (x, y) \in I^2,\ f(x) = f(y) \Rightarrow x = y$.

## Exercice 15 : inégalités

Soient $a, b, c$ trois réels. Montrer que :

1. $ab < \dfrac{a^2 + b^2}{2}$ (voir « Points à vérifier ») ;
2. $ab + ac + bc \le a^2 + b^2 + c^2$ ;
3. $3ab + 3bc + 3ac \le (a + b + c)^2$.

Piste (complément) : passer par $(a - b)^2 \ge 0$, puis sommer les inégalités obtenues pour chaque paire.

## Exercice 16 : contraposée

1. Montrer : $\forall n \in \mathbb{N},\ n$ impair $\Rightarrow n^2$ impair.
2. Montrer : $\forall (x, y) \in \mathbb{R}^2,\ [x^2 + y^2 = 0] \Rightarrow [x = y = 0]$.

## Exercice 17 : l'hérédité ne suffit pas

Pour tout entier naturel $n$, on considère :

$$P_n :\ 10^n - 1 \text{ est divisible par } 9, \qquad Q_n :\ 10^n + 1 \text{ est divisible par } 9.$$

1. Démontrer que si $P_n$ est vraie alors $P_{n+1}$ est vraie.
2. Démontrer que si $Q_n$ est vraie alors $Q_{n+1}$ est vraie.
3. Un élève affirme : « Donc $P_n$ et $Q_n$ sont vraies pour tout entier naturel $n$. » Qu'en pensez-vous ? Justifier.
4. Démontrer que $P_n$ est vraie pour tout entier naturel $n$.
5. Démontrer que pour tout entier naturel $n$, $Q_n$ est fausse (on pourra utiliser un [[Raisonnement par l'absurde|raisonnement par l'absurde]]).

Enjeu : une récurrence exige l'initialisation ; $Q_n$ est héréditaire mais n'est vraie pour aucun $n$.

## Exercice 18 : identité sur les coefficients binomiaux

Démontrer que pour tous $n, p, k \in \mathbb{N}$, $n \ge p \ge q$ (sic, lire $k$) :

$$\binom{n}{k}\binom{n-k}{p-k} = \binom{p}{k}\binom{n}{p}.$$

Calculer :
$$\sum_{k=0}^{p} \binom{n}{k}\binom{n-k}{p-k}.$$

## Exercice 19 : binôme de Newton

Soient $a$ et $b$ deux réels et $n$ un entier naturel.

1. Exprimer $(a + b)^n$ en fonction de $k \in \mathbb{Z}$ (sic : formule du binôme, avec une somme sur $k$).
2. Calculer, en justifiant :
$$A = \sum_{k=0}^{n} \binom{n}{k} \qquad\text{et}\qquad B = \sum_{k=0}^{n} \binom{n}{k}(-1)^k.$$

## Points à vérifier

- **Exercice 15, question 1** : l'inégalité stricte $ab < \frac{a^2 + b^2}{2}$ est fausse pour $a = b$ ; il faut $\leq$ (complément).
- **Exercice 17** : $P_n$ est écrit « $10^{n1} - 1$ », coquille pour $10^n - 1$ (complément).
- **Exercice 18** : « $n \geq p \geq q$ » doit se lire $n \geq p \geq k$, puisque l'identité porte sur $k$ (complément).
- **Exercice 3** : la consigne imprimée « Ecriresangation » (mot collé, en italique) se lit « Écrire sa négation » ; l'assertion $(A8) \equiv ((A \wedge B)(C))$ manque d'un connecteur entre $(A \wedge B)$ et $(C)$, illisible telle quelle.
- **Exercice 6** : la feuille ne définit pas $P$, $Q$, $R$, et la phrase 1 (« J'ai soif mon verre n'est pas vide ») manque d'un mot de liaison.
- **Exercice 9, question 2** : la proposition mélange une majuscule et une minuscule ($S \Rightarrow t$).
- **Exercice 19, question 1** : « en fonction de $k \in \mathbb{Z}$ » est étrange ; on attend la formule du binôme avec $k$ de $0$ à $n$.
