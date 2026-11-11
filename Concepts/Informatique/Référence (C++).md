---
type: concept
tags: [year4]
aliases: [passage par référence, référence constante, pass by reference, const reference]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - C++]]) : un paramètre déclaré avec `&` (`std::ostream& os`, `const Point& p`) est passé **par référence** : la fonction travaille sur l'objet original, pas sur une copie.

Avantages selon le cours :
- **évite la copie** de l'objet (plus efficace) ;
- **permet de modifier l'objet original** (si la référence n'est pas `const`).

**Référence constante** (`const Point& p`) : l'objet n'est pas copié, et `const` garantit qu'il ne sera pas modifié, ce qui protège contre les modifications accidentelles. C'est la forme du paramètre du [[Constructeur (programmation)|constructeur par copie]] (`Point(const Point& autre)`) et de l'objet affiché par `operator<<` (voir [[Surcharge d'opérateurs]]).

La [[4 - Prise de note]] décrit `const Point& autre` comme « on récupère l'adresse (pointeur) ». Complément, hors du cours : une référence se comporte comme un autre nom de l'objet ; contrairement à un [[Pointeur et adresse mémoire|pointeur]], elle s'utilise sans `*` ni `->` (`autre.x`), ne peut pas être nulle et ne change pas d'objet.

En C, faute de références, on modifie une variable en passant son adresse (voir [[Passage par valeur]]).

Notion parente : [[Langage C++]]. Voir aussi : [[Passage de paramètres]].

## Dans le cours

[[4 - Cours complet]] définit la référence comme un nouveau nom, synonyme d'une variable définie ailleurs (`int &j = i;` puis `j = j + 1;` modifie `i`), initialisée une seule fois et liée à la même variable toute sa vie ; on ne peut ni la rediriger ni la créer sur une valeur (`int &k = 44;`). Elle existe en C++, pas en C. L'exercice 6 refait `ordonne3()` par passage par référence, plus simple que le passage par adresse.

Résumés : [[4 - C++]], [[4 - Prise de note]], [[4 - Cours complet]]
