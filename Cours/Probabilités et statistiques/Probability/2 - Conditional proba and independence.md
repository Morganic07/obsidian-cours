---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les énoncés et démonstrations, donnés en images, sont recopiés en LaTeX ; les deux schémas sont intégrés.

## Idée générale

Mesurer un événement une fois qu'on sait qu'un autre a eu lieu, puis en déduire trois outils : la règle de multiplication, les probabilités totales et le théorème de Bayes. Le chapitre finit sur l'indépendance.

## Probabilité conditionnelle

**Définition ([[Probabilité conditionnelle|conditional probability]]).** Pour deux événements $A, B$ avec $P(B) > 0$, la probabilité conditionnelle de $A$ sachant que $B$ s'est produit (*given that B has occurred*) est notée $P(A|B)$ et vaut :
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
On dit aussi que $P(A|B)$ est la « probabilité de $A$ sachant $B$ » (*given B*). [[Erreurs du cours#^e-2-conditional-proba-and-independence|✎]]

**Interprétation.** Dans une expérience à issues [[Équiprobabilité|équiprobables]] (*equally likely outcomes*), la probabilité conditionnelle est la probabilité de $A$ relativement à $B$ : conditionner sur $B$, c'est prendre $B$ comme nouvel [[Espace probabilisé|espace d'échantillonnage]] ; de $A$ il ne reste que $A \cap B$.

![[Chp 2 - Conditional proba and independence - image7.png]]
*Figure : conditionner sur $B$ (*"conditioning" on event B*) — $B$ devient le nouveau *sample space*, et $A \cap B$ est ce qui reste de l'événement $A$.*

Exemple : on lance un dé équilibré ; $A$ = « faire 6 », $B$ = « faire un nombre pair ». Sans information, $P(A) = 1/6$ ; sachant que le résultat est pair, il ne reste que 3 issues possibles, $\{2, 4, 6\}$, d'où $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/6}{1/2} = \frac{1}{3}$. L'information « pair » a doublé la probabilité de $A$. [[Complément hors du cours|ⓘ]]

Pour $B$ fixé, l'application $A \mapsto P(A|B)$ est elle-même une probabilité : elle vérifie les axiomes du [[1 - Sample space,events, proba|chapitre 1]] ($P(S|B) = 1$, additivité). Toutes les propriétés vues alors s'appliquent donc telles quelles « sachant $B$ », par exemple $P(A^c|B) = 1 - P(A|B)$. [[Complément hors du cours|ⓘ]]

En général, $P(A|B) \neq P(B|A)$ : la probabilité qu'un animal soit un chat sachant qu'il a quatre pattes n'est pas celle qu'il ait quatre pattes sachant que c'est un chat (qui vaut presque 1). Les deux sont reliées par le théorème de Bayes, ci-dessous ; les confondre est une erreur de raisonnement classique, dite **sophisme du procureur** quand elle porte sur une preuve judiciaire. [[Complément hors du cours|ⓘ]]

## Règle de multiplication (*multiplication rule*)

De la définition :
$$P(A|B) = \frac{P(A \cap B)}{P(B)} \;\Rightarrow\; P(A \cap B) = P(A|B)\,P(B)$$
et symétriquement :
$$P(A \cap B) = P(B|A)\,P(A)$$

**Usage.** Très utile quand l'expérience se fait en plusieurs étapes successives : $B$ est le résultat de la première étape, $A$ celui de la deuxième.

**Généralisation à trois étapes** ($A_1$, $A_2$, $A_3$ résultats des étapes 1, 2, 3) :
$$P(A_1 \cap A_2 \cap A_3) = P(A_3 | A_1 \cap A_2)\,P(A_1 \cap A_2) = P(A_3 | A_1 \cap A_2)\,P(A_2 | A_1)\,P(A_1)$$

Pour $n$ étapes, c'est la **formule des probabilités composées**, valable dès que $P(A_1 \cap \dots \cap A_{n-1}) > 0$ (pour que tous les conditionnements aient un sens) : [[Complément hors du cours|ⓘ]]
$$P(A_1 \cap \dots \cap A_n) = P(A_1)\,P(A_2|A_1)\,P(A_3|A_1 \cap A_2) \cdots P(A_n|A_1 \cap \dots \cap A_{n-1})$$

Exemple : une urne contient 3 boules rouges et 2 noires ; on en tire trois, sans remise. Probabilité de tirer trois rouges : $P(R_1 \cap R_2 \cap R_3) = \frac{3}{5} \cdot \frac{2}{4} \cdot \frac{1}{3} = \frac{1}{10}$. Chaque facteur est une proportion dans l'urne telle qu'elle est après les tirages précédents. On retrouve le résultat par [[Dénombrement|dénombrement]] : $\binom{3}{3} / \binom{5}{3} = 1/10$ (voir [[3 - Combinatorics]]). [[Complément hors du cours|ⓘ]]

