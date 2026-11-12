---
type: concept
tags: [year4]
aliases: [magnitude de Richter, magnitude locale, Richter scale, échelle de magnitude de Richter]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp3/3.11.c|3.11.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'échelle de Richter est l'échelle de **magnitude** des [[Séisme|séismes]] proposée en 1935 par le sismologue américain Charles Richter, avec Beno Gutenberg, pour les séismes de Californie du Sud. La magnitude locale $M_L$ se calcule à partir du [[Échelle logarithmique|logarithme]] décimal de l'amplitude maximale des ondes enregistrées par un sismographe d'un modèle donné (Wood-Anderson), corrigée de la distance à l'épicentre :

$$M_L = \log_{10} A - \log_{10} A_0(\delta)$$

où $A$ est l'amplitude mesurée et $A_0(\delta)$ celle d'un séisme de référence à la même distance $\delta$.

Propriétés :

- elle est **logarithmique** : un degré de plus correspond à une amplitude des ondes 10 fois plus grande et à une énergie libérée environ 32 fois plus grande ($10^{1{,}5}$) ; un séisme de magnitude 7 libère environ 1 000 fois plus d'énergie qu'un séisme de magnitude 5 ;
- elle est **ouverte** : elle n'a pas de maximum théorique, contrairement à une idée répandue (« échelle de 1 à 9 »), et une magnitude peut être négative pour les microséismes ;
- elle **sature** au-delà d'environ 6,5 à 7 : pour les très grands séismes, l'amplitude mesurée n'augmente plus avec la taille réelle de la rupture. Les organismes sismologiques publient alors la [[Magnitude de moment|magnitude de moment]] $M_w$, que les médias appellent encore souvent « magnitude sur l'échelle de Richter ».

La magnitude mesure la taille du séisme à sa source, une seule valeur par séisme ; l'**intensité** (échelles de Mercalli ou EMS-98, en chiffres romains) mesure ses effets en un lieu donné et varie avec la distance et le sol.

## Dans le cours

- [[tp3]] : le programme 3.11 lit une magnitude et affiche la description des effets du séisme avec un `switch` ; le cas « supérieur à 9 », écrit `case richter>9:`, ne compilait pas et passe dans le `default`. La fiche note que la magnitude est un réel et que l'échelle est ouverte.

Voir aussi : [[Séisme]], [[Magnitude de moment]], [[Échelle logarithmique]].
