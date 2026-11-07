import contextlib
import hashlib
import io
import json
import shutil
import subprocess
import tempfile
import unicodedata
import unittest
from pathlib import Path

import chemins
import maj
from test_convertir import PNG, fabriquer_docx

M = chemins.MIROIR


def faux_rclone(drive, appels=None, code=0):
    """Imite rclone sync --backup-dir entre deux dossiers locaux : la version remplacée ou
    supprimée part dans le dossier de sauvegarde, au même chemin relatif."""

    def lancer(commande, journal):
        if appels is not None:
            appels.append(commande)
        if code:
            return code
        assert commande[:3] == ["rclone", "sync", maj.DRIVE], commande
        miroir = Path(commande[3])
        sauvegarde = Path(commande[commande.index("--backup-dir") + 1])
        for f in sorted(miroir.rglob("*")):
            if not f.is_file():
                continue
            relatif = f.relative_to(miroir)
            source = drive / relatif
            if not source.is_file() or source.read_bytes() != f.read_bytes():
                cible = sauvegarde / relatif
                cible.parent.mkdir(parents=True, exist_ok=True)
                f.replace(cible)
        for s in sorted(drive.rglob("*")):
            cible = miroir / s.relative_to(drive)
            if s.is_file() and not cible.exists():
                cible.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(s, cible)
        return 0

    return lancer


def transcrit(image, modele):
    return "texte de l'image"


class Base(unittest.TestCase):
    def setUp(self):
        dossier = tempfile.TemporaryDirectory()
        self.addCleanup(dossier.cleanup)
        self.racine = Path(dossier.name)
        self.coffre = self.racine / "coffre"
        self.travail = self.racine / "travail"
        self.drive = self.racine / "drive"
        self.fabrique = self.racine / "fabrique"
        self.ecrire(f"{chemins.CONCEPTS}/Matrice.md",
                    "---\naliases: [matrices]\n---\nVoir [[Chp 1]].\n")
        self.ecrire(f"{chemins.MATIERES}/Algebre/Chp 1.md",
                    f'---\ntype: source\nsources: ["[[{M}/Year 2/Algebre/Chp 1.docx|Chp 1.docx]]"]\n---\nFiche.\n')
        self.ecrire(f"{chemins.MATIERES}/Vieux/old.md",
                    f'---\nsources:\n  - "[[{M}/Year 1/Vieux/old.docx|old.docx]]"\n---\nFiche.\n')
        self.ecrire(f"{chemins.MATIERES}/Vieux/_index.md", "- [[old|old]]\n")
        self.docx("Year 2/Algebre/Chp 1.docx", "Une matrice simple.\n\n![](pixel.png)\n")
        self.docx("Year 2/Algebre/Chp 2.docx", "Deuxième chapitre.\n")
        self.docx("Year 1/Vieux/old.docx", "Ancien cours.\n")
        # État de départ : le miroir est à jour.
        faux_rclone(self.drive)(["rclone", "sync", maj.DRIVE, str(self.coffre / M),
                                 "--backup-dir", str(self.racine / "jeter")], None)
        self.wiki_avant = self.etat_du_wiki()

    def ecrire(self, relatif, texte):
        f = self.coffre / relatif
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(texte, encoding="utf-8")

    def docx(self, relatif, markdown):
        fabriquer_docx(self.drive / relatif, markdown, self.fabrique)

    def etat_du_wiki(self):
        return {p.relative_to(self.coffre).as_posix(): p.read_bytes()
                for p in sorted(self.coffre.rglob("*"))
                if p.is_file() and p.relative_to(self.coffre).parts[0] not in (M, chemins.TRANSCRIPTIONS)}

    def lancer(self, *options, lancer=None, appel=transcrit):
        sortie, erreurs = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreurs):
            code = maj.main(["--coffre", str(self.coffre), "--travail", str(self.travail), *options],
                            lancer=lancer or faux_rclone(self.drive), appel=appel)
        self.sortie, self.erreurs = sortie.getvalue(), erreurs.getvalue()
        return code

    def lot(self, debut):
        trouves = [f for f in (self.travail / maj.LOT).iterdir() if f.name.startswith(debut)]
        self.assertEqual(len(trouves), 1, debut)
        return trouves[0].read_text(encoding="utf-8")

    def changer_drive(self):
        self.docx("Year 2/Algebre/Chp 1.docx", "Une matrice modifiée.\n\n![](pixel.png)\n")
        (self.drive / "Year 1/Vieux/old.docx").unlink()
        self.docx("Year 2/Algebre/Chp 3.docx", "Troisième chapitre.\n")
        archive = self.drive / "Year 2/Algebre/Archive"
        archive.mkdir()
        (self.drive / "Year 2/Algebre/Chp 2.docx").rename(archive / "Chp 2.docx")


