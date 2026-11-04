import base64
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import convertir

PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
)


def lie(texte, *concepts, chemin="Year 2/Algebre/cours.docx"):
    liste = [(nom, [nom, *variantes], matieres) for nom, variantes, matieres in concepts]
    return convertir.lier(texte, liste, chemin)


class TestLier(unittest.TestCase):
    def test_premiere_occurrence_seulement_et_texte_garde(self):
        self.assertEqual(
            lie("Les entropies et les entropies", ("Entropie", ["entropies"], [])),
            "Les [[Entropie|entropies]] et les entropies",
        )

    def test_nom_exact_sans_alias(self):
        self.assertEqual(lie("Une Matrice", ("Matrice", [], [])), "Une [[Matrice]]")

    def test_limites_de_mot(self):
        for texte in ("multilinear", "non-linear", "linear-map", "linearité"):
            self.assertEqual(lie(texte, ("linear", [], [])), texte)
        self.assertEqual(lie("l'entropie", ("entropie", [], [])), "l'[[entropie]]")

    def test_variante_la_plus_longue_prioritaire(self):
        resultat = lie(
            "une bilinear form",
            ("Forme", ["bilinear form"], []),
            ("Autre", ["form"], []),
        )
        self.assertEqual(resultat, "une [[Forme|bilinear form]]")

    def test_zones_protegees(self):
        for texte in (
            "$a + form$",
            "$$\nform\n$$",
            "`form`",
            "```\nform\n```",
            "![[Cours/form.png]]",
            "[[form]]",
            "![form](form.png)",
            "[form](https://exemple.fr)",
            "https://exemple.fr/form",
            '<img alt="form">',
            "## form",
            "> ## form",
            "> [!info]- form",
        ):
            with self.subTest(texte):
                self.assertEqual(lie(texte, ("form", [], [])), texte)

    def test_lien_dans_un_tableau_echappe_la_barre(self):
        self.assertEqual(
            lie("| une form | b |", ("Forme", ["form"], [])),
            r"| une [[Forme\|form]] | b |",
        )

    def test_restriction_par_matiere(self):
        concept = ("Mémoire", ["memory"], ["Operating System"])
        self.assertEqual(lie("memory", concept), "memory")
        self.assertEqual(
            lie("memory", concept, chemin="Year 2/Operating System/c.docx"),
            "[[Mémoire|memory]]",
        )

    def test_idempotent(self):
        concept = ("Forme", ["form"], [])
        une_fois = lie("une form et | form |", concept)
        self.assertEqual(lie(une_fois, concept), une_fois)

    def test_sans_concept(self):
        self.assertEqual(convertir.lier("texte", [], "a.docx"), "texte")


class TestFrontmatter(unittest.TestCase):
    def test_liste_en_ligne_commentaire_et_guillemets(self):
        texte = '---\naliases: [a b, "c, d"]   # note\nmatieres: Physique\n---\ncorps'
        self.assertEqual(
            convertir.lire_frontmatter(texte),
            {"aliases": ["a b", "c, d"], "matieres": ["Physique"]},
        )

    def test_diese_entre_guillemets_garde(self):
        texte = "---\nsource: \"Year 2/Exo #2 l'algo.docx\"\n---\n"
        self.assertEqual(
            convertir.lire_frontmatter(texte), {"source": ["Year 2/Exo #2 l'algo.docx"]}
        )

    def test_liste_en_blocs_ecrite_par_obsidian(self):
        texte = "---\naliases:\n  - a\n  - b\n---\n"
        self.assertEqual(convertir.lire_frontmatter(texte), {"aliases": ["a", "b"]})

    def test_sans_entete(self):
        self.assertEqual(convertir.lire_frontmatter("# titre\n"), {})


class TestNomSur(unittest.TestCase):
    def test_caracteres_refuses_par_obsidian(self):
        self.assertEqual(convertir.nom_sur("Chp 1 : Sample #2"), "Chp 1 - Sample - 2")

    def test_tabulations_et_sauts_de_ligne(self):
        self.assertEqual(convertir.nom_sur("\t\t\tReyou\n a\tb"), "Reyou a b")

    def test_espace_final(self):
        self.assertEqual(convertir.nom_sur("culture du soin "), "culture du soin")


