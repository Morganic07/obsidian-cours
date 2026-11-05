---
type: source
sources: ["[[Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-05
---

Résumé de [[Chp 3 - Limite et continuité d’applications]], dans [[Year 2 - Analyse dans Rn]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

La limite s'étend aux applications entre espaces normés. La différence avec $\mathbb{R}$ : on peut approcher un point par une infinité de chemins, et la limite doit être la même sur tous.

## Contenu, dans l'ordre du cours

- **[[Limite et continuité|Limite]]** : $\forall \epsilon > 0, \exists \eta > 0, \forall x \in A, \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$. Elle est unique, et ne dépend pas du choix entre normes équivalentes. Elle se calcule composante par composante.
- **Continuité** : $f$ est continue en $a$ si elle y admet une limite.
- **[[Application lipschitzienne]]** : $\|f(x) - f(y)\|_F \le k\|x - y\|_E$. Le cours la relie à la continuité uniforme, où le $\delta$ est le même partout.
- **Méthode pour $\mathbb{R}^2 \to \mathbb{R}$** : calculer $f(x_0, y_0)$. Si la forme est indéterminée, passer en polaires ou comparer des chemins. Deux chemins de valeurs différentes prouvent qu'il n'y a pas de limite. Sinon, on tient une candidate $l_c$, et il faut montrer que $|f(x, y) - l_c| \to 0$.
- **Exemples** : $xy/(x^2 + y^2)$ n'a pas de limite en $(0, 0)$ (valeurs $1/2$ et $0$ selon le chemin). $1 + x^3/(x^2 + y^2)$ tend vers 1, majoré par $|x|$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« f k-lipschitzien ⇔ f uniformément continue »** : image lue directement, c'est ta note manuscrite. Seule l'implication ⇒ est vraie. Contre-exemple : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue, mais pas lipschitzienne (complément). **À corriger avant un examen.**
2. **Test en polaires** : image lue directement, « si le résultat ne dépend pas de $\theta$ alors la fonction admet une limite ». Ce test seul ne suffit pas. Contre-exemple : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé pour tout $\theta$, mais vaut $1/2$ sur le chemin $y = x^2$. Il faut une majoration indépendante de $\theta$, comme dans l'exemple 2 du cours (complément). **À corriger avant un examen.**
3. **Étape 1 de la méthode** : l'absence de forme indéterminée ne garantit pas que $f(x_0, y_0)$ soit la limite, si la fonction est définie à part en ce point. Il faut savoir qu'elle y est continue (complément).
4. **Définition de la continuité** : « admet une limite en $a$ » suffit ici parce que la définition 1 inclut $x = a$, ce qui force la limite à valoir $f(a)$ (complément). Le paragraphe suivant s'arrête au milieu d'une phrase, sur « on ».
5. **Écriture de la limite** : l'image écrit $(\rho, \theta) \to (0, \theta)$, seul $\rho$ tend vers 0. La transcription de cette image indique à tort $(0, 0)$, et l'exemple 1 du cours écrit aussi $(0, 0)$.
