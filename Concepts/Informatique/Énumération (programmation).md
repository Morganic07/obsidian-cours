---
type: concept
tags: [year4]
aliases: [enum class, type énuméré, enumeration]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : type défini par la liste de ses valeurs possibles, chacune nommée et associée à une constante entière : `enum Couleur { ROUGE, VERT, BLEU };` (ROUGE vaut 0, VERT 1…). Il remplace avantageusement des entiers « magiques » et se prête au `switch`. Depuis C++11, `enum class Couleur { Rouge, Vert };` crée une énumération fortement typée, dont les noms restent dans leur portée (`Couleur::Rouge`) et ne se convertissent pas implicitement en entiers.

## Dans le cours

[[4 - Cours complet]] indique que la valeur testée par un `switch` doit être un entier, un `char` ou une énumération, « qu'on verra plus tard » (voir [[Structure conditionnelle]]).

Résumés : [[4 - Cours complet]]
