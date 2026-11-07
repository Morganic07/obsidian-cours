---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 4 : Estimation.docx|Cours 4 - Estimation]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 4 : Estimation.docx|Cours 4 - Estimation]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Estimer un paramètre de population par un point, puis par un intervalle de confiance, et savoir lire cet intervalle.

## Mode, médiane et moyenne

Voir [[Mesures de tendance centrale]].

- **Mode** : la valeur la plus fréquente.
- **Médiane** : la valeur du milieu (50 % de l'aire de chaque côté).
- **Moyenne** : la valeur moyenne (« *average or norm* »).

![[Séance 4 - Estimation - image1.png]]

*Figure : sur une distribution asymétrique à droite, le mode est au sommet, la médiane partage l'aire en deux moitiés, la moyenne est plus à droite.*

## Pourquoi des intervalles plutôt que des points ?

Utiliser une seule valeur (comme la moyenne d'échantillon $\bar{X}$) pour estimer un [[Paramètre et statistique|paramètre de population]] $\mu$ s'appelle une **[[Estimateur|estimation ponctuelle]]**.

## Les estimateurs par intervalle de confiance

La largeur de l'[[Intervalle de confiance]] dépend du **niveau de confiance** souhaité : plus l'intervalle est **large**, plus on a **confiance** qu'il contient le vrai paramètre $\mu$.

| Niveau de confiance | Exemple d'intervalle (revenu) | Note |
|---|---|---|
| 100 % | de 0 € à +∞ € | totalement certain, mais inutile |
| 95 % | de 35 000 € à 41 000 € | standard des statisticiens |
| 0 % | 38 000 € | une estimation ponctuelle |

Formule de l'intervalle de confiance pour $\mu$ (telle qu'écrite dans le cours) :

$$\bar{X} \pm Z_{\alpha} \frac{\sigma}{\sqrt{n}}$$

(Pour un intervalle bilatéral de niveau $1-\alpha$, il faut $Z_{\alpha/2}$ : voir « Erreurs du cours ».)

**Note importante** : si $\sigma$ est inconnu, on utilise l'[[Espérance et variance|écart-type]] de l'échantillon $s$, à condition que l'échantillon soit grand : $n \geq 30$.

## Interprétation et application

### 1. L'interprétation correcte

Un intervalle de confiance à 95 % (exemple : 11,01 à 11,99 ans) signifie que **dans 95 échantillons sur 100**, la moyenne de la population se trouverait dans les intervalles construits avec la même procédure.

**Erreur à éviter** : il est incorrect de dire qu'il y a 95 % de chances que la moyenne « tombe » dans cet intervalle précis, car $\mu$ est une valeur **fixe**, pas une variable aléatoire.

### 2. Comment réduire la largeur d'un intervalle ?

Pour un intervalle plus étroit (plus précis) sans diminuer la confiance :

1. **augmenter la taille de l'échantillon $n$** : on divise par $\sqrt{n}$, donc un $n$ plus grand réduit l'erreur ;
2. **réduire la variabilité**, par des procédures d'[[Échantillonnage|échantillonnage]] plus efficaces comme la **stratification**.

## Percentiles et valeurs Z

Un **[[Quantile|percentile]]** est une valeur de la distribution en dessous de laquelle se trouve un certain pourcentage de la population. Formule :

$$X = \mu + Z \cdot \sigma$$

Voir [[Centrage et réduction]] et [[Loi normale]].

## Points clés à retenir

- Dès qu'on travaille sur un échantillon, la certitude à 100 % est impossible.
- Pour une certitude absolue, il faut un **recensement** (étudier toute la population).
- Le niveau de confiance standard est **95 %**.
- $s^2$ est un **estimateur sans biais** de $\sigma^2$ ([[Variance et écart-type d'échantillon]]).

## Erreurs du cours

- [[Raw/Year 3/Data analysis (Thanos)/Cours 4 : Estimation.docx|Cours 4 - Estimation]] écrit « $\overline{X} \pm Z_{\alpha} \dfrac{\sigma}{\sqrt{n}}$ » (vérifié sur l'image) ; pour un intervalle bilatéral de niveau $1-\alpha$, il faut « $Z_{\alpha/2}$ », comme dans [[7 - Z-Test|Cours 7]] et dans le tableau récapitulatif de [[8 - Chi²-Test|Cours 8]].
