---
type: source
sources: ["[[Cours 8 - Chi²-Test]]"]
maj: 2026-11-05
---

Résumé de [[Cours 8 - Chi²-Test]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

La loi du χ² sert à deux choses : estimer et tester une variance, et tester l'indépendance de deux variables catégorielles sur un tableau croisé. Le second usage est le [[Test du χ²]].

## Contenu, dans l'ordre du cours

- **Loi du χ²** : variable continue, toujours asymétrique à droite, de plus en plus symétrique quand les degrés de liberté $k$ augmentent. Densité $\dfrac{1}{2^{k/2}\Gamma(k/2)}x^{k/2-1}e^{-x/2}$, avec $\Gamma(x) = \int_0^\infty t^{x-1}e^{-t}dt$. Moyenne $k$, variance $2k$.
- **Variance d'échantillon** : si les $X_i$ sont normales, $\dfrac{(n-1)S^2}{\sigma^2}$ suit une loi du χ² à $n-1$ degrés de liberté. Le cours le justifie par $(n-1)s^2 = \sum(x_i - \bar{x})^2$, somme de carrés.
- **Intervalle de confiance de $\sigma^2$** : $\dfrac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}} \le \sigma^2 \le \dfrac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}$. Pour $\sigma$, on prend les racines. Exemple de points : $\chi^2_{0{,}05;10} = 18{,}31$ et $\chi^2_{0{,}95;10} = 3{,}94$.
- **Récapitulatif des intervalles à $100(1-\alpha)\,\%$** : $\mu$ avec $\sigma^2$ connu, $\bar{X} \pm z_{\alpha/2}\sigma/\sqrt{n}$ ; $\mu$ avec $\sigma^2$ inconnu, $\bar{X} \pm t_{\alpha/2,n-1}S/\sqrt{n}$ ; $\sigma^2$, intervalle ci-dessus. Le tableau donne aussi les intervalles unilatéraux.
- **Test sur une variance** : statistique $\chi^{2*} = \dfrac{(n-1)s^2}{\sigma_0^2}$. Les tables du χ² ne sont pas symétriques : les valeurs des queues inférieure et supérieure sont listées séparément.
- **Test du χ² sur tableau croisé** : on compare les effectifs observés $f_o$ aux effectifs attendus par hasard $f_e = \dfrac{\text{marge de ligne} \times \text{marge de colonne}}{N}$. Le test dit seulement si les variables sont indépendantes, pas la forme du lien (pour la voir, comparer les pourcentages par colonne). $df = (\text{lignes} - 1)(\text{colonnes} - 1)$, statistique $\chi^2 = \sum\dfrac{(f_o - f_e)^2}{f_e}$.
- **Limites** : la statistique croît avec $N$, donc avec un grand échantillon, une relation sans importance devient significative. Le cours conseille $\alpha = 0{,}01$ quand $N > 1000$. Significatif ne veut pas dire important. Pour justifier le test à l'examen : échantillonnage aléatoire simple, variables catégorielles, effectif attendu d'au moins 5 par cellule.
- **Exemple** : 25 villes, ventes d'armes (haut ou bas) et taux d'homicides (bas ou haut). Observé : 8 et 5 pour ventes hautes, 4 et 8 pour ventes basses. Effectifs attendus 6,24 ; 6,76 ; 5,76 ; 6,24. $\chi^2 = 0{,}50 + 0{,}46 + 0{,}54 + 0{,}50 = 2{,}00$. Valeur critique 3,841 ($\alpha = 0{,}05$, $df = 1$). Comme $2{,}00 < 3{,}841$, on ne rejette pas $H_0$ : pas de lien significatif entre les deux variables.
- **Test non paramétrique** : le χ² ne suppose rien sur la forme de la loi d'échantillonnage. Hypothèses : $H_0$ variables indépendantes (ou $P_0 = P_1$), $H_1$ dépendantes.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images ouvertes : le tableau récapitulatif des intervalles et la table du χ².

1. **Phrase d'introduction sur la loi** : le cours demande ce qu'est la somme des carrés d'une loi de Student et répond que $x_1^2 + \dots + x_n^2$ suit un χ² à $n-1$ degrés de liberté si $X$ est normale. La somme des carrés de $n$ normales centrées réduites indépendantes suit un χ² à $n$ degrés. Le degré $n-1$ vaut pour les écarts à la moyenne, comme dans la suite du cours. La mention d'une loi de Student n'a pas de sens ici (complément). **À corriger avant un examen.**
2. **Tableau récapitulatif, ligne $\sigma^2$ connu** : image lue directement. L'intervalle « supérieur » est écrit $(\bar{X} + z_\alpha\sigma/\sqrt{n}, \infty)$ avec un signe plus, alors que la ligne $\sigma^2$ inconnu écrit un moins. Le signe correct est « moins » (complément). Alerte de la transcription confirmée.
3. **Table du χ²** : image lue directement. La colonne 0,005 ne correspond pas aux tables usuelles dès $df = 2$ (valeur usuelle 0,0100, la diapositive écrit 0,0001) ni pour $df = 25$ à 30 (usuelles autour de 10,5 à 13,8, la diapositive écrit 6,08 à 8,50). Les autres colonnes lues semblent cohérentes (complément). Ne pas utiliser cette colonne telle quelle.
4. **Étiquettes « Lower » et « Upper Interval »** du tableau récapitulatif : les intervalles de la colonne « Lower » sont de la forme $(-\infty, \dots)$, donc ce sont des bornes supérieures de confiance. Libellés ambigus, repris tels quels.
5. **Calcul de l'exemple** : somme des colonnes recalculée, 2,00 (1,99 avant arrondi). L'alerte de la transcription sur la somme des $f_e$ est une fausse alerte.
6. **Fragments d'axe** (0, 4, 8, 12) en haut à droite d'une image : sans importance, fausse alerte.
