---
type: source
sources: ["[[démonstrations - integration]]"]
maj: 2026-11-05
---

Résumé de [[démonstrations - integration]], dans [[Year 2 - Analyse]]. En cas d'écart, le cours et ses images font foi.

Cette note donne les preuves de [[Chap7-Integration]].

## Preuves et idée de chacune

- **Fonctions en escalier** : chaque propriété se lit sur une subdivision adaptée à toutes les fonctions à la fois.
- **Encadrement** : à partir de $\theta$ en escalier à $\epsilon/2$ de $f$, prendre $\theta \pm \epsilon/2$.
- **Existence de l'[[Intégrale]]** : les deux ensembles sont non vides et bornés, donc $\alpha$ et $\beta$ existent, avec $\alpha \le \beta$. L'encadrement donne $0 \le \beta - \alpha \le \epsilon(b - a)$.
- **Linéarité** : approcher $f$ et $g$ par des fonctions en escalier, puis utiliser le lemme.
- **Chasles** : une inégalité par restriction aux deux morceaux, l'autre en appliquant ce résultat à $-f$.
- **Fonction positive d'intégrale nulle** : par contraposée, la continuité donne un intervalle sur lequel $f$ reste au-dessus de $f(c)/2$.
- **Théorème fondamental** : majorer $\left|\frac{F(x) - F(x_0)}{x - x_0} - f(x_0)\right|$ par la continuité de $f$ en $x_0$. L'unicité vient de ce que deux [[Primitive|primitives]] diffèrent d'une constante.
- **Parties et changement de variable** : dériver $fg$, et $F \circ \varphi$.
- **Sommes de Riemann** : preuve faite pour $f$ [[Application lipschitzienne|lipschitzienne]], avec une erreur de $K(b - a)^2/n$. La note ne couvre pas le cas continu général.
- **Exemples** : $\int \frac{\cos x\,dx}{2 - \cos^2 x} = \arctan(\sin x) + c$ par Bioche, et $\int_{-\pi/2}^0 \frac{dx}{1 - \sin x} = 1$ avec $t = \tan(x/2)$.

## Points à vérifier dans le cours

Ces points viennent des transcriptions, sans que j'aie ouvert les images. Rien n'a été corrigé dans le cours.

1. **Fonction positive d'intégrale nulle** : la preuve écrit $f(x) \le f(c)/2$. Il faut $f(x) \ge f(c)/2$ pour obtenir la minoration qui suit (complément).
2. **Linéarité** : le calcul de $\Delta$ passe de la valeur absolue d'une somme à une somme de valeurs absolues avec « = ». Il faut « ≤ ».
3. **Théorème fondamental** : même confusion entre « = » et « ≤ ». Et comme $x - x_0$ peut être négatif, il faut une valeur absolue autour du facteur et de l'intégrale.
4. **Primitives** : « deux primitives de la fonction $F$ » doit se lire $f$.
5. **Existence de l'intégrale** : $I^-_{[a,b]}(f)$ doit se lire $A^-_{[a,b]}(f)$.
