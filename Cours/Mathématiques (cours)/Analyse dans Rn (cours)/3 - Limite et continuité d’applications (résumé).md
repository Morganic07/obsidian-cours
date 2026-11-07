---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]] (« Chapitre 3 : Limite et continuité d'applications »), dans [[Analyse dans Rn (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

La limite s'étend aux applications entre espaces normés. La différence avec $\mathbb{R}$ : on peut approcher un point par une infinité de chemins, et la limite doit être la même sur tous.

## 1. Limite

On généralise la [[Limite et continuité|limite]] des fonctions de $\mathbb R$ dans $\mathbb R$ aux fonctions d'un EVN ([[Norme|espace vectoriel normé]]) dans un autre.

> **Définition 1 (limite en un point)** : soit $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux EVN, $A \subset E$, $f : A \to F$, $a \in \overline A$ ([[Intérieur et adhérence|adhérence]] de $A$) et $l \in F$. $f$ admet la limite $l$ quand $x$ tend vers $a$ si et seulement si l'une des propriétés équivalentes suivantes est vérifiée :
> 1. $\forall \epsilon > 0,\ \exists \eta > 0,\ \forall x \in A,\ \|x - a\|_E < \eta \Rightarrow \|f(x) - l\|_F < \epsilon$ ;
> 2. $\forall \epsilon > 0,\ \exists \eta > 0,\ \forall x \in A,\ x \in B_E(a, \eta) \Rightarrow f(x) \in B_F(l, \epsilon)$ ;
> 3. $\forall V_F \in \mathcal V(l),\ \exists V_E \in \mathcal V_E(a),\ \forall x \in A,\ (x \in V_E \Rightarrow f(x) \in V_F)$ ;
> 4. $\forall V_F \in \mathcal V(l),\ \exists V_E \in \mathcal V_E(a),\ f(V_E \cap A) \subset V_F$.

(Voir [[Boule et voisinage]].)

**Remarques** : $\epsilon$ est la précision avec laquelle on connaît la valeur de $f(x)$. On fixe $\epsilon$ ; il existe alors $\eta$ tel que tout $x$ à [[Distance|distance]] inférieure à $\eta$ de $a$ a une image à distance de $l$ inférieure à $\epsilon$. Si $\epsilon$ tend vers 0, $\eta$ doit tendre vers 0.

![[Chp 3 - Limite et continuité d’applications - image3.png]]
*Figure : dans $A$, un disque de rayon $\eta$ centré en $a$ contenant $x$ ; $f$ envoie $x$ sur $f(x)$, dans le disque de rayon $\epsilon$ centré en $l$ dans $F$.*

- **Propriété 1 (unicité de la limite)** : si $f$ admet une limite $l \in F$ en $a \in \overline A$, elle est unique ; on la note $\lim_{x \to a} f(x) = l$.
- **Propriété 2** : remplacer $\|\cdot\|_E$ et $\|\cdot\|_F$ par des normes équivalentes ne change ni l'existence de la limite, ni sa valeur.
- **Propriété 3 (linéarité)** : si $\lim_{x \to a} f(x) = l_1$ et $\lim_{x \to a} g(x) = l_2$ ($f, g : A \to F$), alors pour tout $\lambda \in \mathbb R$,
$$\lim_{x \to a} \big(f(x) + \lambda g(x)\big) = l_1 + \lambda l_2.$$
- **Propriété 4 (produit, quotient)** : pour $f, g : A \to \mathbb R$, de limites $l_1, l_2 \in \mathbb R$ en $a$ :
  1. $\lim_{x \to a} f(x)g(x) = l_1 l_2$ ;
  2. si $l_2 \neq 0$, $\lim_{x \to a} f(x)/g(x) = l_1/l_2$.

> **Propriété 5 (composantes)** : soit $E = \mathbb R^n$, $F = \mathbb R^p$. $f : E \to F$ admet $l = (l_1, \ldots, l_p)$ pour limite en $a$ si et seulement si, pour tout $i \in [\![1, p]\!]$, la $i$-ème application composante $f_i : E \to \mathbb R$ admet $l_i$ pour limite en $a$.
>
> Autrement dit, la limite se calcule composante par composante.

## 2. Continuité

> **Définition 2 (application continue)** : soit $A \subset E$, $f : A \to F$ et $a \in A$. $f$ est **continue en $a$** si et seulement si $f$ admet une limite en $a$. Elle est **discontinue** en $a$ sinon. Elle est continue sur $A$ si elle est continue en tout point de $A$. On note $\mathcal C(A, F)$ l'ensemble des fonctions continues de $A$ dans $F$.

La continuité en $a$ revient à étudier si, **quel que soit le chemin** par lequel on s'approche de $a$, la fonction tend vers la même valeur. C'est aussi la définition dans le cas de $\mathbb R \to \mathbb R$ (la phrase suivante du cours est coupée, voir « Points à vérifier »).

## 3. Applications lipschitziennes

> Soit $f : E \to F$, $A \subset E$. $f$ est **$k$-lipschitzienne** sur $A$ ([[Application lipschitzienne]]) si et seulement si
> $$\forall \mathbf x, \mathbf y \in A,\quad \|f(\mathbf x) - f(\mathbf y)\| \le k\,\|\mathbf x - \mathbf y\|_E.$$
> La première norme est celle de $F$ : le cours ne lui met pas d'indice.
> Si $f : \mathbb R \to \mathbb R$ : $|f(x) - f(y)| \le k\,|x - y|$.

La note manuscrite écrit « $f$ $k$-lipschitzienne $\iff$ $f$ [[Continuité uniforme|uniformément continue]] » : seule l'implication $\Rightarrow$ est vraie (voir « Points à vérifier »).

> **Continuité uniforme** : $f : E \to F$ entre espaces métriques est uniformément continue si, pour toute précision fixée, on trouve une « marge de manœuvre » $\delta$ qui marche **partout** :
> $$\forall \epsilon > 0,\ \exists \delta > 0,\ \forall x, y \in E,\ d_E(x, y) < \delta \Rightarrow d_F(f(x), f(y)) < \epsilon.$$
> - Continuité classique : $\delta$ peut dépendre du point $x$ (local).
> - Continuité uniforme : $\delta$ est le même partout (global).

## 4. Méthode : limite d'une fonction de $\mathbb R^2$ dans $\mathbb R$ en $a = (x_0, y_0)$

On cherche $\lim_{(x,y) \to (x_0, y_0)} f(x, y)$.

**Étape 1** : calculer $f(x_0, y_0)$. Si l'on n'obtient pas de [[Forme indéterminée|forme indéterminée]] ($0 \times \infty$, $\infty/\infty$, $0/0$, $\infty - \infty$, …), alors $\lim f(x, y) = f(x_0, y_0)$. Sinon, il faut lever l'indétermination : étape 2.

**Étape 2** : montrer soit (i) que tous les chemins vers $a$ donnent la même valeur (et $f$ est continue en $a$ et prend cette valeur), soit (ii) qu'au moins deux chemins vers $a$ donnent des valeurs différentes (et $f$ n'a pas de limite en $a$).
1. **[[Coordonnées polaires]]**, surtout si le dénominateur s'y prête (par exemple $(x - x_0)^2 + (y - y_0)^2$) : on pose
$$x = x_0 + \rho\cos\theta, \qquad y = y_0 + \rho\sin\theta,$$
ce qui définit $\tilde f(\rho, \theta) = f(x, y)$, et
$$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = \lim_{(\rho,\theta) \to (0,\theta)} \tilde f(\rho, \theta).$$
Selon le cours : si le résultat ne dépend pas de $\theta$, $f$ admet cette limite (la valeur ne dépend pas du chemin) ; s'il dépend de $\theta$, $f$ n'a pas de limite en $a$ (voir « Points à vérifier » : ce test seul ne suffit pas).
2. **Chemins cartésiens**, si la fonction ne se prête pas aux polaires : on calcule $f$ le long de différents chemins $(x, \alpha(x))$, avec $\alpha : \mathbb R \to \mathbb R$. Si deux chemins donnent des valeurs différentes, pas de limite. Si tous donnent la même valeur $l_c$, c'est un bon candidat : étape 3.
3. Calculer $|f(x, y) - l_c|$ : si cette quantité tend vers 0 quand $(x, y) \to (x_0, y_0)$, alors $\lim f(x, y) = l_c$ ; sinon, $f$ n'a pas de limite en $(x_0, y_0)$.

