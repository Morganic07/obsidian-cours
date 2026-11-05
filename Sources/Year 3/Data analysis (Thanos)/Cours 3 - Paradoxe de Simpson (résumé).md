---
type: source
sources: ["[[Cours 3 - Paradoxe de Simpson]]"]
maj: 2026-11-05
---

Résumé de [[Cours 3 - Paradoxe de Simpson]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une moyenne globale peut donner la conclusion inverse de celle de chaque sous-groupe. C'est le [[Paradoxe de Simpson]], expliqué par un exemple médical.

## Contenu, dans l'ordre du cours

- **Exemple** : traitement d'une tumeur. Au total, les médicaments réussissent à 76 % et la chirurgie à 66 %.
- **Tableau détaillé** (transcrit de l'image, effectifs rouge = échec, vert = réussite) :

| | Médicaments | Chirurgie |
|---|---|---|
| Grosses tumeurs | 49 % (92 échecs, 90 réussites) | 63 % (331 échecs, 564 réussites) |
| Petites tumeurs | 82 % (147 échecs, 671 réussites) | 90 % (11 échecs, 94 réussites) |
| Total | 76 % (239 échecs, 761 réussites) | 66 % (342 échecs, 658 réussites) |

- **Le paradoxe** : la chirurgie fait mieux dans chaque catégorie, mais les médicaments gagnent au total.
- **Explication du cours** : les grosses tumeurs sont plus dures à guérir, et la chirurgie est surtout choisie pour elles. Elle reçoit donc les cas difficiles, ce qui tire son pourcentage global vers le bas.
- **Variable cachée** : facteur de confusion (confounding factor), ici la gravité de la maladie. Sans elle dans l'analyse, la conclusion est fausse.
- **Détection avec R** : stratifier, c'est-à-dire séparer par groupes, et colorer par groupe avec `ggplot2` (`geom_smooth(method = "lm")` avec `color = stade_cancer`).
- **À retenir** : ne pas se fier à une moyenne globale sans regarder les sous-groupes ; visualiser les variables catégorielles avec des couleurs ; la régression multivariée « ajuste » les résultats en tenant compte des variables cachées.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Effectifs de la figure** : les pourcentages et les totaux sont cohérents (par exemple 90/182 = 49 %, 564/895 = 63 %, 761/1000 = 76 %). Alerte « À vérifier » de la transcription : fausse alerte. Image non ouverte.
2. **Paquets cités** : le cours renvoie à « tes commandes `glimpse()` et le paquet `finalfit` » et à un jeu `meldata`, qui ne figurent pas dans les notes de cette matière. Le code donné est un exemple, pas un résultat.
3. **Effectifs par groupe** (complément) : le paradoxe tient à la répartition très inégale des cas, environ 18 % de grosses tumeurs chez les médicaments contre environ 90 % pour la chirurgie. Le cours ne donne pas ce calcul.