class TestTranscriptions(unittest.TestCase):
    EMP = {"a.png": "h"}

    def test_sous_l_image(self):
        self.assertEqual(
            convertir.inserer_transcriptions("![[a.png]]\nsuite", self.EMP, {"h": "x = 1"}),
            "![[a.png]]\n\n"
            "> [!info]- Transcription (automatique, l'image fait foi)\n> x = 1\n\nsuite",
        )

    def test_dans_un_encadre_reste_dans_l_encadre(self):
        resultat = convertir.inserer_transcriptions("> ![[a.png]]", self.EMP, {"h": "x"})
        self.assertIn("> > [!info]-", resultat)
        self.assertIn("> > x", resultat)

    def test_cellule_de_tableau_renvoyee_apres_le_tableau(self):
        corps = "| ![[a.png]] |\n|---|\n| b |\nfin"
        lignes = convertir.inserer_transcriptions(corps, self.EMP, {"h": "x"}).split("\n")
        self.assertLess(lignes.index("| b |"), lignes.index("> x"))
        self.assertLess(lignes.index("> x"), lignes.index("fin"))

    def test_tableau_en_fin_de_note(self):
        resultat = convertir.inserer_transcriptions("| ![[a.png]] |", self.EMP, {"h": "x"})
        self.assertIn("> x", resultat)

    def test_transcription_vide_ou_absente(self):
        for textes in ({"h": "  \n"}, {}):
            self.assertEqual(
                convertir.inserer_transcriptions("![[a.png]]", self.EMP, textes), "![[a.png]]"
            )


SOURCE_MD = """# Chapitre

Une form ici.

| Encadré |
|---------|
| Dans la **boite** une matrice |

| Col A | Col B |
|-------|-------|
| une matrice | deux |

![](pixel.png)
"""


