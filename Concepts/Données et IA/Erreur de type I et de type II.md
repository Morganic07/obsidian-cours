---
type: concept
tags: [year3, year4]
aliases: [type I error, type II error, erreur de type I, erreur de type II, erreur α, erreur β, risque alpha, risque bêta, erreur de première espèce, erreur de seconde espèce, faux positif, faux négatif, faux positifs, faux négatifs]
sources: ["[[Cours 5 - Hypothesis Testing]]", "[[Chp1 - intro to data mining]]"]
maj: 2026-11-06
---

Les deux erreurs possibles d'un [[Test d'hypothèse|test d'hypothèse]] :

- **erreur α (type I)** : rejeter $H_0$ alors qu'elle est vraie ;
- **erreur β (type II)** : ne pas rejeter $H_0$ alors qu'elle est fausse.

Il y a un compromis : diminuer α fait augmenter β, et inversement, de même qu'on ne peut avoir un [[Intervalle de confiance|intervalle]] à la fois étroit et très confiant ([[Cours 5 - Hypothesis Testing]]).

**En data mining**, dans l'exemple du filtre anti-spam de la note de cours : les 2 faux positifs (FP) sont des « fausses alertes », erreur de type I (e-mails importants classés en spam, l'erreur pénalisante) ; les 5 faux négatifs (FN) sont des « manqués », erreur de type II (spams arrivés dans la boîte principale). Voir [[Validation d'un classifieur]].

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Seuil de signification]], [[Intervalle de confiance]], [[Validation d'un classifieur]].

## À vérifier

- La correspondance FP = type I suppose que « positif » signifie rejeter $H_0$ ; un autre choix de $H_0$ échange les types. Cette remarque est un complément du résumé, pas du cours.
- « Erreur de première espèce » et « de seconde espèce » sont des variantes françaises usuelles, absentes du cours.

Résumés : [[Séance 5 - Hypothesis Testing (résumé)]], [[Chp1 - intro to data mining (résumé)]]
