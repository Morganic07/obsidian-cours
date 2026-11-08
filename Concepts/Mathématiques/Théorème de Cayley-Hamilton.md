---
type: concept
tags: [year1]
aliases: [Cayley-Hamilton, Cayley-Hamilton theorem, théorème de Cayley Hamilton]
sources: ["[[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : toute matrice carrée $A$ de taille $n$ annule son polynôme caractéristique :

$$\chi_A(A) = 0, \qquad \text{où } \chi_A(\lambda) = \det(A - \lambda I_n) = c_n\lambda^n + \dots + c_1\lambda + c_0,$$

et où $\chi_A(A)$ désigne la matrice $c_nA^n + \dots + c_1A + c_0 I_n$ : on remplace $\lambda^k$ par $A^k$ et la constante $c_0$ par $c_0 I_n$. Le résultat vaut aussi pour un endomorphisme $f$ d'un espace de dimension finie : $\chi_f(f) = 0$.

**Cas $n = 2$** : comme $\chi_A(\lambda) = \lambda^2 - \text{tr}(A)\,\lambda + \det A$ ([[Équation caractéristique]], [[Trace d'une matrice]]),
$$A^2 - \text{tr}(A)\,A + \det(A)\, I_2 = 0.$$

**Usages** :
- **Inverse** : si $\det A \neq 0$, on isole $I_n$ dans $\chi_A(A) = 0$ et on factorise par $A$, ce qui donne $A^{-1}$ comme polynôme en $A$ ([[Matrice inversible]]). Pour $n = 2$ : $A\big(\text{tr}(A)\,I_2 - A\big) = \det(A)\, I_2$, d'où
$$A^{-1} = \frac{1}{\det A}\big(\text{tr}(A)\, I_2 - A\big).$$
- **Puissances** : $A^n$ s'exprime en fonction de $I_n, A, \dots, A^{n-1}$, et par récurrence toute puissance $A^k$ aussi ; en pratique, $A^k$ est le reste de la division euclidienne de $\lambda^k$ par $\chi_A$, évalué en $A$.

**Exemple** : $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\text{tr}(A) = 4$, $\det A = 3$, donc $\chi_A(\lambda) = \lambda^2 - 4\lambda + 3$ et $A^2 = 4A - 3I_2$. Vérification : $A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 8 & 4 \\ 4 & 8 \end{pmatrix} - \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$. On en tire $A^{-1} = \frac{1}{3}(4I_2 - A) = \frac{1}{3}\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.

**Piège** : on ne peut pas « démontrer » le théorème en remplaçant $\lambda$ par $A$ dans $\det(A - \lambda I_n)$ : on obtiendrait $\det(A - A) = 0$, un scalaire, alors que $\chi_A(A)$ est une matrice. Les preuves usuelles passent par la comatrice de $A - \lambda I_n$ ou par la trigonalisation.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[7 - Algèbre linéaire]], à la suite du polynôme caractéristique.

Voir aussi : [[Équation caractéristique]], [[Trace d'une matrice]], [[Déterminant]], [[Matrice inversible]], [[Valeur propre]], [[Polynôme]].

Résumés : [[7 - Algèbre linéaire]]
