---
type: concept
aliases: [suite numérique, suites numériques, suite adjacente, suites adjacentes, suite extraite, suites extraites, sous-suite, théorème de la limite monotone, suite récurrente, suites récurrentes, suite convergente, suites convergentes]
matieres: [Analyse Maths]
sources: ["[[raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1]]", "[[raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]"]
maj: 2026-11-06
---

Une **suite** est une application $u : \mathbb{N} \to \mathbb{R}$ (ou $\mathbb{C}$). Résumés : [[AnalyseID1 (résumé)]] (cours, chapitre 2) et [[TDSuites (résumé)]].

## Définitions

- Majorée, minorée, bornée ($\exists M, \forall n, |u_n| \le M$) ; croissante, décroissante, monotone.
- **Limite finie $\ell$** : $\forall\varepsilon > 0,\ \exists N,\ \forall n \ge N,\ |u_n - \ell| \le \varepsilon$. Limite $+\infty$ : $\forall A,\ \exists N,\ \forall n \ge N,\ u_n \ge A$. Une suite est convergente si sa limite est finie.
- La limite est unique. Toute suite convergente est bornée ; la réciproque est fausse ($(-1)^n$).

## Résultats d'existence de limite

- **Opérations** sur les limites, avec les formes indéterminées $\infty - \infty$, $0 \times \infty$, $\infty/\infty$, $0/0$.
- **Passage à la limite** dans les inégalités larges (les strictes deviennent larges).
- **Gendarmes** : $u_n \le v_n \le w_n$ avec $u_n$ et $w_n$ de même limite $\ell$ donne $v_n \to \ell$.
- **Limite monotone** : une suite croissante majorée converge vers $\sup\{u_n\}$ (voir [[Borne supérieure]]) ; croissante non majorée, elle tend vers $+\infty$.
- **Suites adjacentes** : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$. Elles convergent vers la même limite $\ell$, avec $u_n \le \ell \le v_n$. Utile pour une suite alternée, en prenant les suites des indices pairs et impairs.
- **Suites extraites** : si $u_n \to \ell$, toute suite extraite tend vers $\ell$. Si $u_{2n}$ et $u_{2n+1}$ tendent vers $\ell$, alors $u_n \to \ell$. Deux suites extraites de limites différentes prouvent qu'il n'y a pas de limite.

## Suites récurrentes $u_{n+1} = f(u_n)$

1. Trouver un intervalle $I$ stable par $f$ (sinon la suite peut n'être pas définie).
2. $f$ croissante : $(u_n)$ est monotone, croissante si $f(u_0) \ge u_0$.
3. $f$ décroissante : $(u_{2n})$ et $(u_{2n+1})$ sont monotones de sens contraires.
4. Si $f$ est continue et $u_n \to \ell$, alors $f(\ell) = \ell$ : on cherche les points fixes.

## Suites complexes

La convergence se lit sur la partie réelle et la partie imaginaire, ou sur le module. Les notions d'ordre (monotonie, gendarmes, suites adjacentes, limites infinies) n'ont plus de sens. Voir [[Nombre complexe]].

## Liens

[[Limite et continuité]] (même démarche pour les fonctions), [[Comparaison asymptotique]] (suites équivalentes), [[Série numérique]] (suite des sommes partielles), [[Critère de d'Alembert et de Cauchy]], [[Récurrence]].
