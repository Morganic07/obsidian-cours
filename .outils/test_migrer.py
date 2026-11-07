import contextlib
import io
import tempfile
import unicodedata
import unittest
from pathlib import Path

import chemins
import migrer

M, N = chemins.MIROIR, chemins.NOTES
NOUVEAU = "Raw"
MAT = chemins.MATIERES


class Base(unittest.TestCase):
    def setUp(self):
        dossier = tempfile.TemporaryDirectory()
        self.addCleanup(dossier.cleanup)
        self.racine = Path(dossier.name)
        # Miroir : seuls les noms comptent.
        for document in ("Year 2/Algebre/Chp 1 : Intro.docx", "Year 2/Algebre/td.pdf",
                         "Year 2/Algebre/Projet 2025[1].pdf", "Year 4/SHS/rendu perso.docx",
                         unicodedata.normalize("NFD", "Year 1/Contrôles.pdf")):
            self.ecrire(f"{M}/{document}", "")
        # Notes converties : le champ source simplifie les espaces et retire « : ».
        self.ecrire(f"{N}/Year 2/Algebre/Chp 1 - Intro.md",
                    '---\ngenere: true\nsource: "Year 2/Algebre/Chp 1 : Intro.docx"\n---\n')
        self.ecrire(f"{N}/Year 2/Algebre/Chp 2.md",
                    '---\ngenere: true\nsource: "Year 2/Algebre/Chp 2.docx"\n---\n')
        self.ecrire(f"{N}/Year 4/SHS/rendu perso.md",
                    '---\ngenere: true\nsource: "Year 4/SHS/rendu perso.docx"\n---\n')
        self.ecrire(f"{MAT}/Algebre/Séance 1 - Intro (résumé).md",
                    '---\nsources: ["[[Chp 1 - Intro]]"]\n---\nRésumé de [[Chp 1 - Intro]].\n')
        self.ecrire(f"{MAT}/SHS/Recherches (résumé).md",
                    '---\nsources: ["Note d\'origine dans Cours/Year 4/SHS"]\n---\nTexte.\n')
        self.ecrire(f"{MAT}/Algebre/Projet retiré (résumé).md",
                    '---\nsources: ["[[Projet retiré]]"]\n---\nRésumé de [[Projet retiré]].\n')
        self.correspondances = {"Recherches (résumé)": f"{N}/Year 4/SHS/rendu perso"}

    def ecrire(self, relatif, texte):
        f = self.racine / relatif
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(texte, encoding="utf-8")

    def lire(self, relatif):
        return (self.racine / relatif).read_text(encoding="utf-8")

    def migrer(self, *options, correspondances=True):
        fichier = self.racine.parent / f"{self.racine.name}.tsv"
        fichier.write_text("".join(f"{k}\t{v}\n" for k, v in self.correspondances.items()),
                           encoding="utf-8")
        self.addCleanup(fichier.unlink, missing_ok=True)
        sortie, erreurs = io.StringIO(), io.StringIO()
        arguments = ["--coffre", str(self.racine), "--nouveau-miroir", NOUVEAU, *options]
        if correspondances:
            arguments += ["--correspondances", str(fichier)]
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreurs):
            code = migrer.main(arguments)
        self.sortie, self.erreurs = sortie.getvalue(), erreurs.getvalue()
        return code

    def page(self, texte, nom=f"{chemins.CONCEPTS}/Page.md"):
        self.ecrire(nom, texte)
        self.assertEqual(self.migrer(), 0, self.erreurs)
        return self.lire(nom)


class TestLiensVersLesNotes(Base):
    def test_vers_la_fiche_en_gardant_le_texte_affiche(self):
        self.assertEqual(
            self.page("[[Chp 1 - Intro]], [[Chp 1 - Intro|le chapitre]], "
                      f"[[{N}/Year 2/Algebre/Chp 1 - Intro|chp1 (Algebre)]]\n"),
            "[[Séance 1 - Intro (résumé)|Chp 1 - Intro]], [[Séance 1 - Intro (résumé)|le chapitre]], "
            "[[Séance 1 - Intro (résumé)|chp1 (Algebre)]]\n")

    def test_dans_un_tableau_la_barre_est_echappee(self):
        self.assertEqual(self.page("| [[Chp 1 - Intro]] | [[Chp 1 - Intro\\|x]] |\n"),
                         "| [[Séance 1 - Intro (résumé)\\|Chp 1 - Intro]] | [[Séance 1 - Intro (résumé)\\|x]] |\n")

    def test_ancre_retiree(self):
        self.assertEqual(self.page("[[Chp 1 - Intro#Partie 2|partie 2]]\n"),
                         "[[Séance 1 - Intro (résumé)|partie 2]]\n")

    def test_la_fiche_lie_son_document(self):
        texte = self.lire_apres_migration(f"{MAT}/Algebre/Séance 1 - Intro (résumé).md")
        lien = f"[[{NOUVEAU}/Year 2/Algebre/Chp 1 : Intro.docx|Chp 1 - Intro]]"
        self.assertEqual(texte, f'---\nsources: ["{lien}"]\n---\nRésumé de {lien}.\n')

    def lire_apres_migration(self, relatif):
        self.assertEqual(self.migrer(), 0, self.erreurs)
        return self.lire(relatif)

    def test_correspondance_remplace_sources_en_texte(self):
        texte = self.lire_apres_migration(f"{MAT}/SHS/Recherches (résumé).md")
        self.assertIn(f'sources: ["[[{NOUVEAU}/Year 4/SHS/rendu perso.docx|Recherches]]"]', texte)

    def test_note_sans_fiche_laissee(self):
        self.assertEqual(self.page("[[Chp 2]]\n"), "[[Chp 2]]\n")
        self.assertIn("note sans fiche, laissée : 1", self.sortie)

    def test_lien_casse_vers_une_note_retiree(self):
        self.assertEqual(self.page(f"[[Projet retiré]] et [[{N}/Year 1/Projet retiré|le projet]]\n"),
                         "[[Projet retiré (résumé)|Projet retiré]] et [[Projet retiré (résumé)|le projet]]\n")
        self.assertEqual(self.lire(f"{MAT}/Algebre/Projet retiré (résumé).md"),
                         '---\nsources: ["Projet retiré"]\n---\nRésumé de Projet retiré.\n')

    def test_code_titres_et_autres_liens_intacts(self):
        texte = ("`[[ c && c ]]` [[#Year 2|Year 2]] [[Autre page]] ![[image.png]]\n"
                 "```\n[[Chp 1 - Intro]]\n```\n")
        self.assertEqual(self.page(texte), texte)


