---
type: concept
tags: [year1]
aliases: [équations du second degré, trinôme du second degré, signe du trinôme, discriminant, trinôme, polynôme complexe, racine double]
matieres: [Analyse Maths, Algo Maths, Outil Maths]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]", "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]", "[[5 - Complexes (résumé)|Chapitre 5 - Complexes]]"]
maj: 2026-11-06
---

Équation $az^2 + bz + c = 0$ ($a \neq 0$), étudiée par le signe du discriminant $\Delta = b^2 - 4ac$.

**Dans $\mathbb{C}$** (Outil Maths, chapitre 5) : le trinôme $az^2 + bz + c$ a toujours des racines. Si $\Delta > 0$ : $z_{1,2} = \frac{-b \mp \sqrt{\Delta}}{2a}$ ; si $\Delta = 0$ : racine double $-b/2a$ ; si $\Delta < 0$ : $z_{1,2} = \frac{-b \mp i\sqrt{-\Delta}}{2a}$, conjuguées. Il se factorise toujours en $a(z - z_1)(z - z_2)$. Le TD 4 s'en sert pour $(x,y) \mapsto (x+y, xy)$ et $z \mapsto z + 1/z$ ; un contrôle traite le cas à coefficients complexes.

**Analyse Maths** : le cours renvoie au discriminant (signe du trinôme) pour le degré 2 ; au-delà, on cherche une racine évidente puis on factorise, sinon on étudie la fonction. En TD, la positivité d'un trinôme se montre par le discriminant ou par la forme canonique ($x^2 + 2x + 2 = (x+1)^2 + 1$).

**Algo Maths** : la résolution est une procédure avec disjonction de cas sur $\Delta$.

Voir aussi : [[Polynôme]], [[Nombre complexe]].

## À vérifier

- Chapitre 5 (Outil Maths) : la barre de conjugaison de $z_2 = \overline{z_1}$ est coupée sur l'image (alerte de transcription, lecture cohérente).

Résumés : [[0 - Rappels-etc (résumé)]], [[TD0-Rappel (résumé)]], [[td0slides (résumé)]], [[0 - diapo prof (résumé)]], [[Contrôles (résumé)]], [[5 - Complexes (résumé)]], [[TD4Applications-Solutions (résumé)]]
