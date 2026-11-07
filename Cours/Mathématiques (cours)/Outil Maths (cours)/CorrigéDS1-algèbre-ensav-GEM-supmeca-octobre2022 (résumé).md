---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du Corrigé DS1 algèbre, octobre 2022 (PDF) ([[Raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf]]) (5 pages), dans [[Outil Maths (index)]]. Devoir surveillé 1 de Préing 1, algèbre I, du mardi 25 octobre 2022 : 1 h 30, appareils électroniques interdits, 6 exercices à traiter dans l'ordre voulu, rédaction et précision des justifications prises en compte. Barème détaillé dans le corrigé (notation de $\Delta$ et de $\mathbb{N}$ comme dans le cours). Il couvre les chapitres de logique et d'ensembles : [[chp 1 - logique (résumé)]], [[chp 2 - ensembles (résumé)]], [[Logique propositionnelle]], [[Opérations sur les ensembles]], [[Récurrence]].

Le document ne contient aucune figure (seul le logo de l'école en tête).

## Vue d'ensemble

| Exercice | Thème | Méthode et résultat |
|---|---|---|
| 1 (4 pts) | Calculs sur $E = \{0,\ldots,7\}$ : $C^c \cap (A \cup B)$, $A \Delta B$, $\mathcal{P}(C)$, $(A \cap B) \times C$ ; partition de ce produit en 4 sous-ensembles | Calcul direct ; les 6 couples sont regroupés en 4 blocs non vides, disjoints, d'union le produit |
| 2 (5 pts) | Valeurs de vérité avec $P$ faux, $Q$ et $R$ vrais ; preuve de $(P \Rightarrow Q) \Rightarrow [(P \wedge R) \Rightarrow (Q \wedge R)]$ | Évaluer les sous-formules ; table de vérité à 8 lignes |
| 3 (4 pts) | Écrire « tout étudiant se réveille au moins un jour avant 8 h » avec des quantificateurs ; négation de la définition de limite d'une suite | $\forall x\, \exists j$ ; la négation échange les quantificateurs et nie la conclusion : $\exists \varepsilon > 0, \forall N, \exists n, (n > N \text{ et } \lvert u_n - \ell \rvert \geq \varepsilon)$ |
| 4 (5 pts) | Contraposée : si $n^2 - 1$ n'est pas divisible par 8, alors $n$ est pair | Contraposée « $n$ impair $\Rightarrow$ 8 divise $n^2 - 1$ » ; écrire $n = 4k + r$, $r \in \{1,3\}$, puis développer les deux cas |
| 5 (5 pts) | Récurrence : 3 divise $4^n + 2$ ; tout $n \geq 8$ s'écrit $3a + 5b$ | Initialisation, hérédité. Pour la seconde, deux cas dans l'hérédité : $b \geq 1$ (on remplace un 5 par deux 3) ou $b = 0$ (on remplace trois 3 par deux 5) |
| 6 (4 pts) | Ensembles : $A = (A \cup B) \cap (A \cup B^c)$ ; $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$ ; $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$ | Distributivité et $B \cap B^c = \emptyset$ ; De Morgan ; chaîne d'équivalences sur $\mathcal{P}$ |

## Exercice 1 (4 points) : opérations sur les ensembles

**Énoncé.** Dans $E = \{0 ; 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7\}$, on considère $A = \{0 ; 2 ; 5\}$, $B = \{1 ; 2 ; 3 ; 4 ; 5 ; 6\}$ et $C = \{4 ; 5 ; 7\}$.

1. Déterminer $C^c \cap (A \cup B)$ ; $A \Delta B$ ; $\mathcal{P}(C)$ ; $(A \cap B) \times C$.
2. Donner une [[Partition d'un ensemble|partition]] de $(A \cap B) \times C$ contenant exactement 4 sous-ensembles $P_1, P_2, P_3, P_4$.

**Corrigé.**

1. 0,75 point par ensemble.
   - $C^c \cap (A \cup B) = \{0, 1, 2, 3, 6\}$ ;
   - $A \Delta B = \{0, 1, 3, 4, 6\}$ (voir [[Différence symétrique]]) ;
   - $\mathcal{P}(C) = \{\emptyset, \{4\}, \{5\}, \{7\}, \{4,5\}, \{4,7\}, \{5,7\}, \{4,5,7\}\}$ ;
   - $(A \cap B) \times C = \{2, 5\} \times \{4, 5, 7\} = \{(2,4), (2,5), (2,7), (5,4), (5,5), (5,7)\}$ (voir [[Produit cartésien]]).
2. 1 point. Une partition possible :
$$\big\{\{(2,4)\},\ \{(2,5)\},\ \{(2,7), (5,4)\},\ \{(5,5), (5,7)\}\big\}$$

## Exercice 2 (5 points) : valeurs de vérité

**Énoncé.**

1. $P$ est fausse, $Q$ et $R$ sont vraies. Lesquelles de ces assertions sont vraies ?
   - (a) $\big(P \Rightarrow \text{non}(Q)\big)$ ou $\text{non}(R \text{ et } Q)$ ;
   - (b) $\text{non}\big[\text{non}(P) \Rightarrow (Q \text{ et non}(R))\big]$.
2. Montrer que l'implication suivante est toujours vraie : $(P \Rightarrow Q) \Rightarrow [(P \text{ et } R) \Rightarrow (Q \text{ et } R)]$.

**Corrigé.**

1. (a) 1,5 point. $P \Rightarrow \text{non}(Q)$ : Faux $\Rightarrow$ Faux $=$ Vrai ; $\text{non}(R \text{ et } Q) = \text{non}(\text{Vrai et Vrai}) =$ Faux ; Vrai ou Faux $=$ **Vrai**.
   (b) 1,5 point. $\text{non}(P) =$ Vrai ; $Q$ et $\text{non}(R) =$ Vrai et Faux $=$ Faux ; Vrai $\Rightarrow$ Faux $=$ Faux ; la négation donne **Vrai**.
2. 2 points. Table de vérité (voir [[Implication logique]] et [[Tautologie]]) :

| $P$ | $Q$ | $R$ | $Q$ et $R$ | $P$ et $R$ | $P \Rightarrow Q$ | $(P \text{ et } R) \Rightarrow (Q \text{ et } R)$ | Implication totale |
|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | V |
| V | V | F | F | F | V | V | V |
| V | F | V | F | V | F | F | V |
| V | F | F | F | F | F | V | V |
| F | V | V | V | F | V | V | V |
| F | V | F | F | F | V | V | V |
| F | F | V | F | F | V | V | V |
| F | F | F | F | F | V | V | V |

La dernière colonne ne contient que des V : l'implication est toujours vraie.

## Exercice 3 (4 points) : quantificateurs

**Énoncé.**

1. $E$ est l'ensemble des étudiants, $S$ celui des jours de la semaine, $h_j(x)$ l'heure de réveil de l'étudiant $x$ le jour $j$. Écrire avec des symboles : « Tout étudiant se réveille au moins un jour de la semaine avant 8 h ».
2. Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle et $\ell \in \mathbb{R}$. Donner la négation de
$$\forall \varepsilon > 0,\ \exists N \in \mathbb{N},\ \forall n \in \mathbb{N},\ (n > N \Rightarrow |u_n - \ell| < \varepsilon).$$

**Corrigé.** Voir [[Quantificateur]].

1. 2 points. $\forall x \in E,\ \exists j \in S,\ h_j(x) \le 8$.
2. 2 points. La négation est
$$\exists \varepsilon > 0,\ \forall N \in \mathbb{N},\ \exists n \in \mathbb{N},\ (n > N \text{ et } |u_n - \ell| \ge \varepsilon).$$

## Exercice 4 (5 points) : raisonnement par contraposition

**Énoncé.** Démontrer par [[Preuve par contraposition|contraposition]], pour $n \ge 2$, $n \in \mathbb{N}$, la propriété
$P$ : « Si l'entier $n^2 - 1$ n'est pas divisible par 8, alors l'entier $n$ est pair. »

1. Définir la contraposée d'une implication $A \Rightarrow B$.
2. Écrire la contraposée de $P$.
3. Démontrer qu'un entier impair $n$ s'écrit $n = 4k + r$ avec $k \in \mathbb{N}$ et $r \in \{1, 3\}$.
4. Prouver la contraposée de $P$.
5. A-t-on démontré la propriété de l'énoncé ?

**Corrigé.**

1. 0,75 point. $\text{non } B \Rightarrow \text{non } A$.
2. 0,75 point. Si $n$ est impair, alors $n^2 - 1$ est divisible par 8.
3. 1,5 point. Soit $n$ impair : il existe $k' \in \mathbb{Z}$ tel que $n = 2k' + 1$. Si $k'$ est pair, $k' = 2k$ et $n = 4k + 1$. Si $k'$ est impair, $k' = 2k + 1$ et $n = 4k + 3$. Donc $n = 4k + r$ avec $r \in \{1, 3\}$ ([[Raisonnement par disjonction des cas|disjonction des cas]], [[Parité d'un entier|parité]]).
4. 1,25 point. Soit $n > 2$ impair, $n = 4k + r$ :
$$n^2 - 1 = 16k^2 + 8kr + r^2 - 1 = \begin{cases} 16k^2 + 8k & \text{si } r = 1 \\ 16k^2 + 24k + 8 & \text{si } r = 3 \end{cases}$$
Dans les deux cas, $n^2 - 1$ est divisible par 8 (voir [[Divisibilité]]).
5. 0,75 point. Oui, car toute implication est équivalente à sa contraposée.

## Exercice 5 (5 points) : récurrence

**Énoncé.**

1. Démontrer que pour tout $n \in \mathbb{N}$, 3 divise $4^n + 2$.
2. Démontrer que pour tout $n \ge 8$, il existe $a, b \in \mathbb{N}$ tels que $n = 3a + 5b$.

**Corrigé.**

1. 2 points. $P(n)$ : « 3 divise $4^n + 2$ ».
   - *Initialisation* (0,5 point) : $4^0 + 2 = 3$, donc $P(0)$ est vraie.
   - *Hérédité* (1,5 point) : supposons $4^n + 2 = 3k$, $k \in \mathbb{Z}$. Montrons qu'il existe $k'$ tel que $4^{n+1} + 2 = 3k'$ :
   $$4^{n+1} + 2 = 4 \cdot 4^n + 2 = 4(3k - 2) + 2 = 3 \cdot 4k - 8 + 2 = 3 \cdot 4k - 6 = 3\underbrace{(4k - 2)}_{k'}.$$
   - Conclusion : pour tout $n \in \mathbb{N}$, 3 divise $4^n + 2$.
2. 2 points. $P(n)$ : « il existe $a, b \in \mathbb{N}$ tels que $n = 3a + 5b$ », pour $n \ge 8$.
   - *Initialisation* (0,5 point) : $8 = 3 \cdot 1 + 5 \cdot 1$.
   - *Hérédité* (2,5 points) : supposons $n = 3a + 5b$. Alors $n + 1 = 3a + 5b + 1$. Deux cas :
     - si $b \in \mathbb{N}^*$, $b - 1 \in \mathbb{N}$ et $n + 1 = 3a + 5b + 3 \cdot 2 - 5 = 3(a + 2) + 5(b - 1)$ ;
     - si $b = 0$, comme $n + 1 > 8$, $a \ge 3$, donc $a - 3 \in \mathbb{N}$ et $n + 1 = 3a + 5 \cdot 2 - 3 \cdot 3 = 3(a - 3) + 5 \cdot 2$.
   - Conclusion : tout $n \ge 8$ s'écrit $3a + 5b$.

## Exercice 6 (4 points) : égalités d'ensembles

**Énoncé.** Soit $A$, $B$, $C$ trois parties d'un ensemble $E$. Démontrer :

1. $A = (A \cup B) \cap (A \cup B^c)$.
2. $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.
3. $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$.

**Corrigé.**

1. 1 point. $A = A \cup \emptyset = A \cup (B \cap B^c) = (A \cup B) \cap (A \cup B^c)$ (distributivité). Une [[Double inclusion|double inclusion]] facile permet aussi de conclure.
2. 1,5 point. Avec les [[Lois de De Morgan|lois de De Morgan]] :
$$A \setminus (B \cup C) = A \cap (B \cup C)^c = A \cap (B^c \cap C^c) = A \cap A \cap B^c \cap C^c = (A \cap B^c) \cap (A \cap C^c) = (A \setminus B) \cap (A \setminus C).$$
3. 1,5 point. (Rédigé avec $E$ et $F$ à la place de $A$ et $B$.)
$$\begin{aligned} X \in \mathcal{P}(E) \cap \mathcal{P}(F) &\iff X \in \mathcal{P}(E) \text{ et } X \in \mathcal{P}(F) \\ &\iff X \subset E \text{ et } X \subset F \\ &\iff X \subset E \cap F \\ &\iff X \in \mathcal{P}(E \cap F). \end{aligned}$$
D'où $\mathcal{P}(E) \cap \mathcal{P}(F) = \mathcal{P}(E \cap F)$. (Le corrigé nomme $A$ la partie générique ; renommée $X$ ici pour éviter la confusion.)

## Méthodes et pièges

- Pour la négation, ne pas oublier de passer de $<$ à $\geq$ et d'inverser chaque quantificateur dans l'ordre.
- Une contraposée prouve l'implication d'origine : le corrigé le rappelle (« toute implication est équivalente à sa contraposée »).
- Dans une récurrence à départ 8, l'hérédité doit traiter à part le cas où il n'y a aucun 5 dans l'écriture.

## Points à vérifier

- **Exercice 3, question 1** : « avant 8 h » demande $h_j(x) < 8$ ; le corrigé écrit $\leq 8$ (complément).
- **Exercice 6, question 3** : la solution est rédigée avec les lettres $E$ et $F$ au lieu de $A$ et $B$ (le raisonnement est identique).
- **Exercice 4** : l'énoncé dit $n \geq 2$ et la preuve prend $n > 2$ ; sans conséquence pour la contraposée, qui est vraie pour tout $n$ impair (complément).
- **Barème** (complément) : les en-têtes annoncent 4 + 5 + 4 + 5 + 5 + 4 = 27 points ; l'ancienne version de cette fiche disait « 22 points environ ». À l'exercice 5, la question 2 est notée « 2 points » alors que son initialisation et son hérédité valent 0,5 + 2,5 = 3 points.
- **Exercice 5, question 1** : le corrigé écrit d'abord $4^n + 2 = 3k$, puis remplace $4^n$ par $3k - 2$ ; c'est cohérent. La phrase « montrons C'est-à-dire » est une coquille de rédaction.
- **Exercice 6, question 1** : le corrigé écrit deux fois $A \cup (B \cap B^c)$ dans la chaîne d'égalités, sans effet sur le résultat.
