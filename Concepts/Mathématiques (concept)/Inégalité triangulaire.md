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
  - "[[5 - Complexes (résumé)|Chapitre 5 - Complexes]]"
  - "[[1 - Integration (résumé)|Chap7-Integration]]"
  - "[[2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]]"
maj: 2026-11-06
---

Pour des réels : $|x + y| \le |x| + |y|$. Par le [[Principe des substitutions]], on en tire la forme généralisée $\big||x| - |y|\big| \le |x + y| \le |x| + |y|$. Piège signalé par le cours : $|x - y| \le |x| + |y|$, et non $|x| - |y|$.

**Outil Maths** : pour les complexes, $|z + z'| \leq |z| + |z'|$. Le TD Relations s'en sert pour la transitivité de l'ordre $|x - x'| \leq y' - y$ sur $\mathbb{R}^2$.

**Analyse (Year 2)** : pour l'intégrale, $\left|\int_{[a,b]} f\right| \le \int_{[a,b]} |f|$.

**Analyse dans Rn** : pour une norme, $\|x+y\| \le \|x\|+\|y\|$ ; pour une distance, $d(X,Z) \le d(X,Y)+d(Y,Z)$.

Notion parente : [[Valeur absolue]]. Voir aussi : [[Norme]], [[Nombre complexe]], [[Intégrale]], [[Distance]].

## À vérifier

- Chap0 est scanné : l'énoncé est relevé d'après le résumé.
- Le texte extrait du TD Relations ne contient pas l'expression « inégalité triangulaire » (accents ou mise en page) : l'usage vient du résumé.
- Cas d'égalité (Chp 2) : le cours écrit $x=\lambda y$ avec $\lambda\in\mathbb{R}$, il faut $\lambda \ge 0$ (résumé Chp 2, point 1).

Résumés : [[0 - Rappels-etc (résumé)]], [[5 - Complexes (résumé)]], [[1 - Integration (résumé)]], [[2 - éléments de topologie dans Rn (résumé)]]
