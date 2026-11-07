---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part2 : Inferential statistics.docx|Chp4 Part2 - Inferential statistics]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Statistics/Chp4 Part2 : Inferential statistics.docx|Chp4 Part2 - Inferential statistics]], dans [[Statistics (index)]] : chapitre 4, partie 2, intervalles de confiance (*confidence intervals*). On passe d'une estimation ponctuelle à un encadrement : l'[[Intervalle de confiance]] pour la moyenne d'une [[Loi normale|loi normale]] quand $\sigma$ est connu. En cas d'écart, le cours et ses images font foi. Les formules viennent des transcriptions des images.

## Intervalle de confiance à 95 % (variable gaussienne)

On part de l'intervalle aléatoire

$$\text{(B)}\quad \left(\overline{X} - 1{,}96 \cdot \frac{\sigma}{\sqrt{n}},\ \overline{X} + 1{,}96 \cdot \frac{\sigma}{\sqrt{n}}\right)$$

**Définition.** Si, après avoir observé $X_1 = x_1, \dots, X_n = x_n$, on calcule la [[Moyenne empirique|moyenne observée]] $\bar{x}$ et qu'on la substitue à $\overline{X}$ dans (B), l'intervalle fixe obtenu est un **intervalle de confiance à 95 % pour $\mu$** :
$$\left(\bar{x} - 1{,}96 \cdot \frac{\sigma}{\sqrt{n}},\ \bar{x} + 1{,}96 \cdot \frac{\sigma}{\sqrt{n}}\right)$$
ou encore $\bar{x} - 1{,}96\,\sigma/\sqrt{n} < \mu < \bar{x} + 1{,}96\,\sigma/\sqrt{n}$ « avec 95 % de confiance ».

## Intervalle de confiance général

- $\alpha$ représente la probabilité d'erreur (la zone que l'on rejette). Pour un niveau de confiance de 95 %, $1 - \alpha = 0{,}95$, donc $\alpha = 0{,}05$.

**Définition.** Un intervalle de confiance à $100(1-\alpha)\,\%$ pour la moyenne $\mu$ d'une population normale, quand $\sigma$ est connu, est
$$\left(\bar{x} - z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}},\ \bar{x} + z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}\right),\quad \text{soit } \bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}.$$

![[Chp4 Part2 - Inferential statistics - image6.png]]

*Figure : courbe $z$ : aire centrale $1 - \alpha$ entre $-z_{\alpha/2}$ et $z_{\alpha/2}$, deux queues grisées d'aire $\alpha/2$ chacune ; $P(-z_{\alpha/2} \le Z \le z_{\alpha/2}) = 1 - \alpha$.*

### Valeurs usuelles de $z_{\alpha/2}$

| Niveau de confiance | 99,73 % | 99 % | 98 % | 96 % | 95,45 % | 95 % | 90 % | 80 % | 68,27 % | 50 % |
|---|---|---|---|---|---|---|---|---|---|---|
| $z_{\alpha/2}$ | 3,00 | 2,58 | 2,33 | 2,05 | 2,00 | 1,96 | 1,645 | 1,28 | 1,00 | 0,6745 |

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

## Interprétation de l'intervalle de confiance

![[Chp4 Part2 - Inferential statistics - image5.png]]

*Figure : 16 intervalles de confiance calculés sur 16 échantillons, autour de la valeur $\mu$ (ligne grise) ; tous contiennent $\mu$ sauf le n° 11.*

Sur de nombreux échantillons, le niveau de confiance est la proportion d'intervalles qui contiennent $\mu$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Lecture de l'intervalle** : le cours dit « $\mu$ est dans l'intervalle avec 95 % de confiance ». Le hasard porte sur l'intervalle, pas sur $\mu$ : après calcul, l'intervalle observé contient $\mu$ ou non (complément).
2. **Figure d'interprétation** : le texte seul ne dit pas, pour la figure, que les intervalles sont des intervalles à 95 %. Cette lecture est la plus probable : un sur seize ne contient pas $\mu$. Image non ouverte.
3. **Titre « for a given confidence level α »** : $\alpha$ est le risque d'erreur, le niveau de confiance est $1 - \alpha$ (complément).
