# Étape 3 : le schéma relationnel (MLD)

La liste des tables avec les PK (<u>Primary Key</u>) / FK (#*Foreign Key*)

FORMATION ( <u>code</u>, intitule)

ETUDIANT ( <u>numero</u>, nom, date_naissance, #*code*)

Figure : Une flèche part de l'attribut `#code` de la table ETUDIANT et pointe vers l'attribut `code` (clé primaire) de la table FORMATION. Elle représente la clé étrangère.
