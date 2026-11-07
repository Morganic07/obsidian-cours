---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/probabilité statistiques utilitaire.docx|probabilité statistiques utilitaire]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Statistics/probabilité statistiques utilitaire.docx|probabilité statistiques utilitaire]], dans [[Statistics (index)]] : aide-mémoire de formules en deux pages (« Statistics formulas »), sans commentaire. En cas d'écart, le cours et ses images font foi. Les deux images ne contiennent que des formules : elles sont recopiées ici d'après leurs transcriptions ; la page 2 a été vérifiée sur l'image.

Il va plus loin que les chapitres intégrés : tests d'hypothèse, deux échantillons, régression, khi-deux. Le wiki ne reprend comme explication que les formules dont un chapitre intégré établit le sens ; les autres sont seulement recopiées.

## Page 1

### Statistique descriptive

| Grandeur | Formule |
|---|---|
| Moyenne d'échantillon | $\overline{X} = \dfrac{\sum_{i=1}^{n} X_i}{n}$ |
| Moyenne de population | $\mu = \dfrac{\sum_{i=1}^{N} X_i}{N}$ |
| Écart interquartile | $IQR = Q_3 - Q_1$ (voir [[Quartiles et valeurs aberrantes]]) |
| [[Coefficient de variation]] | $CV = \dfrac{s}{\overline{X}} \times 100\,\%$ |
| Écart-type d'échantillon | $s = \sqrt{\dfrac{\sum_{i=1}^{n}(X_i - \overline{X})^2}{n-1}}$ |
| Variance d'échantillon | $s^2 = \dfrac{\sum_{i=1}^{n}(X_i - \overline{X})^2}{n-1}$ |
| Écart-type de population | $\sigma = \sqrt{\dfrac{\sum_{i=1}^{N}(X_i - \mu)^2}{N}}$ |
| Variance de population | $\sigma^2 = \dfrac{\sum (X_i - \mu)^2}{N}$ |

