---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
complet: true
enrichi: 2026-11-18
---

Résumé du PDF chp 2 - association rules ([[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]) (18 diapositives beamer, « Association Rules », daté du 11 novembre 2026), dans [[Cours/Informatique/Data mining/_index|Data mining]]. Le cours est en anglais, les exercices en français. Il fait suite à [[1 - intro to data mining]] et [[1 - pdf du prof]], où les [[Règle d'association|règles d'association]] n'étaient que nommées. Les passages ajoutés finissent par ⓘ, les passages corrigés par ✎.

Plan : tâches du data mining ; introduction ; terminologie et définitions (support, confiance, lift) ; algorithme Apriori ; génération des règles (redondance simple et stricte) ; trois exercices.

## 1. Les tâches du data mining

Le cours replace les règles d'association parmi les tâches de la [[Fouille de données|fouille de données]] :

- **Approches supervisées** ([[Apprentissage supervisé]]) : chaque instance est décrite par $p$ variables prédictives et une [[Variable cible et variable explicative|variable cible]] à prédire.
  - [[Classifieur|Classification]] : variable cible discrète. Exemple : le diagnostic d'une maladie.
  - [[Régression (apprentissage automatique)|Régression]] : variable cible continue. Exemple : l'estimation d'un prix.
- **Approches non supervisées** ([[Apprentissage non supervisé]]) :
  - [[Clustering]] : exemple, la détection de profils d'utilisateurs ([[Profilage des consommateurs]]).
  - **Association** : exemple, l'analyse des [[Fichier journal|journaux]] (*logs*) d'un [[Serveur web|serveur web]].

![[Association rules - p3.jpg]]
*Figure : les tâches du data mining. Prédictives : classification, régression, analyse de [[Série temporelle|séries temporelles]], prédiction. Descriptives : clustering, résumé (summarization), règles d'association, découverte de séquences.*

Le schéma ajoute deux tâches descriptives que le texte ne détaille pas : le [[Résumé de données|résumé]] (*summarization*), qui décrit un jeu de données de façon compacte (statistiques, profils de groupes), et la **découverte de séquences** ([[Extraction de motifs séquentiels]]), qui cherche des enchaînements fréquents dans le temps (« acheter un appareil photo, puis une carte mémoire le mois suivant ») [[Complément hors du cours|ⓘ]]

## 2. Introduction

- La fouille de règles d'association cherche des relations entre **items** dans de grandes [[Système de gestion de base de données|bases de données]] de **transactions**.
- Le problème de la recherche des [[Itemset fréquent|itemsets fréquents]] a été introduit par Agrawal en 1993.
- L'[[Algorithme Apriori]] repose sur la [[Propriété de fermeture descendante|propriété de fermeture descendante]] (*downward closure*) : si un itemset n'est pas fréquent, aucun de ses sur-ensembles ne l'est.
- Apriori fait une recherche en largeur ([[Parcours en largeur|breadth-first search]]) dans l'espace de recherche : il génère les candidats de longueur $k+1$ à partir des itemsets fréquents de longueur $k$.

L'article fondateur est celui d'Agrawal, Imieliński et Swami (SIGMOD, 1993), écrit chez [[IBM]] à partir de données de ventes en supermarché ; l'algorithme Apriori lui-même est publié l'année suivante par Agrawal et Srikant (VLDB, 1994). L'enjeu est l'[[Explosion combinatoire|explosion combinatoire]] : avec $n$ items, il existe $2^n - 1$ itemsets non vides (l'[[Opérations sur les ensembles|ensemble des parties]] privé du vide), soit déjà plus de $10^{30}$ pour 100 produits ; une [[Recherche exhaustive|recherche exhaustive]] est impossible, et la propriété de fermeture descendante permet d'élaguer des branches entières de cet espace [[Complément hors du cours|ⓘ]]

## 3. Terminologie

- Le domaine est décrit par un [[Ensemble (mathématiques)|ensemble]] d'atomes appelés **items**.
- Application type : le « panier de la ménagère » d'un supermarché ([[Analyse du panier de la ménagère]]), par exemple [vin, fromage, chocolat].
- Un **ensemble d'items** (*itemset*) est une suite d'items rangés dans un ordre prédéfini.
- Une **[[Transaction (fouille de données)|transaction]]** est un ensemble d'items :
  - T1 [vin, fromage, viande]
  - T2 [vin, fromage, chocolat]
- L'ensemble des transactions $D$ est l'ensemble d'apprentissage.

L'ordre prédéfini (en pratique l'[[Relation d'ordre|ordre lexicographique]]) sert à la génération des candidats : il évite de produire deux fois le même itemset sous deux permutations. Un itemset de $k$ items s'appelle un **$k$-itemset**. Une transaction de fouille n'est pas une [[Transaction (base de données)|transaction de SGBD]] (suite d'opérations atomique) : c'est un simple enregistrement, comme un ticket de caisse [[Complément hors du cours|ⓘ]]

**But** : trouver les associations présentes dans $D$, par exemple vin $\Rightarrow$ fromage, ou vin, fromage $\Rightarrow$ jambon.

## 4. Définitions : support, confiance, lift

Pour une règle $A \Rightarrow B$, où $A$ et $B$ sont des sous-ensembles d'items et $P(A)$ le pourcentage (la probabilité) des transactions qui contiennent $A$ :

- [[Support (règle d'association)|Support]] : $\text{support}(A \Rightarrow B) = P(A \cup B)$.
- [[Confiance (règle d'association)|Confiance]] : $\text{confidence}(A \Rightarrow B) = P(B \mid A) = \dfrac{P(A \cup B)}{P(A)}$.
- [[Lift (règle d'association)|Lift]] : $\text{lift}(A \Rightarrow B) = \dfrac{\text{confidence}(A \Rightarrow B)}{P(B)} = \dfrac{P(A \cup B)}{P(A)\,P(B)}$.

Dans $P(A \cup B)$, la [[Intersection et union d'ensembles|réunion]] porte sur les items : c'est la proportion des transactions qui contiennent tous les items de $A$ **et** tous ceux de $B$. En termes d'[[Événement (probabilités)|événements]], si $E_A$ est l'événement « la transaction contient $A$ », le support vaut $P(E_A \cap E_B)$, et la confiance est la [[Probabilité conditionnelle|probabilité conditionnelle]] $P(E_B \mid E_A)$, estimée par une [[Fréquence relative|fréquence relative]]. C'est la notation du manuel de Han, Kamber et Pei (*Data Mining: Concepts and Techniques*), qu'il faut lire ainsi pour ne pas la confondre avec la réunion d'événements [[Complément hors du cours|ⓘ]]

Le lift se lit par rapport à 1 [[Complément hors du cours|ⓘ]] :

- lift $= 1$ : $A$ et $B$ sont [[Indépendance d'événements|indépendants]], la règle n'apporte rien ;
- lift $> 1$ : acheter $A$ rend $B$ plus probable que dans l'ensemble des transactions (corrélation positive) ; un lift de 2 double la probabilité de $B$ ;
- lift $< 1$ : $A$ rend $B$ moins probable (corrélation négative).

Les trois mesures se lisent dans le [[Tableau de contingence|tableau de contingence]] 2 × 2 qui croise « contient $A$ » et « contient $B$ ». Le lift est symétrique ($\text{lift}(A \Rightarrow B) = \text{lift}(B \Rightarrow A)$), contrairement à la confiance. Il corrige le principal défaut de la confiance : une règle vers un item très fréquent (le pain) a une forte confiance même sans aucun lien. Comme toute mesure de [[Covariance et corrélation|corrélation]], un lift élevé ne prouve aucune [[Corrélation et causalité|causalité]] [[Complément hors du cours|ⓘ]]

## 5. Principe : deux seuils, deux étapes

Les **itemsets fréquents** sont les motifs fréquents de l'ensemble des transactions $D$. On fixe deux paramètres :

- `minSupp` : support minimal ;
- `minConf` : confiance minimale.

Puis :

1. trouver les itemsets fréquents de toutes les longueurs, ceux de support $\geq$ `minSupp` ;
2. en tirer les règles d'association de confiance $\geq$ `minConf`.

**Exemple** : si $ABCD$ est un itemset fréquent, on peut construire la règle $AB \Rightarrow CD$, de confiance $\text{support}(ABCD)/\text{support}(AB)$, et la garder si cette confiance est $\geq$ `minConf` ; et ainsi de suite pour les autres découpages.

Toute règle tirée d'un itemset fréquent a automatiquement un support $\geq$ `minSupp` (son support est celui de l'itemset), et sa confiance se calcule sans relire la base, à partir des supports déjà comptés. C'est pourquoi tout le coût est dans l'étape 1. Un itemset de $k$ items donne $2^k - 2$ règles possibles (tous les découpages en deux parties non vides) [[Complément hors du cours|ⓘ]]

## 6. Algorithme Apriori

### Notations

- $L_k$ : ensemble des itemsets fréquents de longueur $k$.
- $C_k$ : ensemble des itemsets **candidats** de longueur $k$.
- On a $L_k \subseteq C_k$ ([[Inclusion (ensembles)|inclusion]]).

### Propriété de fermeture descendante

**Propriété** : si $X_k$ est un itemset fréquent, tous les itemsets inclus dans $X_k$ sont fréquents. [[Erreurs du cours#^e-2-association-rules|✎]]

Exemple : si $ABCD$ est fréquent, alors $ABC$, $ABD$, $ACD$, $BCD$, $AB$, $AC$, $AD$, $BC$, $BD$, $CD$, $A$, $B$, $C$, $D$ sont fréquents. [[Erreurs du cours#^e-2-association-rules|✎]]

Justification : toute transaction qui contient $X$ contient chacun de ses sous-ensembles, donc $Y \subseteq X \Rightarrow \text{support}(Y) \geq \text{support}(X)$ ; le support est **anti-monotone**. Par [[Preuve par contraposition|contraposition]], si $Y$ n'est pas fréquent, aucun sur-ensemble de $X \supseteq Y$ ne l'est : c'est la forme utilisée pour élaguer. Un itemset de $k$ items a $2^k - 1$ sous-ensembles non vides, d'où les 15 de l'exemple. Dans le [[Diagramme de Hasse|diagramme de Hasse]] des itemsets ordonnés par inclusion, les itemsets fréquents forment le « bas » du treillis, fermé vers le bas [[Complément hors du cours|ⓘ]]

### Pseudo-code

Le [[Pseudo-code|pseudo-code]] du cours :

```text
Calculer L1
k ← 2
Tant que L(k-1) ≠ ∅
    1. Ck ← apriori-gen(L(k-1))
    2. Pour chaque transaction t ∈ D
         1. Ct ← subSet(Ck, t)
         2. Pour chaque c ∈ Ct : c.count++
    3. Lk ← { c ∈ Ck | c.count × 100 / |D| ≥ minSup }
    4. k ← k + 1
Retourner ⋃k Lk
```

Les « While » du cours sur $t \in D$ et $c \in C_t$ sont des boucles « pour chaque ». À l'étape 3, `minSup` est un pourcentage ($c.\text{count} \times 100 / |D|$), alors que les exemples donnent `minSupp` en fraction ($2/4$, soit 50 %). $L_1$ se calcule par une première lecture de la base qui compte chaque item. Chaque passage de la boucle relit toute la base : Apriori fait jusqu'à une lecture de $D$ de plus que la longueur du plus grand itemset fréquent. Le [[Cardinal d'un ensemble|cardinal]] $|D|$ est le nombre de transactions [[Complément hors du cours|ⓘ]]

### apriori-gen : jointure puis suppression

**Étape de jointure** (*join*), écrite à la façon d'une requête [[Langage SQL|SQL]] :

```sql
insert into Ck
select p[1], p[2], ..., p[k-1], q[k-1]
from L(k-1) p, L(k-1) q
where p[1] = q[1], ..., p[k-2] = q[k-2], p[k-1] < q[k-1]
```

On joint deux itemsets fréquents de longueur $k-1$ qui ont les mêmes $k-2$ premiers items et diffèrent par le dernier. C'est une auto-jointure ([[Algèbre relationnelle|jointure]] d'une table avec elle-même) de $L_{k-1}$ ; la condition $p[k-1] < q[k-1]$, possible grâce à l'ordre des items, évite les doublons [[Complément hors du cours|ⓘ]]

**Étape de suppression** (*delete*, ou *prune*) : on retire de $C_k$ tout candidat dont l'un des sous-ensembles de longueur $k-1$ n'est pas dans $L_{k-1}$ (fermeture descendante) [[Complément hors du cours|ⓘ]]

Exemple du cours :

1. $L_3 = \{\{123\}, \{124\}, \{134\}, \{135\}, \{234\}\}$ ;
2. la jointure donne $C_4 = \{\{1234\}, \{1345\}\}$ ($123$ avec $124$, $134$ avec $135$) ;
3. la suppression donne $C_4 = \{\{1234\}\}$.

$\{1345\}$ est supprimé parce que ses sous-ensembles $\{145\}$ et $\{345\}$ ne sont pas dans $L_3$ ; les quatre sous-ensembles de $\{1234\}$ ($123$, $124$, $134$, $234$) y sont tous. C'est l'exemple de l'article d'Agrawal et Srikant (1994) [[Complément hors du cours|ⓘ]]

**subSet** calcule l'ensemble $C_t \subseteq C_k$ des candidats contenus dans la transaction $t$. Dans l'article d'origine, les candidats sont rangés dans un **arbre de hachage** (*hash tree*, combinant [[Arbre (théorie des graphes)|arbre]] et [[Table de hachage|table de hachage]]) pour ne pas comparer chaque transaction à tous les candidats [[Complément hors du cours|ⓘ]]

### Exemple : itemsets fréquents

| Transaction | Items |
|---|---|
| 100 | 1 3 4 |
| 200 | 2 3 5 |
| 300 | 1 2 3 5 |
| 400 | 2 5 |

Avec `minSupp` $= 2/4$ :

- itemsets fréquents : $L_1 = \{1, 2, 3, 5\}$, $L_2 = \{13, 23, 25, 35\}$, $L_3 = \{235\}$ ;
- règles d'association : $R_1 : 2 \to 35$ de confiance $2/3$, $R_2 : 3 \to 5$ de confiance $2/3$, etc.

Le déroulé, avec les comptages, est donné dans la correction de l'exercice 1.

### Limites et autres algorithmes

La [[Complexité algorithmique|complexité]] d'Apriori dépend surtout du nombre de candidats : il en génère beaucoup quand les itemsets fréquents sont longs (un itemset fréquent de 100 items impose d'avoir trouvé ses $2^{100}-1$ sous-ensembles, tous fréquents) et relit la base à chaque niveau. L'[[Algorithme FP-Growth]] (Han, Pei et Yin, 2000) évite la génération de candidats en compressant la base dans un arbre de préfixes, et Eclat (Zaki et ses coauteurs, 1997) parcourt l'espace [[Parcours en profondeur|en profondeur]] sur une représentation verticale (pour chaque item, la liste des transactions qui le contiennent). Ces algorithmes trouvent les mêmes itemsets fréquents qu'Apriori, plus vite. Ils sont disponibles dans les outils de la matière : paquet `arules` du [[Langage R|langage R]], bibliothèque `mlxtend` en [[Langage Python|Python]], Weka [[Complément hors du cours|ⓘ]]

## 7. Génération des règles

Approches descendantes (*top-down*), fondées sur la [[Redondance des règles d'association|redondance des règles]].

### Redondance simple

On teste d'abord, pour un itemset fréquent donné, les règles qui ont le moins de conditions à gauche. Exemple :

- $R_1 : A \Rightarrow B, C$
- $R_2 : A, B \Rightarrow C$

$\text{confidence}(R_1) = \text{support}(ABC)/\text{support}(A)$ et $\text{confidence}(R_2) = \text{support}(ABC)/\text{support}(AB)$, donc $\text{confidence}(R_2) \geq \text{confidence}(R_1)$. [[Erreurs du cours#^e-2-association-rules|✎]]

### Redondance stricte

On commence la recherche des règles par les itemsets les plus longs. Exemple :

- $R_1 : A \Rightarrow B, C, D$
- $R_2 : A \Rightarrow B, C$

$\text{confidence}(R_1) = \text{support}(ABCD)/\text{support}(A)$ et $\text{confidence}(R_2) = \text{support}(ABC)/\text{support}(A)$, donc $\text{confidence}(R_2) \geq \text{confidence}(R_1)$. [[Erreurs du cours#^e-2-association-rules|✎]]

### Ce qu'on en tire

Les deux inégalités viennent de l'anti-monotonie du support : $\text{support}(AB) \leq \text{support}(A)$ et $\text{support}(ABCD) \leq \text{support}(ABC)$. L'égalité est possible (exercice 1 : $2 \to 35$ et $25 \to 3$ ont la même confiance $2/3$, parce que les items 2 et 5 apparaissent toujours ensemble). On en déduit deux règles d'élagage [[Complément hors du cours|ⓘ]] :

- **redondance simple** : si $A \Rightarrow BC$ est valide (confiance $\geq$ `minConf`), alors $AB \Rightarrow C$ et $AC \Rightarrow B$ le sont aussi, sans calcul ; elles sont dites redondantes, car déduites d'une règle plus générale. À l'inverse, si $AB \Rightarrow C$ échoue, $A \Rightarrow BC$ échoue aussi ;
- **redondance stricte** : si $A \Rightarrow BCD$ est valide, $A \Rightarrow BC$, $A \Rightarrow B$, etc. le sont aussi. À l'inverse, si $A \Rightarrow BC$ échoue, $A \Rightarrow BCD$ échoue aussi.

Chaque règle déduite est une [[Implication logique|implication]] de moins à tester ; le gain dépend du seuil, comme le montre l'exercice 1. Les règles d'association sont la base des [[Système de recommandation|systèmes de recommandation]] simples (« les clients qui ont acheté ceci ont aussi acheté… ») et de l'organisation des rayons ou des promotions croisées en [[Marketing|marketing]] [[Complément hors du cours|ⓘ]]

## 8. Exercices

Le cours ne donne pas de correction ; les corrections ci-dessous sont ajoutées, calculs vérifiés [[Complément hors du cours|ⓘ]]

### Exercice 1

Base $D$ : 100 = {1, 3, 4}, 200 = {2, 3, 5}, 300 = {1, 2, 3, 5}, 400 = {2, 5}.

1. Appliquer l'algorithme Apriori pour extraire les itemsets fréquents avec `minSupp` $= 2/4$.
2. Générer les règles d'association avec `minConf` $= 1$, puis avec `minConf` $= 0{,}5$, par les méthodes de la redondance simple et stricte. Comparer les nombres de tests effectués.
3. Expliquer deux utilisations possibles de ces méthodes de redondance, qui peuvent correspondre à des stratégies optimiste ou pessimiste.

**Correction** [[Complément hors du cours|ⓘ]]

1. Seuil : au moins 2 transactions sur 4.
   - $C_1$ : 1 (2), 2 (3), 3 (3), 4 (1), 5 (3) ; $L_1 = \{1, 2, 3, 5\}$.
   - $C_2$ (toutes les paires de $L_1$) : 12 (1), 13 (2), 15 (1), 23 (2), 25 (3), 35 (2) ; $L_2 = \{13, 23, 25, 35\}$.
   - Jointure : seuls $23$ et $25$ partagent leur premier item, d'où $C_3 = \{235\}$ ; ses sous-ensembles $23$, $25$, $35$ sont dans $L_2$, il reste. Support 2 : $L_3 = \{235\}$. $C_4$ est vide, fin.
2. Les 14 règles possibles et leur confiance :

   | Itemset | Règles (confiance) |
   |---|---|
   | 13 | $1 \to 3$ (1), $3 \to 1$ (2/3) |
   | 23 | $2 \to 3$ (2/3), $3 \to 2$ (2/3) |
   | 25 | $2 \to 5$ (1), $5 \to 2$ (1) |
   | 35 | $3 \to 5$ (2/3), $5 \to 3$ (2/3) |
   | 235 | $2 \to 35$, $3 \to 25$, $5 \to 23$ (2/3 chacune) ; $23 \to 5$ (1), $25 \to 3$ (2/3), $35 \to 2$ (1) |

   - `minConf` $= 1$ : 5 règles, $1 \to 3$, $2 \to 5$, $5 \to 2$, $23 \to 5$, $35 \to 2$.
   - `minConf` $= 0{,}5$ : les 14 règles.
   - Tests, sans élagage : 14 dans les deux cas. Avec la redondance simple (règles à un antécédent d'abord) : à 0,5, les trois règles $2 \to 35$, $3 \to 25$, $5 \to 23$ passent et valident les trois règles à deux antécédents, soit 8 + 3 = 11 tests ; à 1, elles échouent toutes, il faut tester les trois autres, soit 14 tests. Avec la redondance stricte (itemset le plus long d'abord) : à 0,5, les trois règles à un antécédent de $235$ passent et valident les six règles à un antécédent de $23$, $25$ et $35$, il ne reste que $1 \to 3$ et $3 \to 1$, soit 6 + 2 = 8 tests ; à 1, rien n'est déduit, 14 tests.
3. **Stratégie optimiste** : partir des règles les plus générales (moins d'antécédents, ou conséquent le plus long) en pariant qu'elles passent ; chaque succès valide sans calcul les règles plus spécifiques. Elle paie quand `minConf` est bas (8 ou 11 tests au lieu de 14 à 0,5) et ne gagne rien quand il est haut. **Stratégie pessimiste** : utiliser les mêmes inégalités dans l'autre sens, en partant des règles de plus forte confiance (plus d'antécédents, ou conséquent le plus court) et en pariant qu'elles échouent ; chaque échec élimine sans calcul les règles plus générales. Ainsi, à `minConf` $= 1$, l'échec de $25 \to 3$ élimine $2 \to 35$ et $5 \to 23$ ; elle paie quand le seuil est haut.

### Exercice 2

Base $D$ d'achats de produits parmi $\{A, B, C, D, E\}$ : 1 = AD, 2 = ABC, 3 = AE, 4 = ADE, 5 = BD.

1. En ne considérant que $\{A, B, C\}$, trouver les règles qui prédisent l'achat de deux produits en améliorant la prédiction par rapport à la mesure statistique induite par la base. Calculer la confiance et le lift de chaque règle, et donner une signification à la valeur du lift.
2. Même question pour les règles qui prédisent l'achat d'un produit.

**Correction** [[Complément hors du cours|ⓘ]]

Supports sur 5 transactions : $A = 4/5$, $B = 2/5$, $C = 1/5$, $AB = AC = BC = ABC = 1/5$. « Améliorer la prédiction par rapport à la base » veut dire : confiance supérieure à la probabilité du conséquent, soit un lift $> 1$.

1. Conséquent de deux produits :

   | Règle | Confiance | Lift |
   |---|---|---|
   | $A \to BC$ | 1/4 | 1,25 |
   | $B \to AC$ | 1/2 | 2,5 |
   | $C \to AB$ | 1 | 5 |

   Les trois ont un lift $> 1$ et sont retenues. $C \to AB$ : le client qui achète $C$ achète aussi $A$ et $B$ ; la probabilité d'acheter $A$ et $B$ passe de $P(AB) = 1/5$ à 1, d'où un lift de 5.
2. Conséquent d'un produit :

   | Règle | Confiance | Lift |
   |---|---|---|
   | $A \to B$ | 1/4 | 0,625 |
   | $B \to A$ | 1/2 | 0,625 |
   | $A \to C$ | 1/4 | 1,25 |
   | $C \to A$ | 1 | 1,25 |
   | $B \to C$ | 1/2 | 2,5 |
   | $C \to B$ | 1 | 2,5 |
   | $AB \to C$ | 1 | 5 |
   | $AC \to B$ | 1 | 2,5 |
   | $BC \to A$ | 1 | 1,25 |

   Toutes sont retenues sauf $A \to B$ et $B \to A$ : leur lift $< 1$ signale une corrélation négative (acheter $A$ rend $B$ moins probable). Bien que $B \to A$ ait une confiance de 1/2, elle fait moins bien que la fréquence de base de $A$ ($P(A) = 4/5$). On vérifie la symétrie du lift : $A \to C$ et $C \to A$ ont le même.

### Exercice 3

| Transaction | Items |
|---|---|
| T1 | HotDogs, Buns, Ketchup |
| T2 | HotDogs, Buns |
| T3 | HotDogs, Coca, Chips |
| T4 | Chips, Coca |
| T5 | Chips, Ketchup |
| T6 | HotDogs, Coca, Chips |

1. Appliquer l'algorithme Apriori pour extraire les itemsets fréquents avec `minSupp` $= 1/3$.
2. Générer les règles d'association avec `minConf` $= 2/3$.

**Correction** [[Complément hors du cours|ⓘ]]

1. Seuil : au moins 2 transactions sur 6.
   - $L_1$ : HotDogs (4), Buns (2), Ketchup (2), Coca (3), Chips (4), tous fréquents.
   - $C_2$ : les $\binom{5}{2} = 10$ paires ([[Coefficient binomial]]). Fréquentes : {HotDogs, Buns} (2), {HotDogs, Coca} (2), {HotDogs, Chips} (2), {Coca, Chips} (3). Les autres ont un support de 0 ou 1.
   - $C_3$ : la jointure des paires commençant par HotDogs donne {HotDogs, Buns, Coca}, {HotDogs, Buns, Chips} et {HotDogs, Coca, Chips} ; les deux premiers sont supprimés ({Buns, Coca} et {Buns, Chips} ne sont pas fréquents). {HotDogs, Coca, Chips} a un support de 2 (T3, T6) : $L_3$ = {HotDogs, Coca, Chips}. $C_4$ est vide.
2. Règles de confiance $\geq 2/3$ (8 sur 14) :

   | Règle | Confiance | Lift |
   |---|---|---|
   | Buns → HotDogs | 1 | 1,5 |
   | Coca → HotDogs | 2/3 | 1 |
   | Coca → Chips | 1 | 1,5 |
   | Chips → Coca | 3/4 | 1,5 |
   | Coca → HotDogs, Chips | 2/3 | 2 |
   | HotDogs, Coca → Chips | 1 | 1,5 |
   | HotDogs, Chips → Coca | 1 | 2 |
   | Coca, Chips → HotDogs | 2/3 | 1 |

   Rejetées (confiance 1/2) : HotDogs → Buns ; HotDogs → Coca ; HotDogs → Chips ; Chips → HotDogs ; HotDogs → {Coca, Chips} ; Chips → {HotDogs, Coca}. Coca → HotDogs et Coca, Chips → HotDogs passent le seuil avec un lift de 1 : leur conséquent est aussi probable sans elles ($P(\text{HotDogs}) = 4/6 = 2/3$), elles n'apprennent rien. C'est la limite de la confiance seule, que le lift fait voir.

## Concepts

[[Règle d'association]], [[Algorithme Apriori]], [[Itemset fréquent]], [[Transaction (fouille de données)]], [[Support (règle d'association)]], [[Confiance (règle d'association)]], [[Lift (règle d'association)]], [[Propriété de fermeture descendante]], [[Redondance des règles d'association]], [[Analyse du panier de la ménagère]], [[Algorithme FP-Growth]], [[Explosion combinatoire]], [[Système de recommandation]], [[Régression (apprentissage automatique)]], [[Résumé de données]], [[Extraction de motifs séquentiels]], [[Algèbre relationnelle]]
