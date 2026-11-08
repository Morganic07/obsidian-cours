---
type: concept
tags: [year4]
aliases: [destructeur, destructor, règle de trois, rule of three]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le destructeur est la méthode spéciale **appelée automatiquement quand un objet cesse d'exister** : à la fin du bloc où un objet local est déclaré, ou au `delete` d'un objet alloué par `new`. Il porte le nom de la classe précédé de `~` (`~Point()`), n'a **ni paramètre ni type de retour**, et une classe n'en a **qu'un**.

- **Rôle** : libérer ce que l'objet a acquis pendant sa vie, mémoire allouée dynamiquement, fichier ouvert.
- **Destructeur généré** : si on n'en écrit pas, le compilateur en génère un qui ne fait rien de particulier (il détruit seulement les attributs). Cela suffit pour une classe qui ne contient que des `int`, comme `Point`.
- **Ordre** : les objets locaux sont détruits dans l'ordre inverse de leur création.

```cpp
class Tampon {
    int* t;
public:
    Tampon(int n) { t = new int[n]; }
    ~Tampon() { delete[] t; }
};

void f() {
    Tampon a(10);   // constructeur : new int[10]
}                   // fin du bloc : ~Tampon(), delete[] t
```

**Règle de trois** : une classe qui a besoin d'un destructeur écrit à la main a presque toujours besoin aussi d'un [[Constructeur (programmation)|constructeur par copie]] et d'un opérateur d'affectation `operator=` écrits à la main. Sinon, la copie superficielle générée recopie le pointeur `t` : deux objets partagent la même zone mémoire, et chacun la libère à sa destruction, soit deux `delete[]` sur la même adresse, ce qui est un comportement indéfini.

## Dans le cours

Le cours ne le nomme pas : [[4 - C++]] présente les trois constructeurs de `Point` sans parler de destruction. La notion apparaît dans les compléments de [[4 - C++]].

Voir aussi : [[Constructeur (programmation)]], [[Allocation dynamique]], [[Classe et objet]], [[Surcharge d'opérateurs]], [[Programmation orientée objet]].

Résumés : [[4 - C++]]
