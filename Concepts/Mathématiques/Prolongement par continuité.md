---
type: concept
tags: [year1, year2]
aliases: [prolongeable par continuité, théorème du prolongement]
matieres: [Analyse Maths, Analyse dans Rn]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]", "[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-08
---

$f$ se prolonge par continuité en $a$ si et seulement si elle a une limite finie en $a$ ; le prolongement est alors unique.

Les DS3 et DS4 demandent l'énoncé du théorème et des prolongements ($\sin x \sin(1/x)$, $\ln(1+x)/x$, ...).

**En plusieurs variables (complément, hors du cours)** : le critère est le même. Si $f$ est définie sur $A \setminus \{a\}$, elle se prolonge par continuité en $a$ si et seulement si elle admet en $a$ une limite finie $\ell$ ; on pose alors $f(a) = \ell$.

- $f_2(x, y) = 1 + \dfrac{x^3}{x^2 + y^2}$ : $\left|\dfrac{x^3}{x^2 + y^2}\right| \le \sqrt{x^2 + y^2} \to 0$, donc $f_2$ se prolonge en posant $f_2(0, 0) = 1$.
- $\dfrac{xy}{x^2 + y^2}$ vaut $0$ sur les axes et $1/2$ sur la droite $y = x$ : elle n'a pas de limite en $(0, 0)$ et ne se prolonge par aucune valeur.

Notion parente : [[Limite et continuité]]. Voir aussi : [[Développement limité]], [[Coordonnées polaires]].

Résumés : [[0 - rappels pdf]], [[3 - Limite et continuité d’applications]]
