---
type: concept
aliases: [classe Ck, classe C1, classe C2]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]", "[[Chp 5 - Calcul différentiel d'ordre supérieur]]", "[[Chp4 - dérivabilité]]"]
maj: 2026-11-05
---

$f$ est de classe $\mathcal{C}^k$ sur l'ouvert $U$ si ses dérivées partielles d'ordre $k$ existent et sont continues sur $U$, et $\mathcal{C}^\infty$ si elle est $\mathcal{C}^k$ pour tout $k$.

Chaîne d'implications : $\mathcal{C}^1$ ⇒ différentiable ⇒ continue et dérivées partielles définies.

- $f$ est $\mathcal{C}^k$ si et seulement si ses composantes le sont.
- Les dérivées d'ordre inférieur à $k$ sont aussi continues.
- La composée de deux applications $\mathcal{C}^k$ est $\mathcal{C}^k$, si $f(U) \subset V$.
- $\mathcal{C}^1(U, F)$ est un sous-espace vectoriel de $\mathcal{C}(U, F)$. Toute application linéaire est $\mathcal{C}^1$.

**En une variable** : $f$ est $\mathcal{C}^n$ si elle est $n$ fois dérivable et si $f^{(n)}$ est continue. $\mathcal{C}^1$ signifie « dérivable à dérivée continue », et non « dérivable et continue ». Produit, quotient (si le dénominateur ne s'annule pas) et réciproque (si $f'$ ne s'annule pas) restent $\mathcal{C}^n$. Formule de Leibniz : $(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)}g^{(n-k)}$.

Liens : [[Dérivée partielle]], [[Différentielle]], [[Limite et continuité]], [[Difféomorphisme]], [[Dérivabilité]], [[Développement limité]]

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]], [[Chp 5 - Calcul différentiel d'ordre supérieur (résumé)]], [[Chp4 - dérivabilité (résumé)]]
