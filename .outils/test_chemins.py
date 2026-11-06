import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import chemins
import maj
import transcrire

ICI = Path(__file__).resolve().parent


class TestChemins(unittest.TestCase):
    def test_noms_valides(self):
        # maj.py lance rclone sync sur le miroir : un nom vide ou un chemin ferait
        # d'un autre dossier, voire de la racine du coffre, la cible de la synchronisation.
        for nom in chemins.NOMS:
            valeur = getattr(chemins, nom)
            self.assertTrue(valeur, nom)
            self.assertNotIn("/", valeur, nom)
            self.assertNotIn(valeur, (".", ".."), nom)

    def test_lecture_en_ligne_de_commande(self):
        sortie = subprocess.run([sys.executable, str(ICI / "chemins.py"), "MIROIR"],
                                capture_output=True, text=True, check=True).stdout
        self.assertEqual(sortie.strip(), chemins.MIROIR)

    def test_nom_inconnu_refuse(self):
        resultat = subprocess.run([sys.executable, str(ICI / "chemins.py"), "INCONNU"],
                                  capture_output=True, text=True)
        self.assertEqual(resultat.returncode, 2)
        self.assertEqual(resultat.stdout, "")

    def test_travail_hors_du_coffre_par_defaut(self):
        with mock.patch.dict(os.environ, {"MAJ_COURS_TRAVAIL": ""}):
            travail = chemins.travail()
        coffre = ICI.parent.resolve()
        self.assertNotIn(coffre, [travail.resolve(), *travail.resolve().parents])
        maj.verifier_travail(travail, coffre)

    def test_travail_remplace_par_la_variable(self):
        with mock.patch.dict(os.environ, {"MAJ_COURS_TRAVAIL": "/tmp/ailleurs"}):
            self.assertEqual(chemins.travail(), Path("/tmp/ailleurs"))

    def test_transcrire_suit_un_renommage(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(chemins, "TRANSCRIPTIONS", "_tr"), \
                mock.patch.object(chemins, "A_FAIRE", "liste.tsv"):
            coffre, travail = Path(d) / "coffre", Path(d) / "travail"
            (coffre / "_tr").mkdir(parents=True)
            travail.mkdir()
            (coffre / "_tr" / "e2.md").write_text("fait", encoding="utf-8")
            (travail / "liste.tsv").write_text(
                "e1\tconversions/01/nouveau/a.png\tYear 1/Maths/c.docx\n"
                "e2\tconversions/01/nouveau/b.png\tYear 1/Maths/c.docx\n", encoding="utf-8")
            restantes = transcrire.lire_a_faire(coffre, travail=travail)
        self.assertEqual(restantes, [("e1", "conversions/01/nouveau/a.png")])

    def lancer_recuperer(self, coffre, travail):
        vues = []

        def lancer(commande, journal):
            vues.append(commande)
            return 0

        maj.recuperer(coffre, travail, lancer)
        return vues

    def test_maj_suit_un_renommage_du_miroir(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(chemins, "MIROIR", "Autre miroir"):
            coffre, travail = Path(d) / "coffre", Path(d) / "travail"
            coffre.mkdir()
            commande = self.lancer_recuperer(coffre, travail)[0]
        self.assertEqual(commande[3], str(coffre / "Autre miroir"))

    def test_nom_de_miroir_invalide_arrete_avant_rclone(self):
        for valeur in ("", ".", "..", "a/b"):
            with self.subTest(valeur), tempfile.TemporaryDirectory() as d, \
                    mock.patch.object(chemins, "MIROIR", valeur):
                coffre = Path(d) / "coffre"
                coffre.mkdir()
                with self.assertRaises(maj.Erreur):
                    self.lancer_recuperer(coffre, Path(d) / "travail")
                self.assertEqual(list(coffre.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
