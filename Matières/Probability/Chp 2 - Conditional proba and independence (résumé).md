---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les énoncés et démonstrations, donnés en images, sont recopiés en LaTeX ; les deux schémas sont intégrés.

## Idée générale

Mesurer un événement une fois qu'on sait qu'un autre a eu lieu, puis en déduire trois outils : la règle de multiplication, les probabilités totales et le théorème de Bayes. Le chapitre finit sur l'indépendance.

## Probabilité conditionnelle

**Définition ([[Probabilité conditionnelle|conditional probability]]).** Pour deux événements $A, B$ avec $P(B) > 0$, la probabilité conditionnelle de $A$ sachant que $B$ s'est produit (*given that B has occurred*) est notée $P(A|B)$ et vaut :
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
On dit aussi « probabilité de $A$ sachant $B$ » (*given B*).

**Interprétation.** Dans une expérience à issues [[Équiprobabilité|équiprobables]] (*equally likely outcomes*), la probabilité conditionnelle est la probabilité de $A$ relativement à $B$ : conditionner sur $B$, c'est prendre $B$ comme nouvel [[Espace probabilisé|espace d'échantillonnage]] ; de $A$ il ne reste que $A \cap B$.

![[Chp 2 - Conditional proba and independence - image7.png]]
*Figure : conditionner sur $B$ (*"conditioning" on event B*) — $B$ devient le nouveau *sample space*, et $A \cap B$ est ce qui reste de l'événement $A$.*

## Règle de multiplication (*multiplication rule*)

De la définition :
$$P(A|B) = \frac{P(A \cap B)}{P(B)} \;\Rightarrow\; P(A \cap B) = P(A|B)\,P(B)$$
et symétriquement :
$$P(A \cap B) = P(B|A)\,P(A)$$

**Usage.** Très utile quand l'expérience se fait en plusieurs étapes successives : $B$ est le résultat de la première étape, $A$ celui de la deuxième.

**Généralisation à trois étapes** ($A_1$, $A_2$, $A_3$ résultats des étapes 1, 2, 3) :
$$P(A_1 \cap A_2 \cap A_3) = P(A_3 | A_1 \cap A_2)\,P(A_1 \cap A_2) = P(A_3 | A_1 \cap A_2)\,P(A_2 | A_1)\,P(A_1)$$

## Loi des probabilités totales (*law of total probability*)

**Définition.** Des événements $A_1, \dots, A_n$ d'un espace $S$ sont **exhaustifs** (*exhaustive*) si
$$A_1 \cup A_2 \cup \dots \cup A_n = S$$

