---
type: concept
tags:
  - year3
aliases:
  - héritage en base de données
  - héritage exclusif total
  - spécialisation et généralisation
  - table fille et table mère
  - is-a
  - liaison is-a
matieres:
  - ligue football
  - Data base
sources:
  - "sujet database.pdf, dans Raw/Year 3/ligue football/for me (exclu du miroir)"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Rapport du projet]]"
  - "[[1 - Database|Cours 1 et 2 - Database]]"
maj: 2026-11-07
---

L'héritage, dans un [[Modèle entité-association]], regroupe les attributs communs de plusieurs entités dans une entité parente. Les entités filles ne gardent que leurs attributs propres. Dans le projet de Ligue football, `Personne` est le parent de `Joueur` et `Arbitre` ; le sujet impose cet héritage.

## Dans le cours de Data base

Le cours parle de liaison **« is-a »** ([[UML]]) : `Client` est spécialisé en `PersonnePhysique` et `PersonneMorale`, traduit en `Client(numero)`, `PersonnePhysique(#numeroPP, nom, prenom)` et `PersonneMorale(#numeroPM)` ([[1 - Database]]).

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

Résumés : [[1 - Database]]
