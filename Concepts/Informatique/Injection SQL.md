---
type: concept
tags: [year3]
aliases: [SQL injection, injection de code SQL, requête préparée, requêtes préparées, requête paramétrée, prepared statement]
sources: ["[[Raw/Year 3/Data base/Cours 3 : opérateurs et SQL.docx|Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'injection SQL est une attaque contre une application, typiquement une application web en [[Architecture n-tiers|architecture 3 tiers]], qui construit ses requêtes [[Langage SQL|SQL]] en y collant telle quelle une saisie de l'utilisateur. Une saisie bien choisie se lit alors comme du SQL et change le sens de la requête.

**Exemple.** Le serveur construit la requête de connexion par concaténation :

```sql
SELECT * FROM utilisateur WHERE login = '<saisie1>' AND mdp = '<saisie2>';
```

Avec `' OR '1'='1` dans le champ mot de passe, la requête devient :

```sql
SELECT * FROM utilisateur WHERE login = 'alice' AND mdp = '' OR '1'='1';
```

Comme `AND` est évalué avant `OR`, la condition `WHERE` est toujours vraie : la requête renvoie tous les utilisateurs et l'application ouvre une session sans mot de passe. D'autres saisies permettent de lire des tables entières (avec `UNION SELECT`) ou, si le SGBD accepte plusieurs requêtes à la suite, d'en modifier ou d'en supprimer.

**Parades.**
- **Requête préparée** (paramétrée) : la requête est envoyée au SGBD avec des emplacements (`WHERE login = ? AND mdp = ?`), puis les valeurs sont transmises séparément ; elles ne sont jamais interprétées comme du SQL, quel que soit leur contenu. C'est la parade principale.
- **Moindre privilège** : le compte SQL utilisé par l'application n'a que les droits dont elle a besoin (voir [[Gestion des droits SQL]]) ; une injection ne peut alors pas supprimer une table que ce compte ne peut pas toucher.
- En complément : valider les saisies (type, longueur) et ne pas afficher les messages d'erreur du SGBD à l'utilisateur. Échapper les caractères spéciaux à la main est fragile et ne remplace pas la requête préparée.

L'injection SQL figure depuis des années parmi les failles web les plus répandues dans les classements de l'OWASP (*Open Worldwide Application Security Project*), dans la catégorie des injections.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - opérateurs et SQL]], à propos de l'architecture 3 tiers, où le serveur d'application envoie au SGBD des requêtes construites à partir de ce que l'utilisateur a saisi.

Voir aussi : [[Architecture n-tiers]], [[Gestion des droits SQL]], [[Langage SQL]], [[Système de gestion de base de données]]

Résumés : [[2 - opérateurs et SQL]]