On peut aussi utiliser la [[Caractérisation séquentielle de la limite|caractérisation séquentielle]] : comparer $f(u_n)$ et $f(v_n)$ pour deux suites $u_n, v_n \to a$.

## 5. Exemples

### Exemple 1 : $f_1(x, y) = \dfrac{xy}{x^2 + y^2}$ en $(0,0)$

$f_1(0,0) = 0/0$ : forme indéterminée.

| Coordonnées polaires | Caractérisation séquentielle | Caractérisation cartésienne |
|---|---|---|
| $x = \rho\cos\theta$, $y = \rho\sin\theta$ donnent $\tilde f_1(\rho, \theta) = \cos\theta\sin\theta$. Si $\theta = \pi/4$, la limite vaut $1/2$ ; si $\theta = \pi/2$, elle vaut $0$. | $u_n = (1/n, 1/n)$ et $v_n = (0, 1/n)$ tendent vers $(0,0)$, mais $f_1(u_n) \to 1/2$ et $f_1(v_n) \to 0$. | Chemin $(x, x)$ : $f_1(x,x) = 1/2$. Chemin $(0, y)$ : $f_1(0, y) = 0$. |

Conclusion : deux chemins donnent des valeurs différentes, donc **$f_1$ n'a pas de limite en $(0,0)$**.

