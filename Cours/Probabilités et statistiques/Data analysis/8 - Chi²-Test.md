---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

La loi du χ² sert à deux choses : estimer et tester une variance, et tester l'indépendance de deux variables catégorielles sur un tableau croisé. Le second usage est le [[Test du χ²]].

## Présentation de la loi du χ²

**Question du cours** : que dire de la **somme des carrés** $x_1^2 + x_2^2 + \dots + x_n^2$ de valeurs tirées d'une loi normale ? [[Erreurs du cours#^e-8-chi2-test|✎]]

**Réponse** : les statisticiens ont montré que **si $X$ est normale centrée réduite**, la [[Somme des carrés (SST, SSR, SSE)|somme des carrés]] de $n$ valeurs indépendantes $x_i$ suit une **loi du $\chi^2$ à $n$ degrés de liberté** ; la somme des carrés des écarts à la moyenne, $\sum (x_i - \bar{x})^2/\sigma^2$, suit une **loi du $\chi^2$ à $(n-1)$ degrés de liberté**. [[Erreurs du cours#^e-8-chi2-test|✎]]

Voir [[Loi du khi-deux]].

- La loi du $\chi^2$ est une variable aléatoire continue à $n-1$ [[Variance et écart-type d'échantillon|degrés de liberté]].
- Elle est toujours **asymétrique à droite** (*right tailed*).
- Elle devient symétrique et se rapproche de la loi normale quand $n$ augmente.

![[Séance 8 - Chi²-Test - image3.png]]

*Figure : densités $f_k(x)$ de la loi $\chi^2_k$ pour $k$ = 1, 2, 3, 4, 6, 9 ; le maximum s'abaisse et se décale vers la droite quand $k$ augmente.*

Densité ($k$ = degrés de liberté), avec la [[Fonction Gamma]] :

$$f_k(x) = \frac{1}{2^{k/2}\Gamma(k/2)}\, x^{k/2-1} e^{-x/2} \qquad \Gamma(x) = \int_0^{\infty} t^{x-1} e^{-t}\, dt$$

**Théorème** : soit $X_1, \ldots, X_n$ un échantillon aléatoire d'une [[Loi normale|loi normale]] de moyenne $\mu$ et de variance $\sigma^2$, et $S^2$ la variance d'échantillon. Alors

$$X^2 = \frac{(n-1)\,S^2}{\sigma^2}$$

suit une loi du $\chi^2$ à $n-1$ degrés de liberté.

Si l'on connaissait $\mu$, $\sum (X_i - \mu)^2/\sigma^2$ serait une somme de $n$ carrés de normales centrées réduites indépendantes, donc un $\chi^2_n$. Remplacer $\mu$ par $\bar X$ fait perdre un degré de liberté, car les écarts $X_i - \bar X$ sont liés par $\sum (X_i - \bar X) = 0$ : il ne reste que $n-1$ carrés « libres ». Le théorème établit aussi que $\bar X$ et $S^2$ sont indépendants, ce qui sert à construire la [[Loi de Student|loi de Student]] ([[6 - T-Test]]). [[Complément hors du cours|ⓘ]]

La **moyenne** de la loi du $\chi^2$ est $k$ et sa **variance** $2k$.

## Intervalle de confiance de la variance

Si $s^2$ est la variance d'un échantillon aléatoire de $n$ observations d'une loi normale de variance inconnue $\sigma^2$, un [[Intervalle de confiance|intervalle de confiance]] à $100(1-\alpha)$ % de $\sigma^2$ est :

$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}}$$

où $\chi^2_{\alpha/2,\,n-1}$ et $\chi^2_{1-\alpha/2,\,n-1}$ sont les points de pourcentage supérieur et inférieur à $100\alpha/2$ % de la loi du $\chi^2$ à $n-1$ degrés de liberté. L'intervalle de confiance de **$\sigma$** a pour bornes les racines carrées de ces bornes.

Pourquoi le grand quantile est au dénominateur de la borne inférieure : on part de $P\left(\chi^2_{1-\alpha/2} \leq \dfrac{(n-1)S^2}{\sigma^2} \leq \chi^2_{\alpha/2}\right) = 1 - \alpha$ et on isole $\sigma^2$, ce qui inverse les inégalités. L'intervalle n'est pas centré sur $s^2$, puisque la loi du $\chi^2$ n'est pas symétrique. [[Complément hors du cours|ⓘ]]

Exemple chiffré : $n = 11$ observations, $s^2 = 4$, intervalle à 95 %, donc 10 degrés de liberté. Dans la table du cours, la colonne 0,025 donne 3,25 et la colonne 0,975 donne 20,48 (les en-têtes de la table sont des aires **à gauche**, alors que la notation $\chi^2_{\alpha/2}$ désigne le point qui laisse $\alpha/2$ **à droite** : $\chi^2_{0{,}025;\,10} = 20{,}48$ se lit dans la colonne 0,975). D'où
$$\frac{10 \times 4}{20{,}48} \leq \sigma^2 \leq \frac{10 \times 4}{3{,}25} \iff 1{,}95 \leq \sigma^2 \leq 12{,}31, \qquad 1{,}40 \leq \sigma \leq 3{,}51$$
L'intervalle est large : estimer une variance demande beaucoup plus d'observations qu'estimer une moyenne. [[Complément hors du cours|ⓘ]]

![[Séance 8 - Chi²-Test - image22.png]]

*Figure : (a) le point $\chi^2_{\alpha,k}$, avec l'aire $\alpha$ à sa droite ; (b) $\chi^2_{0{,}95;10} = 3{,}94$ et $\chi^2_{0{,}05;10} = 18{,}31$, avec 0,05 dans chaque queue.*

### Récapitulatif des intervalles de confiance

Intervalles à $100(1-\alpha)$ % pour $X_1, \ldots, X_n \sim \mathcal{N}(\mu, \sigma^2)$, avec $\bar{X} = \sum X_i / n$ et $S = \sqrt{\sum (X_i - \bar{X})^2 / (n-1)}$ :

| Hypothèse | Paramètre | Intervalle de confiance | « Lower Interval » | « Upper Interval » |
|---|---|---|---|---|
| $\sigma^2$ connu | $\mu$ | $\bar{X} \pm z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + z_{\alpha} \dfrac{\sigma}{\sqrt{n}}\right)$ | $\left(\bar{X} - z_{\alpha} \dfrac{\sigma}{\sqrt{n}},\ \infty\right)$ [[Erreurs du cours#^e-8-chi2-test\|✎]] |
| $\sigma^2$ inconnu | $\mu$ | $\bar{X} \pm t_{\alpha/2,\, n-1} \dfrac{S}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + t_{\alpha,\, n-1} \dfrac{S}{\sqrt{n}}\right)$ | $\left(\bar{X} - t_{\alpha,\, n-1} \dfrac{S}{\sqrt{n}},\ \infty\right)$ |
| $\mu$ inconnu | $\sigma^2$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha/2,\, n-1}},\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2,\, n-1}}\right)$ | $\left(0,\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha,\, n-1}}\right)$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha,\, n-1}},\ \infty\right)$ |

