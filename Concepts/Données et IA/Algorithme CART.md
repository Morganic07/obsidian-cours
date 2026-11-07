---
type: concept
tags: [year4]
aliases: [CART, Classification and Regression Tree]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
---

*Classification and Regression Tree* (Breiman, Friedman, Olshen, Stone, 1984) : algorithme d'[[Arbre de décision]] binaire (deux fils par nœud), qui accepte tous types de variables et choisit les séparations par l'[[Indice de Gini]].

**Construction** : tant que les conditions d'arrêt ne sont pas remplies (profondeur, nombre de feuilles, effectif d'un fils, performance suffisante ou plus d'amélioration), on cherche la meilleure séparation et on découpe. L'[[Élagage]] est facultatif.

Chaque feuille reçoit la classe majoritaire ; l'erreur globale est la somme pondérée des erreurs des feuilles.

Notion parente : [[Arbre de décision]]. Voir aussi : [[Indice de Gini]], [[Élagage]].

## À vérifier

- Le cours écrit « maximising Gini index » dans la construction, alors qu'on maximise le gain de pureté (un Gini petit correspond à un nœud pur).
- Exemple windy, fils vrai P(3) N(3) : la classe affectée est notée « P ?? » dans le cours, l'égalité n'est pas tranchée.

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
