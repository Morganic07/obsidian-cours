---
type: source
sources: ["[[Chp2 - Descriptive statistics]]"]
maj: 2026-11-05
---

Résumé de [[Chp2 - Descriptive statistics]], dans [[Year 3 - Statistics]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Résumer un jeu de données par des graphiques, puis par des indicateurs de position (moyenne, médiane, quartiles) et de dispersion (étendue, variance, écart interquartile).

## Contenu, dans l'ordre du cours

- **Graphiques pour données quantitatives** : tige et feuilles (stem and leaf), diagramme en points (dotplot), histogramme. Pour un histogramme, on découpe l'axe en classes d'égale largeur, chaque observation tombe dans une seule classe, et la hauteur est proportionnelle à la fréquence. **Fréquence relative** = nombre d'occurrences / taille de l'échantillon. **Densité** d'une classe = fréquence relative / largeur de la classe (échelle de densité).
- **Convention de bord** : une observation sur une borne va dans la classe de droite (15 pile va dans l'intervalle supérieur). Nombre de classes $\approx \sqrt{\text{nombre d'observations}}$.
- **Formes** : symétrique unimodale, bimodale, asymétrie positive (queue à droite), asymétrie négative (queue à gauche).
- **Tableaux** : distribution de fréquences et de fréquences relatives (exemple de 42 salaires de départ).
- **Données catégorielles** : diagramme circulaire, diagramme en barres. Rappel du cours : histogramme pour les données quantitatives, diagramme en barres pour les qualitatives. Pour une variable qualitative, on calcule la proportion $\hat{p}$ ; pour une quantitative, moyenne et écart-type.
- **Moyenne d'échantillon** $\bar{x} = \sum x_i / n$. **Médiane** : valeur d'ordre $(n+1)/2$ si $n$ impair, moyenne des valeurs d'ordre $n/2$ et $n/2 + 1$ si $n$ pair (exemple : $n = 12$, $(66{,}4 + 67{,}4)/2 = 66{,}90$).
- **Percentile** : $x_p$ tel qu'au moins $100p\,\%$ des données soient $\le x_p$ et au moins $100(1-p)\,\%$ soient $\ge x_p$. La valeur ordonnée $x_{(i)}$ est le percentile $p = (i - 1/2)/n$.
- **Moyenne et médiane de population** : $\mu$ et $\tilde{\mu}$. Asymétrie négative : $\mu < \tilde{\mu}$ ; symétrique : $\mu = \tilde{\mu}$ ; positive : $\tilde{\mu} < \mu$.
- **Dispersion** : étendue = max $-$ min. Somme des écarts à la moyenne $= 0$.
- **[[Variance et écart-type d'échantillon]]** : $S_{xx} = \sum (x_i - \bar{x})^2$, $s = \sqrt{S_{xx}/(n-1)}$, $s^2$ variance. Forme alternative $S_{xx} = \sum x_i^2 - n\bar{x}^2$ (démonstrée dans la note). Les $n$ écarts sommant à 0, $s$ a $n - 1$ degrés de liberté. Diviser par $n - 1$ est la correction de Bessel.
- **Population finie** : $\mu = \sum x_i/N$, $\sigma^2 = \sum (x_i - \mu)^2/N$. Pour une population infinie, ce sont l'espérance et la variance de la variable aléatoire.
- **[[Quartiles et valeurs aberrantes]]** : $q_1$ est la médiane de la moitié inférieure, $q_3$ celle de la moitié supérieure (la médiane est dans les deux moitiés si $n$ est impair). $\mathrm{iqr} = q_3 - q_1$. Une valeur est aberrante si $x < q_1 - 1{,}5\,\mathrm{iqr}$ ou $x > q_3 + 1{,}5\,\mathrm{iqr}$, extrême au-delà de $3\,\mathrm{iqr}$ d'un quartile, modérée sinon.
- **Boîte à moustaches** : rectangle de $q_1$ à $q_3$, trait à la médiane, valeurs aberrantes marquées une à une, moustaches jusqu'aux valeurs extrêmes qui ne sont pas aberrantes. Exemple de 57 charges d'azote quotidiennes : $q_1 = 45{,}64$, $q_3 = 167{,}79$, $\mathrm{iqr} = 122{,}15$, seuil $351{,}015$ ; 563,92, 690,11, 826,54 et 1529,35 sont extrêmes, 352,09, 371,47, 444,68 et 460,86 modérées.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Exemple de la boîte à moustaches : « $\bar{x} = 92{,}17$ »** : image non ouverte pour ce point, mais le calcul tranche. 92,17 est la 29e des 57 valeurs triées : c'est la médiane, pas la moyenne. Le symbole devrait être $\tilde{x}$ (complément).
2. **Définition des quartiles, deux versions** : la définition ($q_1$, $q_3$ médianes des moitiés, médiane incluse si $n$ impair) diffère de la procédure du dessin (« divide the data at the median into two equal groups »), qui ne dit rien de la médiane. Les logiciels donnent d'ailleurs des valeurs légèrement différentes, comme le cours le dit.
3. **Phrase coupée** : la note de définition des percentiles s'arrête net : « The upper quartile is $x_{0.75}$, the value “at or below” which 75 % of the data points lie, and “at or above” which ». La suite (25 % des données) manque.
4. **Alertes de la transcription** : la valeur 65 absente des tableaux de salaires (de 64 à 66) et le « .2.5 » de l'histogramme sont des défauts de l'image, non des erreurs de fond. Image non ouverte, ne rien reprendre de ces valeurs.
