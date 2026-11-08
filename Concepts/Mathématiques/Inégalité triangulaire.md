---
type: concept
tags:
  - year1
  - year2
aliases:
  - inégalité triangulaire généralisée
  - triangle inequality
matieres:
  - Analyse Maths
  - Outil Maths
  - Analyse
  - Analyse dans Rn
sources:
  - "[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel.pdf]]"
  - "[[5 - Complexes|Chapitre 5 - Complexes]]"
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]"
maj: 2026-11-08
---

Pour des réels : $|x + y| \le |x| + |y|$. Par le [[Principe des substitutions]], on en tire la forme généralisée $\big||x| - |y|\big| \le |x + y| \le |x| + |y|$. Piège signalé par le cours : $|x - y| \le |x| + |y|$, et non $|x| - |y|$.

**Preuve et cas d'égalité pour les réels (complément, hors du cours)** : les deux membres étant positifs, il suffit de comparer leurs carrés. Comme $xy \le |xy|$,
$$|x+y|^2 = x^2 + 2xy + y^2 \le x^2 + 2|xy| + y^2 = (|x|+|y|)^2,$$
d'où $|x+y| \le |x|+|y|$. L'égalité a lieu si et seulement si $xy = |xy|$, c'est-à-dire $xy \ge 0$ : $|x+y| = |x|+|y| \iff x$ et $y$ sont de même signe (l'un des deux pouvant être nul). Exemple : $|3 + (-2)| = 1 < 5$.

**Outil Maths** : pour les complexes, $|z + z'| \leq |z| + |z'|$. Le TD Relations s'en sert pour la transitivité de l'ordre $|x - x'| \leq y' - y$ sur $\mathbb{R}^2$.

**Analyse (Year 2)** : pour l'intégrale, $\left|\int_{[a,b]} f\right| \le \int_{[a,b]} |f|$.

**Analyse dans Rn** : pour une norme, $\|x+y\| \le \|x\|+\|y\|$, et la « 2nd inégalité triangulaire » $\|x-y\| \ge \big|\|x\|-\|y\|\big|$ ; pour une distance, $d(X,Z) \le d(X,Y)+d(Y,Z)$. Cas d'égalité pour la norme euclidienne : $\|x+y\| = \|x\| + \|y\|$ si et seulement si $x$ et $y$ sont positivement colinéaires ($y = 0$, ou $x = \lambda y$ avec $\lambda \ge 0$). [[Erreurs du cours#^e-inegalite-triangulaire|✎]]

Notion parente : [[Valeur absolue]]. Voir aussi : [[Norme]], [[Nombre complexe]], [[Intégrale]], [[Distance]].

Résumés : [[0 - Rappels-etc]], [[5 - Complexes]], [[1 - Integration]], [[2 - éléments de topologie dans Rn]]
