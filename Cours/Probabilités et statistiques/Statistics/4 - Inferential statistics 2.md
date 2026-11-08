---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part2 : Inferential statistics.docx|Chp4 Part2 - Inferential statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp4 Part2 : Inferential statistics.docx|Chp4 Part2 - Inferential statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : chapitre 4, partie 2, intervalles de confiance (*confidence intervals*). On passe d'une estimation ponctuelle à un encadrement : l'[[Intervalle de confiance]] pour la moyenne d'une [[Loi normale|loi normale]] quand $\sigma$ est connu. Les formules viennent des transcriptions des images.

## Intervalle de confiance à 95 % (variable gaussienne)

On part de l'intervalle aléatoire

$$\text{(B)}\quad \left(\overline{X} - 1{,}96 \cdot \frac{\sigma}{\sqrt{n}},\ \overline{X} + 1{,}96 \cdot \frac{\sigma}{\sqrt{n}}\right)$$

D'où vient (B) : pour un échantillon d'une loi normale, $\overline{X}$ suit $\mathcal{N}(\mu, \sigma/\sqrt{n})$, donc $Z = (\overline{X} - \mu)/(\sigma/\sqrt{n})$ suit la loi normale centrée réduite, et $P(-1{,}96 < Z < 1{,}96) = 0{,}95$ puisque $\Phi(1{,}96) \approx 0{,}975$. Les bornes de (B) dépendent de $\overline{X}$ : c'est un intervalle **aléatoire**, qui contient $\mu$ avec probabilité 0,95 avant l'observation (voir la démarche plus bas). [[Complément hors du cours|ⓘ]]

**Définition.** Si, après avoir observé $X_1 = x_1, \dots, X_n = x_n$, on calcule la [[Moyenne empirique|moyenne observée]] $\bar{x}$ et qu'on la substitue à $\overline{X}$ dans (B), l'intervalle fixe obtenu est un **intervalle de confiance à 95 % pour $\mu$** :
$$\left(\bar{x} - 1{,}96 \cdot \frac{\sigma}{\sqrt{n}},\ \bar{x} + 1{,}96 \cdot \frac{\sigma}{\sqrt{n}}\right)$$
ou encore $\bar{x} - 1{,}96\,\sigma/\sqrt{n} < \mu < \bar{x} + 1{,}96\,\sigma/\sqrt{n}$ « avec 95 % de confiance ».

Exemple : $n = 25$ mesures d'une population normale d'écart-type connu $\sigma = 10$, de moyenne observée $\bar{x} = 80$. $\sigma/\sqrt{n} = 2$, la marge d'erreur vaut $1{,}96 \times 2 = 3{,}92$, d'où l'intervalle $(76{,}08 ;\ 83{,}92)$. [[Complément hors du cours|ⓘ]]

## Intervalle de confiance général

Intervalle pour un niveau de confiance donné $1 - \alpha$. [[Erreurs du cours#^e-4-inferential-statistics-2|✎]]

- $\alpha$ représente la probabilité d'erreur (la zone que l'on rejette). Pour un niveau de confiance de 95 %, $1 - \alpha = 0{,}95$, donc $\alpha = 0{,}05$.

**Définition.** Un intervalle de confiance à $100(1-\alpha)\,\%$ pour la moyenne $\mu$ d'une population normale, quand $\sigma$ est connu, est
$$\left(\bar{x} - z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}},\ \bar{x} + z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}\right),\quad \text{soit } \bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}.$$

![[Chp4 Part2 - Inferential statistics - image6.png]]

*Figure : courbe $z$ : aire centrale $1 - \alpha$ entre $-z_{\alpha/2}$ et $z_{\alpha/2}$, deux queues grisées d'aire $\alpha/2$ chacune ; $P(-z_{\alpha/2} \le Z \le z_{\alpha/2}) = 1 - \alpha$.*

### Valeurs usuelles de $z_{\alpha/2}$

| Niveau de confiance | 99,73 % | 99 % | 98 % | 96 % | 95,45 % | 95 % | 90 % | 80 % | 68,27 % | 50 % |
|---|---|---|---|---|---|---|---|---|---|---|
| $z_{\alpha/2}$ | 3,00 | 2,58 | 2,33 | 2,05 | 2,00 | 1,96 | 1,645 | 1,28 | 1,00 | 0,6745 |

