---
type: concept
aliases: [clé primaire, clef primaire, clé étrangère, clef étrangère, clés primaires, primary key, foreign key]
matieres: [Data base]
sources: ["[[Cours 1 et 2 - Database]]"]
maj: 2026-11-05
---

**Clé primaire** (PK) d'une relation : attribut, ou groupe d'attributs, qui identifie un enregistrement sans ambiguïté. Les attributs qui ne sont pas clé primaire peuvent apparaître plusieurs fois dans différentes tables.

**Clé étrangère** (FK) : attribut, éventuellement plusieurs, d'une table qui référence la clé primaire d'une autre table. Dans le schéma relationnel, la PK est soulignée et la FK précédée de `#` : `ETUDIANT(numero, nom, date_naissance, #code)` référence `FORMATION(code, intitule)`.

**Cas particulier** : dans une table de correspondance d'une association N-N, le couple des deux clés étrangères devient la clé primaire. Si l'association porte des attributs distinctifs (année universitaire), ils peuvent s'y ajouter.

Liens : [[Modèle entité-association]], [[Schéma relationnel]], [[Algèbre relationnelle]]

Résumé : [[Cours 1 et 2 - Database (résumé)]]
