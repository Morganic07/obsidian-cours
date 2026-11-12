---
type: concept
tags: [year4]
aliases: [EOF, end of file, Ctrl-D, Ctrl+D]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : condition d'un flux d'entrée qui n'a plus de données à fournir. Sur un fichier, elle survient à la fin du contenu ; au clavier sous Unix, **Ctrl-D** en début de ligne la provoque (Ctrl-Z puis Entrée sous Windows). En C, `getchar()` renvoie alors la constante `EOF` ; en C++, la lecture `cin >> x` échoue et le flux passe en état `eof`, ce qui rend fausse la condition `while (cin >> x)`.

## Dans le cours

[[4 - Cours complet]] indique que sous Linux, Ctrl-D signale qu'il n'y a plus de saisie et termine ainsi la boucle du détecteur de mots répétés ; Ctrl-Z et Ctrl-C sont des [[Signal Unix|signaux]], d'une autre nature.

Voir aussi : [[Flux standard]], [[Flux d'entrée-sortie (C++)]].

Résumés : [[4 - Cours complet]]
