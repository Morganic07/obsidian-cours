---
type: source
tags: [year3]
sources: ["[[Cours 7 - Z-Test]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Cours 7 - Z-Test]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Panorama des tests d'hypothèse (paramétriques ou non, appariés ou indépendants), puis le test $Z$ sur une proportion, avec un échantillon et avec deux.

## Statistiques de test

- Une [[Statistique de test]] est une variable aléatoire calculée à partir des données de l'échantillon et utilisée dans un [[Test d'hypothèse|test d'hypothèse]].
- Elle permet de décider s'il faut rejeter l'hypothèse nulle.
- Elle sert aussi à calculer la [[P-value|p-value]].

| Test d'hypothèse | Statistique de test |
|---|---|
| [[Test Z\|z-test]] | statistique z |
| [[Test t\|t-test]] | statistique t |
| [[ANOVA]] | [[Statistique F\|statistique F]] |
| [[Test du χ²\|test du khi-deux]] | statistique χ² |

## Limites du test d'hypothèse

- Tester une hypothèse n'est pas prendre une décision, mais aide à la prendre.
- Les tests n'expliquent pas **pourquoi** une différence existe ; ils indiquent seulement si elle vient, par exemple, des fluctuations d'[[Échantillonnage|échantillonnage]] ou d'autres causes.
- Les tests reposent sur des probabilités : on ne peut pas les interpréter avec une certitude complète.
- Les inférences tirées de tests de significativité ne sont pas des preuves entièrement correctes de la vérité de l'hypothèse.

## Tests paramétriques et non paramétriques

Les tests statistiques permettent de **généraliser** à la population à partir d'un échantillon. Un test est une technique formelle, fondée sur une **loi de probabilité**, pour conclure sur le caractère raisonnable d'une hypothèse. Voir [[Test paramétrique et non paramétrique]].

- **Test paramétrique** : il **dispose d'information sur le [[Paramètre et statistique|paramètre de la population]]** ; on utilise souvent un test $t$ fondé sur la statistique de Student. Exemple : l'hypothèse « la **moyenne** de la population vaut 15 » est paramétrique.
- **Test non paramétrique** : le chercheur **n'a aucune idée du paramètre de la population** et ne veut pas supposer que les données viennent d'une [[Loi normale|loi gaussienne]].

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 7 - Z-Test/image4.png]]

*Figure : la [[Statistique inférentielle|statistique inférentielle]] — un échantillon représentatif est tiré de la population, puis on en tire des conclusions sur la population.*

## Hiérarchie des tests d'hypothèse

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 7 - Z-Test/image11.png]]

*Figure : organigramme des tests d'hypothèse, paramétriques et non paramétriques, à un ou deux échantillons, indépendants ou appariés.*

- **Tests paramétriques**
  - Un échantillon : test $t$, test $z$.
  - Deux échantillons [[Échantillons appariés et indépendants|indépendants]] : test $t$ à deux groupes, test $Z$.
  - Deux échantillons appariés : test $t$ apparié.
- **Tests non paramétriques**
  - Un échantillon : khi-deux, [[Test de Kolmogorov-Smirnov|Kolmogorov-Smirnov]], [[Test des runs|runs]], [[Test binomial|binomial]].
  - Deux échantillons indépendants : khi-deux, [[Test de Mann-Whitney|Mann-Whitney]], [[Test de la médiane|médiane]], Kolmogorov-Smirnov.
  - Deux échantillons appariés : [[Test du signe|signe]], [[Test de Wilcoxon|Wilcoxon]], [[Test de McNemar|McNemar]], khi-deux.

## Échantillons appariés ou indépendants

Une étude peut produire des mesures **appariées** (*paired*) ou totalement **indépendantes** ; le test doit être choisi en conséquence.

Exemple : effet d'un traitement médical sur le taux d'insuline. Deux plans d'expérience possibles :

- le taux d'insuline est mesuré sur 30 patients **avant et après** le traitement : les données sont organisées **par paires** (chaque patient a deux mesures). La diapositive conseille un « **two-sample t-test** » (voir Points à vérifier : c'est un test $t$ apparié) ;
- le taux est mesuré sur 30 patients sous placebo et 30 **autres** sous traitement : toutes les mesures sont **indépendantes** → test $t$ **à deux groupes indépendants**.

## Procédure du test d'hypothèse

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 7 - Z-Test/image5.png]]

*Figure : organigramme des cinq étapes, la dernière débouchant sur « ne pas rejeter $H_0$ » ou « rejeter $H_0$ et accepter $H_1$ ».*

1. Poser l'hypothèse nulle et l'hypothèse alternative.
2. Choisir un [[Seuil de signification|niveau de signification]].
3. Identifier la statistique de test.
4. Formuler une règle de décision.
5. Prendre un échantillon et décider : **ne pas rejeter $H_0$**, ou **rejeter $H_0$ et accepter $H_1$**.

## Test Z sur une proportion (un échantillon)

