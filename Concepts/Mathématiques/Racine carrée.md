---
type: concept
tags: [year1, year4]
aliases: [racines carrées, sqrt, std::sqrt]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]"]
maj: 2026-11-11
---

$\sqrt{x^2} = |x|$ et non $x$ ; $\sqrt{x + y} \ne \sqrt x + \sqrt y$.

Pour une inéquation : $\sqrt u \le v \iff u \ge 0,\ v \ge 0,\ u \le v^2$. On n'élève au carré que des membres positifs, et l'on vérifie ensuite que les solutions sont conservées.

## En C++

[[5 - Compilation séparée]] calcule la longueur d'un segment par `std::sqrt(dx*dx + dy*dy)`, déclarée dans l'en-tête `<cmath>` de la [[Bibliothèque standard du C++|bibliothèque standard]]. `std::sqrt` d'un nombre négatif renvoie `NaN` (*not a number*) au lieu de s'arrêter. [[Complément hors du cours|ⓘ]]

Voir aussi : [[Valeur absolue]], [[Équation du second degré]], [[Théorème de Pythagore]].

[[4 - Cours complet]] cite une fonction `racineCarree` comme exemple de traitement : elle produit 7 à partir de 49. [[Erreurs du cours#^e-racine-carree|✎]]

Résumés : [[0 - Rappels-etc]], [[5 - Compilation séparée]], [[4 - Cours complet]]
