---
type: source
tags: [year3]
sources: ["[[Chp4 Part2 - Inferential statistics]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 Part2 - Inferential statistics]], dans [[Statistics (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Passer d'une estimation ponctuelle à un encadrement : l'[[Intervalle de confiance]] pour la moyenne d'une loi normale, quand $\sigma$ est connu.

## Contenu, dans l'ordre du cours

- **Intervalle à 95 %** : $\left(\bar{x} - 1{,}96\frac{\sigma}{\sqrt{n}},\ \bar{x} + 1{,}96\frac{\sigma}{\sqrt{n}}\right)$ pour $\mu$. Il se déduit de l'intervalle aléatoire $(\bar{X} \pm 1{,}96\,\sigma/\sqrt{n})$ en remplaçant $\bar{X}$ par la valeur observée $\bar{x}$.
- **Niveau $100(1-\alpha)\,\%$** : $\alpha$ est la probabilité d'erreur, soit $\alpha = 0{,}05$ pour 95 %. L'intervalle est $\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$. Le quantile $z_\alpha$ vérifie $P(Z > z_\alpha) = \alpha$, donc $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$.
- **Valeurs usuelles de $z_{\alpha/2}$** : 99,73 % : 3,00 ; 99 % : 2,58 ; 98 % : 2,33 ; 96 % : 2,05 ; 95,45 % : 2,00 ; 95 % : 1,96 ; 90 % : 1,645 ; 80 % : 1,28 ; 68,27 % : 1,00 ; 50 % : 0,6745.
- **Démarche** : à partir de $P\{-z_{\alpha/2} < \sqrt{n}(\bar{X} - \mu)/\sigma < z_{\alpha/2}\} = 1 - \alpha$, on isole $\mu$ pour obtenir $P\{\bar{X} - z_{\alpha/2}\sigma/\sqrt{n} < \mu < \bar{X} + z_{\alpha/2}\sigma/\sqrt{n}\} = 1 - \alpha$. Règle retenue : intervalle = estimation ponctuelle $\pm$ marge d'erreur.
- **Interprétation** : la figure montre 16 intervalles construits sur 16 échantillons, tous contenant $\mu$ sauf le numéro 11. Le niveau de confiance est la proportion d'intervalles qui contiennent $\mu$ sur de nombreux échantillons.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Lecture de l'intervalle** : le cours dit « $\mu$ est dans l'intervalle avec 95 % de confiance ». Le hasard porte sur l'intervalle, pas sur $\mu$ : après calcul, l'intervalle observé contient $\mu$ ou non (complément).
2. **Figure d'interprétation** : le texte seul ne dit pas, pour la figure, que les intervalles sont des intervalles à 95 %. Cette lecture est la plus probable : un sur seize ne contient pas $\mu$. Image non ouverte.