class TestLot(Base):
    def setUp(self):
        super().setUp()
        self.changer_drive()
        self.assertEqual(self.lancer(), 0, self.erreurs)

    def test_modifie_avec_diff_fiche_annee_concepts_et_transcription(self):
        texte = self.lot("03 - Chp 1")
        self.assertIn("- État : modifié", texte)
        self.assertIn("-Une matrice simple.", texte)
        self.assertIn("+Une matrice modifiée.", texte)
        self.assertIn(f"Fiche existante : `{chemins.MATIERES}/Algebre/Chp 1.md`", texte)
        self.assertIn("Année : year2", texte)
        self.assertIn("Concepts existants repérés : Matrice", texte)
        self.assertIn("> texte de l'image", texte)
        self.assertIn(f"`[[{M}/Year 2/Algebre/Chp 1.docx|Chp 1.docx]]`", texte)

    def test_supprime_signale_sans_rien_supprimer(self):
        texte = self.lot("01 - old")
        self.assertIn("- État : supprimé", texte)
        self.assertIn(f"`{chemins.MATIERES}/Vieux/old.md`", texte)
        self.assertIn(f"`{chemins.MATIERES}/Vieux/_index.md`", texte)
        self.assertIn("## Texte de la version supprimée", texte)
        self.assertIn("Ancien cours.", texte)
        self.assertEqual(self.etat_du_wiki(), self.wiki_avant)

    def test_deplace_reconnu_par_son_contenu(self):
        texte = self.lot("02 - Chp 2")
        self.assertIn(f"- État : déplacé (ancien chemin : `{M}/Year 2/Algebre/Chp 2.docx`)", texte)
        self.assertNotIn("## Texte converti", texte)

    def test_ajoute_sans_fiche_avec_dossier_probable(self):
        texte = self.lot("04 - Chp 3")
        self.assertIn("- État : ajouté", texte)
        self.assertIn("Fiche existante : aucune", texte)
        self.assertIn(f"Dossier de fiches probable : `{chemins.MATIERES}/Algebre/`", texte)
        self.assertIn("Troisième chapitre.", texte)

    def test_bilan_et_transcription_ecrite(self):
        bilan = (self.travail / maj.LOT / maj.BILAN).read_text(encoding="utf-8")
        self.assertIn("4 documents : ajoutés 1, modifiés 1, déplacés 1, supprimés 1.", bilan)
        self.assertIn("Images sans transcription : 0.", bilan)
        transcriptions = list((self.coffre / chemins.TRANSCRIPTIONS).glob("*.md"))
        self.assertEqual(len(transcriptions), 1)

    def test_wiki_jamais_modifie(self):
        self.assertEqual(self.etat_du_wiki(), self.wiki_avant)

    def test_second_lot_refuse_sans_contacter_drive(self):
        appels = []
        self.assertEqual(self.lancer(lancer=faux_rclone(self.drive, appels)), 3)
        self.assertEqual(appels, [])
        self.assertIn("pas clos", self.erreurs)

    def test_reprendre_redonne_le_meme_lot(self):
        avant = {f.name: f.read_bytes() for f in (self.travail / maj.LOT).iterdir()}
        appels = []
        self.assertEqual(self.lancer("--reprendre", lancer=faux_rclone(self.drive, appels)), 0)
        self.assertEqual(appels, [])
        self.assertEqual({f.name: f.read_bytes() for f in (self.travail / maj.LOT).iterdir()}, avant)

    def test_clore_puis_aucun_changement(self):
        self.assertEqual(self.lancer("--clore"), 0)
        self.assertFalse(self.travail.exists())
        self.assertEqual(self.lancer(), 0)
        self.assertIn("Aucun changement", self.sortie)
        self.assertFalse(self.travail.exists())