class TestMentionsDuMiroir(Base):
    def test_yaml_et_accents_graves_deviennent_des_liens(self):
        texte = self.page(f'---\nsources: ["{M}/Year 2/Algebre/td.pdf"]\n---\nVoir (`{M}/Year 2/Algebre/td.pdf`).\n')
        lien = f"[[{NOUVEAU}/Year 2/Algebre/td.pdf|td.pdf]]"
        self.assertEqual(texte, f'---\nsources: ["{lien}"]\n---\nVoir ({lien}).\n')

    def test_dans_un_tableau(self):
        self.assertEqual(self.page(f"| `{M}/Year 2/Algebre/td.pdf` |\n"),
                         f"| [[{NOUVEAU}/Year 2/Algebre/td.pdf\\|td.pdf]] |\n")

    def test_dossier_et_texte_courant_changent_de_prefixe(self):
        self.assertEqual(self.page(f'"PDF du brief, dans {M}/Year 2/Algebre" et `{M}/` et `{M}/Year 2`\n'),
                         f'"PDF du brief, dans {NOUVEAU}/Year 2/Algebre" et `{NOUVEAU}/` et `{NOUVEAU}/Year 2`\n')

    def test_nom_avec_crochets_reste_en_texte(self):
        self.assertEqual(self.page(f'"{M}/Year 2/Algebre/Projet 2025[1].pdf"\n'),
                         f'"{NOUVEAU}/Year 2/Algebre/Projet 2025[1].pdf"\n')

    def test_nom_decompose_lie_avec_le_nom_du_disque(self):
        texte = self.page(f"`{M}/Year 1/Contrôles.pdf`\n")
        disque = unicodedata.normalize("NFD", "Contrôles.pdf")
        self.assertEqual(texte, f"[[{NOUVEAU}/Year 1/{disque}|{disque}]]\n")

    def test_journal_garde_ses_mentions_mais_pas_ses_liens(self):
        journal = f"{chemins.SUIVI}/log.md"
        self.assertEqual(self.page(f"Miroir dans {M}/ ; [[Chp 1 - Intro]]\n", journal),
                         f"Miroir dans {M}/ ; [[Séance 1 - Intro (résumé)|Chp 1 - Intro]]\n")


class TestCommande(Base):
    def test_essai_n_ecrit_rien(self):
        self.ecrire(f"{chemins.CONCEPTS}/Page.md", "[[Chp 1 - Intro]]\n")
        self.assertEqual(self.migrer("--essai"), 0)
        # La page, les deux fiches qui lient leur note, celle de la note retirée.
        self.assertIn("Pages à modifier : 4", self.sortie)
        self.assertEqual(self.lire(f"{chemins.CONCEPTS}/Page.md"), "[[Chp 1 - Intro]]\n")

    def test_relancer_ne_change_plus_rien(self):
        self.ecrire(f"{chemins.CONCEPTS}/Page.md", f"[[Chp 1 - Intro]] `{M}/Year 2/Algebre/td.pdf`\n")
        self.assertEqual(self.migrer(), 0)
        self.assertEqual(self.migrer(), 0)
        self.assertIn("Pages modifiées : 0", self.sortie)

    def test_correspondance_introuvable_arrete_tout(self):
        self.correspondances["Absente (résumé)"] = f"{N}/nulle part"
        self.ecrire(f"{chemins.CONCEPTS}/Page.md", "[[Chp 1 - Intro]]\n")
        self.assertEqual(self.migrer(), 1)
        self.assertIn("correspondance introuvable", self.erreurs)
        self.assertEqual(self.lire(f"{chemins.CONCEPTS}/Page.md"), "[[Chp 1 - Intro]]\n")

    def test_mesure_avant_et_apres(self):
        self.ecrire(f"{chemins.CONCEPTS}/Page.md", f"[[Chp 1 - Intro]] [[Absente]] `{M}/Year 2/Algebre/td.pdf`\n")
        self.migrer("--mesurer")
        self.assertIn(f"lien → {N} : 3", self.sortie)  # la page, sources et texte de la fiche
        self.assertIn("cassés : 3", self.sortie)  # Absente, et Projet retiré deux fois
        self.assertIn(f"mentions {M}/ : 1", self.sortie)
        self.migrer()
        self.migrer("--mesurer")
        self.assertNotIn(f"lien → {N}", self.sortie)
        # sources et texte de la fiche, sources de la correspondance, td.pdf de la page
        self.assertIn(f"lien → {NOUVEAU} : 4", self.sortie)
        self.assertIn("cassés : 1", self.sortie)
        self.assertIn(f"mentions {M}/ : 0", self.sortie)


if __name__ == "__main__":
    unittest.main()
