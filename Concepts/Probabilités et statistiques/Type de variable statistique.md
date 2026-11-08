---
type: concept
tags:
  - year3
aliases:
  - variable qualitative
  - variable quantitative
  - variable catégorielle
  - categorical variable
  - variables catégorielles
  - variable nominale
  - variable ordinale
  - niveau de mesure
  - levels of measurement
  - échelle nominale
  - échelle ordinale
  - échelle d'intervalle
  - échelle de ratio
  - données univariées
  - données bivariées
  - données multivariées
sources:
  - "[[2 - Introduction statistics|Cours 2 - Introduction statistics]]"
  - "[[1 - Intro to statistics|Chp1 - Intro to statistics]]"
  - "[[Raw/Year 3/Data analysis (Thanos)/Cours 2 : Introduction statistics.docx|Cours 2 - Introduction statistics]]"
maj: 2026-11-08
---

Une variable est soit **qualitative** (ou catégorielle), soit **quantitative**.

- **Qualitative** : *nominale* (classification seule) ou *ordinale* (classification et ordre). Aucune opération arithmétique n'a de sens.
- **Quantitative** : discrète ou continue ; *d'intervalle* (l'écart entre deux valeurs est significatif) ou *de ratio* (il existe un zéro absolu).

**Niveaux de mesure et statistiques permises** : mode et fréquences pour le nominal, médiane pour l'ordinal, moyenne pour l'intervalle, et toutes, y compris le [[Coefficient de variation]], pour le ratio.

Selon le nombre de variables étudiées, les données sont univariées, bivariées (couples de valeurs) ou multivariées.

## Compléments (hors du cours)

**Un exemple par niveau** :

| Niveau | Exemples | Ce qui a un sens |
|---|---|---|
| Nominal | couleur des yeux, code postal | égalité, effectifs |
| Ordinal | niveau de satisfaction, mention au bac | ordre, mais pas les écarts |
| Intervalle | température en °C, année | écarts ; zéro conventionnel, donc pas de rapports (20 °C n'est pas « deux fois plus chaud » que 10 °C) |
| Ratio | taille, revenu, température en kelvins | écarts et rapports ; zéro absolu |

**Coefficient de variation** : le [[Coefficient de variation|CV]] $= s/\bar{x}$ exige une échelle de ratio. Sur une échelle d'intervalle, il change quand on déplace le zéro : une même série de températures n'a pas le même CV en °C et en °F, puisque l'écart-type est seulement multiplié par 1,8 alors que la moyenne est aussi décalée de 32.

**Origine** : la classification en quatre niveaux vient du psychologue Stanley Smith Stevens (« On the Theory of Scales of Measurement », *Science*, 1946).

**Variable binaire** (dichotomique) : variable qualitative à deux modalités (oui/non) ; on la code en 0/1, comme une [[Variable indicatrice|variable indicatrice]].

**En R** : une variable qualitative se déclare en facteur avec `factor()` ; une variable ordinale en facteur ordonné, `factor(x, levels = c("faible", "moyen", "fort"), ordered = TRUE)`, qui permet les comparaisons `<` et `>` entre modalités.

Voir aussi : [[Mesures de tendance centrale]], [[Facteur (variable catégorielle)]], [[Coefficient de variation]], [[Variable indicatrice]].

Résumés : [[2 - Introduction statistics]], [[1 - Intro to statistics]], [[2 - Descriptive statistics]]
