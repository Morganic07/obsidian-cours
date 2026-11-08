---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 6 : T-Test.docx|Cours 6 - T-Test]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 6 : T-Test.docx|Cours 6 - T-Test]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Le test $t$ remplace le test $Z$ quand $\sigma$ est inconnu et l'échantillon petit. Le cours le présente pour un échantillon, puis pour deux échantillons indépendants.

Pourquoi un autre test : avec $\sigma$ connu, $\dfrac{\bar X - \mu_0}{\sigma/\sqrt n}$ suit une loi normale centrée réduite. Quand on remplace $\sigma$ par son estimation $s$, on ajoute une seconde source d'aléa (l'erreur sur $s$, d'autant plus forte que $n$ est petit) : la statistique fluctue davantage que $Z$ et suit une loi plus étalée, la loi de Student. La loi a été publiée en 1908 par William Gosset, chimiste de la brasserie Guinness, sous le pseudonyme « Student », d'où son nom. [[Complément hors du cours|ⓘ]]

## La loi de Student (*t-distribution*)

### Comprendre les degrés de liberté

Soit un échantillon de taille $n = 3$, par exemple $\{2, 4, 6\}$, de moyenne **4**. Si l'on tire un autre échantillon en imposant que sa moyenne soit aussi 4 :

- la première observation peut prendre n'importe quelle valeur (1 par exemple) ;
- la deuxième aussi (5 par exemple) ;
- la troisième n'a **aucune liberté** : elle vaut nécessairement 6, pour que $(1+5+6)/3 = 4$.

