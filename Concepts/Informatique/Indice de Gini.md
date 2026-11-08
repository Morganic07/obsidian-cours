---
type: concept
tags: [year4]
aliases: [Gini index, critère de Gini]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

Critère d'impureté d'un nœud utilisé par CART :

$$IG(N_o) = 1 - \sum_{i=1}^{N_C} p_i^2$$

où $p_i$ est la fréquence de la classe $i$ dans le nœud. Plus il est petit, plus le nœud est pur. On cherche la variable qui maximise

$$IG(\text{avant}) - [W_1\, IG(\text{fils}_1) + W_2\, IG(\text{fils}_2)]$$

Pour deux classes, la courbe est une parabole de maximum 0,5.

## Compléments (complément, hors du cours)

- **Interprétation** : $1 - \sum_i p_i^2 = \sum_i p_i(1 - p_i)$ est la probabilité que deux exemples tirés avec remise dans le nœud soient de classes différentes ; c'est aussi la probabilité de se tromper en étiquetant un exemple du nœud au hasard selon les fréquences des classes.
- **Bornes** : 0 pour un nœud pur, au plus $1 - 1/N_C$ quand les classes sont équiréparties (0,5 à deux classes).
- **Exemple windy** (9 oui, 5 non) : $IG = 1 - \frac{81 + 25}{196} = \frac{90}{196} \approx 0{,}459$. Fils *false* (6 oui, 2 non) : $0{,}375$ ; fils *true* (3 oui, 3 non) : $0{,}5$. Moyenne pondérée $\frac{8}{14}\cdot 0{,}375 + \frac{6}{14}\cdot 0{,}5 = \frac{84}{196}$, donc gain $= \frac{6}{196} \approx 0{,}031$.
- **CART** est binaire : pour une variable qualitative, il essaie les regroupements de ses valeurs en deux paquets ; pour une variable continue, les seuils $x \le s$. En régression, l'impureté est la variance de la cible et la feuille prédit la moyenne.
- Gini et [[Entropie (théorie de l'information)|entropie]] classent presque toujours les coupes dans le même ordre ; Gini se calcule plus vite (pas de logarithme).

Notion parente : [[Algorithme CART]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