## La variance d'échantillon suit une loi du χ²

La **variance d'échantillon** est définie par

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$$

Donc

$$(n-1)s^2 = \sum (x_i - \bar{x})^2 = (x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \ldots + (x_n - \bar{x})^2$$

Le membre de droite étant une **somme de carrés**, **quand $X$ est normale**, $(n-1)s^2$ (rapporté à $\sigma^2$) suit une loi du $\chi^2$ à $(n-1)$ degrés de liberté.

## Standardiser la statistique de test

Dans un test d'hypothèse sur une variance de population $\sigma^2$, la [[Statistique de test|statistique de test]] est la variance d'échantillon $s^2$. La statistique standardisée est

$$\chi^{2*} = \frac{(n-1)s^2}{\sigma_0^2}$$

Les valeurs standardisées se lisent dans les tables du $\chi^2$.

Règle de décision, sous $H_0 : \sigma^2 = \sigma_0^2$ et $n-1$ degrés de liberté : en bilatéral ($H_1 : \sigma^2 \neq \sigma_0^2$), on rejette si $\chi^{2*} < \chi^2_{1-\alpha/2}$ ou $\chi^{2*} > \chi^2_{\alpha/2}$ ; en unilatéral à droite ($H_1 : \sigma^2 > \sigma_0^2$), si $\chi^{2*} > \chi^2_{\alpha}$ ; à gauche, si $\chi^{2*} < \chi^2_{1-\alpha}$. Avec l'exemple précédent et $\sigma_0^2 = 2$ : $\chi^{2*} = 10 \times 4 / 2 = 20$, compris entre 3,25 et 20,48, on ne rejette pas $H_0$ à 5 %, comme le dit l'intervalle (2 est dans $[1{,}95 ;\ 12{,}31]$). [[Complément hors du cours|ⓘ]]

Ce test et cet intervalle reposent fortement sur la normalité de la population : contrairement au test $t$ sur une moyenne, ils ne deviennent pas robustes quand $n$ grandit, et une loi à queues épaisses fausse nettement le risque $\alpha$. Pour comparer les variances de deux populations, on utilise le rapport $s_1^2/s_2^2$, qui suit une loi $F$ ([[Statistique F]]). [[Complément hors du cours|ⓘ]]

### Caractéristiques de la table du χ²

- Les tables du $\chi^2$ ne sont **pas symétriques**.
- Il faut donc lister séparément les valeurs de la queue inférieure et de la queue supérieure (en jaune pour la queue inférieure, en bleu pour la supérieure, sur la diapositive).

![[Séance 8 - Chi²-Test - image14.png]]

*Figure : densité du $\chi^2$ avec une aire $\alpha/2$ dans chaque queue, aux points $\chi^2_{1-\alpha/2,\nu}$ et $\chi^2_{\alpha/2,\nu}$, et extrait de la table.*

Extrait de la table du cours (en-têtes : aire, lue comme indiqué sur la diapositive) ; la colonne 0,005 donne les valeurs des tables usuelles : [[Erreurs du cours#^e-8-chi2-test|✎]]

| df | 0,005 | 0,01 | 0,025 | 0,05 | 0,1 | 0,9 | 0,95 | 0,975 | 0,99 | 0,995 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,0000393 | 0,000157 | 0,000982 | 0,00393 | 0,0158 | 2,71 | 3,84 | 5,02 | 6,63 | 7,88 |
| 2 | 0,0100 | 0,020 | 0,0506 | 0,103 | 0,211 | 4,61 | 5,99 | 7,38 | 9,21 | 10,60 |
| 3 | 0,072 | 0,115 | 0,216 | 0,352 | 0,584 | 6,25 | 7,81 | 9,35 | 11,34 | 12,84 |
| 4 | 0,207 | 0,297 | 0,484 | 0,711 | 1,064 | 7,78 | 9,49 | 11,14 | 13,28 | 14,86 |
| 5 | 0,412 | 0,554 | 0,831 | 1,145 | 1,61 | 9,24 | 11,07 | 12,83 | 15,09 | 16,75 |
| 10 | 2,16 | 2,56 | 3,25 | 3,94 | 4,87 | 15,99 | 18,31 | 20,48 | 23,21 | 25,19 |
| 30 | 13,79 | 14,95 | 16,79 | 18,49 | 20,60 | 40,26 | 43,77 | 46,98 | 50,89 | 53,67 |

(La table complète, $df$ = 1 à 12 et 25 à 30, est sur l'image ; ne pas en reprendre la colonne 0,005, dont les valeurs à partir de $df = 2$ sont trop petites : par exemple, pour $df = 25$ à 30, la colonne 0,005 vaut environ 10,52 à 13,79.) [[Erreurs du cours#^e-8-chi2-test|✎]]

## Test du χ² sur un tableau croisé (*bivariate tables*)

### Logique de base

- Le [[Test du χ²]] est un **test de significativité** fondé sur des **tableaux croisés** ([[Tableau de contingence]]).
- On cherche des écarts significatifs entre les **effectifs observés** de chaque cellule ($f_o$) et les **effectifs attendus par le seul hasard** ($f_e$).
- Les données sont souvent présentées en tableau ; à partir de données brutes sur deux variables, il faut d'abord construire le tableau croisé.

La statistique a été proposée par Karl Pearson en 1900. Elle a trois usages, avec la même formule $\sum (f_o - f_e)^2/f_e$ : [[Complément hors du cours|ⓘ]]
- **indépendance** (le cas du cours) : deux variables catégorielles mesurées sur un même échantillon ; [[Complément hors du cours|ⓘ]]
- **homogénéité** : une variable catégorielle comparée entre plusieurs populations échantillonnées séparément (la répartition des réponses est-elle la même dans chaque groupe ?) ; même calcul, même $df = (r-1)(c-1)$ ; [[Complément hors du cours|ⓘ]]
- **[[Test d'adéquation du χ²|adéquation]]** (*goodness of fit*) : un seul échantillon, dont on compare les effectifs observés à ceux que prévoit une loi donnée, $f_e = N \times p_i$, avec $df = k - 1$ pour $k$ catégories (moins un par paramètre estimé sur les données). C'est le khi-deux « à un échantillon » de l'organigramme de [[7 - Z-Test]]. Exemple : un dé lancé 60 fois est-il équilibré ? On attend $f_e = 10$ par face et on compare la statistique au $\chi^2_5$ (11,07 à 5 %). [[Complément hors du cours|ⓘ]]

### Le tableau croisé

- Il doit avoir un titre.
- Les cellules sont les intersections des lignes et des colonnes.
- Les sous-totaux s'appellent les **marges** (*marginals*).
- $N$ est indiqué à l'intersection des marges de ligne et de colonne.
- Les **colonnes** sont les valeurs de la variable **indépendante** (autant de colonnes que de valeurs).
- Les **lignes** sont les valeurs de la variable **dépendante** (autant de lignes que de valeurs).
- Il y a autant de cellules que de combinaisons de valeurs des deux variables ; chaque cellule donne le nombre de fois où la combinaison s'est produite.

| | Colonne 1 | Colonne 2 | Total |
|---|---|---|---|
| Ligne 1 | cellule a | cellule b | marge de ligne 1 |
| Ligne 2 | cellule c | cellule d | marge de ligne 2 |
| Total | marge de colonne 1 | marge de colonne 2 | $N$ |

### Le test

Le test du $\chi^2$ sert à déterminer si **deux variables catégorielles** ont une corrélation significative. Les deux variables viennent de la même population et sont catégorisées (homme/femme, rouge/vert, oui/non…).

- La loi du $\chi^2$ est asymétrique et ne prend que des valeurs positives.
- Degrés de liberté, d'après le tableau :
$$df = (\text{lignes} - 1) \times (\text{colonnes} - 1)$$
- Raison de cette formule : les marges sont fixées par les données. Dans chaque ligne, la dernière cellule se déduit de la marge, de même dans chaque colonne ; seules $(r-1)(c-1)$ cellules peuvent être choisies librement. Dans un tableau $2 \times 2$, une seule cellule suffit à déterminer les trois autres. [[Complément hors du cours|ⓘ]]

![[Séance 8 - Chi²-Test - image5.png]]

*Figure : loi du $\chi^2$ avec la [[Valeur critique|valeur critique]] $\chi^2_c$ ; à gauche « ne pas rejeter $H_0$ », à droite « rejeter $H_0$ ».*

### Interpréter le χ²

- Le test dit **seulement** si les variables sont **indépendantes** ou non.
- Il ne dit pas la forme ni la nature de la relation.
- Pour l'étudier, calculer les pourcentages dans chaque colonne et les comparer d'une colonne à l'autre.

### Limites du χ²

- Comme tout test, le $\chi^2$ est sensible à la **taille de l'échantillon** : quand $N$ augmente, le $\chi^2$ obtenu augmente ; avec de grands échantillons, des relations insignifiantes peuvent devenir significatives. Correction : quand $N > 1000$, prendre $\alpha = 0{,}01$.
- **Significatif** ne veut pas dire **important**.
- Pour mesurer l'**intensité** du lien indépendamment de $N$, on utilise le **[[V de Cramér]]** : $V = \sqrt{\dfrac{\chi^2}{N\,(\min(r, c) - 1)}}$, compris entre 0 (indépendance) et 1 (lien parfait) ; pour un tableau $2 \times 2$, il se réduit au coefficient $\varphi = \sqrt{\chi^2/N}$. C'est une [[Taille d'effet|taille d'effet]], qui répond à la question « important ? » laissée ouverte par le test. [[Complément hors du cours|ⓘ]]

**Note pour l'examen** : dire aussi **pourquoi** l'approche convient : la méthode d'[[Échantillonnage|échantillonnage]] est aléatoire simple, les variables sont catégorielles, et l'effectif attendu est **au moins 5** dans chaque cellule du tableau de contingence.

Cette condition vient de ce que la loi du $\chi^2$ n'est qu'une **approximation** de la loi de la statistique, valable pour des effectifs attendus assez grands (règle usuelle, attribuée à Cochran : pas d'effectif attendu inférieur à 1 et au plus 20 % des cellules sous 5). Si elle n'est pas remplie, on regroupe des modalités voisines ou, pour un tableau $2 \times 2$, on fait le **test exact de Fisher**, qui calcule la probabilité exacte du tableau observé sans approximation. Pour un $2 \times 2$, on applique aussi souvent la **correction de continuité de Yates**, $\sum \dfrac{(\lvert f_o - f_e \rvert - 0{,}5)^2}{f_e}$, plus prudente. [[Complément hors du cours|ⓘ]]

## Exemple : homicides et ventes d'armes

Question : le taux d'homicides et le volume des ventes d'armes sont-ils liés, pour un échantillon de 25 villes ?

| Ventes d'armes \\ Taux d'homicides | Bas | Haut | Total |
|---|---|---|---|
| Hautes | 8 | 5 | 13 |
| Basses | 4 | 8 | 12 |
| Total | 12 | 13 | $N = 25$ |

Tableau $2 \times 2$ à 4 cellules (taux d'homicides en colonnes, ventes d'armes en lignes).

**Étape 1 : hypothèses et conditions du test**

- Échantillons aléatoires indépendants.
- Niveau de mesure nominal.
- **Aucune hypothèse sur la forme de la distribution d'échantillonnage.** Quand la distribution est normale, on peut utiliser un [[Test paramétrique et non paramétrique|test paramétrique]] (Z, [[Test t|t]], [[ANOVA]]) ; le $\chi^2$ est **non paramétrique** et s'utilise quand on ne suppose pas la normalité.

**Étape 2 : hypothèse nulle et alternative**

- $H_0$ : les variables sont indépendantes (ou $P_0 = P_1$, mêmes proportions).
- $H_1$ : les variables sont dépendantes (ou $P_0 \neq P_1$).

**Étape 3 : distribution d'échantillonnage et région critique**

- Pas de normalité supposée et données en tableau → loi du $\chi^2$.
- $\alpha = 0{,}05$ ; $df = (r-1)(c-1) = 1$ ; $\chi^2_{critique} = 3{,}841$.

**Étape 4 : calcul de la statistique**

$$\chi^2_{obtenu} = \sum \frac{(f_o - f_e)^2}{f_e}$$

D'où vient $f_e$ : sous $H_0$ (indépendance), la probabilité d'être à la fois dans la ligne $i$ et dans la colonne $j$ est le produit des probabilités, estimées par les marges : $\dfrac{\text{marge de ligne}}{N} \times \dfrac{\text{marge de colonne}}{N}$. En multipliant par $N$, on obtient l'effectif attendu ci-dessous. Chaque terme $(f_o - f_e)^2/f_e$ mesure l'écart d'une cellule à l'indépendance, rapporté à l'effectif attendu ; la somme est nulle si le tableau observé est exactement celui de l'indépendance. [[Complément hors du cours|ⓘ]]

1. Effectifs attendus de chaque cellule : $f_e = \dfrac{\text{marge de ligne} \times \text{marge de colonne}}{N}$ :
   - $(13 \cdot 12)/25 = 6{,}24$ ; $(13 \cdot 13)/25 = 6{,}76$ ;
   - $(12 \cdot 12)/25 = 5{,}76$ ; $(12 \cdot 13)/25 = 6{,}24$.

| Ventes \\ Homicides | Bas | Haut | Total |
|---|---|---|---|
| Hautes | $f_o = 8$, $f_e = 6{,}24$ | $f_o = 5$, $f_e = 6{,}76$ | 13 |
| Basses | $f_o = 4$, $f_e = 5{,}76$ | $f_o = 8$, $f_e = 6{,}24$ | 12 |
| Total | 12 | 13 | 25 |

(les totaux ne changent pas).

2. Tableau de calcul :

| $f_o$ | $f_e$ | $f_o - f_e$ | $(f_o - f_e)^2$ | $(f_o - f_e)^2 / f_e$ |
|---|---|---|---|---|
| 8 | 6,24 | 1,76 | 3,10 | 0,50 |
| 5 | 6,76 | −1,76 | 3,10 | 0,46 |
| 4 | 5,76 | −1,76 | 3,10 | 0,54 |
| 8 | 6,24 | 1,76 | 3,10 | 0,50 |
| **25** | **25** | **0** | | $\chi^2 = 2{,}00$ |

**Étape 5 : décision et interprétation**

$\chi^2_{critique} = 3{,}841$, $\chi^2_{obtenu} = 2{,}00$ : la statistique **n'est pas** dans la région critique. **On ne rejette pas $H_0$** (les variables sont indépendantes). **Conclusion** : pas de relation significative entre taux d'homicides et ventes d'armes, d'après ces données.

Compléments sur l'exemple : la p-value est $P(\chi^2_1 \geq 2{,}00) \approx 0{,}16$, bien au-dessus de 0,05. Les pourcentages par colonne, comme le recommande le cours pour décrire le lien, montrent pourtant une tendance : 67 % des villes à taux d'homicides bas ont des ventes d'armes hautes (8 sur 12), contre 38 % des villes à taux haut (5 sur 13). Le [[V de Cramér|coefficient φ]] vaut $\sqrt{2{,}00/25} \approx 0{,}28$, proche d'un lien moyen selon les repères usuels de Cohen (0,1 faible, 0,3 moyen, 0,5 fort). Avec 25 villes, le test n'a pas assez de [[Puissance d'un test|puissance]] pour conclure : « non significatif » ne veut pas dire « pas de lien ». Les effectifs attendus (5,76 à 6,76) respectent juste la condition des 5. [[Complément hors du cours|ⓘ]]

En R : `chisq.test(matrix(c(8, 4, 5, 8), nrow = 2))` fait le test sur le tableau (rempli colonne par colonne) ; pour un $2 \times 2$, R applique par défaut la correction de Yates (`correct = FALSE` pour retrouver le calcul du cours). `chisq.test(x, p = c(…))` fait un test d'adéquation, `fisher.test()` le test exact. [[Complément hors du cours|ⓘ]]

![[Séance 8 - Chi²-Test - image4.png]]

*Figure : loi du $\chi^2$ et région de rejet au-delà de $\chi^2_c$ ; la valeur obtenue tombe dans la zone « ne pas rejeter ».*
