---
type: source
sources: ["[[Cours 3 - opérateurs et SQL]]"]
maj: 2026-11-05
---

Résumé de [[Cours 3 - opérateurs et SQL]], dans [[Year 3 - Data base]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les opérateurs de l'[[Algèbre relationnelle]], puis le [[Langage SQL]] et l'architecture d'un SGBD.

## Contenu, dans l'ordre du cours

- **Vocabulaire** : relation = table, attributs = colonnes, SGBD, SGBDR (relationnel).
- **Sur une relation** : projection $\pi_A(R)$ (choisir des colonnes), restriction $\sigma_F(R)$ (choisir des lignes), renommage $\rho_{A \to B}$ (indispensable quand deux attributs de même nom se rencontrent).
- **Entre deux relations** : produit cartésien $R \times S$, jointure naturelle $R \bowtie S$ (sur les noms de champs identiques, souvent une clé étrangère ; équivaut à un produit suivi d'une restriction), division $R \div S$ (éléments de $R$ associés à tous ceux de $S$).
- **Exemples** : jointure `PROGRAMME` avec `SALLE` sur `id_salle` (la salle sans film disparaît). Division : employés ayant toutes les certifications requises. Avec `Alice` (Sécurité, Réseau), `Bob` (Sécurité), `Charlie` (Sécurité, Réseau, Cloud) et `REQUIS` = Sécurité, Réseau : le résultat est Alice et Charlie.
- **Opérateurs ensemblistes** (même schéma, c'est-à-dire même nombre de colonnes, mêmes types, en général mêmes noms) : union, intersection, différence.
- **Récapitulatif** : tous les opérateurs ne sont pas implémentés dans les SGBD (la division, par exemple) ; certains se dérivent (jointure = produit + restriction).
- **SQL** : DDL (`CREATE`, `ALTER`, `DROP`, `DESCRIBE`), DML (`INSERT`, `UPDATE`, `DELETE`, `SELECT ... FROM ... [WHERE ...]`), gestion des droits (`GRANT`, `REVOKE`), avec une syntaxe qui varie selon le SGBDR.
- **Architecture** : client-serveur 2 tiers (console ou graphique), web 3 tiers (navigateur, serveur web, SGBD), possibilité de 4 tiers avec serveur d'application. L'administration peut se faire en 2 ou 3 tiers, jamais en 1 tier. Les architectures peuvent tourner en local.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 19 (droits) a été ouverte ; les autres sont lues par leur transcription.

1. **`REVOKE UPDATE ON dbname.tablename TO user ;`** (complément). **À corriger avant un examen.** Image ouverte : le cours écrit bien `TO`. En SQL, on retire un droit avec `REVOKE ... FROM user`. `TO` appartient à `GRANT`. Même ligne : `dbname.tablename` désigne une table alors que le `GRANT` voisin vise une base (`dbname`).
2. **`GRANT ... IDENTIFIED BY password`** (complément) : cette forme est propre à certaines versions de MySQL. Le cours précise de toute façon que la syntaxe varie beaucoup.
3. **`ALTER TABLE ... DATE NOT NULL) ;`** : la parenthèse fermante est en trop. Alerte de la transcription confirmée par le texte.
4. **`DESCRIBE`** est rangé dans le DDL, mais c'est une commande propre à certains SGBD (le cours le signale : syntaxe variable).
5. **Fausses alertes** : « +1 » et « +2 » sont des badges d'interface, pas du cours.
6. **Images de la division** : l'image de la relation `R` semble coupée en bas, d'autres lignes pourraient manquer. Le résultat du cours reste cohérent avec les lignes visibles.
7. **Contenu absent** : pas de jointure SQL ni de `GROUP BY` dans cette note.
