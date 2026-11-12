---
type: concept
tags: [year4]
aliases: [ASCII art, art textuel, dessin en caractères]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp4/4.7.c|4.7.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'art ASCII compose des images avec les caractères imprimables d'un jeu de caractères, à l'origine le [[Code ASCII|code ASCII]] (lettres, chiffres, ponctuation, `*`, `/`, `\`, `#`…). Il suppose une police à chasse fixe, où tous les caractères ont la même largeur, pour que les colonnes s'alignent. Il est né avec les téléscripteurs (voir [[Télex]]) et les imprimantes ligne, qui ne savaient tracer que des caractères, puis s'est répandu sur les terminaux texte, les [[Forum Internet|forums]] et les messages électroniques ; il reste courant dans les bannières des programmes en [[Interface en ligne de commande|ligne de commande]].

En programmation, dessiner des motifs avec des `*` est un exercice classique de [[Boucle imbriquée|boucles imbriquées]] : la boucle externe parcourt les lignes, la boucle interne les colonnes, et une [[Structure conditionnelle|condition]] sur les indices décide du caractère à afficher.

```c
for (int i = 0; i < 3; i++) {          // 3 lignes
    for (int j = 0; j < 5; j++)        // 5 colonnes
        printf("*");
    printf("\n");
}
```

Un triangle s'obtient en faisant dépendre la borne de la boucle interne du compteur externe (`j <= i`), un contour en n'affichant `*` que sur la première et la dernière ligne ou colonne.

## Dans le cours

- [[tp4]] : les programmes 4.7 à 4.9 dessinent un rectangle plein, un triangle et le contour d'un rectangle en étoiles.

Voir aussi : [[Boucle imbriquée]], [[Code ASCII]], [[Caractère d'échappement]].
