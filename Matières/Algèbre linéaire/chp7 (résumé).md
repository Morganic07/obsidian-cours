---
type: source
tags:
  - year1
sources:
  - "[[chp7|chp7 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[chp7|chp7 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 7, éléments propres d'un [[Morphisme|endomorphisme]]. En cas d'écart, le cours fait foi.

## Valeur propre, vecteur propre et sous-espace propre

**Définition** : soit $f \in L(E)$. S'il existe $v$ **non nul** et $\lambda$ tels que
$$f(v) = \lambda v,$$
$\lambda$ est une [[Valeur propre|valeur propre]] et $v$ un [[Vecteur propre|vecteur propre]] associé (dessin du cours, disposition perdue).

- L'ensemble des valeurs propres de $f$ s'appelle le [[Spectre (algèbre linéaire)|spectre]] de $f$, noté $\text{Sp}(f)$.
- Un vecteur propre n'est jamais nul, mais une valeur propre peut être nulle : si $\text{Ker} f \neq \{0\}$ ([[Espace nul]]), il existe $u \in \text{Ker} f$ non nul avec $f(u) = 0 = 0 \times u$.

**Propriété** : soit $f \in L(E)$, $\lambda \in \mathbb{R}$, et $E_\lambda = \{ x \in E \mid f(x) = \lambda x \}$. Alors $E_\lambda$ est un [[Espace vectoriel|espace vectoriel]].

Démonstration du cours : si $f(x) = \lambda x$, alors $f(x) - \lambda x = 0$. Avec $\text{Id}(x) = x$, $f(x) - \lambda \text{Id}(x) = 0 \iff [f - \lambda \text{Id}](x) = 0$, donc $x \in \text{Ker}(f - \lambda \text{Id})$. Ainsi
$$E_\lambda = \text{Ker}(f - \lambda \text{Id})$$
est l'[[Espace propre|espace propre]] associé à la valeur propre $\lambda$.

**Propriété** : $\lambda$ est valeur propre de $f$ $\iff E_\lambda \neq \{0\}$, c'est-à-dire
$$\lambda \in \text{Sp}(f) \iff E_\lambda \neq \{0\} \iff f - \lambda \text{Id} \text{ non injective.}$$

**Propriété** : soit $e_1$ un vecteur propre associé à la valeur propre $\lambda_1$ et $e_2$ un vecteur propre associé à $\lambda_2$. Si $\lambda_1 \neq \lambda_2$, alors $\{e_1, e_2\}$ est libre.

Plus généralement : une famille de vecteurs propres associés à des valeurs propres distinctes est toujours [[Indépendance linéaire|libre]].

## Somme directe d'espaces vectoriels

**Théorème** : soient $E_1$ et $E_2$ deux sev de $E$.
$$E_1, E_2 \text{ supplémentaires} \iff \forall x \in E,\ \exists!\, (x_1, x_2) \in E_1 \times E_2,\ x = x_1 + x_2$$
$$\iff \dim E = \dim E_1 + \dim E_2 \text{ et } E_1 \cap E_2 = \{0\}$$

Tout élément $x$ de $E$ est la somme d'un élément de $E_1$ et d'un élément de $E_2$. On note $E_1 \oplus E_2$ et on dit qu'ils sont en [[Somme directe|somme directe]].

**Théorème** : soit $f \in L(E)$ et $\lambda_1, \dots, \lambda_p$ ses valeurs propres distinctes. Alors $E_{\lambda_1}, \dots, E_{\lambda_p}$ sont en somme directe, c'est-à-dire :
$$\forall (x_1, \dots, x_p) \in E_{\lambda_1} \times \dots \times E_{\lambda_p},\quad x_1 + \dots + x_p = 0 \Rightarrow x_1 = \dots = x_p = 0.$$

## Éléments propres d'une matrice carrée

**Définition** : soit $A \in \mathcal{M}_n(\mathbb{R})$. $\lambda$ est valeur propre de $A$ s'il existe un vecteur (une [[Matrice|matrice]] colonne) $X$ non nul tel que $A X = \lambda X$ ; $X$ est un vecteur propre associé à $\lambda$.

**Théorème** :
$$\lambda \text{ valeur propre de } A \iff \text{Ker}(A - \lambda \text{Id}) \neq \{0\} \iff A - \lambda \text{Id} \text{ non injective} \iff \det(A - \lambda \text{Id}) = 0$$
(les vecteurs colonnes de $A - \lambda \text{Id}$ sont liés ; voir [[Déterminant]] et [[Équation caractéristique]]).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Ǝ un vecteur nul X tq A・X = λ・X »** : il faut lire « non nul ». Avec $X = 0$, tout $\lambda$ conviendrait. **À corriger avant un examen.**
2. **Coquilles** : « non-injonctive » pour « non injective », et « une valeur propre peut si Ker f ≠ {0} » a perdu « être nulle ».
3. **Somme directe des espaces propres** : le cours écrit les $x_i$ dans « $E_1 \times E_2 \times \dots \times E_p$ » ; il s'agit des espaces propres $E_{\lambda_1}, \dots, E_{\lambda_p}$.