![[Chp 3 - Limite et continuité d’applications - image10.png]]
*Figure : exemple 1, les trois méthodes et les deux chemins vers l'origine (diagonale $\theta = \pi/4$ et axe vertical $\theta = \pi/2$).*

### Exemple 2 : $f_2(x, y) = 1 + \dfrac{x^3}{x^2 + y^2}$ en $(0,0)$

$f_2(0,0)$ donne $0/0$ : forme indéterminée.

| Coordonnées polaires | Caractérisation séquentielle | Caractérisation cartésienne |
|---|---|---|
| $\tilde f_2(\rho, \theta) = \rho\cos^3\theta + 1 \to 1$ quand $\rho \to 0$ : « la fonction est continue ». | $u_n = (1/n, 1/n)$, $v_n = (1/n, 0)$ : $f_2(u_n) \to 1$ et $f_2(v_n) \to 1$. **On ne peut pas conclure.** | Chemins $(x, x)$ et $(x, 0)$ : limite 1 dans les deux cas. **On ne peut pas conclure.** |

Deux chemins qui donnent 1 ne prouvent pas la continuité. On étudie $|f(x, y) - l_c|$ avec $l_c = 1$ :
$$|f_2(x, y) - 1| = \left|\frac{x^3}{x^2 + y^2}\right| = \frac{x^2}{x^2 + y^2}\,|x| \le |x| \underset{(x,y) \to (0,0)}{\longrightarrow} 0.$$
Avec les trois méthodes, **$\lim_{(x,y) \to (0,0)} f_2(x, y) = 1$**.

![[Chp 3 - Limite et continuité d’applications - image14.png]]
*Figure : exemple 2, les trois méthodes, les chemins $u_n$ (diagonale) et $v_n$ (axe horizontal), et la majoration finale.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« f k-lipschitzien ⇔ f uniformément continue »** : image lue directement, c'est ta note manuscrite. Seule l'implication ⇒ est vraie. Contre-exemple : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue, mais pas lipschitzienne (complément). **À corriger avant un examen.**
2. **Test en polaires** : image lue directement, « si le résultat ne dépend pas de $\theta$ alors la fonction admet une limite ». Ce test seul ne suffit pas. Contre-exemple : $x^2y/(x^4 + y^2)$ tend vers 0 à $\theta$ fixé pour tout $\theta$, mais vaut $1/2$ sur le chemin $y = x^2$. Il faut une majoration indépendante de $\theta$, comme dans l'exemple 2 du cours (complément). **À corriger avant un examen.**
3. **Étape 1 de la méthode** : l'absence de forme indéterminée ne garantit pas que $f(x_0, y_0)$ soit la limite, si la fonction est définie à part en ce point. Il faut savoir qu'elle y est continue (complément).
4. **Définition de la continuité** : « admet une limite en $a$ » suffit ici parce que la définition 1 inclut $x = a$, ce qui force la limite à valoir $f(a)$ (complément). Le paragraphe suivant s'arrête au milieu d'une phrase, sur « on ».
5. **Écriture de la limite en polaires** : le cours n'écrit pas la même chose partout. La méthode (deux fois) et l'exemple 1 écrivent $(\rho, \theta) \to (0, \theta)$, seul $\rho$ tend vers 0 ; l'exemple 2 écrit $(\rho, \theta) \to (0, 0)$, ce qui laisserait croire que $\theta$ tend aussi vers 0. Dans les deux exemples, seul $\rho$ tend vers 0 (complément).
6. **Autres mentions « À vérifier » des transcriptions** : Propriété 5, « pour tout entier $[\![1;p]\!]$ » sans « $i \in$ » ; définition lipschitzienne, la première norme n'a pas d'indice dans la note manuscrite (c'est celle de $F$) ; version $\mathbb R \to \mathbb R$ manuscrite ambiguë (vecteurs fléchés) ; « si prête bien » pour « se prête bien ».
7. **Exemple 2, colonne polaire** : la conclusion « la fonction est continue » tirée de $\rho\cos^3\theta + 1 \to 1$ est juste ici parce que $|\rho\cos^3\theta| \le \rho$ ne dépend pas de $\theta$ ; le cours ne le dit pas (complément, lié au point 2). La fonction n'est d'ailleurs pas définie en $(0,0)$ : « continue » signifie ici prolongeable par continuité par la valeur 1 ([[Prolongement par continuité]]).
