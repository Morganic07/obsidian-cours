import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import chemins
import convertir
import transcrire

ICI = Path(__file__).resolve().parent


class TestChemins(unittest.TestCase):
    def test_noms_valides(self):
        # maj.sh lance rclone sync sur le miroir : un nom vide ou un chemin ferait
        # d'un autre dossier, voire de la racine du coffre, la cible de la synchronisation.
        for nom in chemins.NOMS:
            valeur = getattr(chemins, nom)
            self.assertTrue(valeur, nom)
            self.assertNotIn("/", valeur, nom)
            self.assertNotIn(valeur, (".", ".."), nom)

    def test_lecture_par_maj_sh(self):
        sortie = subprocess.run([sys.executable, str(ICI / "chemins.py"), "MIROIR"],
                                capture_output=True, text=True, check=True).stdout
        self.assertEqual(sortie.strip(), chemins.MIROIR)

    def test_nom_inconnu_refuse(self):
        resultat = subprocess.run([sys.executable, str(ICI / "chemins.py"), "INCONNU"],
                                  capture_output=True, text=True)
        self.assertEqual(resultat.returncode, 2)
        self.assertEqual(resultat.stdout, "")

    def test_convertir_suit_un_renommage(self):
        with mock.patch.object(chemins, "NOTES", "Autres notes"):
            note = convertir.chemin_note(Path("/coffre"), Path("Year 1/Maths/Chp 1.docx"))
        self.assertEqual(note, Path("/coffre/Autres notes/Year 1/Maths/Chp 1.md"))

    def test_transcrire_suit_un_renommage(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(chemins, "NOTES", "Autres notes"), \
                mock.patch.object(chemins, "TRANSCRIPTIONS", "_tr"):
            coffre = Path(d)
            (coffre / "_tr").mkdir()
            (coffre / "_tr" / chemins.A_FAIRE).write_text(
                "e1\tAutres notes/Year 1/Maths/medias/a.png\n"
                "e2\tAutres notes/Year 2/OS/medias/b.png\n", encoding="utf-8")
            restantes = transcrire.lire_a_faire(coffre, "Year 1/Maths")
        self.assertEqual(restantes, [("e1", "Autres notes/Year 1/Maths/medias/a.png")])


if __name__ == "__main__":
    unittest.main()
