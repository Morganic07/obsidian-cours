---
type: concept
aliases: [clé primaire, clef primaire, clé étrangère, clef étrangère, clés primaires, primary key, foreign key, clé composée, clé primaire composée, composite key]
matieres: [Data base, ligue football]
sources: ["[[Cours 1 et 2 - Database]]", "[[raw/Year 3/ligue football/Ligue Football - Projet DATABASE ID3-B.pdf|Ligue Football - Projet DATABASE ID3-B]]", "[[Cours/Year 3/ligue football/readme|readme (ligue football)]]"]
maj: 2026-11-06
---

**Clé primaire** (PK) d'une relation : attribut, ou groupe d'attributs, qui identifie un enregistrement sans ambiguïté. Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.

**Clé étrangère** (FK) : attribut, éventuellement plusieurs, d'une table qui référence la clé primaire d'une autre table. Dans le schéma relationnel, la PK est soulignée et la FK précédée de `#` : `ETUDIANT(numero, nom, date_naissance, #code)` référence `FORMATION(code, intitule)`.

**Cas particulier** : dans une table de correspondance d'une association N-N, le couple des deux clés étrangères devient la clé primaire. Si l'association porte des attributs distinctifs (année universitaire), ils peuvent s'y ajouter (voir [[Table de correspondance]]).

**Dans le projet Ligue Football** : clés primaires composées (match, joueur) et (sponsor, équipe, saison). Une clé étrangère empêche de supprimer un joueur qui a des statistiques.

Voir aussi : [[Table de correspondance]], [[Modèle entité-association]], [[Schéma relationnel]], [[Algèbre relationnelle]]

## À vérifier

- Dans le DDL du rapport du projet, `id_equipe` de JOUEUR n'a pas de clé étrangère, alors que le MLD en note une.

Résumés : [[Cours 1 et 2 - Database (résumé)]], [[Rapport du projet Ligue Football (résumé)]], [[readme (résumé)]], [[sujet database (résumé)]]
