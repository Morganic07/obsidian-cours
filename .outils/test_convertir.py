import base64
import contextlib
import io
import re
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

import chemins
import convertir

DESSIN_GROUPE = (
    '<w:p><w:r><w:rPr/><mc:AlternateContent><mc:Choice Requires="wpg"><w:drawing>'
    '<wp:inline><wp:extent cx="100" cy="100"/><wp:docPr id="1" name=""/><a:graphic>'
    '<a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup">'
    '<wpg:wgp><pic:pic><pic:nvPicPr><pic:cNvPr id="2" name="Shape 2"/><pic:cNvPicPr/></pic:nvPicPr>'
    '<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
    '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm>'
    '<a:prstGeom prst="rect"/></pic:spPr></pic:pic>'
    '<wps:wsp><wps:txbx><w:txbxContent><w:p><w:r><w:t>Annotation</w:t></w:r></w:p>'
    '<w:p><w:r><w:t xml:space="preserve">   </w:t></w:r></w:p></w:txbxContent></wps:txbx></wps:wsp>'
    '<wps:wsp><wps:txbx><w:txbxContent><w:p><w:r><w:t>Seconde boite</w:t></w:r>'
    '<w:r><w:rPr><w:vertAlign w:val="superscript"/></w:rPr><w:t>2</w:t></w:r></w:p>'
    '</w:txbxContent></wps:txbx></wps:wsp></wpg:wgp></a:graphicData></a:graphic></wp:inline>'
    '</w:drawing></mc:Choice><mc:Fallback><w:p><w:r><w:t>repli</w:t></w:r></w:p></mc:Fallback>'
    '</mc:AlternateContent></w:r></w:p>'
)

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

    def test_bloc_de_code_dans_un_callout_protege(self):
        texte = "> ```\n> $ form $1\n> ```"
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


def fabriquer_docx(cible, markdown, dossier):
    """Produit un vrai .docx avec pandoc, à partir de Markdown pouvant citer pixel.png."""
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "pixel.png").write_bytes(PNG)
    (dossier / "s.md").write_text(markdown, encoding="utf-8")
    cible.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pandoc", "s.md", "-o", str(cible)], cwd=dossier, check=True)


class TestConceptsPresents(unittest.TestCase):
    CONCEPTS = [("Matrice", ["Matrice", "matrices"], []),
                ("Mémoire", ["Mémoire", "memory"], ["Operating System"])]

    def test_variantes_et_restriction_par_matiere(self):
        texte = "Des matrices et de la memory."
        self.assertEqual(convertir.concepts_presents(texte, self.CONCEPTS, "Year 2/Algebre/c.docx"),
                         ["Matrice"])
        self.assertEqual(
            convertir.concepts_presents(texte, self.CONCEPTS, "Year 2/Operating System/c.docx"),
            ["Matrice", "Mémoire"])

    def test_liens_deja_presents_et_images_ignores(self):
        texte = "![[conversions/01/nouveau/Matrice.png]] et [[Matrice]]"
        self.assertEqual(convertir.concepts_presents(texte, self.CONCEPTS, "c.docx"), [])


