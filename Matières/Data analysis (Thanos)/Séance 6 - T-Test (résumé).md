---
type: source
tags: [year3]
sources: ["[[Cours 6 - T-Test]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Cours 6 - T-Test]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le test $t$ remplace le test $Z$ quand $\sigma$ est inconnu et l'échantillon petit. Le cours le présente pour un échantillon, puis pour deux échantillons indépendants.

## La loi de Student (*t-distribution*)

### Comprendre les degrés de liberté

Soit un échantillon de taille $n = 3$, par exemple $\{2, 4, 6\}$, de moyenne **4**. Si l'on tire un autre échantillon en imposant que sa moyenne soit aussi 4 :

- la première observation peut prendre n'importe quelle valeur (1 par exemple) ;
- la deuxième aussi (5 par exemple) ;
- la troisième n'a **aucune liberté** : elle vaut nécessairement 6, pour que $(1+5+6)/3 = 4$.

Le nombre de [[Variance et écart-type d'échantillon|degrés de liberté]] est donc 2, soit **$n-1$**.

### Une famille de lois

Il n'existe pas **une** [[Loi de Student]], mais une infinité, une par nombre de degrés de liberté. Une même valeur de statistique peut donc donner des [[P-value|p-values]] très différentes selon le nombre de degrés de liberté (donc la taille de l'échantillon).

| df | $P(\lvert X\rvert \geq 2{,}05)$ | chaque queue | centre |
|---|---|---|---|
| 1 | 0,28893 | 14,45 % | 71,11 % |
| 5 | 0,09564 | 4,78 % | 90,44 % |
| 20 | 0,05371 | 2,69 % | 94,63 % |
| 100 | 0,04298 | 2,15 % | 95,7 % |

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 6 - T-Test/image4.png]]

*Figure : densités de la loi t pour df = 1, 5, 20 et 100, avec les queues au-delà de ±2,05 ; plus df augmente, plus les queues s'amincissent.*

### Propriétés

- Ressemble à la [[Loi normale|loi normale]], mais **plus étalée**.
- **Symétrique** autour de la moyenne : moyenne = médiane = mode.
- Ce n'est pas une seule loi, mais une série de lois, une par nombre de degrés de liberté.
- Quand $n$ grandit, la loi $t$ se rapproche de la loi normale.

## Le test t en pratique (un échantillon)

Voir [[Test t]].

Pour tester une hypothèse ($n-1$ degrés de liberté) :

$$t_{n-1} = \frac{\bar{X} - \mu_0}{s_{\bar{X}}} = \frac{\bar{X} - \mu_0}{\dfrac{s}{\sqrt{n}}}$$

où $s_{\bar{X}} = s/\sqrt{n}$ est l'**erreur standard** (*[[Estimateur|standard error]]*) et $\mu_{H_0}$ ou $\mu_0$ la **moyenne de population** affirmée (par exemple l'affirmation d'une entreprise).

Intervalle de confiance à $(1-\alpha)$ % :

$$\bar{X} \pm t_{\alpha} \frac{s}{\sqrt{n}}$$

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

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 6 - T-Test/image2.png]]

*Figure : zones de rejet d'un test bilatéral ($\alpha/2$ dans chaque queue), unilatéral à gauche et unilatéral à droite ($\alpha$ dans une queue).*

### Exemple 1a : honoraires de consultants

Un cabinet de conseil affirme que ses consultants gagnent en moyenne **exactement** 260 € de l'heure. On teste l'affirmation sur un échantillon de 16 consultants : $\bar{X} = 200$ €, $s = 96$ €, au seuil $\alpha = 0{,}05$. On suppose la population normale.

- **Étape 1** : $H_0 : \mu = 260$ € ; $H_1 : \mu \neq 260$ €.
- **Étape 2** : $\alpha = 0{,}05$.
- **Étape 3** : statistique de test : loi $t$, car $n$ est petit (16) et $\sigma$ inconnu.
- **Étape 4** : valeurs critiques. C'est une $t_{15}$ : on **ne peut pas** utiliser les valeurs critiques ±1,96 du test $Z$. Dans la table $t$, colonne 0,025 et ligne 15 degrés de liberté : **±2,1315**. Ne pas oublier qu'on a $n-1$ degrés de liberté : $n = 16$, mais d.f. = 15.

![[Cours/Year 3/Data analysis (Thanos)/medias/Cours 6 - T-Test/image5.png]]

*Figure : loi $t_{15}$ avec deux zones de rejet de 2,5 % au-delà de −2,1315 et 2,1315.*

- **Étape 5** : valeur calculée :
$$t_{15} = \frac{200 - 260}{\dfrac{96}{\sqrt{16}}} = \frac{-60}{24} = -2{,}50$$
- **Étape 6** : $-2{,}50 < -2{,}1315$ : **on rejette $H_0$**.

**Intervalle de confiance avec $t$** : sans affirmation sur la moyenne, on construirait un intervalle de confiance à 95 % pour $\mu$ :

$$200 \pm 2{,}1315 \frac{96}{\sqrt{16}} = 200 \text{ €} \pm 51{,}16 \text{ €} \quad\Rightarrow\quad 148{,}84 \text{ €} \leftrightarrow 251{,}16 \text{ €}$$

Interprétation : on a 95 % de confiance que cet intervalle contienne vraiment la **vraie moyenne de la population** $\mu$.

## Test à deux échantillons

- Semblable au test à un échantillon.
- On utilise la statistique $Z$ **si on le peut** ([[Test Z]]) : si $\sigma_1$ et $\sigma_2$ sont **connus**, ou si les échantillons sont **assez grands**. « Assez grand » : les deux échantillons réunis comptent **au moins 32** (certains disent 60 ou plus).
- On doit donc utiliser **$t$** quand :
  - $\sigma_1$ et $\sigma_2$ sont **inconnus**,
  - les échantillons sont **petits**,
  - les populations sont **normales**.

Voir [[Échantillons appariés et indépendants]].

Statistique $t$ à deux échantillons (« theory → you need to learn this formula ») :

$$t_{n_1+n_2-2} = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{s^2_{pooled}\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}$$

Il faut d'abord calculer la **variance commune** (*pooled variance*) : la variance qu'on obtiendrait en réunissant les deux groupes. C'est une **moyenne pondérée** de $s_1^2$ et $s_2^2$, pondérée par les degrés de liberté :

$$s^2_{pooled} = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

## Idée générale des statistiques de test

Pour tester si un **modèle s'ajuste aux données** (cours suivants) ou si une **hypothèse explique bien les données**, on compare la variation **systématique** à la variation **non systématique** : à quel point le modèle explique bien les données, contre à quel point il se trompe (l'erreur).

$$\text{statistique de test} = \frac{\text{variance expliquée par le modèle}}{\text{variance non expliquée par le modèle}} = \frac{\text{effet}}{\text{erreur}}$$

C'est l'idée reprise par la [[Statistique F]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes : les calculs ont été refaits à la main (t, intervalle).

1. **Valeur de $t_\alpha$ dans l'intervalle** : pour un intervalle bilatéral à $1-\alpha$, c'est $t_{\alpha/2,\,n-1}$. Le calcul de l'exemple (2,1315) utilise bien la colonne 0,025 (complément).
2. **« Both samples together at least 32 »** : seuil donné sans justification, avec la mention « some say 60, or more ».
3. **Décision de l'exemple 1a** : la case « Reject $H_0$ » est cochée, ce qui est cohérent avec $-2{,}50 < -2{,}1315$.
