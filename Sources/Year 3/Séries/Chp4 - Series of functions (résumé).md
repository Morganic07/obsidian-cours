---
type: source
sources: ["[[Chp4 - Series of functions]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 - Series of functions]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Une série de fonctions est la suite de ses sommes partielles : on applique les résultats sur les séries numériques (en fixant $x$) et ceux de [[Chp3 - Sequence of function (résumé)|la convergence uniforme]]. Voir [[Convergence uniforme]].

## Contenu, dans l'ordre du cours

- **Définition** : $S_n(x) = \sum_{k=0}^n f_k(x)$. Convergence simple : celle de $(S_n)$. La somme est $S(x) = \lim S_n(x)$.
- **Reste** $R_n = S - S_n$ : converge simplement vers la fonction nulle.
- **Convergence uniforme** de la série : celle de $(S_n)$. Équivalente à la convergence simple plus convergence uniforme de $(R_n)$ vers 0. Si la série converge uniformément, $(f_n)$ converge uniformément vers 0 ; contraposée pour réfuter l'uniformité.
- **Convergence normale** : chaque $f_n$ est bornée et $\sum \|f_n\|_\infty$ converge. **Critère de Weierstrass** : $\|f_n\|_\infty \le a_n$ avec $\sum a_n$ convergente à termes positifs.
- **Convergence absolue** : $\sum |f_n(x)|$ converge pour tout $x$.
- **Relations** : normale implique uniforme, absolue et simple ; uniforme implique simple ; absolue implique simple (schéma du cours).
- **Échange somme-limite** : si $f_n \to \ell_n$ en $a$ et si la série converge uniformément, alors $\sum \ell_n$ converge et $\lim_{x\to a} S(x) = \sum \ell_n$.
- **Continuité** : somme d'une série uniformément convergente de fonctions continues (en $x_0$ ou sur $X$) continue.
- **Intégrale** sur $[a, b]$ : intégration terme à terme pour des fonctions continues et une convergence uniforme.
- **Dérivée** sur un intervalle borné $I$ : si $\sum f_n(x_0)$ converge et $\sum f_n'$ converge uniformément, la série converge uniformément vers une somme dérivable, de dérivée $\sum f_n'$. Version $\mathcal{C}^1$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition des sommes partielles** : « $\forall s \in X$ » au lieu de $x$ et $\sum f_n$ au lieu de $f_k$ (alerte confirmée, coquilles). La dernière phrase de la définition de la convergence simple écrit $\sum_{n\in\mathbb{N}}$ sans terme.
2. **Schéma des convergences** : il ne dit pas que les implications inverses sont fausses (uniforme n'implique pas absolue, ni l'inverse). Le cours ne les justifie pas ici.
3. **Hypothèse « intervalle borné »** pour la dérivation terme à terme : demandée ici, absente du chapitre 3 pour les suites ; sans conséquence pour la logique du chapitre.
4. **« The the », « does not converges »** : fautes d'anglais répétées, sans enjeu.
