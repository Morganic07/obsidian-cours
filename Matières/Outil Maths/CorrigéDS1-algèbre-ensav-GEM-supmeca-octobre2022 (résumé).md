---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|Corrigé DS1 algèbre, octobre 2022 (PDF)]]"]
maj: 2026-11-06
---

Résumé du [[raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|Corrigé DS1 algèbre, octobre 2022 (PDF)]] (5 pages), dans [[Outil Maths (matière)]]. Devoir surveillé de 1 h 30, pré-ingénieur 1, algèbre I, sur 22 points environ avec barème détaillé (notation de $\Delta$ et de $\mathbb{N}$ comme dans le cours). Il couvre les chapitres de logique et d'ensembles : [[Chapitre 1 logique (résumé)]], [[Chapitre 2 ensembles (résumé)]], [[Logique propositionnelle]], [[Opérations sur les ensembles]], [[Récurrence]].

## Exercices

| Exercice | Thème | Méthode et résultat |
|---|---|---|
| 1 (4 pts) | Calculs sur $E = \{0,\ldots,7\}$ : $C^c \cap (A \cup B)$, $A \Delta B$, $\mathcal{P}(C)$, $(A \cap B) \times C$ ; partition de ce produit en 4 sous-ensembles | Calcul direct ; les 6 couples sont regroupés en 4 blocs non vides, disjoints, d'union le produit |
| 2 (5 pts) | Valeurs de vérité avec $P$ faux, $Q$ et $R$ vrais ; preuve de $(P \Rightarrow Q) \Rightarrow [(P \wedge R) \Rightarrow (Q \wedge R)]$ | Évaluer les sous-formules ; table de vérité à 8 lignes |
| 3 (4 pts) | Écrire « tout étudiant se réveille au moins un jour avant 8 h » avec des quantificateurs ; négation de la définition de limite d'une suite | $\forall x\, \exists j$ ; la négation échange les quantificateurs et nie la conclusion : $\exists \varepsilon > 0, \forall N, \exists n, (n > N \text{ et } \lvert u_n - \ell \rvert \geq \varepsilon)$ |
| 4 (5 pts) | Contraposée : si $n^2 - 1$ n'est pas divisible par 8, alors $n$ est pair | Contraposée « $n$ impair $\Rightarrow$ 8 divise $n^2 - 1$ » ; écrire $n = 4k + r$, $r \in \{1,3\}$, puis développer les deux cas |
| 5 (5 pts) | Récurrence : 3 divise $4^n + 2$ ; tout $n \geq 8$ s'écrit $3a + 5b$ | Initialisation, hérédité. Pour la seconde, deux cas dans l'hérédité : $b \geq 1$ (on remplace un 5 par deux 3) ou $b = 0$ (on remplace trois 3 par deux 5) |
| 6 (4 pts) | Ensembles : $A = (A \cup B) \cap (A \cup B^c)$ ; $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$ ; $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$ | Distributivité et $B \cap B^c = \emptyset$ ; De Morgan ; chaîne d'équivalences sur $\mathcal{P}$ |

## Méthodes et pièges

- Pour la négation, ne pas oublier de passer de $<$ à $\geq$ et d'inverser chaque quantificateur dans l'ordre.
- Une contraposée prouve l'implication d'origine : le corrigé le rappelle (« toute implication est équivalente à sa contraposée »).
- Dans une récurrence à départ 8, l'hérédité doit traiter à part le cas où il n'y a aucun 5 dans l'écriture.

## Points à vérifier

- **Exercice 3, question 1** : « avant 8 h » demande $h_j(x) < 8$ ; le corrigé écrit $\leq 8$ (complément).
- **Exercice 6, question 3** : la solution est rédigée avec les lettres $E$ et $F$ au lieu de $A$ et $B$ (le raisonnement est identique).
- **Exercice 4** : l'énoncé dit $n \geq 2$ et la preuve prend $n > 2$ ; sans conséquence pour la contraposée, qui est vraie pour tout $n$ impair (complément).
