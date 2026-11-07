---
type: source
tags:
  - year2
sources:
  - "[[Raw/Year 2/Anglais/stars.html.docx|stars.html]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Anglais/stars.html.docx|stars.html]], dans [[Anglais (matière)]]. Le fichier contient le code d'un site web 3D sur la taille des [[Étoile|étoiles]] (HTML, CSS, JavaScript ; interface en anglais), puis le brouillon des textes en français, étoile par étoile, et une conclusion bilingue.

## Le site (code)

- Une page HTML avec un **panneau latéral** noir (300 px, police Google *Play*) et une **iframe** qui intègre un modèle 3D Sketchfab (titre « Stars by … » dans le code).
- Un bouton `#panel-toggle` (◀) masque ou affiche le panneau : un script ajoute ou retire la classe `hidden` sur le panneau et le bouton, et `panel-hidden` sur `body` ; l'iframe prend alors toute la largeur. Transitions CSS de 0,3 s.

```js
toggleButton.addEventListener('click', () => {
  panel.classList.toggle('hidden');
  toggleButton.classList.toggle('hidden');
  body.classList.toggle('panel-hidden');
});
```

- Le code commence par un en-tête dupliqué (`<!DOCTYPE html>` … `<style>` répété deux fois).

### Mode d'emploi (« How to navigate on the website »)

- « ? » en bas à gauche : aide pour naviguer en 3D ; « ⌞⌝ » : plein écran ; ne pas toucher aux autres boutons.
- Flèches en bas au milieu (ou touches J et K) pour passer d'une étoile à l'autre, dans l'ordre conseillé (Jupiter, Soleil, Sirius…).
- Si les encadrés débordent, dézoomer (CTRL + « - »).
- Brouillon : suivre les numéros, molette pour zoomer, clic droit pour la vue 3D, double clic pour centrer une étoile.

## Comprendre les étoiles

- Une étoile est un corps céleste massif, surtout d'hydrogène et d'hélium, qui produit de l'énergie par [[Fusion nucléaire|fusion nucléaire]] (*nuclear fusion*) en son cœur : lumière, chaleur et autres rayonnements. Taille, température, couleur et durée de vie varient (de quelques millions à plusieurs milliards d'années).
- « Comme en boxe », la catégorie d'une étoile dépend de sa **masse**, pas de sa taille.
- Plus une étoile est massive et dense, plus sa matière est concentrée et plus elle est chaude.
- Plus elle est froide, plus elle tire vers le **rouge** ; plus elle est chaude, plus elle tire vers le **blanc-bleu**, voire le violet dans de rares cas. Selon le texte, une étoile rouge est peu dense, une étoile blanche ou bleue est extrêmement dense.
- La taille ne détermine ni la masse ni la température. Les étoiles commencent « petites » ; quand leurs réserves d'hydrogène s'épuisent, l'**équilibre hydrostatique** se rompt, la pression interne l'emporte sur la pression externe, et l'étoile se dilate (de 4 à 200 fois son volume initial, selon sa masse). Sa densité baisse et sa couleur vire au rouge ; sa masse est conservée.

### Catégories par taille (de la plus petite à la plus grande)

1. Naine rouge (*red dwarf*)
2. Étoile de type solaire (*solar-type star*)
3. Géante (*giant*)
4. Supergéante (*supergiant*)
5. Hypergéante (*hypergiant*)

### Unités

- **Rayon solaire** $R_\odot$ : un astre de 2 rayons solaires a deux fois le rayon du Soleil.
- **[[Masse solaire]]** $M_\odot$ : un astre de 4 masses solaires a quatre fois la masse du Soleil.
- **Kelvin** : 0 K = −273,15 °C (zéro absolu).

## Le parcours, étoile par étoile

| Étoile | Type | Taille ($R_\odot$) | Masse ($M_\odot$) | Température |
|---|---|---|---|---|
| Soleil | type solaire | 1 | 1 | 5 772 K |
| Sirius | — | 1,7 | 2 | 9 845 K |
| Pollux | géante orange | 9 | 2 (unité absente) | 4,586 (unité absente) |
| Arcturus | géante rouge | 25 | 1,08 | 4 286 K |
| Rigel | supergéante bleue | 79 | 17 | 10 000 K |
| Pistol Star | supergéante bleue | 306 | 165 | 35 000 K |
| Antares | supergéante rouge | 700 | 15 | 3 570 K |
| VY Canis Majoris | hypergéante rouge | 1 420 | 10 | 3 490 K |

