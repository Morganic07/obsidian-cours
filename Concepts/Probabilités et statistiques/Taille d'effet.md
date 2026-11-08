---
type: concept
tags: [year3]
aliases: [effect size, d de Cohen, Cohen's d]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 6 : T-Test.docx|Cours 6 - T-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une taille d'effet mesure l'**ampleur** d'un effet (un écart entre moyennes, un lien entre variables) sur une échelle qui ne dépend pas de la taille de l'échantillon, contrairement à la [[Statistique de test|statistique de test]] et à la [[P-value|p-value]]. Le test répond à « l'effet est-il significatif ? », la taille d'effet à « l'effet est-il important ? ». Avec un très grand échantillon, un effet minuscule devient significatif ; avec un petit, un effet important peut ne pas l'être.

**d de Cohen** (écart de moyennes exprimé en écarts-types) :

- pour une moyenne comparée à une valeur de référence : $d = \dfrac{\bar X - \mu_0}{s}$ ;
- pour deux groupes indépendants : $d = \dfrac{\bar X_1 - \bar X_2}{s_{pooled}}$, avec $s^2_{pooled} = \dfrac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$.

Repères usuels de Cohen : 0,2 petit, 0,5 moyen, 0,8 grand. Le lien avec le test t à un échantillon est direct : $t = d\sqrt n$, d'où une statistique qui grandit avec $n$ à effet égal.

**Pour un tableau croisé** : le coefficient $\varphi = \sqrt{\chi^2/N}$ (tableau $2 \times 2$) ou le [[V de Cramér]] ; repères 0,1 faible, 0,3 moyen, 0,5 fort.

D'autres mesures jouent le même rôle : le coefficient de corrélation $r$ ([[Covariance et corrélation]]), le [[Coefficient de détermination|coefficient de détermination]] $R^2$.

**Exemple** ([[6 - T-Test]]) : honoraires de 16 consultants, $\bar X = 200$ €, $s = 96$ €, contre $\mu_0 = 260$ € : $d = 60/96 \approx 0{,}63$, un effet moyen.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[6 - T-Test]] (d de Cohen sur l'exemple des consultants) et de [[8 - Chi²-Test]] (coefficient $\varphi$ sur 25 villes).

Voir aussi : [[P-value]], [[Puissance d'un test]], [[Test t]], [[Test du χ²]], [[Seuil de signification]].

Résumés : [[6 - T-Test]], [[8 - Chi²-Test]]