Voir [[Variance et écart-type d'échantillon]].

### Scores $Z$

$$Z = \frac{X - \overline{X}}{s} \qquad Z = \frac{X - \mu}{\sigma} \qquad Z = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \qquad Z = \frac{\overline{X} - \mu}{s/\sqrt{n}}$$

Voir [[Centrage et réduction]].

### Probabilités

- $P(A \text{ or } B) = P(A \cup B) = P(A) + P(B)$ si $A$ et $B$ sont [[Événements incompatibles|incompatibles]] (*mutually exclusive*) ;
- $P(A \text{ or } B) = P(A \cup B) = P(A) + P(B) - P(A \text{ and } B)$ en général ;
- $P(A \text{ and } B) = P(A \cap B) = P(A)\,P(B)$ si $A$ et $B$ sont [[Indépendance d'événements|indépendants]] ;
- $P(A \text{ and } B) = P(A \cap B) = P(A|B)\,P(B) = P(B|A)\,P(A)$ « si $A$ et $B$ ne sont pas indépendants » ;
- [[Probabilité conditionnelle]] : $P(A|B) = P(A \text{ and } B)/P(B)$ et $P(B|A) = P(B \text{ and } A)/P(A)$, avec $P(A \text{ and } B) = P(B \text{ and } A)$.

### Dénombrement et loi binomiale

- [[Permutation (dénombrement)|Arrangements]] : $_nP_r = \dfrac{n!}{(n-r)!}$ ;
- [[Combinaison (dénombrement)|Combinaisons]] : $_nC_r = \dfrac{n!}{r!\,(n-r)!}$ ;
- [[Loi binomiale]] : $P(x) = {}_nC_x\, P^x (1-P)^{n-x}$, de moyenne $\mu = nP$ et de variance $\sigma^2 = nP(1-P)$.

### Corrélation et régression

- Coefficient de corrélation d'échantillon (voir [[Covariance et corrélation]]) :
$$r = \frac{n\sum XY - \sum X \sum Y}{\sqrt{\left(n\sum X^2 - (\sum X)^2\right)\left(n\sum Y^2 - (\sum Y)^2\right)}}$$
- Test de la corrélation : $t_{n-2} = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}}$ ;
- Droite de [[Régression linéaire|régression]] $\hat{Y} = a + bX$, avec
$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \qquad a = \overline{Y} - b\overline{X}$$
Notation : $a$ est aussi noté $b_0$, et $b$ est noté $b_1$.

## Page 2

### Une moyenne, une proportion

| Cas | Statistique de test | Intervalle de confiance |
|---|---|---|
| Moyenne, $\sigma$ connu | $Z = \dfrac{\overline{X} - \mu_H}{\sigma/\sqrt{n}}$ | $\overline{X} \pm Z_\alpha \dfrac{\sigma}{\sqrt{n}}$ |
| Moyenne, $\sigma$ inconnu | $t_{n-1} = \dfrac{\overline{X} - \mu_H}{s/\sqrt{n}}$ | $\overline{X} \pm t_{\alpha,\,n-1} \dfrac{s}{\sqrt{n}}$ |
| Proportion | $Z \approx \dfrac{P_s - P}{\sqrt{P(1-P)/n}}$ | $P_s \pm Z_\alpha \sqrt{\dfrac{P_s(1-P_s)}{n}}$ |

$\mu_H$ : valeur de $\mu$ sous l'hypothèse testée ; $P_s$ : proportion de l'échantillon. Voir [[Test Z]], [[Test t]], [[Intervalle de confiance]].

### Deux échantillons

| Cas | Statistique de test | Intervalle de confiance |
|---|---|---|
| Deux moyennes, variances connues | $Z = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ | $(\overline{X}_1 - \overline{X}_2) \pm Z_\alpha \sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}$ |
| Deux moyennes, variances estimées | $Z = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | $(\overline{X}_1 - \overline{X}_2) \pm Z_\alpha \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ |
| Deux moyennes, variance poolée | $t_{n_1+n_2-2} = \dfrac{\overline{X}_1 - \overline{X}_2}{\sqrt{S^2_{pooled}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$ | — |
| Deux proportions | $Z \approx \dfrac{P_{s1} - P_{s2}}{\sqrt{\overline{P}(1-\overline{P})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$ | — |

avec
$$S^2_{pooled} = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}, \qquad \overline{P} = \frac{x_1 + x_2}{n_1 + n_2}.$$

Voir [[Échantillons appariés et indépendants]].

### Taille d'échantillon

Pour une marge d'erreur $e$ :
$$n = \frac{Z^2 \sigma^2}{e^2} \ \text{(moyenne)}, \qquad n = \frac{Z^2 P(1-P)}{e^2} \ \text{(proportion)}.$$

### Khi-deux

([[Test du χ²]], [[Tableau de contingence]])
$$\chi^2 = \sum \frac{(f_o - f_e)^2}{f_e}, \qquad f_e = \frac{\text{total ligne} \times \text{total colonne}}{n}$$
($f_o$ : effectif observé, $f_e$ : effectif attendu ; l'image écrit la formule sans le signe $\sum$.)

Les intervalles de la moyenne et de la proportion rejoignent le chapitre 4 : voir [[chp 4 - Part 2 - Inferential statistics (résumé)]] et [[chp 4 - Part 3 - Inferential statistics (résumé)]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Notation $Z_\alpha$** : l'aide-mémoire écrit $\bar{X} \pm Z_\alpha\sigma/\sqrt{n}$, alors que le chapitre 4 écrit $z_{\alpha/2}$ pour un intervalle bilatéral. L'aide-mémoire désigne sans doute le quantile bilatéral sous le nom $Z_\alpha$ ; à lire avec le chapitre, sans quoi on se trompe d'un facteur 2 sur $\alpha$ (complément).
2. **Probabilité d'une intersection** : « $P(A \cap B) = P(A|B)P(B)$ if A and B are not independent » est vrai aussi dans le cas indépendant (complément).
3. **Formules de tests et de régression** : elles n'ont pas de chapitre intégré dans le wiki. Aucune explication n'est reprise.
4. **Khi-deux sans $\sum$** : l'image (ouverte pour ce point) écrit bien $\chi^2 = (f_o - f_e)^2/f_e$, sans signe somme ; la statistique est la somme de ces termes sur toutes les cases (complément).
5. **Somme de la moyenne de population** : la transcription écrit $\mu = \sum_{i=1}^{n} X_i / N$ ; la borne devrait être $N$.
