---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 3 : Paradoxe de Simpson.docx|Cours 3 - Paradoxe de Simpson]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 3 : Paradoxe de Simpson.docx|Cours 3 - Paradoxe de Simpson]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Une moyenne globale peut donner la conclusion inverse de celle de chaque sous-groupe. C'est le [[Paradoxe de Simpson]], expliqué par un exemple médical.

Le paradoxe porte le nom du statisticien britannique E. H. Simpson, qui l'a décrit en 1951. L'exemple le plus cité est celui des admissions de l'université de Berkeley en 1973 (étude publiée dans *Science* en 1975) : au total, les femmes étaient moins souvent admises que les hommes, alors que dans la plupart des départements pris un à un elles l'étaient autant ou plus ; elles postulaient surtout dans les départements les plus sélectifs. [[Complément hors du cours|ⓘ]]

## Un exemple concret : le succès d'un traitement

On veut traiter une tumeur :

- **médicaments** : 76 % de réussite ;
- **chirurgie** : 66 % de réussite.

On se dit : « Les médicaments sont meilleurs ! ». Mais si l'on regarde la **taille des tumeurs** :

![[Séance 3 - Paradoxe de Simpson - image1.png]]

*Figure : tableau à la craie comparant médicaments et chirurgie par taille de tumeur, avec des camemberts réussite (vert) / échec (rouge).*

| | Médicaments | Chirurgie |
|---|---|---|
| Grosses tumeurs | 49 % (92 échecs, 90 réussites) | 63 % (331 échecs, 564 réussites) |
| Petites tumeurs | 82 % (147 échecs, 671 réussites) | 90 % (11 échecs, 94 réussites) |
| Total | 76 % (239 échecs, 761 réussites) | 66 % (342 échecs, 658 réussites) |

**Le paradoxe** : la chirurgie est meilleure dans **chaque catégorie** prise séparément, mais quand on mélange tout, ce sont les médicaments qui gagnent.

**Pourquoi ?** Les grosses tumeurs sont beaucoup plus dures à guérir que les petites. Quand quelqu'un a une grosse tumeur, il se fait opérer : la chirurgie traite donc les cas difficiles. Dans le total, son pourcentage est plus bas parce qu'elle a toujours eu les cas difficiles.

**Le calcul derrière le paradoxe.** Chaque groupe compte 1 000 patients, mais pas répartis de la même façon : sur les 1 000 patients sous médicaments, 818 ont une petite tumeur et 182 une grosse ; sur les 1 000 opérés, 895 ont une grosse tumeur et 105 une petite. Le taux global est une **moyenne pondérée** des taux par catégorie, les poids étant la part de chaque catégorie dans le groupe : $p_{\text{global}} = \sum_k w_k \, p_k$. [[Complément hors du cours|ⓘ]]

$$p_{\text{médicaments}} = 0{,}182 \times 49{,}5\,\% + 0{,}818 \times 82{,}0\,\% \approx 76\,\%, \qquad p_{\text{chirurgie}} = 0{,}895 \times 63{,}0\,\% + 0{,}105 \times 89{,}5\,\% \approx 66\,\%$$

Les médicaments ont surtout des petites tumeurs (poids 0,818 sur le meilleur taux), la chirurgie surtout des grosses : la comparaison des totaux compare donc des patients différents, pas des traitements. Le paradoxe n'est possible que si les groupes ont des compositions très différentes ; à composition égale, il disparaît. [[Complément hors du cours|ⓘ]]

## Pourquoi cela arrive-t-il ? La variable cachée

Le [[Paradoxe de Simpson]] survient quand une **variable cachée** — un **facteur de confusion** (*confounding factor*) — influence les résultats. Ici, la variable cachée est la **gravité de la maladie**. Si on ne la prend pas en compte dans l'analyse R, on tire une conclusion totalement fausse. Voir aussi [[Corrélation et causalité]].

Un facteur de confusion est une variable liée **à la fois** à la variable étudiée (ici le choix du traitement) **et** au résultat (ici la guérison). La gravité remplit les deux conditions : elle oriente vers la chirurgie et elle diminue les chances de guérison. Une variable liée à une seule des deux ne crée pas de confusion. [[Complément hors du cours|ⓘ]]

La parade de référence est l'**[[Essai contrôlé randomisé|essai contrôlé randomisé]]** : on tire au sort le traitement de chaque patient, si bien que la gravité se répartit en moyenne de la même façon dans les deux groupes, y compris pour les facteurs que l'on n'a pas mesurés. Stratifier ou ajuster ne corrige que les facteurs de confusion connus et mesurés : c'est la limite des données observationnelles. [[Complément hors du cours|ⓘ]]

Il ne faut pas pour autant ajuster sur n'importe quelle variable : si la variable est une **conséquence** du traitement (un intermédiaire entre le traitement et le résultat), la stratification fausse au contraire la conclusion. Choisir entre le résultat global et le résultat par sous-groupe demande donc de raisonner sur les causes, pas seulement sur les chiffres. [[Complément hors du cours|ⓘ]]

## Comment le détecter avec R ?

La note renvoie aux commandes `glimpse()` et au paquet `finalfit`. Une analyse globale ne montre rien ; si l'on **stratifie** (on sépare par groupes), le paradoxe saute aux yeux.

- `glimpse()` (paquet `dplyr`, du tidyverse) affiche la structure d'un [[Data frame|data frame]] : le nombre de lignes et de colonnes, le type de chaque colonne et ses premières valeurs. Il sert à repérer les variables catégorielles qui pourraient définir des sous-groupes. [[Complément hors du cours|ⓘ]]
- `finalfit` produit des tableaux de résultats prêts à publier ; sa fonction `finalfit()` affiche côte à côte, pour chaque variable, l'effet **univarié** (brut) et l'effet **multivarié** (ajusté sur les autres variables). Un écart net entre les deux, voire un changement de sens, signale un facteur de confusion. [[Complément hors du cours|ⓘ]]
- Pour un tableau stratifié avec le tidyverse, on calcule le taux de réussite par sous-groupe plutôt que globalement : `donnees %>% group_by(taille, traitement) %>% summarise(taux = mean(reussite))`. [[Complément hors du cours|ⓘ]]

Exemple de code : avec une ligne de tendance qui descend mais des points groupés, on colore par groupe avec [[Bibliothèque ggplot2|ggplot2]] :

```r
# Mauvaise analyse (tendance globale)
ggplot(meldata, aes(x = age, y = survie)) +
  geom_smooth(method = "lm")

# Bonne analyse (on colore par groupe pour voir le paradoxe)
ggplot(meldata, aes(x = age, y = survie, color = stade_cancer)) +
  geom_smooth(method = "lm")
```

## Ce qu'il faut retenir

1. **Ne jamais se fier à une moyenne globale** sans vérifier s'il existe des sous-groupes très différents.
2. **Toujours visualiser les données** avec des couleurs pour les [[Type de variable statistique|variables catégorielles]] (les *factors*, voir [[Facteur (variable catégorielle)]]).
3. C'est pour éviter ce paradoxe qu'on utilise des modèles plus complexes (comme la régression multivariée) qui « ajustent » les résultats en tenant compte des variables cachées.

Ajuster, c'est introduire le facteur de confusion comme variable explicative supplémentaire : le coefficient du traitement mesure alors son effet **à gravité égale**. Pour un résultat binaire comme guéri / non guéri, on utilise une [[Régression logistique|régression logistique]] plutôt qu'une [[Régression linéaire|régression linéaire]] ; en R, par exemple `glm(reussite ~ traitement + taille, family = binomial)`. [[Complément hors du cours|ⓘ]]
