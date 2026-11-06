---
type: source
sources: ["[[raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1]] (95 pages), dans [[Year 1 - Analyse Maths]]. C'est le polycopié complet du cours d'Analyse I (PréING1, 2020-2021) : cinq chapitres de cours, chacun suivi de sa feuille de TD. Il regroupe donc des documents résumés ailleurs :

| Chapitre | Pages | Résumé détaillé |
|---|---|---|
| 0. Rappels, sigma et pi, trigonométrie | 1 à 14 | [[Chap0-Rappels-etc (résumé)]], [[TD0-Rappel (résumé)]] |
| 1. L'ensemble $\mathbb{R}$ | 15 à 24 | [[Chap1-reels (résumé)]], [[TD1-numbres-reels (résumé)]] |
| 2. Suites numériques | 25 à 43 | ci-dessous |
| 3. Limites et continuité | 44 à 60 | ci-dessous |
| 4. Dérivabilité | 61 à 72 | [[Chp4 - dérivabilité (résumé)]] |
| 5. Analyse asymptotique | 73 à 95 | [[Sources/Year 1/Analyse Maths/chp5 (résumé)\|chp5 (résumé)]], [[TD5-AnalAsympt (résumé)]] |

Les chapitres 0 à 3 ont été lus en image. Pour les chapitres 4 et 5, seuls les titres de sections et les énoncés des TD ont été relus : le contenu est déjà couvert par les notes de `Cours/` correspondantes.

## Chapitre 0 : rappels (pages 1 à 14)

Les premières pages sont les rappels sur les inégalités et sur $\sum$ et $\prod$ (voir [[Chap0-Rappels-etc (résumé)]]). Le polycopié y ajoute un rappel de trigonométrie : cercle trigonométrique, $\cos^2 + \sin^2 = 1$, parité et périodicité, équations $\sin x = \sin y \iff x \equiv y\ [2\pi]$ ou $x \equiv \pi - y\ [2\pi]$ et $\cos x = \cos y \iff x \equiv \pm y\ [2\pi]$, formules d'addition, de duplication et de produit, définition de $\tan$ ($\pi$-périodique, impaire, $\tan x = \tan y \iff x \equiv y\ [\pi]$), valeurs remarquables. Exemple traité : $\sin x = \cos x \iff x \equiv \pi/4\ [\pi]$.

## Chapitre 2 : suites numériques (pages 25 à 43)

- **Définitions** : suite $u : \mathbb{N} \to \mathbb{R}$ ; majorée, minorée, bornée ($\exists M, \forall n, |u_n| \le M$) ; croissante, décroissante, monotone, strictement monotone. Exemples : $\sqrt n$, $(-1)^n$, Fibonacci, $1/n^2$.
- **Limite** : finie $\ell$ ($\forall\varepsilon > 0,\ \exists N,\ \forall n \ge N,\ |u_n - \ell| \le \varepsilon$), égale à $\pm\infty$ avec $A$. Formulation unique par les voisinages. Convergente si la limite est finie, divergente sinon. **Unicité de la limite** (preuve par l'absurde avec $\varepsilon < |\ell - \ell'|/2$). **Toute suite convergente est bornée** ; la réciproque est fausse ($(-1)^n$), et une suite non bornée n'a pas forcément de limite infinie ($(-1)^n n$).
- **Opérations** : somme, produit (tableaux avec les formes indéterminées $\infty - \infty$, $0 \times \infty$), inverse et quotient, composition par une fonction. **Passage à la limite dans les inégalités larges** : les inégalités strictes deviennent larges ($1/(n+1) > 0$ mais la limite est $0$).
- **Théorèmes d'existence** : encadrement (gendarmes), minoration et majoration pour $+\infty$ et $-\infty$ ; **limite monotone** (croissante majorée converge vers $\sup$, croissante non majorée tend vers $+\infty$) ; **suites adjacentes** ($u_n$ croissante, $v_n$ décroissante, $v_n - u_n \to 0$) convergent vers la même limite, avec $u_n \le \ell \le v_n$. Exemples : $\sum 1/k^2$ converge, $\sum 1/k!$ et $u_n + 1/(n\,n!)$ adjacentes. Les preuves reposent sur [[Borne supérieure]].
- **Suites extraites** : $(u_{\varphi(n)})$ avec $\varphi$ strictement croissante, $\varphi(n) \ge n$. Si $u_n \to \ell$, toute suite extraite tend vers $\ell$ ; si $u_{2n}$ et $u_{2n+1}$ tendent vers $\ell$, alors $u_n \to \ell$. Usage pratique : deux suites extraites de limites différentes prouvent qu'une suite n'a pas de limite.
- **Suites récurrentes $u_{n+1} = f(u_n)$** : existence si l'intervalle $I$ est stable par $f$ ; si $f$ est croissante, $(u_n)$ est monotone (sens donné par le signe de $f(u_0) - u_0$) ; si $f$ est décroissante, $(u_{2n})$ et $(u_{2n+1})$ sont monotones de sens contraires ; si $f$ est continue et $u_n \to \ell$, alors $f(\ell) = \ell$ (point fixe). Exercice type : $u_{n+1} = \sqrt{1 + u_n}$.
- **Suites complexes** : bornée, convergente avec le module ; $u_n \to \ell \iff \mathrm{Re}\,u_n \to \mathrm{Re}\,\ell$ et $\mathrm{Im}\,u_n \to \mathrm{Im}\,\ell$. Restent valables : unicité, caractère borné, opérations, suites extraites. Ne le sont plus : monotonie, limites infinies, passage à la limite dans $\le$, gendarmes, limite monotone, suites adjacentes.
- **TD de suites** (pages 38 à 43) : limites par la définition, suites extraites, suites adjacentes, suites récurrentes. Voir [[TDSuites (résumé)]].

## Chapitre 3 : limites et continuité de fonctions (pages 44 à 60)

- **Limite d'une fonction** en $a$, en $\pm\infty$, finie ou infinie, avec quantificateurs et par les voisinages ; $f \to \ell \iff |f - \ell| \to 0$. Unicité. Limites à gauche et à droite ; une fonction bornée au voisinage d'un point où elle a une limite finie. **Caractérisation séquentielle** : $f(x) \to \ell$ en $a$ si et seulement si $f(u_n) \to \ell$ pour toute suite $u_n \to a$ ; pour réfuter une limite, exhiber deux suites $x_n$, $y_n$ de même limite $a$ avec des images de limites différentes.
- **Opérations** (somme, produit, quotient, composition) démontrées par la caractérisation séquentielle ; mêmes formes indéterminées. Passage à la limite dans les inégalités larges.
- **Théorèmes d'existence** : encadrement, majoration et minoration, **limite monotone** pour une fonction monotone sur $]a, b[$ ; une fonction monotone a des limites à gauche et à droite en tout point intérieur, avec $f(a^-) \le f(a) \le f(a^+)$ si elle est croissante.
- **Continuité** : en un point ($f$ a une limite finie en $a$, égale à $f(a)$), à gauche, à droite, sur un intervalle ($\mathcal{C}^0(I, \mathbb{R})$) ; la partie entière est continue à droite mais pas à gauche aux entiers. **Prolongement par continuité** en $a$ si et seulement si $f$ a une limite finie en $a$, et il est unique. Caractérisation séquentielle de la continuité. Stabilité par somme, produit, quotient (dénominateur non nul), composée.
- **Grands théorèmes** :
  - **TVI** : $f$ continue, $f(a)f(b) \le 0$, alors $f$ s'annule entre $a$ et $b$ ; preuve par dichotomie, avec deux suites adjacentes (approximation de $c$ à $(b-a)/2^n$ près). Conséquence : l'image d'un intervalle par une fonction continue est un intervalle.
  - Une fonction continue sur un **segment** est bornée et atteint ses bornes ; l'image d'un segment est un segment.
  - Une fonction continue est **injective si et seulement si strictement monotone**.
  - Une fonction continue strictement monotone sur $I$ réalise une **bijection** de $I$ sur $f(I)$, de réciproque continue strictement monotone de même sens.
- **TD3** (pages 57 à 60) : quantificateurs sur les fonctions ; limites par la définition ; périodique avec limite finie en $+\infty$ implique constante ; calculs de limites ; continuité et prolongement ; $\mathbf{1}_{\mathbb{Q}}$ discontinue partout ; équations fonctionnelles $f(x) = f(3x)$ ; TVI.

## Chapitre 4 : dérivabilité (pages 61 à 72)

Plan relevé : nombre dérivé et opérations, dérivées usuelles, dérivées successives, classe $\mathcal{C}^n$ et formule de Leibniz, extremum local, Rolle, sens de variation, inégalité des accroissements finis, règle de l'Hôpital. TD4 : dérivabilité de $x|x|$, prolongements, dérivées, raccord $\mathcal{C}^2$, bijection $x\ln x - x$, parité et périodicité des dérivées, dérivées $n$-ièmes, Rolle pour compter les racines, suites $x_{n+1} = f(x_n)$ et point fixe attractif ou répulsif, injectivité locale. Voir [[Chp4 - dérivabilité (résumé)]].

## Chapitre 5 : analyse asymptotique (pages 73 à 95)

Plan relevé : domination, négligeabilité, équivalence pour les suites puis pour les fonctions, développements limités (généralités, Taylor-Young, opérations, applications). TD5 identique à [[TD5-AnalAsympt (résumé)]]. Voir [[Sources/Year 1/Analyse Maths/chp5 (résumé)|chp5 (résumé)]].

## Points à vérifier

- **TVI (théorème 21)** : l'hypothèse est $f(a)f(b) \le 0$, mais la preuve par dichotomie maintient l'invariant $f(a_n)f(b_n) < 0$ avant de conclure avec une inégalité large. Il faut traiter à part le cas $f(a)f(b) = 0$ (trivial) ou écrire $\le 0$ dans l'invariant. Coquille sans conséquence sur le résultat.

## Liens

[[Suite numérique]], [[Limite et continuité]], [[Dérivabilité]], [[Développement limité]], [[Comparaison asymptotique]], [[Borne supérieure]], [[Nombre complexe]].