Le nombre de [[Variance et écart-type d'échantillon|degrés de liberté]] est donc 2, soit **$n-1$**.

C'est la même raison qui fait diviser par $n-1$ dans l'écart-type $s$ : les écarts à la moyenne vérifient toujours $\sum (x_i - \bar x) = 0$, donc seuls $n-1$ d'entre eux sont libres. Estimer un paramètre (ici $\mu$ par $\bar x$) « consomme » un degré de liberté ; en général, $df = n - (\text{nombre de paramètres estimés})$, d'où $n_1 + n_2 - 2$ plus bas, avec deux moyennes estimées. [[Complément hors du cours|ⓘ]]

### Une famille de lois

Il n'existe pas **une** [[Loi de Student]], mais une infinité, une par nombre de degrés de liberté. Une même valeur de statistique peut donc donner des [[P-value|p-values]] très différentes selon le nombre de degrés de liberté (donc la taille de l'échantillon).

| df | $P(\lvert X\rvert \geq 2{,}05)$ | chaque queue | centre |
|---|---|---|---|
| 1 | 0,28893 | 14,45 % | 71,11 % |
| 5 | 0,09564 | 4,78 % | 90,44 % |
| 20 | 0,05371 | 2,69 % | 94,63 % |
| 100 | 0,04298 | 2,15 % | 95,7 % |

![[Séance 6 - T-Test - image4.png]]

*Figure : densités de la loi t pour df = 1, 5, 20 et 100, avec les queues au-delà de ±2,05 ; plus df augmente, plus les queues s'amincissent.*

### Propriétés

- Ressemble à la [[Loi normale|loi normale]], mais **plus étalée**.
- **Symétrique** autour de la moyenne : moyenne = médiane = mode.
- Ce n'est pas une seule loi, mais une série de lois, une par nombre de degrés de liberté.
- Quand $n$ grandit, la loi $t$ se rapproche de la loi normale.
- Définition exacte : si $Z \sim \mathcal{N}(0,1)$ et $V \sim \chi^2_k$ sont indépendantes, $T = \dfrac{Z}{\sqrt{V/k}}$ suit la loi de Student à $k$ degrés de liberté. Pour un échantillon normal, $\dfrac{\bar X - \mu}{\sigma/\sqrt n} \sim \mathcal{N}(0,1)$ et $\dfrac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$ ([[Loi du khi-deux]], voir [[8 - Chi²-Test]]) sont indépendantes ; leur quotient fait disparaître $\sigma$ et donne exactement $\dfrac{\bar X - \mu}{s/\sqrt n} \sim t_{n-1}$. [[Complément hors du cours|ⓘ]]
- Moyenne 0 (pour $k > 1$) et variance $\dfrac{k}{k-2}$ (pour $k > 2$), toujours supérieure à 1, la variance de la loi normale : c'est l'« étalement » mesuré. À $k = 1$, c'est la loi de Cauchy, qui n'a même pas de moyenne. En pratique, au-delà d'environ 30 degrés de liberté, les valeurs critiques de $t$ et de $Z$ diffèrent peu (2,042 contre 1,96 à 5 % bilatéral pour $df = 30$). [[Complément hors du cours|ⓘ]]

## Le test t en pratique (un échantillon)

Voir [[Test t]].

Pour tester une hypothèse ($n-1$ degrés de liberté) :

$$t_{n-1} = \frac{\bar{X} - \mu_0}{s_{\bar{X}}} = \frac{\bar{X} - \mu_0}{\dfrac{s}{\sqrt{n}}}$$

où $s_{\bar{X}} = s/\sqrt{n}$ est l'**erreur standard** (*[[Estimateur|standard error]]*) et $\mu_{H_0}$ ou $\mu_0$ la **moyenne de population** affirmée (par exemple l'affirmation d'une entreprise).

Conditions d'usage : observations indépendantes, issues d'une population à peu près **normale**. La normalité se contrôle sur un [[Diagramme de probabilité|diagramme quantile-quantile]] ou par un test de Shapiro-Wilk. Le test $t$ est assez robuste à un écart modéré à la normalité, et d'autant plus que $n$ est grand, grâce au [[Théorème central limite|théorème central limite]] ; il est en revanche sensible aux valeurs aberrantes, qui gonflent $s$ et déplacent $\bar X$. Si la normalité est franchement violée sur un petit échantillon, on passe à un test non paramétrique ([[Test de Wilcoxon]], voir [[7 - Z-Test]]). [[Complément hors du cours|ⓘ]]

Intervalle de confiance à $(1-\alpha)$ % : [[Erreurs du cours#^e-6-t-test|✎]]

$$\bar{X} \pm t_{\alpha/2,\,n-1} \frac{s}{\sqrt{n}}$$

$\alpha$ définit la région où l'[[Test d'hypothèse|hypothèse nulle]] est rejetée : plus $\alpha$ est grand, plus la région de rejet (critique) est grande. Rappel : $\alpha$ est une **aire sous la courbe**.

### Unilatéral ou bilatéral ?

L'énoncé du problème détermine le type de test ([[Test unilatéral et bilatéral]]) :

- si l'hypothèse alternative contient « **différent de** » → test **bilatéral** ;
- si elle contient une **inégalité stricte** → test **unilatéral** ;
- $H_a$ indique où se trouve la [[Valeur critique|région de rejet]].

Choix du [[Seuil de signification|seuil de signification]] : en général $\alpha = 0{,}05$ ou $0{,}01$.

| Bilatéral | Unilatéral à gauche | Unilatéral à droite |
|---|---|---|
| $H_0 : \mu = 23$ | $H_0 : \mu \geq 23$ | $H_0 : \mu \leq 23$ |
| $H_1 : \mu \neq 23$ | $H_1 : \mu < 23$ | $H_1 : \mu > 23$ |

- $H_1$ détermine la direction (droite ou gauche) de la queue.
- $H_1$ ne contient **jamais l'égalité** : c'est $\neq$, $>$ ou $<$.

![[Séance 6 - T-Test - image2.png]]

*Figure : zones de rejet d'un test bilatéral ($\alpha/2$ dans chaque queue), unilatéral à gauche et unilatéral à droite ($\alpha$ dans une queue).*

### Exemple 1a : honoraires de consultants

Un cabinet de conseil affirme que ses consultants gagnent en moyenne **exactement** 260 € de l'heure. On teste l'affirmation sur un échantillon de 16 consultants : $\bar{X} = 200$ €, $s = 96$ €, au seuil $\alpha = 0{,}05$. On suppose la population normale.

- **Étape 1** : $H_0 : \mu = 260$ € ; $H_1 : \mu \neq 260$ €.
- **Étape 2** : $\alpha = 0{,}05$.
- **Étape 3** : statistique de test : loi $t$, car $n$ est petit (16) et $\sigma$ inconnu.
- **Étape 4** : valeurs critiques. C'est une $t_{15}$ : on **ne peut pas** utiliser les valeurs critiques ±1,96 du test $Z$. Dans la table $t$, colonne 0,025 et ligne 15 degrés de liberté : **±2,1315**. Ne pas oublier qu'on a $n-1$ degrés de liberté : $n = 16$, mais d.f. = 15.

![[Séance 6 - T-Test - image5.png]]

*Figure : loi $t_{15}$ avec deux zones de rejet de 2,5 % au-delà de −2,1315 et 2,1315.*

- **Étape 5** : valeur calculée :
$$t_{15} = \frac{200 - 260}{\dfrac{96}{\sqrt{16}}} = \frac{-60}{24} = -2{,}50$$
- **Étape 6** : $-2{,}50 < -2{,}1315$ : **on rejette $H_0$**.
- Avec la [[P-value|p-value]] : $p = 2\,P(t_{15} \geq 2{,}50) \approx 0{,}0245 < 0{,}05$, même conclusion. La p-value dit en plus que le rejet n'est pas très confortable : à $\alpha = 0{,}01$, on ne rejetterait pas $H_0$. [[Complément hors du cours|ⓘ]]
- **[[Taille d'effet]]** : l'écart vaut $d = \dfrac{\lvert \bar X - \mu_0 \rvert}{s} = \dfrac{60}{96} \approx 0{,}63$ écart-type, un effet « moyen » selon les repères usuels de Cohen (0,2 petit, 0,5 moyen, 0,8 grand). Contrairement à $t$, qui grandit avec $\sqrt n$, $d$ ne dépend pas de la taille de l'échantillon : il dit si l'écart est important, $t$ s'il est significatif. [[Complément hors du cours|ⓘ]]

**Intervalle de confiance avec $t$** : sans affirmation sur la moyenne, on construirait un intervalle de confiance à 95 % pour $\mu$ :

$$200 \pm 2{,}1315 \frac{96}{\sqrt{16}} = 200 \text{ €} \pm 51{,}16 \text{ €} \quad\Rightarrow\quad 148{,}84 \text{ €} \leftrightarrow 251{,}16 \text{ €}$$

Interprétation : on a 95 % de confiance que cet intervalle contienne vraiment la **vraie moyenne de la population** $\mu$.

Test et intervalle disent la même chose : un test bilatéral au seuil $\alpha$ rejette $H_0 : \mu = \mu_0$ exactement quand $\mu_0$ est **hors** de l'[[Intervalle de confiance|intervalle de confiance]] à $1-\alpha$. Ici, 260 € n'est pas dans $[148{,}84 ;\ 251{,}16]$, ce qui confirme le rejet de l'étape 6. [[Complément hors du cours|ⓘ]]

En R (voir [[14 - functions in RStudio]]), à partir du vecteur `x` des honoraires : `t.test(x, mu = 260)` donne la statistique $t$, les degrés de liberté, la p-value et l'intervalle à 95 % ; `alternative = "less"` ou `"greater"` pour un test unilatéral, `conf.level = 0.99` pour changer de niveau. [[Complément hors du cours|ⓘ]]

## Test à deux échantillons

- Semblable au test à un échantillon.
- On utilise la statistique $Z$ **si on le peut** ([[Test Z]]) : si $\sigma_1$ et $\sigma_2$ sont **connus**, ou si les échantillons sont **assez grands**. « Assez grand » : les deux échantillons réunis comptent **au moins 32** (certains disent 60 ou plus).
- On doit donc utiliser **$t$** quand :
  - $\sigma_1$ et $\sigma_2$ sont **inconnus**,
  - les échantillons sont **petits**,
  - les populations sont **normales**.

Voir [[Échantillons appariés et indépendants]].

Pour des échantillons **appariés** (mêmes individus mesurés avant et après), on ne compare pas deux groupes : on calcule pour chaque individu la différence $d_i = x_{i,\text{après}} - x_{i,\text{avant}}$, puis on fait un test $t$ à un échantillon sur ces différences, avec $H_0 : \mu_d = 0$ :
$$t_{n-1} = \frac{\bar d}{s_d/\sqrt n}$$
où $n$ est le nombre de paires. L'appariement retire la variabilité entre individus, ce qui rend ce test plus puissant que le test à deux groupes sur les mêmes données. [[Complément hors du cours|ⓘ]]

Statistique $t$ à deux échantillons (« theory → you need to learn this formula ») :

$$t_{n_1+n_2-2} = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{s^2_{pooled}\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}$$

Il faut d'abord calculer la **variance commune** (*pooled variance*) : la variance qu'on obtiendrait en réunissant les deux groupes. C'est une **moyenne pondérée** de $s_1^2$ et $s_2^2$, pondérée par les degrés de liberté :

$$s^2_{pooled} = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

Mettre les variances en commun suppose que les deux populations ont la **même variance** $\sigma_1^2 = \sigma_2^2$ ([[Homoscédasticité|homoscédasticité]]), hypothèse que le cours ne cite pas. Les hypothèses sont en général $H_0 : \mu_1 = \mu_2$ contre $H_1 : \mu_1 \neq \mu_2$ (ou une inégalité stricte en unilatéral). [[Complément hors du cours|ⓘ]]

Exemple chiffré : $n_1 = 10$, $\bar X_1 = 25$, $s_1 = 4$ ; $n_2 = 12$, $\bar X_2 = 21$, $s_2 = 5$. Alors $s^2_{pooled} = \dfrac{9 \cdot 16 + 11 \cdot 25}{20} = 20{,}95$, l'erreur standard vaut $\sqrt{20{,}95\left(\frac{1}{10} + \frac{1}{12}\right)} \approx 1{,}96$ et $t_{20} = \dfrac{25 - 21}{1{,}96} \approx 2{,}04$. La valeur critique bilatérale à 5 % pour 20 degrés de liberté est 2,086 : on ne rejette pas $H_0$, de justesse ($p \approx 0{,}055$). [[Complément hors du cours|ⓘ]]

Si les variances semblent différentes (rapport des écarts-types loin de 1, effectifs inégaux), on utilise le **[[Test de Welch|test de Welch]]**, qui ne met pas les variances en commun :
$$t = \frac{\bar X_1 - \bar X_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}, \qquad df \approx \frac{\left(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}}$$
(degrés de liberté de Welch-Satterthwaite, en général non entiers). C'est le test que fait R par défaut : `t.test(x, y)` est un test de Welch, `t.test(x, y, var.equal = TRUE)` le test à variance commune du cours, `t.test(x, y, paired = TRUE)` le test apparié. [[Complément hors du cours|ⓘ]]

## Idée générale des statistiques de test

Pour tester si un **modèle s'ajuste aux données** (cours suivants) ou si une **hypothèse explique bien les données**, on compare la variation **systématique** à la variation **non systématique** : à quel point le modèle explique bien les données, contre à quel point il se trompe (l'erreur).

$$\text{statistique de test} = \frac{\text{variance expliquée par le modèle}}{\text{variance non expliquée par le modèle}} = \frac{\text{effet}}{\text{erreur}}$$

C'est l'idée reprise par la [[Statistique F]].

Le lien est exact : avec deux groupes, l'[[ANOVA]] à un facteur et le test $t$ à variance commune sont le même test, et $F = t^2$ (une $t_\nu$ au carré suit une loi $F(1, \nu)$). L'ANOVA généralise le test $t$ à plus de deux groupes ([[12 - ANOVA and F-statistic]]). [[Complément hors du cours|ⓘ]]
