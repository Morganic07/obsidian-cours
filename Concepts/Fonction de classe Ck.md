---
type: concept
aliases: [classe Ck, classe C1, classe C2, classe Cn, classe C∞, classe C0, classe C infini, C∞, stabilité de Ck par composition]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]", "[[Chp 5 - Calcul différentiel d'ordre supérieur]]", "[[Chp4 - dérivabilité]]"]
maj: 2026-11-06
---

$f$ est de classe $\mathcal{C}^k$ sur l'ouvert $U$ si ses dérivées partielles d'ordre $k$ existent et sont continues sur $U$, et $\mathcal{C}^\infty$ si elle est $\mathcal{C}^k$ pour tout $k$.

Chaîne d'implications : $\mathcal{C}^1$ ⇒ différentiable ⇒ continue et dérivées partielles définies.

- $f$ est $\mathcal{C}^k$ si et seulement si ses composantes le sont.
- Les dérivées d'ordre inférieur à $k$ sont aussi continues.
- La composée de deux applications $\mathcal{C}^k$ est $\mathcal{C}^k$, si $f(U) \subset V$ (voir [[Dérivation en chaîne]]). À l'ordre 2, être $\mathcal{C}^2$ suffit pour le [[Théorème de Schwarz]].
- $\mathcal{C}^1(U, F)$ est un sous-espace vectoriel de $\mathcal{C}(U, F)$. Toute application linéaire est $\mathcal{C}^1$.

**En une variable** : $f$ est $\mathcal{C}^n$ si elle est $n$ fois dérivable et si $f^{(n)}$ est continue. $\mathcal{C}^1$ signifie « dérivable à dérivée continue », et non « dérivable et continue ». $f$ est $\mathcal{C}^\infty$ si elle est infiniment dérivable. Chaîne : $\mathcal{C}^\infty \Rightarrow \dots \Rightarrow \mathcal{C}^1 \Rightarrow$ dérivable $\Rightarrow \mathcal{C}^0$. Produit, quotient (si le dénominateur ne s'annule pas), composée et réciproque (si $f'$ ne s'annule pas) restent $\mathcal{C}^n$. [[Formule de Leibniz]] : $(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)}g^{(n-k)}$.

Notion parente : [[Différentielle]] (plusieurs variables), [[Dérivabilité]] (une variable). Voir aussi : [[Dérivée partielle]], [[Dérivation en chaîne]], [[Théorème de Schwarz]], [[Formule de Leibniz]], [[Limite et continuité]], [[Difféomorphisme]], [[Dérivabilité]], [[Développement limité]]

## À vérifier

- Chp 4 (Analyse dans Rn), théorème 5 : $f \times g$ dans un EVN quelconque, énoncé sans sens.
- Chp 5, théorème 2 : une hypothèse le rend vide.

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]], [[Chp 5 - Calcul différentiel d'ordre supérieur (résumé)]], [[Chp4 - dérivabilité (résumé)]], [[TD5-AnalAsympt (résumé)]], [[TD5-AnalyseAsymptotiqueCorrection (1) (résumé)]]
