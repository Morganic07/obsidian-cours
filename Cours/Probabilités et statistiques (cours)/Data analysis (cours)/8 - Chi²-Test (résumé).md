---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]], dans [[Data analysis (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

La loi du χ² sert à deux choses : estimer et tester une variance, et tester l'indépendance de deux variables catégorielles sur un tableau croisé. Le second usage est le [[Test du χ²]].

## Présentation de la loi du χ²

**Question du cours** : si $x_1 + x_2 + \dots + x_n$ suit une loi de Student à $(n-1)$ degrés de liberté, que dire de la **somme des carrés** $x_1^2 + x_2^2 + \dots + x_n^2$ ?

**Réponse** : les statisticiens ont montré que **si $X$ est normale**, la [[Somme des carrés (SST, SSR, SSE)|somme des carrés]] de $n$ valeurs $x_i$ suit une **loi du $\chi^2$ à $(n-1)$ degrés de liberté** (énoncé du cours, voir Points à vérifier).

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

La **moyenne** de la loi du $\chi^2$ est $k$ et sa **variance** $2k$.

## Intervalle de confiance de la variance

Si $s^2$ est la variance d'un échantillon aléatoire de $n$ observations d'une loi normale de variance inconnue $\sigma^2$, un [[Intervalle de confiance|intervalle de confiance]] à $100(1-\alpha)$ % de $\sigma^2$ est :

$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}}$$

où $\chi^2_{\alpha/2,\,n-1}$ et $\chi^2_{1-\alpha/2,\,n-1}$ sont les points de pourcentage supérieur et inférieur à $100\alpha/2$ % de la loi du $\chi^2$ à $n-1$ degrés de liberté. L'intervalle de confiance de **$\sigma$** a pour bornes les racines carrées de ces bornes.

![[Séance 8 - Chi²-Test - image22.png]]

*Figure : (a) le point $\chi^2_{\alpha,k}$, avec l'aire $\alpha$ à sa droite ; (b) $\chi^2_{0{,}95;10} = 3{,}94$ et $\chi^2_{0{,}05;10} = 18{,}31$, avec 0,05 dans chaque queue.*

### Récapitulatif des intervalles de confiance

Intervalles à $100(1-\alpha)$ % pour $X_1, \ldots, X_n \sim \mathcal{N}(\mu, \sigma^2)$, avec $\bar{X} = \sum X_i / n$ et $S = \sqrt{\sum (X_i - \bar{X})^2 / (n-1)}$ :

| Hypothèse | Paramètre | Intervalle de confiance | « Lower Interval » | « Upper Interval » |
|---|---|---|---|---|
| $\sigma^2$ connu | $\mu$ | $\bar{X} \pm z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + z_{\alpha} \dfrac{\sigma}{\sqrt{n}}\right)$ | $\left(\bar{X} + z_{\alpha} \dfrac{\sigma}{\sqrt{n}},\ \infty\right)$ (sic, voir Points à vérifier) |
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

### Caractéristiques de la table du χ²

- Les tables du $\chi^2$ ne sont **pas symétriques**.
- Il faut donc lister séparément les valeurs de la queue inférieure et de la queue supérieure (en jaune pour la queue inférieure, en bleu pour la supérieure, sur la diapositive).

![[Séance 8 - Chi²-Test - image14.png]]

*Figure : densité du $\chi^2$ avec une aire $\alpha/2$ dans chaque queue, aux points $\chi^2_{1-\alpha/2,\nu}$ et $\chi^2_{\alpha/2,\nu}$, et extrait de la table.*

Extrait de la table du cours (en-têtes : aire, lue comme indiqué sur la diapositive) :

| df | 0,005 | 0,01 | 0,025 | 0,05 | 0,1 | 0,9 | 0,95 | 0,975 | 0,99 | 0,995 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,0000393 | 0,000157 | 0,000982 | 0,00393 | 0,0158 | 2,71 | 3,84 | 5,02 | 6,63 | 7,88 |
| 2 | 0,0001 | 0,020 | 0,0506 | 0,103 | 0,211 | 4,61 | 5,99 | 7,38 | 9,21 | 10,60 |
| 3 | 0,003 | 0,115 | 0,216 | 0,352 | 0,584 | 6,25 | 7,81 | 9,35 | 11,34 | 12,84 |
| 4 | 0,018 | 0,297 | 0,484 | 0,711 | 1,064 | 7,78 | 9,49 | 11,14 | 13,28 | 14,86 |
| 5 | 0,056 | 0,554 | 0,831 | 1,145 | 1,61 | 9,24 | 11,07 | 12,83 | 15,09 | 16,75 |
| 10 | 0,73 | 2,56 | 3,25 | 3,94 | 4,87 | 15,99 | 18,31 | 20,48 | 23,21 | 25,19 |
| 30 | 8,50 | 14,95 | 16,79 | 18,49 | 20,60 | 40,26 | 43,77 | 46,98 | 50,89 | 53,67 |