**Théorème (probabilités totales).** Soit $A_1, \dots, A_n$ des événements [[Événements incompatibles|mutuellement exclusifs]] (*mutually exclusive*) et exhaustifs de $S$ (une [[Partition d'un ensemble|partition]] de $S$). Alors pour tout autre événement $B$ de $S$ :
$$P(B) = P(B|A_1)P(A_1) + P(B|A_2)P(A_2) + \dots + P(B|A_n)P(A_n) = \sum_{i=1}^{n} P(B|A_i)\,P(A_i)$$

![[Chp 2 - Conditional proba and independence - image14.png]]
*Figure : le rectangle $S$ partitionné en $A_1, A_2, A_3, A_4$ ; l'ellipse $B$ recoupe les quatre régions, et ses morceaux $B \cap A_i$ sont hachurés.*

## Théorème de Bayes (« el meilleur théorème des proba », d'après la note)

**Théorème.** Soit $A_1, \dots, A_n$ des événements mutuellement exclusifs et exhaustifs de $S$, avec $P(A_i) > 0$ pour tout $i = 1, \dots, n$. Pour tout autre événement $B$ de $S$ tel que $P(B) > 0$ :
$$P(A_j|B) = \frac{P(A_j \cap B)}{P(B)} = \frac{P(B|A_j)\,P(A_j)}{\sum_{i=1}^{k} P(B|A_i)\,P(A_i)}, \qquad j = 1, \dots, k$$
($k$ et $n$ désignent le même nombre, voir Points à vérifier). Le numérateur vient de la règle de multiplication, le dénominateur des probabilités totales.

## Indépendance d'événements (*independence of events*)

**Définition.** Deux événements $A, B$ sont **indépendants** si $P(A|B) = P(A)$, et **dépendants** sinon. Si $A$ et $B$ sont indépendants, on a aussi $P(B|A) = P(B)$. Voir [[Indépendance d'événements]].

**Conséquence.** $A$ et $B$ sont indépendants si et seulement si
$$P(A \cap B) = P(A)\,P(B)$$

**Propriété.** Si $A$ et $B$ sont indépendants, alors :
1. $A^c$ et $B$ sont indépendants ;
2. $A$ et $B^c$ sont indépendants ;
3. $A^c$ et $B^c$ sont indépendants.

### Démonstrations du cours (manuscrites)

**i) $A^c$ et $B$.** Il faut montrer $P(A^c|B) = P(A^c)$. Lemme (encadré) : $P(B) = P(B \cap A) + P(B \cap A^c)$, donc $P(A^c \cap B) = P(B) - P(A \cap B)$. Alors :
$$P(A^c|B) = \frac{P(A^c \cap B)}{P(B)} = \frac{P(B) - P(A \cap B)}{P(B)} = 1 - \frac{P(A \cap B)}{P(B)} \underset{A, B \text{ indép.}}{=} 1 - \frac{P(A)\,P(B)}{P(B)} = 1 - P(A) = P(A^c)$$
Donc $A^c$ et $B$ sont indépendants.

**ii) $A$ et $B^c$.** Il suffit de montrer $P(A|B^c) = P(A)$ (ou $P(B^c|A) = P(B^c)$) :
$$P(A|B^c) = \frac{P(A \cap B^c)}{P(B^c)} = \frac{P(A) - P(A \cap B)}{P(B^c)} = \frac{P(A) - P(A)P(B)}{P(B^c)} = \frac{P(A)\,(1 - P(B))}{P(B^c)} = \frac{P(A)\,P(B^c)}{P(B^c)} = P(A)$$
Donc $A$ et $B^c$ sont indépendants.

**iii) $A^c$ et $B^c$.** En utilisant ii) appliqué au couple ($A^c$, $B$), indépendant d'après i) :
$$P(A^c|B^c) = \frac{P(A^c \cap B^c)}{P(B^c)} = \frac{P(A^c) - P(A^c \cap B)}{P(B^c)} = \frac{P(A^c) - P(A^c)P(B)}{P(B^c)} = \frac{P(A^c)\,(1 - P(B))}{P(B^c)} = \frac{P(A^c)\,P(B^c)}{P(B^c)} = P(A^c)$$
Donc $A^c$ et $B^c$ sont indépendants.

Le chapitre ne contient ni exemple numérique ni exercice.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition de la probabilité conditionnelle** : la transcription lit « P(A) is the probability of A given B ». Il faudrait $P(A|B)$. Vérifié sur l'image le 2026-11-06 : l'image écrit bien « P(A) » ; c'est une coquille du cours.
2. **Bornes dans Bayes** : l'énoncé parle de $A_1, \dots, A_n$, mais la formule somme jusqu'à $k$ et fait varier $j$ jusqu'à $k$. Cette alerte de la transcription est fondée sur le texte lu : $n$ et $k$ désignent la même chose (complément).
3. **Démonstration du cas $(A, B^c)$** : elle utilise $P(A \cap B^c) = P(A) - P(A \cap B)$ sans la justifier à part, comme pour le premier cas. Le cours ne l'écrit pas ici. Le résultat est juste.
4. **Indépendance et événements incompatibles** : le cours ne dit pas que deux événements disjoints de probabilité non nulle ne sont jamais indépendants. Le wiki ne l'affirme donc pas non plus.
5. **Démonstration du cas $(A^c, B^c)$** : l'étape $P(A^c \cap B) = P(A^c)P(B)$ suppose l'indépendance de $A^c$ et $B$, établie au cas i) ; le cours ne le dit pas explicitement (complément). La transcription signale aussi une flèche vers $(1 - P(B))$ et un petit triangle coupé en haut de l'image, sans incidence.
6. **Coquilles de l'image** : « ocurred » et « cna » (pour *can*) dans les images du cours.
