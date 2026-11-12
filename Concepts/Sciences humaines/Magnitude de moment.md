---
type: concept
tags: [year4]
aliases: [moment magnitude, échelle de magnitude de moment, magnitude Mw, moment sismique]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.11.c|3.11.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la magnitude de moment $M_w$ est l'échelle de magnitude des [[Séisme|séismes]] introduite en 1979 par les sismologues Thomas Hanks et Hiroo Kanamori. Elle ne repose pas sur l'amplitude d'une onde, comme l'[[Échelle de Richter|échelle de Richter]], mais sur le **moment sismique** $M_0$, grandeur physique de la rupture :

$$M_0 = \mu \, S \, D$$

où $\mu$ est la rigidité de la roche, $S$ la surface de la faille rompue et $D$ le glissement moyen entre ses deux bords ($M_0$ en newtons-mètres). La magnitude s'en déduit par une relation [[Échelle logarithmique|logarithmique]] (forme normalisée par l'IASPEI en 2013) :

$$M_w = \frac{2}{3}\left(\log_{10} M_0 - 9{,}1\right)$$

Les coefficients ont été choisis pour que $M_w$ coïncide avec les anciennes magnitudes dans leur domaine de validité. Comme $M_0$ croît sans limite avec la taille de la faille, $M_w$ **ne sature pas** : c'est la seule échelle adaptée aux très grands séismes. Un degré de $M_w$ correspond à un moment environ 32 fois plus grand ($10^{1{,}5}$). Le séisme du Chili de 1960, le plus fort enregistré, a une magnitude de moment de 9,5 ; celui de Tōhoku (Japon, 2011), 9,0 à 9,1.

C'est la magnitude que publient aujourd'hui les organismes sismologiques (USGS aux États-Unis, BCSF-RéNaSS en France) pour les séismes importants, même quand la presse parle encore d'« échelle de Richter ».

## Dans le cours

- [[tp3]] : complément au programme 3.11, qui décrit les effets d'un séisme selon sa magnitude « sur l'échelle de Richter ».

Voir aussi : [[Échelle de Richter]], [[Séisme]], [[Échelle logarithmique]].
