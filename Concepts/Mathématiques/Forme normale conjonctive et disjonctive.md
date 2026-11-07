---
type: concept
tags: [year1]
aliases: [forme normale conjonctive, forme normale disjonctive, formes normales]
matieres: [Outil Maths]
sources: ["[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : en [[Logique propositionnelle]], une formule est sous forme normale conjonctive (FNC) si c'est une conjonction ($\wedge$) de clauses, chaque clause étant une disjonction ($\vee$) de littéraux, c'est-à-dire de variables ou de négations de variables : par exemple $(P\vee\neg Q)\wedge(Q\vee R)$. Elle est sous forme normale disjonctive (FND) si c'est une disjonction de conjonctions de littéraux : par exemple $(P\wedge Q)\vee(\neg P\wedge R)$. Toute formule est équivalente à une formule sous chacune de ces deux formes ; on l'obtient en éliminant $\Rightarrow$ et $\Leftrightarrow$, en portant les négations sur les variables (lois de De Morgan), puis en distribuant $\vee$ sur $\wedge$ (ou l'inverse).

## Dans le cours

Nommée dans l'exercice 9 de la feuille de logique sans définition : il demande d'écrire trois propositions sous forme normale conjonctive et sous forme normale disjonctive, par exemple $(\neg P \wedge Q) \Rightarrow R$. Le cours ne définit pas ces formes.

Notion parente : [[Logique propositionnelle]]. Voir aussi : [[Propriétés des connecteurs logiques]].

Résumés (rapprochement, complément hors du cours) : [[1 - logique]]
