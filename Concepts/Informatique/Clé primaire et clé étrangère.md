---
type: concept
tags:
  - year3
aliases:
  - clé primaire
  - clef primaire
  - clé étrangère
  - clef étrangère
  - clés primaires
  - primary key
  - foreign key
  - clé composée
  - clé primaire composée
  - composite key
  - clé candidate
  - candidate key
  - clé naturelle
  - clé artificielle
  - surrogate key
matieres:
  - Data base
  - ligue football
sources:
  - "[[1 - Database|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
  - "readme.docx, dans Raw/Year 3/ligue football (exclu du miroir)"
  - "[[Raw/Year 3/Data base/Cours 1 et 2 : Database.docx|Cours 1 et 2 - Database]]"
maj: 2026-11-08
---

**Clé primaire** (PK) d'une relation : attribut, ou groupe d'attributs, qui identifie un enregistrement sans ambiguïté. Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.

**Clé étrangère** (FK) : attribut, éventuellement plusieurs, d'une table qui référence la clé primaire d'une autre table. Dans le schéma relationnel, la PK est soulignée et la FK précédée de `#` : `ETUDIANT(numero, nom, date_naissance, #code)` référence `FORMATION(code, intitule)`.

**Cas particulier** : dans une table de correspondance d'une association N-N, le couple des deux clés étrangères devient la clé primaire. Si l'association porte des attributs distinctifs (année universitaire), ils peuvent s'y ajouter (voir [[Table de correspondance]]).

**Dans le projet Ligue Football** : clés primaires composées (match, joueur) et (sponsor, équipe, saison). Une clé étrangère empêche de supprimer un joueur qui a des statistiques. Le MLD note `#id_equipe` dans JOUEUR : le DDL doit donc déclarer `CONSTRAINT fk_joueur_equipe FOREIGN KEY (id_equipe) REFERENCES EQUIPE (id_equipe)`, ce que le script du rapport omet. [[Erreurs du cours#^e-cle-primaire-et-cle-etrangere|✎]]

## Compléments (hors du cours)

- **Propriétés d'une clé primaire** : elle est **unique** (deux lignes ne la partagent pas), **non NULL** et **minimale** (on ne peut retirer aucun de ses attributs sans perdre l'unicité). Une table n'a qu'une clé primaire, mais peut avoir d'autres **clés candidates** (e-mail, numéro de sécurité sociale), déclarées `UNIQUE`.
- **Clé naturelle ou artificielle** : une clé naturelle est une donnée réelle qui identifie déjà l'objet (numéro d'étudiant, ISBN d'un livre) ; une clé artificielle (*surrogate key*) est un identifiant sans signification, créé pour la base, souvent une [[Clé auto-incrémentée|clé auto-incrémentée]]. La seconde ne change jamais, même si les données réelles changent.
- **Clé étrangère vers la même table** : dans une association réflexive, la clé étrangère référence la table elle-même : `ETUDIANT(numero, nom, …, #numero_tuteur)`, où `numero_tuteur` référence `numero` et peut être `NULL` (étudiant sans tuteur).
- **Clé étrangère dans la clé primaire** : une clé étrangère peut faire partie de la clé primaire, dans une [[Table de correspondance|table de correspondance]] (les deux clés étrangères) ou pour une entité faible, identifiée par la clé de son entité forte plus un attribut propre : `ENFANT(#numero_employe, prenom, date_naissance)`.
- **Intégrité référentielle** : le SGBD refuse une clé étrangère qui ne correspond à aucune clé primaire existante, et applique à la suppression de la ligne référencée le comportement déclaré (refus, `ON DELETE CASCADE`, `ON DELETE SET NULL`) : voir [[Contrainte d'intégrité]].

Voir aussi : [[Table de correspondance]], [[Modèle entité-association]], [[Schéma relationnel]], [[Algèbre relationnelle]], [[Contrainte d'intégrité]], [[Clé auto-incrémentée]], [[Normalisation (base de données)]]
Résumés : [[1 - Database]]
