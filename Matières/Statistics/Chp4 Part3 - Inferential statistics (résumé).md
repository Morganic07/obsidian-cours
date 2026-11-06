---
type: source
tags: [year3]
sources: ["[[Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 Part3 - Inferential statistics]], dans [[Statistics (matière)]]. En cas d'écart, le cours et ses images font foi. Seule l'image du tableau récapitulatif des intervalles (image11) a été ouverte ; les autres transcriptions n'ont pas été comparées aux images.

## Idée générale

Compléter les [[Intervalle de confiance|intervalles de confiance]] : taille d'échantillon, méthode générale du pivot, puis les cas où $\sigma$ est inconnu (loi de [[Loi de Student|Student]]), la variance (loi du [[Loi du khi-deux|khi-deux]]) et la proportion.

## Contenu, dans l'ordre du cours

- **Taille d'échantillon, $\sigma$ connu** : pour que l'erreur $|\bar{x} - \mu|$ ne dépasse pas $E$ avec une confiance $100(1-\alpha)\,\%$, il faut $n = (z_{\alpha/2}\sigma/E)^2$. $n$ augmente quand la longueur $2E$ diminue, quand $\sigma$ augmente, et quand le niveau de confiance augmente.
- **Loi quelconque, $n$ grand, $\sigma$ connu** : par le [[Théorème central limite]], $\bar{x} \pm z_{\alpha/2}\sigma/\sqrt{n}$ est un intervalle de niveau approximatif $100(1-\alpha)\,\%$.
- **Méthode générale** : trouver une quantité pivot $g(X_1, \dots, X_n; \theta)$ qui dépend de l'échantillon et de $\theta$, et dont la loi ne dépend d'aucun paramètre inconnu. On cherche $C_L$, $C_U$ avec $P[C_L \le g \le C_U] = 1 - \alpha$, puis on isole $\theta$ pour obtenir $P[L \le \theta \le U] = 1 - \alpha$. Pour $\mu$ avec $\sigma$ connu, $g = (\bar{X} - \mu)/(\sigma/\sqrt{n})$.
- **$\sigma$ inconnu** : on remplace $\sigma$ par $S$ et on pose $T = (\bar{X} - \mu)/(S/\sqrt{n})$. La note se demande si c'est une quantité pivot, sans répondre à cet endroit.
- **Loi du khi-deux** : $X = Z_1^2 + \dots + Z_\nu^2$ pour des normales centrées réduites iid, notée $\chi^2_\nu$. C'est une loi gamma de paramètres $\alpha = \nu/2$, $\beta = 2$, de densité $\frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2 - 1}e^{-x/2}$. Additive : la somme de deux khi-deux indépendantes de degrés $\nu_1$, $\nu_2$ est un khi-deux de degré $\nu_1 + \nu_2$ ; elle est aussi soustractive. Pour un échantillon $N(\mu, \sigma)$, $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ (preuve laissée en devoir). Valeur critique $\chi^2_{\alpha,\nu}$ : aire $\alpha$ à droite.
- **Intervalle pour la variance** : $\frac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}$ ; on prend les racines pour $\sigma$. Exemple de la figure : $\chi^2_{0{,}95,10} = 3{,}94$ et $\chi^2_{0{,}05,10} = 18{,}31$.
- **Loi de Student** : si $Z$ est normale centrée réduite et $Y \sim \chi^2_v$ indépendante, $T = Z/\sqrt{Y/v} \sim t_v$. La densité est donnée. Plus $v$ est grand, plus la courbe est proche de $z$ ; à 1 degré de liberté, les queues sont les plus épaisses. **Théorème de Gosset** : pour un échantillon $N(\mu, \sigma)$, $(\bar{X} - \mu)/(S/\sqrt{n}) \sim t_{n-1}$ (preuve en devoir). Notation $t_{\alpha,\nu}$ : aire $\alpha$ à droite.
- **Intervalle pour $\mu$, $\sigma$ inconnu** : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$.
- **Tableau récapitulatif** (échantillon gaussien, intervalles bilatéral, inférieur, supérieur) : voir le point 1 ci-dessous pour une erreur du tableau.
- **Proportion** : si $n$ est grand, $Z = (\hat{P} - p)/\sqrt{p(1-p)/n}$ est approximativement normale, d'où $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.
- **Taille pour une proportion** : $n = (z_{\alpha/2}/E)^2\,p(1-p)$. Comme $p(1-p) \le 0{,}25$, on prend $n = (z_{\alpha/2}/E)^2 \times 0{,}25$ sans connaître $p$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Tableau récapitulatif, ligne « $\sigma^2$ connu »** : image11 ouverte, l'alerte est fondée. Les intervalles inférieur et supérieur portent tous deux $\bar{X} + z_\alpha\sigma/\sqrt{n}$, ce qui est écrit sur l'image. L'intervalle supérieur devrait être $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$, comme dans la ligne « $\sigma^2$ inconnu » (complément). **À corriger avant un examen.**
2. **Titre de la section sur la variance** : « Gaussian distributed rv, mean known ». Les formules utilisent $s^2$ et $\chi^2_{n-1}$, donc la moyenne est inconnue et estimée par $\bar{x}$. Le tableau récapitulatif écrit d'ailleurs « $\mu$ unknown ». « Mean known » est une erreur de titre (complément). **À corriger avant un examen.**
3. **Quantité pivot de $T$** : la question « is this a pivotal quantity ? » reste sans réponse écrite dans la note. Le théorème de Gosset y répond : $T \sim t_{n-1}$, une loi qui ne dépend d'aucun paramètre inconnu, donc oui (complément, pour un échantillon normal).
4. **Hypothèses de Student** : le théorème de Gosset et l'intervalle de Student supposent un échantillon normal. Le cours le dit pour le théorème, non pour la section sur la proportion ou le TCL : l'intervalle $t$ pour une loi quelconque n'est pas traité.
5. **Figure de $\chi^2$** : la transcription note un « X » majuscule à la place de $\chi$ dans la figure. Défaut de police sans conséquence.
6. **Taille pour une proportion** : « on peut appliquer le TCL tant que $n$ est plus grand que… » mélange deux choses. Avec $p(1-p) \le 0{,}25$, la formule donne la taille suffisante pour une erreur $E$, ce qui n'a pas de lien direct avec la condition du TCL (complément).
