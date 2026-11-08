---
type: concept
tags: [year3]
aliases: [bytecode, javac, compilation Java, fichier .class, JVM, machine virtuelle Java, Java Virtual Machine, JDK, JRE, JIT, compilation à la volée, just-in-time]
matieres: [Java]
sources: ["[[1 - Intro Java|Chp1 - Intro Java]]", "[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"]
maj: 2026-11-08
---

`javac Premier.java` compile le source et produit `Premier.class`, qui contient le bytecode ; `java Premier` l'exécute.

**Complément (hors du cours)** :

- Le **bytecode** est un code intermédiaire, indépendant du processeur et du système, exécuté par la **machine virtuelle Java** (JVM, *Java Virtual Machine*) que lance la commande `java`. Le même `.class` tourne sur toute plateforme qui dispose d'une JVM : c'est le principe « *write once, run anywhere* ».
- La JVM interprète le bytecode et compile à la volée en code machine les parties souvent exécutées : c'est la **compilation JIT** (*just-in-time*), qui rapproche les performances de celles d'un programme compilé directement.
- Le **JDK** (*Java Development Kit*) contient le compilateur `javac`, la JVM et la bibliothèque standard ; le **JRE** (*Java Runtime Environment*) désigne la partie nécessaire à la seule exécution (JVM et bibliothèque standard).
- `java Premier` prend le nom de la **classe**, sans l'extension `.class`.

Notion parente : [[Langage Java]]. Voir aussi : [[Méthode main]], [[Ramasse-miettes]], [[Machine virtuelle]].

Résumés : [[1 - Intro Java]]
