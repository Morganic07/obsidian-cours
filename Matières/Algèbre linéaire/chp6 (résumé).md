---
type: source
tags:
  - year1
sources:
  - "[[chp6|chp6 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[chp6|chp6 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 6, [[Déterminant]]. En cas d'écart, le cours fait foi.

## En dimension 2 et 3

**Définition** : pour $A \in \mathcal{M}_n(\mathbb{R})$, on définit le déterminant par récurrence sur $n$. On note $A_{ij} \in \mathcal{M}_{n-1}(\mathbb{R})$ la [[Matrice|matrice]] obtenue à partir de $A$ en enlevant la ligne $i$ et la colonne $j$.

Les formules (« On définit par récurrence l'application … Par : … On a : ») sont vides dans l'export. La définition est donnée dans [[Chp 0c - Determinants]] ; voir aussi [[Développement colonnes-lignes]] et [[Comatrice]].

## Le déterminant, une forme multilinéaire alternée

([[Forme multilinéaire alternée]])

- **Théorème** : deux lignes égales donnent $\det = 0$ ; deux colonnes égales donnent $\det = 0$.
- Le déterminant est linéaire par rapport à chaque colonne.
- **Théorème** : si l'on échange deux colonnes adjacentes, le déterminant change de signe.
- **Théorème** : si $A = (c_1 \dots c_n)$, alors $\det A \neq 0 \iff (c_1, \dots, c_n)$ est une [[Base (algèbre linéaire)|base]]. Le déterminant d'une matrice est non nul si et seulement si ses vecteurs colonnes forment une [[Indépendance linéaire|famille libre]].
- **Méthode** : pour démontrer qu'une famille de vecteurs est libre, on calcule le déterminant de la matrice formée de ses vecteurs en colonne. Vecteurs liés : $\det = 0$ ; vecteurs libres : $\det \neq 0$.
- Tous les théorèmes vus sur les colonnes valent aussi pour les lignes.
- Un déterminant reste inchangé si l'on ajoute à une ligne (ou une colonne) une [[Combinaison linéaire|combinaison linéaire]] des autres.

## Application des déterminants à la théorie du rang

### Caractérisation des bases

**Théorème fondamental** : soit $A = \| C_1 \dots C_n \|$ une matrice $(n,n)$. Les vecteurs $\{c_1, \dots, c_n\}$ forment une base $\iff \det A \neq 0$.

$\| C_1 \dots C_n \|$ est la matrice dont les colonnes sont les composantes des vecteurs dans la base.

Équivalences :
$$\det A = 0 \iff \text{une des colonnes est combinaison linéaire des autres} \iff \text{la famille des vecteurs colonnes est liée.}$$

Le choix d'une base $(e_1, \dots, e_n)$ de $E$ permet d'identifier $E$ à $\mathbb{K}^n$.

**Théorème** : soit $E$ un espace vectoriel de [[Dimension (algèbre linéaire)|dimension]] $n$. Les vecteurs $(v_1, \dots, v_n)$ forment une base de $E$ $\iff \det \| v_1 \dots v_n \| \neq 0$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Définition absente** : « On définit par récurrence l'application », « Par : » et « On a : » ne sont suivis de rien dans l'export de Google, comme dans [[chp4 (résumé)|chp4 (résumé)]]. Regarde si ton Google Doc contient la formule. La définition est donnée dans [[Chp 0c - Determinants]].
2. **« Forme multilinéaire altérée »** : il faut lire « alternée ».
3. **« Combinaison linéaire des deux autres »** : il faut lire « des autres », à toute taille.
4. **Échange de colonnes** : le signe change pour l'échange de deux colonnes quelconques, pas seulement adjacentes (complément).
