---
type: concept
tags: [year4]
aliases: [nombres de Mersenne, nombre premier de Mersenne, Mersenne prime, Mersenne number]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp5/5.7.c|5.7.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un nombre de Mersenne est un entier de la forme

$$M_p = 2^p - 1$$

du nom du moine et savant français Marin Mersenne (XVIIe siècle), qui en dressa une liste. En binaire, $M_p$ s'écrit avec $p$ chiffres 1 ($M_3 = 7 = 111_2$, voir [[Numération binaire]]). C'est aussi la plus grande valeur d'un entier non signé de $p$ bits : 255 sur 8 bits, $2^{32} - 1$ sur 32 bits.

Propriétés :

- si $M_p$ est [[Nombre premier|premier]], alors $p$ est premier (car $2^{ab} - 1$ est divisible par $2^a - 1$) ;
- la réciproque est fausse : $p = 11$ est premier, mais $M_{11} = 2047 = 23 \times 89$ ;
- premiers nombres premiers de Mersenne : $M_2 = 3$, $M_3 = 7$, $M_5 = 31$, $M_7 = 127$, $M_{13} = 8191$.

**Lien avec les nombres parfaits** (théorème d'Euclide-Euler) : un entier pair est [[Nombre parfait|parfait]] si et seulement s'il s'écrit $2^{p-1}(2^p - 1)$ avec $2^p - 1$ premier. Euclide a démontré le sens direct (*Éléments*, livre IX), Euler la réciproque au XVIIIe siècle. Les quatre premiers nombres parfaits en découlent : $6 = 2 \times 3$, $28 = 4 \times 7$, $496 = 16 \times 31$, $8128 = 64 \times 127$ ; le suivant, pour $p = 13$, est 33 550 336. On ne sait pas s'il existe un nombre parfait impair.

Grâce au test de primalité de Lucas-Lehmer, propre à ces nombres et très rapide, les plus grands nombres premiers connus sont presque tous des nombres de Mersenne. Ils sont cherchés par le projet de calcul distribué GIMPS (*Great Internet Mersenne Prime Search*, depuis 1996) ; en octobre 2024, il a établi la primalité de $2^{136\,279\,841} - 1$, qui compte 41 024 320 chiffres. On ne sait pas s'il existe une infinité de nombres premiers de Mersenne.

## Dans le cours

- [[tp5]] : explique les quatre nombres parfaits affichés par le programme 5.7 (6, 28, 496 et 8128, pour $p = 2, 3, 5, 7$), seuls nombres parfaits inférieurs à 10 000.

Voir aussi : [[Nombre parfait]], [[Nombre premier]], [[Puissance (mathématiques)]].
