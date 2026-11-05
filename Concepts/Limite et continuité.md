---
type: concept
aliases: [limite, limites, continuité, application continue, applications continues, fonction continue, fonctions continues, discontinue]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-05
---

**Limite** : $f$ tend vers $l$ en $a$ si $\forall \epsilon > 0, \exists \eta > 0, \forall x \in A, \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$. La limite est unique, ne change pas entre normes équivalentes, et se calcule composante par composante. Les règles de somme, de produit et de quotient restent valables.

**Continuité** : $f$ est continue en $a \in A$ si elle y admet une limite, et continue sur $A$ si elle l'est en tout point. Cela revient à obtenir la même valeur par tous les chemins qui approchent $a$.

**Méthode pour $\mathbb{R}^2 \to \mathbb{R}$** :

1. Calculer $f(x_0, y_0)$, et continuer si la forme est indéterminée.
2. Passer en polaires, ou comparer des chemins. Deux valeurs différentes prouvent qu'il n'y a pas de limite.
3. Si tous les essais donnent $l_c$, montrer que $|f(x, y) - l_c| \to 0$, par exemple par une majoration.

> [!warning] Écart dans le cours
> [[Chp 3 - Limite et continuité d’applications]] dit qu'un résultat en polaires indépendant de $\theta$ donne la limite. Ce n'est pas suffisant : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé, mais vaut $1/2$ sur $y = x^2$. Il faut une majoration indépendante de $\theta$ (complément).

Liens : [[Norme]], [[Boule et voisinage]], [[Application lipschitzienne]], [[Dérivée partielle]], [[Différentielle]]

Résumé : [[Chp 3 - Limite et continuité d’applications (résumé)]]
