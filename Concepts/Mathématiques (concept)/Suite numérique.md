---
type: concept
tags: [year1, year3]
aliases: [suite numérique, suites numériques, suite récurrente, suites récurrentes, suite bornée, suite majorée, suite minorée, suite monotone]
matieres: [Analyse Maths, Séries]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]", "[[0 - Revision chapter (résumé)|Chp0 - Revision chapter]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

Une **suite** est une application $u : \mathbb{N} \to \mathbb{R}$ (ou $\mathbb{C}$). Résumés : [[0 - rappels pdf (résumé)]] (cours, chapitre 2) et [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]].

## Définitions

- Majorée, minorée, bornée ($\exists M, \forall n, |u_n| \le M$) ; croissante, décroissante, monotone.
- **Limite finie $\ell$** : $\forall\varepsilon > 0,\ \exists N,\ \forall n \ge N,\ |u_n - \ell| \le \varepsilon$. Limite $+\infty$ : $\forall A,\ \exists N,\ \forall n \ge N,\ u_n \ge A$. Une suite est convergente si sa limite est finie : voir [[Convergence d'une suite]].
- La limite est unique. Toute suite convergente est bornée ; la réciproque est fausse ($(-1)^n$).

## Résultats d'existence de limite

- **Opérations** sur les limites, avec les formes indéterminées $\infty - \infty$, $0 \times \infty$, $\infty/\infty$, $0/0$.
- **Passage à la limite** dans les inégalités larges (les strictes deviennent larges).
- **[[Théorème des gendarmes|Gendarmes]]** (encadrement) : $u_n \le v_n \le w_n$ avec $u_n$ et $w_n$ de même limite $\ell$ donne $v_n \to \ell$.
- **[[Théorème de la limite monotone|Limite monotone]]** : une suite croissante majorée converge vers $\sup\{u_n\}$ (voir [[Borne supérieure]]) ; croissante non majorée, elle tend vers $+\infty$.
- **[[Suites adjacentes]]** : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$. Elles convergent vers la même limite $\ell$, avec $u_n \le \ell \le v_n$. Utile pour une suite alternée, en prenant les suites des indices pairs et impairs.
- **[[Suite extraite|Suites extraites]]** $(u_{\varphi(n)})$ : si $u_n \to \ell$, toute suite extraite tend vers $\ell$. Si $u_{2n}$ et $u_{2n+1}$ tendent vers $\ell$, alors $u_n \to \ell$. Deux suites extraites de limites différentes prouvent qu'il n'y a pas de limite.

## Suites récurrentes $u_{n+1} = f(u_n)$

1. Trouver un [[Intervalle stable|intervalle $I$ stable]] par $f$ (sinon la suite peut n'être pas définie).
2. $f$ croissante : $(u_n)$ est monotone, croissante si $f(u_0) \ge u_0$.
3. $f$ décroissante : $(u_{2n})$ et $(u_{2n+1})$ sont monotones de sens contraires.
4. Si $f$ est continue et $u_n \to \ell$, alors $f(\ell) = \ell$ : on cherche les [[Point fixe|points fixes]].

## Suites complexes

La convergence se lit sur la partie réelle et la partie imaginaire, ou sur le module. Les notions d'ordre (monotonie, gendarmes, suites adjacentes, limites infinies) n'ont plus de sens. Voir [[Suite complexe]] et [[Nombre complexe]].

## En Séries (3e année)

Le chapitre de révision ([[0 - Revision chapter (résumé)]]) reprend ces bases : une suite est une fonction de $\mathbb{N}$ dans $\mathbb{R}$, définie par formule ou par récurrence, convergente vers $\ell$ si $\forall \epsilon > 0, \exists N, \forall n \ge N, |a_n - \ell| < \epsilon$ (inégalité stricte, là où le cours de 1re année écrit $\le$). Il cite la [[Suite géométrique]] $a, ar, ar^2, \dots$ ; toute suite convergente est bornée, une suite monotone bornée converge, et deux suites adjacentes ont la même limite.

Le DS2 d'Analyse I ([[Raw/Year 1/Contrôles.pdf|Contrôles]]) demande les définitions de suite décroissante, bornée, de limite $-\infty$ avec quantificateurs, et de suites adjacentes, puis des calculs de limites.

## Liens

Voir aussi : [[Convergence d'une suite]], [[Théorème des gendarmes]], [[Théorème de la limite monotone]], [[Suites adjacentes]], [[Suite extraite]], [[Point fixe]], [[Suite complexe]], [[Suite géométrique]], [[Limite et continuité]] (même démarche pour les fonctions), [[Comparaison asymptotique]] (suites équivalentes), [[Série numérique]] (suite des sommes partielles), [[Critère de d'Alembert et de Cauchy]], [[Récurrence]].

## À vérifier

- Le chapitre 2 du polycopié scanné [[0 - rappels pdf (résumé)|AnalyseID1]] : seul le plan est extractible, le reste vient du résumé (lu en image).
- [[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]], exercice 27 : « périodique donc divergente » est mal justifié (une suite périodique peut converger).

Résumés : [[0 - rappels pdf (résumé)]], [[0 - Revision chapter (résumé)]]