Quand $nP$ et $n(1-P)$ valent tous deux au moins 5, on peut utiliser la loi $Z$ comme approximation de la distribution d'échantillonnage de la proportion ([[Approximation normale]]). Ici $P$ est la **proportion supposée** (hypothétique).

La formule vient de l'approximation de la [[Loi binomiale|loi binomiale]] par la loi normale quand $np$ et $n(1-p) \geq 5$. Pour une binomiale, $\mu = np$ et $\sigma = \sqrt{np(1-p)}$, donc :

$$Z = \frac{x-\mu}{\sigma} = \frac{x-np}{\sqrt{np(1-p)}} = \frac{\frac{x}{n} - p}{\frac{\sqrt{np(1-p)}}{n}} = \frac{P_s - p}{\sqrt{\dfrac{p(1-p)}{n}}}$$

avec $P_s$ la proportion d'échantillon et $P$ la proportion de l'hypothèse (annotation de l'étudiant). Quand $n$ grandit et que $p \to 0{,}5$, la binomiale tend vers la normale ; à utiliser quand $np$ et $n(1-p) > 5$.

**Intervalle de confiance** à $(1-\alpha)$ % de $P$ (test bilatéral, donc $Z_{\alpha/2}$) :

$$IC = \hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### Exemple : la politicienne a-t-elle menti ?

Une politicienne affirme que 70 % des habitants de sa circonscription sont démocrates. Un chercheur interroge 100 personnes et n'en trouve que 50.

(a) Test à $\alpha = 0{,}05$ (bilatéral), rejet de $H_0$ si $p < 0{,}05$ :

$$H_0 : P = 0{,}70 \qquad H_1 : P \neq 0{,}70$$

Valeurs critiques : $-1{,}96$ et $1{,}96$ (2,5 % dans chaque queue).

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 7 - Z-Test/image7.png]]

*Figure : loi normale avec deux zones de rejet de 2,5 % au-delà de ±1,96.*

(b) Intervalle de confiance bilatéral à 95 % de $P$ :

$$0{,}50 \pm 1{,}96\sqrt{\frac{(0{,}50)(0{,}50)}{100}} = 0{,}50 \pm 0{,}10 \qquad \text{(marge d'erreur 0,10)}$$

Réponse : $0{,}40 \leftrightarrow 0{,}60$. On a 95 % de confiance que l'intervalle de 0,40 à 0,60 contienne la **vraie proportion** $P$ de démocrates. (Le cours ne calcule pas la statistique $Z$, voir Points à vérifier.)

## Test Z à deux échantillons pour des proportions

- On cherche à savoir si **l'écart observé entre deux proportions est statistiquement significatif ou n'est qu'une [[Erreur d'échantillonnage|erreur d'échantillonnage]]**.
- On utilise un **test Z à deux échantillons** pour comparer les proportions de deux groupes.
- $n_1$ et $n_2$ doivent être **grands** :
$$n_1 p_1 \geq 5, \quad n_1(1-p_1) \geq 5, \quad n_2 p_2 \geq 5, \quad n_2(1-p_2) \geq 5$$

Ce test utilise l'approximation normale :

$$Z = \frac{P_{s1} - P_{s2}}{\sqrt{\bar{p}(1-\bar{p})\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}$$

- $P_{s1} = X_1/n_1$ : proportion d'échantillon dans la population 1 ; $P_{s2} = X_2/n_2$ : dans la population 2 ;
- $X_1$, $X_2$ : nombre de « succès » dans chaque échantillon (un « succès » est l'issue qui nous intéresse, par exemple une pièce défectueuse) ;
- $n_1$, $n_2$ : tailles des échantillons ;
- $\bar{p}$ : estimation **commune** (*pooled* : mise en commun, regroupée) de la proportion :
$$\bar{p} = \frac{X_1+X_2}{n_1+n_2}$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Données appariées et « two-sample t-test »** : image lue directement, la diapositive écrit « an appropriate test … would be a two-sample t-test » pour le cas avant/après. L'organigramme du même cours donne « Paired t test » pour les échantillons appariés. C'est le test $t$ apparié qui convient (complément). **À corriger avant un examen.**
2. **Exemple de la politicienne** : le cours calcule l'intervalle mais pas la statistique. Avec la formule du cours, $Z = (0{,}50 - 0{,}70)/\sqrt{0{,}7 \times 0{,}3/100} \approx -4{,}4$, donc rejet de $H_0$ (complément). Cohérent avec l'intervalle, qui ne contient pas 0,70.
3. **« CIE »** : l'alerte de la transcription soupçonne une faute pour « CI ». C'est l'abréviation de *confidence interval estimator* dans les diapositives de ce cours, pas une faute (fausse alerte probable).
4. **Formule de l'intervalle coupée** : l'image de l'approximation normale se termine sur « Confidence Interval Estimator of P: ». La formule se trouve sur l'image suivante (dessin de l'étudiant), la phrase ne s'arrête donc pas en perdant du contenu.
5. **Condition d'approximation** : « $\ge 5$ » dans un cas, « $> 5$ » dans la dernière phrase de la diapositive.
