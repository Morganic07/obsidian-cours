---
type: source
sources: ["[[Chp3 - Sequence of function]]"]
maj: 2026-11-05
---

Résumé de [[Chp3 - Sequence of function]], dans [[Year 3 - Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes.

## Idée générale

Deux modes de convergence pour une suite de fonctions, et la raison d'être du second : permettre d'échanger limite et continuité, limite et intégrale, limite et dérivée. Voir [[Convergence uniforme]].

## Contenu, dans l'ordre du cours

- **Convergence simple** sur $X$ : pour chaque $x$, $(f_n(x))$ converge. Le rang $N$ dépend de $x$ et de $\epsilon$. Combinaison linéaire conservée.
- **Questions** : la limite d'une suite de fonctions continues est-elle continue ? $\lim f_n' = f'$ ? $\lim \int f_n = \int f$ ? Réponse du cours : la convergence simple ne suffit pas (pas de continuité de la limite). D'où la convergence uniforme.
- **Convergence uniforme** : $\forall \epsilon, \exists N, n \ge N \Rightarrow \forall x, |f_n(x) - f(x)| < \epsilon$. $N$ ne dépend que de $\epsilon$. Elle implique la convergence simple, pas l'inverse. Image du « tube » $[f - \epsilon, f + \epsilon]$.
- **Norme uniforme** $\|f\|_\infty = \sup_X |f|$. Équivalence : convergence uniforme si et seulement si $\|f_n - f\|_\infty \to 0$. Condition suffisante : $|f_n - f| \le a_n$ avec $a_n \to 0$. Limite uniforme de fonctions bornées : bornée.
- **Point limite** $a$ de $X$, et échange de limites : si chaque $f_n$ a une limite $\ell_n$ en $a$ et si la convergence est uniforme, alors $(\ell_n)$ converge vers $\lim_{x \to a} f(x)$.
- **Continuité** : limite uniforme de fonctions continues en $x_0$ (ou sur $X$) continue.
- **Intégrale** sur $[a, b]$ : fonctions continues convergeant uniformément, alors $\lim \int f_n = \int f$. Contre-exemple de non-uniformité : $f_n$ triangulaire de pente $n^2$, de hauteur $n$ en $1/n$, nulle après $2/n$. Chaque intégrale vaut 1, la limite 0. La condition n'est que suffisante.
- **Dérivée** : si $f_n$ dérivables, $(f_n(x_0))$ converge et $(f_n')$ converge uniformément vers $g$, alors $(f_n)$ converge uniformément vers $f$ dérivable avec $f' = g$. Version $\mathcal{C}^1$ analogue.
- **Méthode** : trouver la limite simple (graphique des premières fonctions) ; pour l'uniformité, étudier $\|f_n - f\|_\infty$ (souvent via la dérivée). Pour réfuter l'uniformité : $f_n$ bornées et limite non bornée ; $f_n$ continues et limite discontinue ; intégrales qui ne passent pas à la limite.
- **Erreurs courantes** : limite bornée, limite continue, ou échange limite-intégrale vérifié n'impliquent pas la convergence uniforme. De même, limite dérivable ou $(\lim f_n)' = \lim f_n'$ n'impliquent pas celle des dérivées.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Point limite** : la définition « $\forall \epsilon, \exists x \in\, ]a - \epsilon, a + \epsilon[\, \cap X$ » n'exclut pas $x = a$ (alerte de la transcription). La définition usuelle demande $x \ne a$, sans quoi tout point de $X$ serait point limite (complément).
2. **Ensemble d'arrivée du contre-exemple** : $f_n : [0,1] \to [0,1]$, alors que $f_n(1/n) = n$ dépasse 1 pour $n \ge 2$. L'ensemble d'arrivée devrait être $\mathbb{R}$ (complément, sans conséquence sur le raisonnement).
3. **« Necessary and convergent condition »** : lire « necessary and sufficient », par cohérence avec la proposition sur la norme uniforme (alerte confirmée).
4. **« Defined on $f$ »** pour la norme uniforme : lire $X$. **« From $X \subset \mathbb{R}$ to $X$ »** dans la condition suffisante : lire $\mathbb{R}$. Coquilles signalées par la transcription.
5. **Note sur l'intégrale** : le théorème conclut aussi que $f$ est continue, ce qui découle du résultat de continuité plus haut.