class TestCas(Base):
    def test_au_dela_du_seuil_attend_l_accord(self):
        self.changer_drive()
        vues = []
        self.assertEqual(self.lancer("--seuil", "0", appel=lambda i, m: vues.append(i) or "x"), 4)
        self.assertEqual(vues, [])
        self.assertFalse((self.travail / maj.LOT).exists())
        self.assertEqual(self.lancer("--reprendre", "--sans-transcrire"), 0)
        self.assertIn("1 sans transcription", self.lot("03 - Chp 1"))

    def test_echec_de_rclone_puis_nouvel_essai(self):
        self.changer_drive()
        self.assertEqual(self.lancer(lancer=faux_rclone(self.drive, code=1)), 1)
        self.assertIn("rclone a échoué", self.erreurs)
        self.assertFalse((self.travail / maj.RCLONE_OK).exists())
        avant = (self.travail / maj.AVANT).read_bytes()
        self.assertEqual(self.lancer(), 0, self.erreurs)
        self.assertEqual((self.travail / maj.AVANT).read_bytes(), avant)
        self.assertIn("4 documents", (self.travail / maj.LOT / maj.BILAN).read_text(encoding="utf-8"))

    def test_reprendre_sans_lot(self):
        self.assertEqual(self.lancer("--reprendre"), 1)
        self.assertIn("aucun lot ouvert", self.erreurs)

    def test_clore_refuse_un_dossier_inattendu(self):
        self.travail.mkdir()
        (self.travail / "a moi.txt").write_text("x", encoding="utf-8")
        self.assertEqual(self.lancer("--clore"), 1)
        self.assertTrue((self.travail / "a moi.txt").exists())

    def test_travail_dans_le_coffre_refuse(self):
        sortie = io.StringIO()
        with contextlib.redirect_stderr(sortie):
            code = maj.main(["--coffre", str(self.coffre), "--travail", str(self.coffre / "x")],
                            lancer=faux_rclone(self.drive))
        self.assertEqual(code, 1)
        self.assertFalse((self.coffre / "x").exists())

    def test_pdf_illisible_et_presentation(self):
        (self.drive / "Year 2/Algebre/td.pdf").write_bytes(b"pas un pdf")
        (self.drive / "Year 2/Algebre/slides.pptx").write_bytes(b"pptx")
        self.assertEqual(self.lancer(), 1)
        self.assertIn("Échec de conversion de la nouvelle version", self.lot("02 - td"))
        self.assertIn("Présentation : pas de conversion", self.lot("01 - slides"))
        self.assertIn("échec de conversion", (self.travail / maj.LOT / maj.BILAN).read_text(encoding="utf-8"))

    def test_image_remplacee_signalee_meme_sans_changement_de_texte(self):
        self.fabrique.mkdir(exist_ok=True)
        autre = self.racine / "autre"
        autre.mkdir()
        # Même texte, même nom d'image dans le docx, contenu d'image différent.
        (autre / "pixel.png").write_bytes(PNG + b"\x00autre")
        (autre / "s.md").write_text("Une matrice simple.\n\n![](pixel.png)\n", encoding="utf-8")
        subprocess.run(["pandoc", "s.md", "-o", str(self.drive / "Year 2/Algebre/Chp 1.docx")],
                       cwd=autre, check=True)
        self.assertEqual(self.lancer(), 0, self.erreurs)
        texte = self.lot("01 - Chp 1")
        # Les images étant comparées par leur contenu, le remplacement apparaît dans les
        # changements, à sa place dans le texte, et dans la liste des images à recopier.
        ancienne = hashlib.sha256(PNG).hexdigest()[:maj.EMPREINTE_COURTE]
        nouvelle = hashlib.sha256(PNG + b"\x00autre").hexdigest()[:maj.EMPREINTE_COURTE]
        self.assertIn(f"-![[image {ancienne}]]", texte)
        self.assertIn(f"+![[image {nouvelle}]]", texte)
        self.assertRegex(texte, rf"Images nouvelles ou remplacées .*\(image {nouvelle}\)")
        # Sans copie dans la fiche, le lot le dit.
        self.assertIn(f"image {ancienne} → aucune copie", texte)

    def test_image_remplacee_retrouve_sa_copie_dans_la_fiche(self):
        # La fiche a copié l'image sous un ancien numéro ; seul le contenu l'y relie.
        images = self.coffre / chemins.MATIERES / "Algebre" / "images"
        images.mkdir()
        (images / "Chp 1 - image7.png").write_bytes(PNG)
        (images / "Autre fiche - image7.png").write_bytes(PNG)
        autre = self.racine / "autre"
        autre.mkdir()
        (autre / "pixel.png").write_bytes(PNG + b"\x00autre")
        (autre / "s.md").write_text("Une matrice simple.\n\n![](pixel.png)\n", encoding="utf-8")
        subprocess.run(["pandoc", "s.md", "-o", str(self.drive / "Year 2/Algebre/Chp 1.docx")],
                       cwd=autre, check=True)
        self.assertEqual(self.lancer(), 0, self.erreurs)
        ancienne = hashlib.sha256(PNG).hexdigest()[:maj.EMPREINTE_COURTE]
        self.assertIn(f"image {ancienne} → `Chp 1 - image7.png`", self.lot("01 - Chp 1"))

    def test_supprime_sans_fiche_signale_les_pages_qui_le_citent(self):
        self.ecrire(f"{chemins.MATIERES}/Algebre/_index.md",
                    f"Voir `{M}/Year 2/Algebre/Chp 2.docx`.\n")
        (self.drive / "Year 2/Algebre/Chp 2.docx").unlink()
        self.assertEqual(self.lancer(), 0, self.erreurs)
        texte = self.lot("01 - Chp 2")
        self.assertIn("Fiche existante : aucune", texte)
        self.assertIn(f"Pages qui citent l'ancien chemin : `{chemins.MATIERES}/Algebre/_index.md`",
                      texte)

    def test_carte_qui_cite_le_document_n_est_pas_une_fiche(self):
        # Les fiches n'ont plus de suffixe : seules les cartes sont écartées, par leur nom
        # « _index » ou leur type matiere.
        source = f'sources: ["[[{M}/Year 2/Algebre/Chp 2.docx|Chp 2.docx]]"]'
        self.ecrire(f"{chemins.MATIERES}/Algebre/_index.md", f"---\n{source}\n---\n")
        self.ecrire(f"{chemins.MATIERES}/Algebre/Carte.md", f"---\ntype: matiere\n{source}\n---\n")
        self.docx("Year 2/Algebre/Chp 2.docx", "Deuxième chapitre modifié.\n")
        self.assertEqual(self.lancer(), 0, self.erreurs)
        self.assertIn("Fiche existante : aucune", self.lot("01 - Chp 2"))

    def test_nom_decompose_sur_drive_retrouve_sa_fiche(self):
        # Cas réel : « Contrôles.pdf » arrive de Drive en Unicode décomposé (NFD).
        nfd = unicodedata.normalize("NFD", "Contrôles.docx")
        self.docx(f"Year 2/Algebre/{nfd}", "Version 1.\n")
        faux_rclone(self.drive)(["rclone", "sync", maj.DRIVE, str(self.coffre / M),
                                 "--backup-dir", str(self.racine / "jeter")], None)
        self.ecrire(f"{chemins.MATIERES}/Algebre/Contrôles.md",
                    f'---\nsources: ["[[{M}/Year 2/Algebre/Contrôles.docx|Contrôles.docx]]"]\n---\n')
        self.docx(f"Year 2/Algebre/{nfd}", "Version 2.\n")
        self.assertEqual(self.lancer(), 0, self.erreurs)
        self.assertIn(f"Fiche existante : `{chemins.MATIERES}/Algebre/Contrôles.md`",
                      unicodedata.normalize("NFC", self.lot("01 - Contro")))

    def test_images_renumerotees_par_google_ne_sont_pas_des_changements(self):
        # Cas réel (Chp1 - intro to data mining) : un mot ajouté, et Google a renuméroté
        # toutes les images du document, sans en changer le contenu.
        self.docx("Year 2/Algebre/Chp 1.docx", "Version modifiée.\n")
        self.assertEqual(self.lancer(), 0, self.erreurs)
        conversions = self.travail / maj.CONVERSIONS / "01"
        for version, texte, noms in (
                ("ancien", "Texte de départ.", {"image1.png": b"X", "image2.png": b"Y"}),
                ("nouveau", "Texte de départ, complété.", {"image2.png": b"X", "image1.png": b"Y"})):
            dossier = conversions / version
            for f in dossier.iterdir():
                f.unlink()
            base = f"{maj.CONVERSIONS}/01/{version}"
            ordre = "\n\n".join(f"![[{base}/{n}]]" for n in noms)
            (dossier / maj.TEXTE).write_text(f"{texte}\n\n{ordre}\n", encoding="utf-8")
            for nom, octets in noms.items():
                (dossier / nom).write_bytes(octets)
        maj.ecrire_lot(self.coffre, self.travail)
        texte = self.lot("01 - Chp 1")
        diff = texte.split("```diff")[1].split("```")[0]
        self.assertIn("-Texte de départ.", diff)
        self.assertIn("+Texte de départ, complété.", diff)
        changees = [l for l in diff.splitlines()[2:] if l[:1] in "+-" and "image" in l]
        self.assertEqual(changees, [])
        self.assertNotIn("Images nouvelles ou remplacées", texte)

    def test_fiche_qui_cite_seulement_le_dossier_signalee(self):
        # Cas réel : les PDF de « Projet courts » portent le nom de tiers, la fiche ne
        # cite que leur dossier.
        self.ecrire(f"{chemins.MATIERES}/Algebre/Brief.md",
                    f'---\nsources: ["PDF du brief, dans {M}/Year 2/Algebre"]\n---\n')
        self.docx("Year 2/Algebre/Brief - Prénom Nom.docx", "Brief.\n")
        self.assertEqual(self.lancer(), 0, self.erreurs)
        texte = self.lot("01 - Brief")
        self.assertIn("Fiche existante : aucune", texte)
        self.assertIn(f"citent son dossier sans le lier (peut-être la sienne) : "
                      f"`{chemins.MATIERES}/Algebre/Brief.md`", texte)
        self.assertNotIn("Algebre/Chp 1.md", texte.split("Fiches qui citent")[1].split("\n")[0])

    def test_tableau_reste_en_html_signale(self):
        # Cas réel (« Cours 1 et 2 : Database ») : plusieurs lignes d'en-tête, que pandoc
        # garde en HTML. Pandoc ne sait pas écrire un tel docx : on place directement le
        # résultat de la conversion, puis on réécrit le lot.
        self.docx("Year 2/Algebre/Chp 3.docx", "Tableau.\n")
        self.assertEqual(self.lancer(), 0, self.erreurs)
        conversion = self.travail / maj.CONVERSIONS / "01" / "nouveau" / maj.TEXTE
        conversion.write_text("<table><tr><th>a</th></tr></table>\n", encoding="utf-8")
        maj.ecrire_lot(self.coffre, self.travail)
        self.assertIn("Tableau resté en HTML", self.lot("01 - Chp 3"))

    def test_transcription_existante_reutilisee(self):
        self.changer_drive()
        self.assertEqual(self.lancer(), 0)
        self.assertEqual(self.lancer("--clore"), 0)
        self.docx("Year 2/Algebre/Chp 1.docx", "Encore une version.\n\n![](pixel.png)\n")
        vues = []
        self.assertEqual(self.lancer(appel=lambda i, m: vues.append(i) or "x"), 0)
        self.assertEqual(vues, [], "même image, même empreinte : rien à retranscrire")
        self.assertIn("> texte de l'image", self.lot("01 - Chp 1"))


