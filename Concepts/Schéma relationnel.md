---
type: concept
aliases: [MLD, modèle logique de données, schéma relationnel, relational diagram]
matieres: [Data base]
sources: ["[[Cours 1 et 2 - Database]]"]
maj: 2026-11-05
---

Le MLD (modèle logique de données) est la liste des tables avec leurs clés primaires (soulignées) et leurs clés étrangères (précédées de `#`). C'est la troisième étape de la méthode MERISE, obtenue à partir du [[Modèle entité-association]].

**Règles de passage du MCD au MLD** (cours)
- Cardinalité 1-N : la clé étrangère est placée du côté de la cardinalité « 1 ». Exemple : `ETUDIANT(numero, ..., #code)` pour un étudiant qui suit une formation.
- Cardinalité N-N : on crée une table de correspondance, `est_inscrit(#code, #numero)`, dont le couple est la clé primaire.
- Association avec attributs portés : une table supplémentaire.
- Cardinalité 1-1 : elle ne devrait pas apparaître dans un schéma de conception.
- Héritage : `Client(numero)`, `PersonnePhysique(#numeroPP, ...)`, `PersonneMorale(#numeroPM, ...)`.

Liens : [[Clé primaire et clé étrangère]], [[Algèbre relationnelle]], [[Héritage en base de données]]

Résumé : [[Cours 1 et 2 - Database (résumé)]]
