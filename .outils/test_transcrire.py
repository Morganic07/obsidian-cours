import hashlib
import tempfile
import unittest
from pathlib import Path

import transcrire


class TestValider(unittest.TestCase):
    def test_texte_garde_avec_fin_de_ligne(self):
        self.assertEqual(transcrire.valider("  $x = 1$ \n"), "$x = 1$\n")

    def test_bloc_de_code_autour_retire(self):
        self.assertEqual(transcrire.valider("```markdown\n$x$\n```"), "$x$\n")

    def test_image_sans_contenu_donne_un_fichier_vide(self):
        self.assertEqual(transcrire.valider(transcrire.AUCUN_CONTENU), "")

    def test_refus(self):
        for reponse in ("", "   \n", "Voici la transcription : x", "Here is the text", "$x = 1"):
            with self.subTest(reponse), self.assertRaises(transcrire.EchecImage):
                transcrire.valider(reponse)

    def test_dollars_dans_le_code_ignores(self):
        for reponse in (
            "```\nmomo@penguin:~/awk$ awk '{print $1, $2}' food.csv\nbread 1.00\n```",
            "La commande `echo $HOME` affiche le dossier.",
            "```bash\n$ ls\n```\nPuis :\n```bash\n$ pwd $\n```",
        ):
            with self.subTest(reponse):
                self.assertEqual(transcrire.valider(reponse), reponse + "\n")

    def test_terminal_hors_bloc_de_code_refuse(self):
        for reponse in (
            "momo@penguin:~/wildcard_lab$ wc -l lab_output.txt\n2 lab_output.txt\nmomo@penguin:~$ ",
            "momo@penguin:~/awk$ awk '{print $1, $2}' food.csv",
        ):
            with self.subTest(reponse), self.assertRaises(transcrire.EchecImage):
                transcrire.valider(reponse)

    def test_terminal_dans_un_bloc_accepte(self):
        reponse = "Résultat :\n```\nuser@host:~$ ls\n```"
        self.assertEqual(transcrire.valider(reponse), reponse + "\n")

    def test_dollar_echappe_ignore(self):
        self.assertEqual(transcrire.valider(r"Prix : 5\$"), "Prix : 5\\$\n")


class TestTranscrire(unittest.TestCase):
    def setUp(self):
        dossier = tempfile.TemporaryDirectory()
        self.addCleanup(dossier.cleanup)
        self.coffre = Path(dossier.name)
        self.dossier = self.coffre / ".transcriptions"
        self.dossier.mkdir()
        lignes = []
        self.empreintes = {}
        for matiere, nom in (("Year 1/Maths", "a.png"), ("Year 1/Maths", "b.png"), ("Year 2/OS", "c.png")):
            image = self.coffre / "Cours" / matiere / "medias" / nom
            image.parent.mkdir(parents=True, exist_ok=True)
            image.write_bytes(nom.encode())
            empreinte = hashlib.sha256(nom.encode()).hexdigest()
            self.empreintes[nom] = empreinte
            lignes.append(f"{empreinte}\t{image.relative_to(self.coffre).as_posix()}\n")
        (self.dossier / "A_FAIRE.tsv").write_text("".join(lignes), encoding="utf-8")

    def fichier(self, nom):
        return self.dossier / f"{self.empreintes[nom]}.md"

    def test_transcrit_tout_et_ecrit_les_fichiers(self):
        resultat = transcrire.transcrire(self.coffre, appel=lambda image, modele: f"texte {image.name}")
        self.assertEqual(resultat, (3, [], None))
        self.assertEqual(self.fichier("a.png").read_text(encoding="utf-8"), "texte a.png\n")

    def test_filtre_matiere_et_limite(self):
        reussies, _, _ = transcrire.transcrire(
            self.coffre, "Year 1/Maths", limite=1, appel=lambda image, modele: "x"
        )
        self.assertEqual(reussies, 1)
        self.assertTrue(self.fichier("a.png").exists())
        self.assertFalse(self.fichier("b.png").exists())
        self.assertFalse(self.fichier("c.png").exists())

    def test_ne_refait_pas_ce_qui_existe(self):
        self.fichier("a.png").write_text("déjà fait", encoding="utf-8")
        vues = []

        def appel(image, modele):
            vues.append(image.name)
            return "x"

        transcrire.transcrire(self.coffre, appel=appel)
        self.assertEqual(vues, ["b.png", "c.png"])
        self.assertEqual(self.fichier("a.png").read_text(encoding="utf-8"), "déjà fait")

    def test_limite_d_usage_arrete_et_garde_le_travail(self):
        def appel(image, modele):
            if image.name == "b.png":
                raise transcrire.LimiteAtteinte("quota")
            return "x"

        reussies, _, arret = transcrire.transcrire(self.coffre, appel=appel)
        self.assertEqual(reussies, 1)
        self.assertIn("limite", arret)
        self.assertTrue(self.fichier("a.png").exists())
        self.assertFalse(self.fichier("b.png").exists())
        self.assertEqual(len(transcrire.lire_a_faire(self.coffre)), 2)

    def test_reponse_invalide_passe_a_la_suivante_sans_rien_ecrire(self):
        def appel(image, modele):
            return "$x" if image.name == "a.png" else "bon"

        reussies, echouees, arret = transcrire.transcrire(self.coffre, appel=appel)
        self.assertEqual((reussies, len(echouees), arret), (2, 1, None))
        self.assertFalse(self.fichier("a.png").exists())

    def test_trois_echecs_de_suite_arretent(self):
        def appel(image, modele):
            raise transcrire.EchecImage("panne")

        _, echouees, arret = transcrire.transcrire(self.coffre, appel=appel)
        self.assertEqual(len(echouees), 3)
        self.assertIn("de suite", arret)

    def test_image_changee_refusee(self):
        (self.coffre / "Cours/Year 1/Maths/medias/a.png").write_bytes(b"autre contenu")
        _, echouees, _ = transcrire.transcrire(self.coffre, appel=lambda image, modele: "x")
        self.assertIn("changée", echouees[0][1])
        self.assertFalse(self.fichier("a.png").exists())

    def test_aucun_fichier_temporaire_restant(self):
        transcrire.transcrire(self.coffre, appel=lambda image, modele: "x")
        self.assertEqual(list(self.dossier.glob(".*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
