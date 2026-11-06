---
type: source
tags: [year4]
sources: ["[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-05
---

Résumé de [[Chp3 - pointeurs , tableaux, listes chainées, structures]], dans [[C++ (matière)]]. Le code est du C. En cas d'écart, le cours et ses images font foi.

## Idée générale

Comment la mémoire se représente (adresses, tableaux contigus), comment les pointeurs la manipulent, puis ce qu'on en tire : passage par adresse, tableaux en paramètre, `struct`, listes chaînées.

## Contenu, dans l'ordre du cours

- **Tableau en mémoire** : `int effectifs[6];` réserve 6 entiers contigus, chacun avec une adresse (en hexadécimal, préfixe `0x`). Les adresses ici avancent de 4 en 4 car un `int` fait 4 octets. Toute allocation est repérée par une adresse. Le C demande le type et la taille au début d'un bloc.
- **Adresses** : `&capacite` donne l'adresse, `%p` l'affiche. Le nom d'un tableau est l'adresse de sa première case. Ajouter 1 à une adresse décale de la taille du type : `effectifs + i` est l'adresse de la case `i`, et `t[i]` équivaut à `*(t + i)`.
- **[[Pointeur et adresse mémoire]]** : `int *ptr;` déclare un pointeur sur entier, variable qui contient une adresse. On peut l'initialiser, l'afficher, lui affecter une adresse (`ptr = &capacite;`, `ptr = effectifs + 3;`), lui ajouter ou retrancher un entier, lire la valeur pointée avec `*ptr`.
- **Programme complet** : `&i`, `p = &i`, `*p = 2` modifie `i`. `malloc` réserve 10 octets sur le tas (heap) et le pointeur contient l'adresse, pas les octets. `pb++` avance d'un octet pour un `unsigned char *`. Après `free`, les pointeurs gardent leur adresse.
- **Passage par valeur, puis par adresse** : `echange(int a, int b)` ne modifie pas `var1` et `var2`, comme le montrent les cadres de pile. `echange(int *a, int *b)` appelée avec `echange(&var1, &var2)` échange vraiment les valeurs, via `*a` et `*b`.
- **Tableaux en paramètre** : la fonction reçoit l'adresse du premier élément (décroissance du tableau en pointeur). Deux écritures équivalentes : `*(t+i)` ou `t[i]`.
- **[[Structure (struct)]]** : regroupe des variables de types différents. Sans `typedef`, on écrit `struct Etudiant eleve1;`. Avec `typedef`, `Etudiant eleve1;`. Accès par `eleve1.age`.
- **[[Liste chaînée]]** : cellule avec valeur et pointeur `suivant`, dernier pointeur à `NULL`, liste définie par son premier élément. Exemple complet avec `typedef struct Chainon`, `ajouter_au_debut(Chainon **premier_ptr, int)` et `afficher_liste(Chainon *premier)`.
- **Pointeur simple et double pointeur** : un double pointeur (`int **dptr`) contient l'adresse d'un pointeur. Utile pour modifier un pointeur depuis une fonction. `nouveau->valeur` équivaut à `(*nouveau).valeur`. Précautions : initialiser, `free` après chaque `malloc`, tester `NULL`.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seule l'image 13 (taille d'un entier) a été ouverte ; les autres sont lues par leur transcription.

1. **Taille d'un entier** (complément). **À corriger avant un examen.** Image ouverte : le cours écrit « sur système 64 bits : 8 octets » pour l'entier. En pratique, un `int` fait en général 4 octets sur les systèmes 32 et 64 bits courants. Ce sont les adresses qui passent à 8 octets en 64 bits. Le cours se contredit d'ailleurs lui-même avec ses adresses qui avancent de 4 en 4, et avec « 4 octets en 32 bits » pour le décalage d'un pointeur.
2. **`%d` ou `%p` pour afficher une adresse** : « soit on fait `%d`, soit `%p` ». `%p` est le bon format. Avec `%d`, une adresse de 64 bits est tronquée ou mal affichée (complément). La sortie du cours montre pourtant des adresses en décimal.
3. **Le programme complet n'est pas cohérent** : le pointeur est déclaré `buffer`, mais l'allocation et les affichages utilisent `bufferinheap`, jamais déclaré, et `free(buffer)` libère un pointeur jamais initialisé. Tel quel, le code ne compile pas.
4. **`free`** : le commentaire dit qu'il « vide le contenu de la mémoire ». `free` libère le bloc, sans l'effacer (complément).
5. **Version par valeur de `echange`** : le texte écrit « echange(&var1, &var2) » alors que l'appel de cette version est `echange(var1, var2)`.
6. **Schéma de pile du second `echange`** : `temp` a la même adresse que `var1` (0xabdafa0). Une des deux est fausse. Alerte des transcriptions confirmée par le texte.
7. **Fausses alertes** : la valeur 38 en face de l'adresse 0x16fdab72 et de l'indice 1 est correcte, car `capacite = effectifs[1]` donne 38. Les adresses de la sortie du terminal (0x16d3836…) diffèrent de celles du schéma parce que ce sont deux exécutions. Le pas de 4 entre 0x…72 et 0x…76 est normal pour un `int`. En revanche, 0x…72 n'est pas aligné sur 4, ce qui n'arrive pas en pratique : détail de schéma.
8. **Flèche de `ptr = &capacite`** : la transcription la trouve inversée. Les autres schémas (image 27) montrent bien la flèche de `ptr` vers `capacite`. Non tranché pour l'image 14.
9. **Schéma des pointeurs** (`x` en 0x1000, `ptr` en 0x1004, `dptr` en 0x1008) : adresses espacées de 4, alors qu'un pointeur occupe 8 octets sur système 64 bits. Simplification de schéma.
10. **Code copié** : la ligne `int ***tptr = &dptr` n'a pas de `;`, et l'exemple de liste contient une annotation `[cite: 1]` restée dans un commentaire. Les sections numérotées du guide sur les doubles pointeurs sautent de 2 à 7.
