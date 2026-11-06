---
type: source
tags: [year3]
sources: ["[[Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-05
---

Résumé de [[Cours 9 - Covariance and Correlation]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Mesurer la relation linéaire entre deux variables : covariance, corrélation de Pearson, coefficient de détermination, puis les corrélations de rang de Spearman et de Kendall.

## Contenu, dans l'ordre du cours

- **Modèles** : un modèle déterministe donne une relation exacte ($F = ma$). Un modèle probabiliste ajoute une erreur aléatoire à une partie déterministe ($y = 10x + \varepsilon$). Il se divise en modèles de régression et modèles de corrélation.
- **Corrélation linéaire** : le cours ne mesure que la relation linéaire entre deux variables aléatoires. Une corrélation n'implique pas une relation de cause à effet.
- **Loi conjointe et marginales** : $p(x,y) = P(X=x \text{ et } Y=y)$, positive, de somme 1. Marginales $p_X(x) = \sum_y p(x,y)$. $X$ et $Y$ sont indépendantes si $p(x,y) = p_X(x)p_Y(y)$ pour tout couple.
- **Espérance** : $E[h(X,Y)] = \sum h(x,y)p(x,y)$. Elle est linéaire. Si $X$ et $Y$ sont indépendantes, $E[g_1(X)g_2(Y)] = E[g_1(X)]E[g_2(Y)]$.
- **Covariance** : $\mathrm{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$, estimée par $\dfrac{\sum(x_i - \bar{X})(y_i - \bar{Y})}{n-1}$. Signe positif : les variables montent ensemble ; négatif : l'une monte quand l'autre baisse ; zéro : pas de relation linéaire évidente. Sa valeur dépend des unités. Propriétés : symétrie, $\mathrm{Cov}(X,X) = \mathrm{Var}(X)$, $\mathrm{Cov}(X,Y) = E(XY) - \mu_X\mu_Y$, distributivité.
- **Corrélation (Pearson)** : $\rho_{X,Y} = \dfrac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$, sans unité. Propriétés : symétrique, $\mathrm{Corr}(X,X) = 1$, invariante par changement d'échelle si $ac > 0$, comprise entre $-1$ et $1$. $\rho = \pm 1$ si et seulement si $Y = aX + b$ avec $a \ne 0$.
- **Indépendance et corrélation** : indépendantes implique $\rho = 0$, mais $\rho = 0$ n'implique pas l'indépendance (annotations de l'étudiant : flèche vers la droite, grande flèche vers le bas, puis flèche inverse barrée). $\rho = 0$ dit seulement qu'il n'y a pas de relation linéaire, une relation non linéaire forte reste possible. Les variables sont alors « non corrélées », ce qui équivaut à $E[XY] = \mu_X\mu_Y$.
- **Coefficient d'échantillon $r$** : estimation de $\rho$, qu'on ne peut calculer qu'avec un recensement. $r = \dfrac{SS_{xy}}{\sqrt{SS_{xx}SS_{yy}}}$ avec $SS_{xy} = \sum xy - \dfrac{\sum x\sum y}{n}$ et de même pour $SS_{xx}$, $SS_{yy}$.
- **Coefficient de détermination** : $R^2 = r^2 = \dfrac{SS_{yy} - SSE}{SS_{yy}}$, proportion de la variation de $Y$ expliquée par $X$, entre 0 et 1. Exemples du cours : $r = 0{,}30$ donne 9 % expliqué (faible), $0{,}50$ donne 25 % (modéré), $0{,}90$ donne 81 % (très fort). En corrélation, X et Y jouent le même rôle ; en [[Régression linéaire|régression]], il faut choisir, et l'équation change si on les échange.
- **Spearman** : corrélation de rang, non paramétrique, mesure une relation monotone entre variables continues ou ordinales. Sans ex æquo : $\rho = 1 - \dfrac{6\sum d_i^2}{n(n^2-1)}$ ($d_i$ différence de rangs). Avec ex æquo : on applique la formule de Pearson aux rangs. Hypothèses : paires indépendantes, échelle ordinale, d'intervalle ou de ratio, relation monotone.
- **Ex æquo** : on attribue la moyenne des rangs hypothétiques. Exemple : trois valeurs 2,2 aux rangs 4, 5, 6 reçoivent 5 chacune ; deux valeurs 5,3 aux rangs 7, 8 reçoivent 7,5.
- **Pearson contre Spearman** : Pearson travaille sur les valeurs et une relation linéaire, Spearman sur les rangs et les relations monotones. Si le nuage semble « peut-être monotone, peut-être linéaire », Spearman est le meilleur choix. Exemples : relation monotone croissante non linéaire, Pearson $0{,}851$ et Spearman $+1$ ; pas de tendance, les deux à $-0{,}093$. Aucun des deux ne capte un autre type de relation non linéaire.
- **Kendall $\tau$** : non paramétrique, alternative à Pearson quand ses hypothèses échouent, et à Spearman pour un petit échantillon avec beaucoup d'ex æquo. Il compte les paires concordantes ($x_2 - x_1$ et $y_2 - y_1$ de même signe) et discordantes (signes opposés). Il est en général plus petit que le $\rho$ de Spearman.
- **Résumé** : Pearson est paramétrique (le cours dit qu'il ne s'emploie que si $x$ et $y$ viennent de lois normales) ; Kendall et Spearman sont fondés sur les rangs.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Spearman is exactly 1 » pour la relation décroissante** : image lue directement. La diapositive écrit bien « Spearman = −1 » sur la ligne puis « Spearman is exactly 1 » dans le commentaire. Il faut lire $-1$ (complément). Alerte de la transcription confirmée.
2. **« Compris strictement entre −1 et 1 »** : la note de commentaire du cours l'écrit, alors que $\pm 1$ sont atteints (relations parfaites) et que la proposition donne $-1 \le \mathrm{Corr} \le 1$. Il faut lire « entre $-1$ et $1$ » (complément).
3. **« $R^2 = r^2$ »** : vrai pour une régression linéaire simple. Avec plusieurs variables explicatives, $R^2$ n'est plus le carré d'un seul coefficient (complément, voir [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11]]).
4. **Covariance d'échantillon à $n-1$** : l'image donne $\dfrac{\sum(x_i - \bar{X})(y_i - \bar{Y})}{n-1}$, alors que la covariance de population (définition) utilise l'espérance. Les deux sont présentées sans les distinguer.
5. **Images non ouvertes** : toutes, sauf celle du comparatif Pearson/Spearman. Les formules sont reprises des transcriptions, sans écart apparent avec les formules usuelles.