class TestFonctions(unittest.TestCase):
    def test_comparer(self):
        avant = {"a": "1", "b": "2", "c": "3", "d": "4"}
        apres = {"a": "1", "b": "9", "x/c": "3", "e": "5"}
        self.assertEqual(maj.comparer(avant, apres), [
            {"etat": "modifié", "chemin": "b", "origine": None},
            {"etat": "supprimé", "chemin": "d", "origine": None},
            {"etat": "ajouté", "chemin": "e", "origine": None},
            {"etat": "déplacé", "chemin": "x/c", "origine": "c"},
        ])

    def test_contenu_identique_deux_fois_un_seul_deplacement(self):
        changements = maj.comparer({"a": "1"}, {"b": "1", "c": "1"})
        self.assertEqual([c["etat"] for c in changements], ["déplacé", "ajouté"])

    def test_verifier_travail(self):
        coffre = Path("/home/x/coffre")
        for refuse in ("/", str(Path.home()), str(Path.home().parent), "/home/x/coffre",
                       "/home/x/coffre/.cache", "/home/x"):
            with self.subTest(refuse), self.assertRaises(maj.Erreur):
                maj.verifier_travail(Path(refuse), coffre)
        self.assertEqual(maj.verifier_travail(Path("/tmp/travail"), coffre), Path("/tmp/travail").resolve())

    def test_cible_des_sources(self):
        self.assertEqual(maj.cible(f"[[{M}/Year 1/a.docx|a.docx]]"), f"{M}/Year 1/a.docx")
        self.assertEqual(maj.cible(f"[[{M}/Year 1/a.docx\\|a.docx]]"), f"{M}/Year 1/a.docx")
        self.assertEqual(maj.cible(".raw/Year 1/b.pdf"), ".raw/Year 1/b.pdf")
        self.assertEqual(maj.cible("`.raw/c.pdf`"), ".raw/c.pdf")

    def test_annee(self):
        self.assertEqual(maj.annee("Year 3/SHS/a.docx"), "year3")
        self.assertTrue(maj.annee("Divers/a.docx").startswith("inconnue"))

    def test_bloc_plus_long_que_le_texte(self):
        self.assertTrue(maj.bloc("a ```` b", "diff").startswith("`````diff\n"))

    def test_changements_enregistres(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.json"
            maj.ecrire_json(f, [{"chemin": "Year 1/é\tx.docx"}])
            self.assertEqual(json.loads(f.read_text(encoding="utf-8")), [{"chemin": "Year 1/é\tx.docx"}])


if __name__ == "__main__":
    unittest.main()
