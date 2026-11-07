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
matieres:
  - Data base
  - ligue football
sources:
  - "[[1 - Database|Cours 1 et 2 - Database]]"
  - "[[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]]"
  - "readme.docx, dans Raw/Year 3/ligue football (exclu du miroir)"
maj: 2026-11-07
---

**Clé primaire** (PK) d'une relation : attribut, ou groupe d'attributs, qui identifie un enregistrement sans ambiguïté. Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.

**Clé étrangère** (FK) : attribut, éventuellement plusieurs, d'une table qui référence la clé primaire d'une autre table. Dans le schéma relationnel, la PK est soulignée et la FK précédée de `#` : `ETUDIANT(numero, nom, date_naissance, #code)` référence `FORMATION(code, intitule)`.

**Cas particulier** : dans une table de correspondance d'une association N-N, le couple des deux clés étrangères devient la clé primaire. Si l'association porte des attributs distinctifs (année universitaire), ils peuvent s'y ajouter (voir [[Table de correspondance]]).

**Dans le projet Ligue Football** : clés primaires composées (match, joueur) et (sponsor, équipe, saison). Une clé étrangère empêche de supprimer un joueur qui a des statistiques.

Voir aussi : [[Table de correspondance]], [[Modèle entité-association]], [[Schéma relationnel]], [[Algèbre relationnelle]]

## Erreurs du cours

- [[Raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B.pdf]] (DDL de JOUEUR) écrit seulement « id_equipe INT NOT NULL » ; il faut ajouter « CONSTRAINT fk_joueur_equipe FOREIGN KEY (id_equipe) REFERENCES EQUIPE (id_equipe) » : le MLD note `#id_equipe` comme clé étrangère.

Résumés : [[1 - Database]]
