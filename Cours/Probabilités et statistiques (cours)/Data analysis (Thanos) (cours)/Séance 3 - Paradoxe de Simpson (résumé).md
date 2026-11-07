---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 3 : Paradoxe de Simpson.docx|Cours 3 - Paradoxe de Simpson]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 3 : Paradoxe de Simpson.docx|Cours 3 - Paradoxe de Simpson]], dans [[Data analysis (Thanos) (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une moyenne globale peut donner la conclusion inverse de celle de chaque sous-groupe. C'est le [[Paradoxe de Simpson]], expliqué par un exemple médical.

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

## Pourquoi cela arrive-t-il ? La variable cachée

Le [[Paradoxe de Simpson]] survient quand une **variable cachée** — un **facteur de confusion** (*confounding factor*) — influence les résultats. Ici, la variable cachée est la **gravité de la maladie**. Si on ne la prend pas en compte dans l'analyse R, on tire une conclusion totalement fausse. Voir aussi [[Corrélation et causalité]].

## Comment le détecter avec R ?

La note renvoie aux commandes `glimpse()` et au paquet `finalfit`. Une analyse globale ne montre rien ; si l'on **stratifie** (on sépare par groupes), le paradoxe saute aux yeux.

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Effectifs de la figure** : les pourcentages et les totaux sont cohérents (par exemple 90/182 = 49 %, 564/895 = 63 %, 761/1000 = 76 %). Alerte « À vérifier » de la transcription : fausse alerte. Image non ouverte.
2. **Paquets cités** : le cours renvoie à « tes commandes `glimpse()` et le paquet `finalfit` » et à un jeu `meldata`, qui ne figurent pas dans les notes de cette matière. Le code donné est un exemple, pas un résultat.
3. **Ton de la note** : le texte s'adresse à « tu » et parle de « mon exemple », de « tes commandes » : il semble repris d'une explication générée ou rédigée pour l'étudiant, pas d'une diapositive du cours.
4. **Effectifs par groupe** (complément) : le paradoxe tient à la répartition très inégale des cas, environ 18 % de grosses tumeurs chez les médicaments contre environ 90 % pour la chirurgie. Le cours ne donne pas ce calcul.