class TestBoutEnBout(unittest.TestCase):
    """Passe par le vrai pandoc et le vrai filtre boites.lua."""

    def setUp(self):
        dossier = tempfile.TemporaryDirectory()
        self.addCleanup(dossier.cleanup)
        racine = Path(dossier.name)
        self.coffre = racine / "coffre"
        (self.coffre / chemins.TRANSCRIPTIONS).mkdir(parents=True)
        self.source = racine / "miroir" / "Year 2" / "Algebre " / "Chp 1 : Intro.docx"
        self.fabrique = racine / "fabrique"
        fabriquer_docx(self.source, SOURCE_MD, self.fabrique)

    def test_conversion(self):
        corps, images = convertir.convertir_docx(self.source, "conversions/01/nouveau")
        self.assertNotIn("<table", corps)
        self.assertIn("> [!note]", corps)
        self.assertIn("| une matrice |", corps)
        self.assertNotIn("[[Matrice", corps, "plus aucun lien automatique")
        # Le nom de l'image dépend de ce qui a produit le docx : on le lit dans le texte.
        image = re.search(r"!\[\[conversions/01/nouveau/([^\]]+\.png)\]\]", corps)
        self.assertIsNotNone(image)
        self.assertEqual(images, {image[1]: PNG})

    def test_empreintes_des_images(self):
        empreintes = convertir.empreintes_images({"image1.png": PNG}, "b")
        self.assertEqual(list(empreintes), ["b/image1.png"])
        self.assertEqual(len(empreintes["b/image1.png"]), 64)

    def test_lire_insere_les_transcriptions(self):
        empreinte = next(iter(convertir.empreintes_images({"x": PNG}, "b").values()))
        (self.coffre / chemins.TRANSCRIPTIONS / f"{empreinte}.md").write_text(
            "texte lu", encoding="utf-8")
        texte = convertir.lire(self.source, self.coffre)
        self.assertIn("> texte lu", texte)

    def test_commande_affiche_sans_rien_ecrire(self):
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            code = convertir.main([str(self.source), "--coffre", str(self.coffre)])
        self.assertEqual(code, 0)
        self.assertIn("# Chapitre", sortie.getvalue())
        self.assertEqual([p.name for p in self.coffre.iterdir()], [chemins.TRANSCRIPTIONS])

    def test_commande_extrait_les_images_hors_du_coffre(self):
        dossier = self.coffre.parent / "images"
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            code = convertir.main([str(self.source), "--coffre", str(self.coffre),
                                   "--images", str(dossier)])
        self.assertEqual(code, 0)
        nom = re.search(r"!\[\[images/([^\]]+)\]\]", sortie.getvalue())[1]
        self.assertEqual((dossier / nom).read_bytes(), PNG)

    def test_commande_refuse_des_images_dans_le_coffre(self):
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            code = convertir.main([str(self.source), "--coffre", str(self.coffre),
                                   "--images", str(self.coffre / "img")])
        self.assertEqual(code, 2)
        self.assertFalse((self.coffre / "img").exists())

    def test_commande_refuse_autre_chose_qu_un_docx(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(convertir.main([str(self.fabrique / "s.md")]), 2)
            self.assertEqual(convertir.main([str(self.fabrique / "absent.docx")]), 2)

    def test_docx_illisible(self):
        self.source.write_bytes(b"pas un docx")
        with self.assertRaises(subprocess.CalledProcessError):
            convertir.convertir_docx(self.source, "b")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(convertir.main([str(self.source), "--coffre", str(self.coffre)]), 1)

    def ajouter_dessin_groupe(self):
        """Ajoute au docx un dessin construit comme ceux qu'exporte Google Docs."""
        with zipfile.ZipFile(self.source) as z:
            contenu = {n: z.read(n) for n in z.namelist()}
        xml = contenu["word/document.xml"].decode("utf-8")
        rid = re.search(r'r:embed="([^"]+)"', xml)[1]
        for prefixe, uri in {
            "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
            "wpg": "http://schemas.microsoft.com/office/word/2010/wordprocessingGroup",
            "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
            "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
            "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
            "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        }.items():
            if f"xmlns:{prefixe}=" not in xml:
                xml = xml.replace("<w:document ", f'<w:document xmlns:{prefixe}="{uri}" ', 1)
        dessin = DESSIN_GROUPE.format(rid=rid)
        contenu["word/document.xml"] = xml.replace("<w:sectPr", f"{dessin}<w:sectPr", 1).encode("utf-8")
        with zipfile.ZipFile(self.source, "w") as z:
            for nom, octets in contenu.items():
                z.writestr(nom, octets)

    def test_dessin_groupe_garde_son_image_et_son_texte(self):
        self.ajouter_dessin_groupe()
        texte, _ = convertir.convertir_docx(self.source, "b")
        ligne = next(l for l in texte.splitlines() if "Texte du dessin" in l)
        self.assertIn("Texte du dessin : Annotation ; Seconde boite<sup>2</sup>", ligne)
        self.assertEqual(texte.count("![["), 2)
        self.assertNotIn("repli", texte)

    def test_crochet_dans_le_texte_alternatif(self):
        cible = self.source.parent / "Alt.docx"
        fabriquer_docx(cible, "![a\\]b](pixel.png)\n", self.fabrique)
        texte, _ = convertir.convertir_docx(cible, "b")
        self.assertNotIn("m/media/", texte)
        self.assertRegex(texte, r"!\[\[b/[^\]]+\.png\]\]")



if __name__ == "__main__":
    unittest.main()