En pratique, on représente une expérience en plusieurs étapes par un **arbre pondéré** : chaque branche porte la probabilité conditionnelle de son étape sachant le chemin qui y mène. La probabilité d'un chemin est le produit des probabilités le long de ce chemin (règle de multiplication), et la somme des probabilités des branches issues d'un même nœud vaut 1. [[Complément hors du cours|ⓘ]]

## Loi des probabilités totales (*law of total probability*)

**Définition.** Des événements $A_1, \dots, A_n$ d'un espace $S$ sont **exhaustifs** (*exhaustive*) si
$$A_1 \cup A_2 \cup \dots \cup A_n = S$$

**Théorème (probabilités totales).** Soit $A_1, \dots, A_n$ des événements [[Événements incompatibles|mutuellement exclusifs]] (*mutually exclusive*) et exhaustifs de $S$ (une [[Partition d'un ensemble|partition]] de $S$). Alors pour tout autre événement $B$ de $S$ :
$$P(B) = P(B|A_1)P(A_1) + P(B|A_2)P(A_2) + \dots + P(B|A_n)P(A_n) = \sum_{i=1}^{n} P(B|A_i)\,P(A_i)$$

![[Chp 2 - Conditional proba and independence - image14.png]]
*Figure : le rectangle $S$ partitionné en $A_1, A_2, A_3, A_4$ ; l'ellipse $B$ recoupe les quatre régions, et ses morceaux $B \cap A_i$ sont hachurés.*

**Pourquoi c'est vrai.** Comme les $A_i$ forment une partition, $B$ est l'union **disjointe** des morceaux $B \cap A_i$ (ceux de la figure). L'additivité donne $P(B) = \sum_i P(B \cap A_i)$, et la règle de multiplication remplace chaque terme par $P(B|A_i)\,P(A_i)$. Le cas le plus courant est la partition $\{A, A^c\}$ : $P(B) = P(B|A)\,P(A) + P(B|A^c)\,P(A^c)$ ; le lemme encadré des démonstrations ci-dessous, $P(B) = P(B \cap A) + P(B \cap A^c)$, en est la première étape. Sur un arbre pondéré, la formule revient à additionner les probabilités de tous les chemins qui mènent à $B$. Une telle partition s'appelle aussi un **système complet d'événements**. [[Complément hors du cours|ⓘ]]

## Théorème de Bayes (« el meilleur théorème des proba », d'après la note)

**Théorème.** Soit $A_1, \dots, A_n$ des événements mutuellement exclusifs et exhaustifs de $S$, avec $P(A_i) > 0$ pour tout $i = 1, \dots, n$. Pour tout autre événement $B$ de $S$ tel que $P(B) > 0$ : [[Erreurs du cours#^e-2-conditional-proba-and-independence|✎]]
$$P(A_j|B) = \frac{P(A_j \cap B)}{P(B)} = \frac{P(B|A_j)\,P(A_j)}{\sum_{i=1}^{n} P(B|A_i)\,P(A_i)}, \qquad j = 1, \dots, n$$
Le numérateur vient de la règle de multiplication, le dénominateur des probabilités totales.

**Vocabulaire.** Bayes « renverse » le conditionnement : il donne $P(\text{cause}|\text{effet})$ à partir des $P(\text{effet}|\text{cause})$. $P(A_j)$ est la probabilité **a priori** (*prior*) de la cause $A_j$, avant l'observation ; $P(B|A_j)$ est la **vraisemblance** (*likelihood*) de l'observation $B$ sous cette cause ; $P(A_j|B)$ est la probabilité **a posteriori** (*posterior*), mise à jour par l'observation. Le dénominateur est le même pour tous les $j$ : a posteriori ∝ vraisemblance × a priori. Le résultat vient d'un texte de Thomas Bayes publié en 1763 et a été généralisé par Laplace ; il fonde la statistique dite **bayésienne**. Voir [[Probabilité conditionnelle]] et [[Vraisemblance]]. [[Complément hors du cours|ⓘ]]

**Exemple classique : le test de dépistage.** Une maladie touche 1 % de la population ; le test est positif chez 99 % des malades (**sensibilité**) et négatif chez 95 % des non-malades (**spécificité**), donc faussement positif chez 5 % d'entre eux. Avec $M$ = « malade » et $+$ = « test positif » : [[Complément hors du cours|ⓘ]]
$$P(+) = P(+|M)P(M) + P(+|M^c)P(M^c) = 0{,}99 \times 0{,}01 + 0{,}05 \times 0{,}99 = 0{,}0594$$
$$P(M|+) = \frac{P(+|M)\,P(M)}{P(+)} = \frac{0{,}0099}{0{,}0594} = \frac{1}{6} \approx 0{,}17$$
Malgré un test fiable à 99 %, cinq positifs sur six ne sont pas malades : la maladie est si rare que les faux positifs (5 % de 99 % de la population) sont bien plus nombreux que les vrais positifs. Négliger la probabilité a priori s'appelle l'**oubli du taux de base** (*base rate fallacy*). Pour le lien avec les tests statistiques, voir [[Erreur de type I et de type II]]. [[Complément hors du cours|ⓘ]]

**Le problème de Monty Hall.** Un jeu télévisé propose trois portes : une voiture derrière l'une, une chèvre derrière les deux autres. Le candidat choisit la porte 1 ; l'animateur, qui sait où est la voiture, ouvre une autre porte, toujours sur une chèvre (disons la 3), et propose de changer. Avec $C_i$ = « la voiture est derrière la porte $i$ » ($P(C_i) = 1/3$) et $O_3$ = « l'animateur ouvre la 3 » : $P(O_3|C_1) = 1/2$ (il choisit au hasard entre 2 et 3), $P(O_3|C_2) = 1$, $P(O_3|C_3) = 0$. Donc $P(O_3) = \frac{1}{3}\big(\frac{1}{2} + 1 + 0\big) = \frac{1}{2}$ et [[Complément hors du cours|ⓘ]]
$$P(C_2|O_3) = \frac{1 \times 1/3}{1/2} = \frac{2}{3}, \qquad P(C_1|O_3) = \frac{1/2 \times 1/3}{1/2} = \frac{1}{3}$$
Changer de porte double les chances de gagner, contre l'intuition du « une chance sur deux ». Le résultat dépend de la règle suivie par l'animateur : s'il ouvrait une porte au hasard et tombait par chance sur une chèvre, les deux portes restantes seraient équiprobables. [[Complément hors du cours|ⓘ]]

## Indépendance d'événements (*independence of events*)

**Définition.** Deux événements $A, B$ sont **indépendants** si $P(A|B) = P(A)$, et **dépendants** sinon. Si $A$ et $B$ sont indépendants, on a aussi $P(B|A) = P(B)$. Voir [[Indépendance d'événements]].

**Conséquence.** $A$ et $B$ sont indépendants si et seulement si
$$P(A \cap B) = P(A)\,P(B)$$

La définition par $P(A|B) = P(A)$ suppose $P(B) > 0$ ; la forme produit n'a pas cette restriction, c'est pourquoi la plupart des manuels la prennent comme définition. Avec elle, un événement de probabilité nulle (ou égale à 1) est indépendant de tout événement. [[Complément hors du cours|ⓘ]]

Exemple : on tire une carte dans un jeu de 52 ; $A$ = « as », $B$ = « cœur ». $P(A \cap B) = \frac{1}{52} = \frac{4}{52} \times \frac{13}{52} = P(A)\,P(B)$ : savoir que la carte est un cœur ne change pas la probabilité que ce soit un as. L'indépendance est une propriété des **probabilités**, pas seulement de l'expérience : elle se vérifie par le calcul. [[Complément hors du cours|ⓘ]]

**Indépendant n'est pas incompatible.** Si $A$ et $B$ sont [[Événements incompatibles|incompatibles]] ($A \cap B = \emptyset$) et de probabilités non nulles, alors $P(A \cap B) = 0 \neq P(A)\,P(B)$ : ils sont **dépendants**, et même fortement, puisque savoir que $B$ s'est produit garantit que $A$ ne s'est pas produit. [[Complément hors du cours|ⓘ]]

**Plus de deux événements.** $A_1, \dots, A_n$ sont **mutuellement indépendants** si, pour toute sous-famille $A_{i_1}, \dots, A_{i_k}$ ($2 \le k \le n$, indices distincts), $P(A_{i_1} \cap \dots \cap A_{i_k}) = P(A_{i_1}) \cdots P(A_{i_k})$. L'indépendance deux à deux ne suffit pas. Contre-exemple : deux lancers d'une pièce équilibrée, $A$ = « pile au 1ᵉʳ », $B$ = « pile au 2ᵉ », $C$ = « les deux résultats sont égaux ». Chacun a probabilité $1/2$, chaque intersection de deux d'entre eux probabilité $1/4$ (indépendance deux à deux), mais $P(A \cap B \cap C) = P(\{PP\}) = 1/4 \neq 1/8$. [[Complément hors du cours|ⓘ]]

En pratique, on **suppose** souvent l'indépendance d'après la façon dont l'expérience est faite (lancers successifs d'un dé, tirages avec remise), et elle permet de multiplier les probabilités. Pour des variables aléatoires, voir [[Indépendance de variables aléatoires]]. [[Complément hors du cours|ⓘ]]

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