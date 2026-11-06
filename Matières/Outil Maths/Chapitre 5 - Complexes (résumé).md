---
type: source
tags: [year1]
sources: ["[[Chapitre 5 - Complexes]]"]
maj: 2026-11-05
---

Résumé de [[Chapitre 5 - Complexes]], dans [[Outil Maths (matière)]]. En cas d'écart, le cours et ses images font foi. Les tableaux de formules de la note sont en partie vides : les formules figurent dans les transcriptions qui suivent.

## Idée générale

Les nombres complexes, de la forme algébrique à la forme exponentielle, avec leur géométrie du plan. Voir [[Nombre complexe]].

## Contenu, dans l'ordre du cours

- **Bases** : $i^2 = -1$. Somme $(a + a') + i(b + b')$, produit $(aa' - bb') + i(ab' + a'b)$, inverse $\frac{1}{z} = \frac{a - ib}{a^2 + b^2}$.
- **Conjugué** $\bar{z} = a - ib$ : compatible avec somme, produit, inverse, quotient, puissance. $z\bar{z} = a^2 + b^2$.
- **Trinôme** $az^2 + bz + c$ : toujours des racines dans $\mathbb{C}$. $\Delta > 0$ : deux racines réelles. $\Delta = 0$ : racine double $-b/2a$. $\Delta < 0$ : $\frac{-b \mp i\sqrt{-\Delta}}{2a}$, conjuguées. Factorisation $a(z - z_1)(z - z_2)$.
- **Forme trigonométrique** : module $|z| = \sqrt{a^2 + b^2}$, argument défini modulo $2\pi$, $z = |z|(\cos\theta + i\sin\theta)$ avec $\cos\theta = a/|z|$, $\sin\theta = b/|z|$.
- **Propriétés module et argument** : $|zz'| = |z||z'|$, $\arg(zz') = \arg z + \arg z'$, et de même pour l'inverse, le quotient, la puissance ; $\arg(-z) = \arg z + \pi$, $\arg\bar z = -\arg z$ ; inégalité triangulaire. Nota bene du cours : les formules d'argument ressemblent à celles du logarithme népérien.
- **Géométrie** : $\overrightarrow{AB}$ a pour affixe $z_B - z_A$ ; $|z_B - z_A| = AB$ ; $\arg\frac{z_B - z_C}{z_A - z_C} = (\overrightarrow{CA}; \overrightarrow{CB})$.
- **Forme exponentielle** : $z = |z|e^{i\theta}$, $e^{i\theta} = \cos\theta + i\sin\theta$. Règles de produit, puissance, quotient, inverse. Conseil du cours : revoir les formules de trigonométrie.
- **Moivre** : $z^n = |z|^n(\cos n\theta + i\sin n\theta)$. **Euler** : $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$. Conseil : revoir le triangle de Pascal.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes.

1. **$|\cos\theta + \sin\theta| = 1$** : faux tel qu'écrit (pour $\theta = \pi/4$, on obtient $\sqrt{2}$). Il faut $|\cos\theta + i\sin\theta| = 1$. Alerte de la transcription confirmée par le calcul (complément). **À corriger avant un examen.**
2. **$\cos 2x = \ldots = 1 - \sin^2 x$** : la dernière égalité est fausse, la bonne est $1 - 2\sin^2 x$. Alerte de la transcription, confirmée (complément). **À corriger avant un examen.**
3. **Triangle de Pascal** : la ligne « 1 1 » manque entre la première et la deuxième ligne. Le triangle est par ailleurs juste.
4. **Barre de conjugaison de $z_2 = \overline{z_1}$** : coupée sur l'image, lecture $\overline{z_1}$ cohérente avec les formules des racines. Fausse alerte probable.