(La table complète, $df$ = 1 à 12 et 25 à 30, est sur l'image ; la colonne 0,005 est douteuse, voir Points à vérifier.)

## Test du χ² sur un tableau croisé (*bivariate tables*)

### Logique de base

- Le [[Test du χ²]] est un **test de significativité** fondé sur des **tableaux croisés** ([[Tableau de contingence]]).
- On cherche des écarts significatifs entre les **effectifs observés** de chaque cellule ($f_o$) et les **effectifs attendus par le seul hasard** ($f_e$).
- Les données sont souvent présentées en tableau ; à partir de données brutes sur deux variables, il faut d'abord construire le tableau croisé.

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

![[Séance 8 - Chi²-Test - image5.png]]

*Figure : loi du $\chi^2$ avec la [[Valeur critique|valeur critique]] $\chi^2_c$ ; à gauche « ne pas rejeter $H_0$ », à droite « rejeter $H_0$ ».*

### Interpréter le χ²

- Le test dit **seulement** si les variables sont **indépendantes** ou non.
- Il ne dit pas la forme ni la nature de la relation.
- Pour l'étudier, calculer les pourcentages dans chaque colonne et les comparer d'une colonne à l'autre.

### Limites du χ²

- Comme tout test, le $\chi^2$ est sensible à la **taille de l'échantillon** : quand $N$ augmente, le $\chi^2$ obtenu augmente ; avec de grands échantillons, des relations insignifiantes peuvent devenir significatives. Correction : quand $N > 1000$, prendre $\alpha = 0{,}01$.
- **Significatif** ne veut pas dire **important**.

**Note pour l'examen** : dire aussi **pourquoi** l'approche convient : la méthode d'[[Échantillonnage|échantillonnage]] est aléatoire simple, les variables sont catégorielles, et l'effectif attendu est **au moins 5** dans chaque cellule du tableau de contingence.

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

![[Séance 8 - Chi²-Test - image4.png]]

*Figure : loi du $\chi^2$ et région de rejet au-delà de $\chi^2_c$ ; la valeur obtenue tombe dans la zone « ne pas rejeter ».*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images ouvertes : le tableau récapitulatif des intervalles et la table du χ².

1. **Phrase d'introduction sur la loi** : le cours demande ce qu'est la somme des carrés d'une loi de Student et répond que $x_1^2 + \dots + x_n^2$ suit un χ² à $n-1$ degrés de liberté si $X$ est normale. La somme des carrés de $n$ normales centrées réduites indépendantes suit un χ² à $n$ degrés. Le degré $n-1$ vaut pour les écarts à la moyenne, comme dans la suite du cours. La mention d'une loi de Student n'a pas de sens ici (complément). **À corriger avant un examen.**
2. **Tableau récapitulatif, ligne $\sigma^2$ connu** : image lue directement. L'intervalle « supérieur » est écrit $(\bar{X} + z_\alpha\sigma/\sqrt{n}, \infty)$ avec un signe plus, alors que la ligne $\sigma^2$ inconnu écrit un moins. Le signe correct est « moins » (complément). Alerte de la transcription confirmée.
3. **Table du χ²** : image lue directement. La colonne 0,005 ne correspond pas aux tables usuelles dès $df = 2$ (valeur usuelle 0,0100, la diapositive écrit 0,0001) ni pour $df = 25$ à 30 (usuelles autour de 10,5 à 13,8, la diapositive écrit 6,08 à 8,50). Les autres colonnes lues semblent cohérentes (complément). Ne pas utiliser cette colonne telle quelle.
4. **Étiquettes « Lower » et « Upper Interval »** du tableau récapitulatif : les intervalles de la colonne « Lower » sont de la forme $(-\infty, \dots)$, donc ce sont des bornes supérieures de confiance. Libellés ambigus, repris tels quels.
5. **Calcul de l'exemple** : somme des colonnes recalculée, 2,00 (1,99 avant arrondi). L'alerte de la transcription sur la somme des $f_e$ est une fausse alerte.
6. **Fragments d'axe** (0, 4, 8, 12) en haut à droite d'une image : sans importance, fausse alerte.
