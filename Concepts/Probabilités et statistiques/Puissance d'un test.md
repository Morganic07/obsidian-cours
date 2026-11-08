---
type: concept
tags: [year3]
aliases: [puissance statistique, statistical power, power of a test]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 5 : Hypothesis Testing .docx|Cours 5 - Hypothesis Testing]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 7 : Z-Test.docx|Cours 7 - Z-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la puissance d'un [[Test d'hypothèse|test d'hypothèse]] est la probabilité de rejeter $H_0$ quand $H_0$ est fausse, c'est-à-dire de détecter un effet qui existe vraiment :

$$\text{puissance} = 1 - \beta = P(\text{rejeter } H_0 \mid H_0 \text{ fausse}),$$

où $\beta$ est le risque d'erreur de type II ([[Erreur de type I et de type II]]). Elle dépend de la valeur réelle du paramètre : plus celle-ci est loin de la valeur posée par $H_0$, plus le test a de chances de rejeter.

**Ce qui la fait varier** :

- elle **augmente** avec la taille d'échantillon $n$ (la statistique fluctue moins) ;
- elle **augmente** avec l'ampleur de l'écart réel à $H_0$ ([[Taille d'effet]]) : un gros effet se repère plus facilement qu'un petit ;
- elle **augmente** avec le [[Seuil de signification|seuil]] $\alpha$ : à $n$ fixé, baisser $\alpha$ baisse la puissance, c'est le compromis entre $\alpha$ et $\beta$ ; seul un $n$ plus grand réduit les deux ensemble ;
- elle **diminue** quand la variabilité $\sigma$ des données augmente.

Exemple pour un [[Test Z]] unilatéral à droite ($H_0 : \mu = \mu_0$, $\sigma$ connu) : si la vraie moyenne vaut $\mu_1 > \mu_0$, la puissance vaut

$$1 - \beta = P\left(Z > z_{1-\alpha} - \frac{\mu_1 - \mu_0}{\sigma/\sqrt n}\right),$$

où $Z$ suit une loi normale centrée réduite : elle croît avec $\mu_1 - \mu_0$, avec $\sqrt n$ et avec $\alpha$, et décroît avec $\sigma$.

**Conséquences pratiques** :

- **Ne pas rejeter $H_0$ ne prouve pas $H_0$** : le test peut simplement manquer de puissance. Exemple de [[8 - Chi²-Test]] : sur 25 villes, le lien entre homicides et ventes d'armes a un coefficient $\varphi \approx 0{,}28$, proche d'un lien moyen, mais le test n'est pas significatif.
- **Calcul d'effectif** : avant une étude, on calcule le $n$ nécessaire pour atteindre une puissance donnée, souvent 80 %, pour un effet jugé important à $\alpha$ fixé.
- À conditions égales, les tests sur [[Échantillons appariés et indépendants|échantillons appariés]] et les [[Test paramétrique et non paramétrique|tests paramétriques]] (quand leurs conditions sont remplies) sont en général plus puissants.

## Dans le cours

Le cours ne la nomme pas. La fiche [[5 - Hypothesis Testing]] présente le compromis entre $\alpha$ et $\beta$ ; la puissance apparaît dans les compléments de [[5 - Hypothesis Testing]], [[7 - Z-Test]] et [[8 - Chi²-Test]].

Voir aussi : [[Erreur de type I et de type II]], [[Test d'hypothèse]], [[Seuil de signification]], [[P-value]], [[Taille d'effet]].

Résumés : [[5 - Hypothesis Testing]], [[7 - Z-Test]], [[8 - Chi²-Test]]
