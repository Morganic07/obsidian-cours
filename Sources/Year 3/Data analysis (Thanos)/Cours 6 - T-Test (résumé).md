---
type: source
sources: ["[[Cours 6 - T-Test]]"]
maj: 2026-11-05
---

Résumé de [[Cours 6 - T-Test]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le test $t$ remplace le test $Z$ quand $\sigma$ est inconnu et l'échantillon petit. Le cours le présente pour un échantillon, puis pour deux échantillons indépendants.

## Contenu, dans l'ordre du cours

- **Degrés de liberté** : pour $n = 3$ observations de moyenne imposée 4, les deux premières valeurs sont libres, la troisième est forcée. Il y a donc $n - 1$ degrés de liberté.
- **Loi de Student** : il n'existe pas une loi mais une famille, une par nombre de degrés de liberté. Une même valeur de statistique donne des p-values différentes. Exemple du cours, pour $P(|X| \ge 2{,}05)$ : 0,289 avec $df = 1$, 0,096 avec $df = 5$, 0,054 avec $df = 20$, 0,043 avec $df = 100$.
- **Propriétés** : forme de la loi normale mais plus étalée, symétrique (moyenne = médiane = mode), tend vers la loi normale quand $n$ grandit.
- **Statistique, un échantillon** : $t_{n-1} = \dfrac{\bar{X} - \mu_0}{s/\sqrt{n}}$, où $s/\sqrt{n}$ est l'erreur standard. Intervalle de confiance : $\bar{X} \pm t_{\alpha}\dfrac{s}{\sqrt{n}}$.
- **Bilatéral ou unilatéral** : $H_1$ avec « différent de » donne un test bilatéral, $H_1$ avec une inégalité stricte un test unilatéral. $H_1$ ne contient jamais l'égalité et indique le sens de la queue. Plus $\alpha$ est grand, plus la zone de rejet est grande.

| Test | $H_0$ | $H_1$ |
|---|---|---|
| bilatéral | $\mu = 23$ | $\mu \ne 23$ |
| à gauche | $\mu \ge 23$ | $\mu < 23$ |
| à droite | $\mu \le 23$ | $\mu > 23$ |

- **Exemple 1a** : un cabinet affirme gagner exactement 260 € de l'heure. Échantillon de 16, $\bar{X} = 200$, $s = 96$, $\alpha = 0{,}05$, population normale. $H_0 : \mu = 260$, $H_1 : \mu \ne 260$. Avec $t_{15}$ la valeur critique est $\pm 2{,}1315$ (et non $\pm 1{,}96$). Calcul : $t = (200 - 260)/(96/4) = -2{,}50$, donc on rejette $H_0$. Intervalle à 95 % : $200 \pm 2{,}1315 \times 24$, soit $[148{,}84 ; 251{,}16]$.
- **Deux échantillons** : on utilise $Z$ si les $\sigma$ sont connus ou si les échantillons sont assez grands (ensemble au moins 32, certains disent 60). On utilise $t$ si les $\sigma$ sont inconnus, les échantillons petits et les populations normales.
- **Statistique à deux échantillons** : $t_{n_1+n_2-2} = \dfrac{\bar{X}_1 - \bar{X}_2}{\sqrt{s^2_{pooled}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$, avec $s^2_{pooled} = \dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$ (moyenne des variances pondérée par les degrés de liberté). Note du cours : « theory → you need to learn this formula ».
- **Idée générale des tests** : statistique = variance expliquée par le modèle / variance non expliquée = effet / erreur. C'est l'idée reprise par la [[Statistique F]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes : les calculs ont été refaits à la main (t, intervalle).

1. **Valeur de $t_\alpha$ dans l'intervalle** : pour un intervalle bilatéral à $1-\alpha$, c'est $t_{\alpha/2,\,n-1}$. Le calcul de l'exemple (2,1315) utilise bien la colonne 0,025 (complément).
2. **« Both samples together at least 32 »** : seuil donné sans justification, avec la mention « some say 60, or more ».
3. **Décision de l'exemple 1a** : la case « Reject $H_0$ » est cochée, ce qui est cohérent avec $-2{,}50 < -2{,}1315$.
