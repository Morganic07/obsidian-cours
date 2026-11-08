---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/probabilité statistiques utilitaire.docx|probabilité statistiques utilitaire]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/probabilité statistiques utilitaire.docx|probabilité statistiques utilitaire]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : aide-mémoire de formules en deux pages (« Statistics formulas »), sans commentaire. Les deux images ne contiennent que des formules : elles sont recopiées ici d'après leurs transcriptions ; la page 2 a été vérifiée sur l'image.

Il va plus loin que les chapitres intégrés : tests d'hypothèse, deux échantillons, régression, khi-deux. Le wiki ne reprend comme explication que les formules dont un chapitre intégré établit le sens ; les autres sont seulement recopiées.

## Page 1

### Statistique descriptive

| Grandeur | Formule |
|---|---|
| Moyenne d'échantillon | $\overline{X} = \dfrac{\sum_{i=1}^{n} X_i}{n}$ |
| Moyenne de population | $\mu = \dfrac{\sum_{i=1}^{N} X_i}{N}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Écart interquartile | $IQR = Q_3 - Q_1$ (voir [[Quartiles et valeurs aberrantes]]) |
| [[Coefficient de variation]] | $CV = \dfrac{s}{\overline{X}} \times 100\,\%$ |
| Écart-type d'échantillon | $s = \sqrt{\dfrac{\sum_{i=1}^{n}(X_i - \overline{X})^2}{n-1}}$ |
| Variance d'échantillon | $s^2 = \dfrac{\sum_{i=1}^{n}(X_i - \overline{X})^2}{n-1}$ |
| Écart-type de population | $\sigma = \sqrt{\dfrac{\sum_{i=1}^{N}(X_i - \mu)^2}{N}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Variance de population | $\sigma^2 = \dfrac{\sum_{i=1}^{N} (X_i - \mu)^2}{N}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |

Voir [[Variance et écart-type d'échantillon]].

On divise par $n - 1$ pour l'échantillon et par $N$ pour la population : avec $n - 1$, la variance d'échantillon $s^2$ est un [[Estimateur|estimateur sans biais]] de $\sigma^2$, ce que $\sum (X_i - \overline{X})^2 / n$ n'est pas, car les écarts à $\overline{X}$ sont en moyenne plus petits que les écarts à $\mu$. Le coefficient de variation, sans unité, sert à comparer la dispersion de séries d'unités ou d'ordres de grandeur différents. [[Complément hors du cours|ⓘ]]

### Scores $Z$

$$Z = \frac{X - \overline{X}}{s} \qquad Z = \frac{X - \mu}{\sigma} \qquad Z = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \qquad Z = \frac{\overline{X} - \mu}{s/\sqrt{n}}$$

Voir [[Centrage et réduction]].

Les deux premières formules situent **une observation** : $Z$ est le nombre d'écarts-types qui la séparent de la moyenne ($Z = 2$ : deux écarts-types au-dessus). Les deux dernières situent **une moyenne d'échantillon** : on divise alors par l'**erreur type** $\sigma/\sqrt{n}$, l'écart-type de $\overline{X}$, plus petit que $\sigma$ (voir [[Distribution d'échantillonnage]]). Pour une loi normale, environ 68 %, 95 % et 99,7 % des valeurs ont un $|Z|$ inférieur à 1, 2 et 3 ([[Loi normale]]). [[Complément hors du cours|ⓘ]]

### Probabilités

- $P(A \text{ or } B) = P(A \cup B) = P(A) + P(B)$ si $A$ et $B$ sont [[Événements incompatibles|incompatibles]] (*mutually exclusive*) ;
- $P(A \text{ or } B) = P(A \cup B) = P(A) + P(B) - P(A \text{ and } B)$ en général ;
- $P(A \text{ and } B) = P(A \cap B) = P(A)\,P(B)$ si $A$ et $B$ sont [[Indépendance d'événements|indépendants]] ;
- $P(A \text{ and } B) = P(A \cap B) = P(A|B)\,P(B) = P(B|A)\,P(A)$ en général, que $A$ et $B$ soient indépendants ou non ; [[Erreurs du cours#^e-0-proba-stats-utilitaire|✎]]
- [[Probabilité conditionnelle]] : $P(A|B) = P(A \text{ and } B)/P(B)$ et $P(B|A) = P(B \text{ and } A)/P(A)$, avec $P(A \text{ and } B) = P(B \text{ and } A)$.

La formule $P(A \cap B) = P(A|B)\,P(B)$ suppose seulement $P(B) > 0$ ; dans le cas indépendant, $P(A|B) = P(A)$ et l'on retrouve $P(A)\,P(B)$. À ne pas confondre : deux événements **incompatibles** de probabilités non nulles ne sont **jamais** indépendants, puisque $P(A \cap B) = 0 \ne P(A)\,P(B)$ ; savoir que $B$ s'est produit apprend justement que $A$ ne s'est pas produit. [[Complément hors du cours|ⓘ]]

En combinant ces règles, on obtient la **formule des probabilités totales** et la **formule de Bayes**, qui « retourne » un conditionnement : si $A_1, \dots, A_k$ forment une partition (incompatibles deux à deux, de réunion certaine), [[Complément hors du cours|ⓘ]]
$$P(B) = \sum_{i=1}^{k} P(B|A_i)\,P(A_i), \qquad P(A_j|B) = \frac{P(B|A_j)\,P(A_j)}{\sum_{i=1}^{k} P(B|A_i)\,P(A_i)}.$$

### Dénombrement et loi binomiale

- [[Permutation (dénombrement)|Arrangements]] : $_nP_r = \dfrac{n!}{(n-r)!}$ ;
- [[Combinaison (dénombrement)|Combinaisons]] : $_nC_r = \dfrac{n!}{r!\,(n-r)!}$ ;
- [[Loi binomiale]] : $P(x) = {}_nC_x\, P^x (1-P)^{n-x}$, de moyenne $\mu = nP$ et de variance $\sigma^2 = nP(1-P)$.

Arrangements et combinaisons comptent les façons de choisir $r$ objets parmi $n$ sans remise ; l'ordre compte dans un arrangement, pas dans une combinaison, d'où $_nC_r = {}_nP_r / r!$ (chaque groupe de $r$ objets peut s'ordonner de $r!$ façons). Exemple : pour un président et un trésorier parmi 5 personnes, $_5P_2 = 20$ ; pour un binôme sans rôles, $_5C_2 = 10$. [[Complément hors du cours|ⓘ]]

La loi binomiale compte le nombre $x$ de succès dans $n$ essais **indépendants**, ayant chacun deux issues et la même probabilité de succès $P$ ; le facteur $_nC_x$ compte les positions possibles des $x$ succès parmi les $n$ essais. [[Complément hors du cours|ⓘ]]

### Corrélation et régression

- Coefficient de corrélation d'échantillon (voir [[Covariance et corrélation]]) :
$$r = \frac{n\sum XY - \sum X \sum Y}{\sqrt{\left(n\sum X^2 - (\sum X)^2\right)\left(n\sum Y^2 - (\sum Y)^2\right)}}$$
- Test de la corrélation : $t_{n-2} = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}}$ ;
- Droite de [[Régression linéaire|régression]] $\hat{Y} = a + bX$, avec
$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \qquad a = \overline{Y} - b\overline{X}$$
Notation : $a$ est aussi noté $b_0$, et $b$ est noté $b_1$.

Lecture : $-1 \le r \le 1$ ; $r$ mesure l'intensité d'une liaison **linéaire** ($r$ proche de $\pm 1$ : points presque alignés ; $r \approx 0$ : pas de liaison linéaire, ce qui n'exclut pas une liaison courbe). Son carré $r^2$ est le [[Coefficient de détermination|coefficient de détermination]], la part de la variance de $Y$ expliquée par la droite. Le test $t_{n-2}$ éprouve l'hypothèse d'une corrélation nulle dans la population, avec $n - 2$ degrés de liberté parce que la droite estime deux paramètres. [[Complément hors du cours|ⓘ]]

La pente s'écrit aussi $b = r\,\dfrac{s_Y}{s_X}$ : elle a le signe de $r$, et la droite passe toujours par le point moyen $(\overline{X}, \overline{Y})$, ce que dit $a = \overline{Y} - b\overline{X}$. Elle est obtenue par la méthode des **moindres carrés**, qui minimise $\sum (Y_i - \hat{Y}_i)^2$. [[Complément hors du cours|ⓘ]]

## Page 2

### Une moyenne, une proportion

| Cas | Statistique de test | Intervalle de confiance |
|---|---|---|
| Moyenne, $\sigma$ connu | $Z = \dfrac{\overline{X} - \mu_H}{\sigma/\sqrt{n}}$ | $\overline{X} \pm z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Moyenne, $\sigma$ inconnu | $t_{n-1} = \dfrac{\overline{X} - \mu_H}{s/\sqrt{n}}$ | $\overline{X} \pm t_{\alpha/2,\,n-1} \dfrac{s}{\sqrt{n}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Proportion | $Z \approx \dfrac{P_s - P}{\sqrt{P(1-P)/n}}$ | $P_s \pm z_{\alpha/2} \sqrt{\dfrac{P_s(1-P_s)}{n}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |

$\mu_H$ : valeur de $\mu$ sous l'hypothèse testée ; $P_s$ : proportion de l'échantillon ; $1 - \alpha$ : niveau de confiance de l'intervalle bilatéral. Voir [[Test Z]], [[Test t]], [[Intervalle de confiance]].

Valeurs courantes du quantile normal pour un intervalle bilatéral : $1{,}645$ à 90 %, $1{,}96$ à 95 %, $2{,}576$ à 99 %. Le $t$ de Student remplace $Z$ quand $\sigma$ est estimé par $s$ : ses quantiles sont plus grands (intervalle plus large, pour payer l'incertitude sur $\sigma$) et se rapprochent de ceux de $Z$ quand $n$ grandit ([[Loi de Student]]). [[Complément hors du cours|ⓘ]]

Pour la proportion, le test met au dénominateur la valeur $P$ de l'hypothèse testée, supposée vraie pendant le test, alors que l'intervalle, qui ne suppose rien, utilise $P_s$. L'[[Approximation normale|approximation normale]] demande un échantillon assez grand ; règle usuelle : $nP \ge 5$ et $n(1-P) \ge 5$ (certains manuels demandent 10). [[Complément hors du cours|ⓘ]]

### Deux échantillons

| Cas | Statistique de test | Intervalle de confiance |
|---|---|---|
| Deux moyennes, variances connues | $Z = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ | $(\overline{X}_1 - \overline{X}_2) \pm z_{\alpha/2} \sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Deux moyennes, variances estimées | $Z = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | $(\overline{X}_1 - \overline{X}_2) \pm z_{\alpha/2} \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ [[Erreurs du cours#^e-0-proba-stats-utilitaire\|✎]] |
| Deux moyennes, variance poolée | $t_{n_1+n_2-2} = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{S^2_{pooled}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$ | — |
| Deux proportions | $Z \approx \dfrac{P_{s1} - P_{s2}}{\sqrt{\overline{P}(1-\overline{P})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$ | — |

avec
$$S^2_{pooled} = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}, \qquad \overline{P} = \frac{x_1 + x_2}{n_1 + n_2}.$$

Voir [[Échantillons appariés et indépendants]].

Conditions d'emploi : le $Z$ à variances estimées n'est valable que pour de grands échantillons (on cite souvent $n_1, n_2 \ge 30$) ; le $t$ à variance poolée suppose des populations normales **de même variance**, d'où la mise en commun des deux $s^2$, pondérés par leurs degrés de liberté. $\overline{P}$ est la proportion commune estimée sous l'hypothèse « les deux proportions sont égales » ($x_1$, $x_2$ : nombres de succès). Ces formules supposent deux échantillons **indépendants** ; pour des mesures appariées (avant/après sur les mêmes individus), on applique le test à une moyenne aux différences. [[Complément hors du cours|ⓘ]]

### Taille d'échantillon

Pour une marge d'erreur $e$ :
$$n = \frac{Z^2 \sigma^2}{e^2} \ \text{(moyenne)}, \qquad n = \frac{Z^2 P(1-P)}{e^2} \ \text{(proportion)}.$$

On arrondit toujours $n$ à l'entier **supérieur**. Pour une proportion inconnue, on prend $P = 0{,}5$, qui maximise $P(1-P)$ (valeur $0{,}25$) : à 95 % et pour $e = 3$ points, $n = 1{,}96^2 \times 0{,}25 / 0{,}03^2 \approx 1067{,}1$, soit $n = 1068$, ordre de grandeur des sondages d'opinion d'environ 1 000 personnes. Diviser la marge par deux demande quatre fois plus d'observations. [[Complément hors du cours|ⓘ]]

### Khi-deux

([[Test du χ²]], [[Tableau de contingence]])
$$\chi^2 = \sum \frac{(f_o - f_e)^2}{f_e}, \qquad f_e = \frac{\text{total ligne} \times \text{total colonne}}{n}$$
($f_o$ : effectif observé, $f_e$ : effectif attendu ; la somme porte sur toutes les cases du tableau.) [[Erreurs du cours#^e-0-proba-stats-utilitaire|✎]]

Pour un tableau de contingence à $l$ lignes et $c$ colonnes, la statistique suit sous l'hypothèse d'indépendance une [[Loi du khi-deux|loi du khi-deux]] à $(l-1)(c-1)$ degrés de liberté ; on rejette l'indépendance quand $\chi^2$ dépasse la valeur critique (test unilatéral à droite, puisque de grands écarts donnent un grand $\chi^2$). Condition usuelle : des effectifs attendus $f_e$ d'au moins 5. [[Complément hors du cours|ⓘ]]

Les intervalles de la moyenne et de la proportion rejoignent le chapitre 4 : voir [[4 - Inferential statistics 2]] et [[4 - Inferential statistics 3]].
