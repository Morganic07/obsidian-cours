---
type: concept
tags:
  - year3
aliases:
  - dummy variable
  - dummy variables
  - variables indicatrices
  - variable dummy
  - indicator variable
sources:
  - "[[1 - Data analysis|Cours 1 (Data analysis)]]"
  - "[[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : variable qui vaut 1 si l'individu appartient à une modalité donnée d'une variable catégorielle, 0 sinon. Elle permet de faire entrer une variable catégorielle dans un modèle de [[Régression linéaire|régression]].

- **$k-1$ indicatrices, pas $k$** : pour un facteur à $k$ modalités, on crée $k-1$ indicatrices quand le modèle a une constante. La somme des $k$ indicatrices vaut toujours 1 : elle serait colinéaire avec la colonne de la constante, et le modèle ne pourrait pas être estimé (piège des variables indicatrices, *dummy variable trap*).
- **Modalité de référence** : celle qui n'a pas d'indicatrice. Chaque coefficient mesure l'écart moyen de la réponse entre sa modalité et la référence, les autres variables étant fixées.
- **Exemple** : facteur région à 3 modalités A, B, C, référence A. On crée deux indicatrices $I_B$ et $I_C$ ; le modèle $y = \beta_0 + \beta_B I_B + \beta_C I_C + \varepsilon$ donne $\beta_0$ pour la moyenne de A, $\beta_0 + \beta_B$ pour B, $\beta_0 + \beta_C$ pour C.
- **En R** : `factor(x)` ou `as.factor(x)` déclare le facteur, `levels(f)` liste ses modalités (la première sert de référence), `relevel(f, ref = "B")` change la référence ; `lm()` crée les indicatrices automatiquement.

## Dans le cours

Nommé dans [[1 - Data analysis|Cours 1 (Data analysis)]] sans définition : ce sont les variables que [[Langage R|R]] crée automatiquement pour coder un facteur déclaré.

Notion parente : [[Facteur (variable catégorielle)]]. Voir aussi : [[Langage R]].

Résumés : [[1 - Data analysis|Cours 1 (Data analysis)]]