Ces valeurs sont des [[Quantile|quantiles]] de la loi normale : $z_{\alpha/2} = \Phi^{-1}(1 - \alpha/2)$, par exemple $\Phi^{-1}(0{,}975) \approx 1{,}96$ ; en R, `qnorm(1 - alpha/2)`. Les niveaux 68,27 %, 95,45 % et 99,73 % correspondent à $z = 1$, 2 et 3 : c'est la règle « 68-95-99,7 » de la [[Loi normale|loi normale]]. [[Complément hors du cours|ⓘ]]

## Démarche : de $Z$ à un encadrement de $\mu$

Le cours montre comment passer d'une affirmation de probabilité centrée sur $Z$ à un encadrement centré sur le paramètre $\mu$ :

1. $z_\alpha$ est tel que $P\{Z > z_\alpha\} = \alpha$, quand $Z$ suit la loi normale centrée réduite (*standard normal random variable*).
2. Donc, pour tout $\alpha$ : $P\{-z_{\alpha/2} < Z < z_{\alpha/2}\} = 1 - \alpha$.
3. Avec $Z = \sqrt{n}\,(\overline{X} - \mu)/\sigma$ :
$$P\left\{-z_{\alpha/2} < \sqrt{n}\,\frac{\overline{X} - \mu}{\sigma} < z_{\alpha/2}\right\} = 1 - \alpha$$
4. On isole $\mu$ :
$$P\left\{\overline{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} < \mu < \overline{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right\} = 1 - \alpha$$
5. Un intervalle de confiance bilatéral à $100(1-\alpha)\,\%$ pour $\mu$ est donc $\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\ \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right)$, où $\bar{x}$ est la moyenne observée.

**Règle retenue** : intervalle = [[Estimateur|estimation ponctuelle]] ($\bar{x}$ par exemple) $\pm$ marge d'erreur.

La **largeur** de l'intervalle vaut $2\,z_{\alpha/2}\,\sigma/\sqrt{n}$. Elle augmente avec le niveau de confiance (plus de certitude coûte de la précision : à 99 %, l'intervalle est $2{,}58/1{,}96 \approx 1{,}32$ fois plus large qu'à 95 %) et avec $\sigma$ ; elle diminue en $1/\sqrt{n}$, si bien que diviser la largeur par 2 demande quatre fois plus d'observations. Le calcul de $n$ pour une marge donnée est dans [[4 - Inferential statistics 3]]. [[Complément hors du cours|ⓘ]]

Le cas « $\sigma$ connu » est rare en pratique : il sert de modèle. Quand $\sigma$ est inconnu, on le remplace par $s$ et $z_{\alpha/2}$ par un quantile de la [[Loi de Student|loi de Student]] ; pour une population non normale et $n$ grand, le [[Théorème central limite]] rend l'intervalle approximativement valable ([[4 - Inferential statistics 3]]). [[Complément hors du cours|ⓘ]]

## Interprétation de l'intervalle de confiance

![[Chp4 Part2 - Inferential statistics - image5.png]]

*Figure : 16 intervalles de confiance calculés sur 16 échantillons, autour de la valeur $\mu$ (ligne grise) ; tous contiennent $\mu$ sauf le n° 11.*

Sur de nombreux échantillons, le niveau de confiance est la proportion d'intervalles qui contiennent $\mu$.

Une fois les données observées, l'intervalle est fixe et $\mu$ aussi : il contient $\mu$ ou non, sans probabilité en jeu. Dire « il y a 95 % de chances que $\mu$ soit entre 76,08 et 83,92 » est donc incorrect dans ce cadre (fréquentiste) ; on dit « avec 95 % de confiance », la confiance portant sur la méthode, qui réussit dans 95 % des cas. L'intervalle n'annonce pas non plus que 95 % des observations y tombent : il encadre la moyenne $\mu$, pas les valeurs individuelles ([[Intervalle de prédiction]]). [[Complément hors du cours|ⓘ]]

Lien avec les tests : une valeur $\mu_0$ est hors de l'intervalle de confiance bilatéral à $100(1-\alpha)\,\%$ exactement quand le [[Test Z|test Z]] bilatéral rejette $H_0 : \mu = \mu_0$ au [[Seuil de signification|seuil de signification]] $\alpha$. L'intervalle en dit donc plus qu'un test : il donne toutes les valeurs de $\mu$ compatibles avec les données. [[Complément hors du cours|ⓘ]]