class TestBoutEnBout(unittest.TestCase):
    """Passe par le vrai pandoc et le vrai filtre boites.lua."""

    def setUp(self):
        dossier = tempfile.TemporaryDirectory()
        self.addCleanup(dossier.cleanup)
        racine = Path(dossier.name)
        self.miroir, self.coffre = racine / "miroir", racine / "coffre"
        (self.coffre / "Concepts").mkdir(parents=True)
        (self.coffre / "Concepts" / "Matrice.md").write_text("une matrice\n", encoding="utf-8")
        self.source = self.miroir / "Year 2" / "Algebre " / "Chp 1 : Intro.docx"
        self.source.parent.mkdir(parents=True)
        fabrique = racine / "fabrique"
        fabrique.mkdir()
        (fabrique / "pixel.png").write_bytes(PNG)
        (fabrique / "s.md").write_text(SOURCE_MD, encoding="utf-8")
        subprocess.run(
            ["pandoc", "s.md", "-o", str(self.source)], cwd=fabrique, check=True
        )
        self.note = self.coffre / "Cours" / "Year 2" / "Algebre" / "Chp 1 - Intro.md"

    def lancer(self, *options):
        return convertir.main(
            ["--miroir", str(self.miroir), "--coffre", str(self.coffre), *options]
        )

    def test_note_generee(self):
        self.assertEqual(self.lancer(), 0)
        texte = self.note.read_text(encoding="utf-8")
        self.assertTrue(texte.startswith("---\ngenere: true\n"))
        self.assertNotIn("<table", texte)
        self.assertIn("> [!note]", texte)
        self.assertIn("| une matrice |", texte.replace("[[", "").replace("]]", ""))
        self.assertEqual(texte.count("[[Matrice|matrice]]"), 1)
        # Le nom de l'image dépend de ce qui a produit le docx : on le lit dans la note.
        image = re.search(r"!\[\[(Cours/Year 2/Algebre/medias/Chp 1 - Intro/[^\]]+\.png)\]\]", texte)
        self.assertIsNotNone(image)
        self.assertEqual((self.coffre / image[1]).read_bytes(), PNG)

    def test_relancer_ne_change_rien(self):
        self.lancer()
        avant = self.note.read_bytes()
        date = self.note.stat().st_mtime_ns
        self.lancer()
        self.assertEqual(self.note.read_bytes(), avant)
        self.assertEqual(self.note.stat().st_mtime_ns, date)

    def test_transcription_appliquee_et_liee(self):
        self.lancer()
        a_faire = self.coffre / ".transcriptions" / "A_FAIRE.tsv"
        empreinte = a_faire.read_text(encoding="utf-8").split("\t")[0]
        (self.coffre / "Concepts" / "Pixel.md").write_text("", encoding="utf-8")
        (self.coffre / ".transcriptions" / f"{empreinte}.md").write_text(
            "un Pixel seul", encoding="utf-8"
        )
        self.lancer()
        texte = self.note.read_text(encoding="utf-8")
        self.assertIn("> un [[Pixel]] seul", texte)
        self.assertEqual(a_faire.read_text(encoding="utf-8"), "")

    def test_source_supprimee(self):
        self.lancer()
        perso = self.note.parent / "perso.md"
        perso.write_text("mes notes", encoding="utf-8")
        autre = self.source.parent / "Autre.docx"
        autre.write_bytes(self.source.read_bytes())
        self.source.unlink()
        self.assertEqual(self.lancer(), 0)
        self.assertFalse(self.note.exists())
        self.assertFalse((self.note.parent / "medias" / "Chp 1 - Intro").exists())
        self.assertTrue(perso.exists(), "une note non générée ne doit jamais être supprimée")

    def test_note_deplacee_arrete_tout_sans_rien_modifier(self):
        self.lancer()
        rangee = self.coffre / "Cours" / "Year 4" / "Chp 1 - Intro.md"
        rangee.parent.mkdir(parents=True)
        self.note.rename(rangee)
        contenu = rangee.read_bytes()
        for options in ((), ("--matiere", "Year 2")):
            with self.subTest(options):
                self.assertEqual(self.lancer(*options), 3)
                self.assertEqual(rangee.read_bytes(), contenu)
                self.assertFalse(self.note.exists(), "la note ne doit pas être régénérée")
        rangee.rename(self.note)
        self.assertEqual(self.lancer(), 0)

    def test_dossier_deplace_sur_drive(self):
        self.lancer()
        empreinte = (self.coffre / ".transcriptions" / "A_FAIRE.tsv").read_text(
            encoding="utf-8").split("\t")[0]
        (self.coffre / ".transcriptions" / f"{empreinte}.md").write_text("texte lu", encoding="utf-8")
        ancien_dossier = self.note.parent
        nouveau = self.miroir / "Year 4" / "Algebre "
        nouveau.parent.mkdir()
        self.source.parent.rename(nouveau)
        (self.miroir / "Year 2").rmdir()

        self.assertEqual(self.lancer(), 0)

        arrivee = self.coffre / "Cours" / "Year 4" / "Algebre" / self.note.name
        self.assertIn("> texte lu", arrivee.read_text(encoding="utf-8"))
        self.assertFalse(ancien_dossier.exists(), "l'ancien dossier ne doit pas rester vide")
        self.assertFalse(ancien_dossier.parent.exists())

    def test_filtre_matiere_ne_retire_rien(self):
        self.lancer()
        autre = self.miroir / "Year 3" / "Stats" / "a.docx"
        autre.parent.mkdir(parents=True)
        autre.write_bytes(self.source.read_bytes())
        self.assertEqual(self.lancer("--matiere", "Year 3/Stats"), 0)
        self.assertTrue(self.note.exists())

    def test_miroir_vide_ne_touche_a_rien(self):
        self.lancer()
        self.source.unlink()
        self.assertEqual(self.lancer(), 2)
        self.assertTrue(self.note.exists())

    def test_docx_illisible_signale_sans_perdre_la_note(self):
        self.lancer()
        self.source.write_bytes(b"pas un docx")
        self.assertEqual(self.lancer(), 1)
        self.assertTrue(self.note.exists())


if __name__ == "__main__":
    unittest.main()
