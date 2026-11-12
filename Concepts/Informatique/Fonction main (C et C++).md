---
type: concept
tags: [year4]
aliases: [int main, main(), argc et argv, fonction main]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : fonction que tout programme C/C++ doit posséder, qui indique où commencer l'exécution. Elle retourne un `int` au « système » qui l'a appelée : 0 signifie que le programme s'est terminé avec succès (convention Unix), une autre valeur signale une erreur (voir [[Code de retour]]).

Complément, hors du cours : `int main(int argc, char **argv)` reçoit les arguments de la ligne de commande (`argc` leur nombre, `argv` leur texte, `argv[0]` étant le nom du programme). En C++, atteindre la fin de `main` sans `return` équivaut à `return 0;`. L'équivalent Java est la [[Méthode main]].

## Dans le cours

[[4 - Cours complet]] décrit ses quatre parties (type de retour, nom, paramètres, corps) sur « Hello world », et utilise la forme `main(int argc, char **argv)` dans l'exercice 2.

Voir aussi : [[Fonction et procédure]].

Résumés : [[4 - Cours complet]]