- **Jupiter** : pour passer d'un astre qui ne brille pas à une étoile, il faut au moins 70 fois la masse de Jupiter ; une telle étoile aurait à peu près la taille de Jupiter, mais assez dense pour produire sa propre énergie. Entre ces petites étoiles et le Soleil se trouvent 85 % des étoiles : les **naines rouges** (brun à rouge).
- **Soleil** : il paraît géant à côté des naines rouges. Il est à la moitié de sa vie ; en fin de vie (hydrogène épuisé), il se dilatera jusqu'à englober l'orbite de Mars.
- **Sirius** : l'une des étoiles les plus lumineuses du ciel nocturne ; elle « scintille » de plusieurs couleurs basse sur l'horizon, à cause de la réfraction atmosphérique. Taille proche de celle du Soleil, mais plus massive ; en se dilatant, elle deviendra deux fois plus grande qu'Arcturus.
- **Pollux** : géante orange de la constellation des Gémeaux, souvent négligée à côté de Castor. « Géante apaisée » : elle a consommé l'hydrogène de son cœur et commencé sa transformation.
- **Arcturus** : ancienne étoile de type solaire en fin de vie, devenue géante rouge ; à la place du Soleil, elle engloberait selon le texte les orbites de la Terre et de Mars.
- **Rigel** : supergéante bleue d'Orion ; ces étoiles ne représentent que 1 % des étoiles. Plus une étoile est massive, plus elle est instable : une étoile massive et géante est très rare.
- **Pistol Star** : plus massive que toutes les autres étoiles du site réunies ; 10 millions de fois plus brillante que le Soleil, elle produit en 6 secondes l'énergie que le Soleil produit en un an. Deuxième étoile la plus massive connue (la première étant R136a1, 365 $M_\odot$ selon le texte). « Comme une rockstar », elle brûle vite et finira en supernova, laissant un trou noir. Image : le Soleil est à Pistol ce qu'une flamme de briquet est à un feu de forêt.
- **Antares** : supergéante rouge, si grande et âgée qu'elle est instable : elle se dilate et se contracte « comme si elle respirait ». Au centre du système solaire, elle s'étendrait jusqu'à Jupiter. Analogie : si le Soleil était une chaise au cœur de Paris, la Terre serait un sucre sur le périphérique et Jupiter une chaussure à Cergy ; Antares irait jusqu'à Cergy.
- **VY Canis Majoris** : la plus grande étoile observée, hypergéante rouge. Taille maximale théorique d'une étoile : 1 700 rayons solaires. Si la Terre était une bille de 2 cm, le Soleil mesurerait 2,20 m et VY 40 km (la taille de Los Angeles). Seulement 10 fois plus massive que le Soleil : sa densité est si faible qu'elle « pourrait flotter sur l'eau comme une boule de coton ».
- Ouverture : certains trous noirs sont des centaines de milliers de fois plus grands que VY Canis Majoris.

## Conclusion

- Citations en anglais (commentaires d'internautes repris tels quels) : « I use this video to help myself understand just how insignificant my problems actually are » ; « No matter how big you imagine the scale of the universe, it's bigger! ».
- Conclusion personnelle : devant le cosmos nous semblons minuscules, mais l'immensité de l'univers rend chaque vie « unique et extraordinaire » ; si l'univers est infiniment grand, il offre une infinité d'occasions d'en découvrir la beauté.
- L'auteur dit avoir volontairement simplifié les informations pour les rendre accessibles.

## Points à vérifier

- « La taille du Soleil augmentera d'ici 5 millions d'années » : il s'agit plutôt de milliards d'années (le Soleil est à la moitié de sa vie).
- « Plus une étoile est rouge, moins elle est dense » : une étoile chaude est massive mais pas forcément dense ; vrai seulement en comparant avec les géantes.
- Arcturus « engloberait les orbites de la Terre et de Mars » : avec 25 rayons solaires, elle n'atteindrait même pas Mercure (complément, d'après les ordres de grandeur usuels).
- Les valeurs de Pollux n'ont pas d'unités (« Masse : 2 », « Temperature : 4,586 », « Taille : 9 RS »).
- Le résumé précédent indiquait les valeurs d'Antares comme absentes : le brouillon français les donne (700 $R_\odot$, 15 $M_\odot$, 3 570 K), elles sont reprises ici.
- Antares « jusqu'à Jupiter » avec 700 $R_\odot$ (environ 3,3 ua) : plutôt entre Mars et Jupiter (complément, ordres de grandeur usuels).
- Les masses citées (Pistol Star 165 $M_\odot$, R136a1 365 $M_\odot$) varient selon les sources ; à recouper avant de les réutiliser.

Aucun point à vérifier sur transcription.
