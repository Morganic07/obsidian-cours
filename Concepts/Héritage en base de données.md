---
type: concept
aliases: [héritage en base de données, héritage exclusif total, spécialisation et généralisation, table fille et table mère]
matieres: [ligue football]
sources: ["[[Sources/Year 3/ligue football/sujet database (résumé)|sujet database (résumé)]]", "[[Sources/Year 3/ligue football/Rapport du projet Ligue Football (résumé)|Rapport du projet (résumé)]]"]
maj: 2026-11-06
---

L'héritage, dans un [[Modèle entité-association]], regroupe les attributs communs de plusieurs entités dans une entité parente. Les entités filles ne gardent que leurs attributs propres. Dans le projet de [[Year 3 - ligue football]], `Personne` est le parent de `Joueur` et `Arbitre`.

## Vocabulaire du projet

L'héritage est dit **exclusif total** : une personne n'est qu'un seul type à la fois (exclusif), et elle est forcément d'un des deux types (total, selon le sens usuel du terme : complément).

## Traduction en schéma relationnel

Dans le rapport, chaque entité devient une table, et la clé primaire de la fille est aussi une clé étrangère vers la mère :

- `PERSONNE(id_personne, nom, prenom, date_naissance, email, photo, nationalite)` ;
- `JOUEUR(id_joueur, poste, pied_fort, numero_maillot, est_capitaine, id_equipe)`, avec `id_joueur` clé étrangère vers `PERSONNE` ;
- `ARBITRE(id_arbitre, grade, annees_experience)`, avec `id_arbitre` clé étrangère vers `PERSONNE`.

Voir [[Clé primaire et clé étrangère]], [[Schéma relationnel]] et [[Langage SQL]].

## Limite

Complément : les contraintes `CHECK` du rapport n'empêchent pas une même personne d'être à la fois dans `JOUEUR` et `ARBITRE` ; l'exclusion reste à la charge de l'application ou d'un déclencheur.
