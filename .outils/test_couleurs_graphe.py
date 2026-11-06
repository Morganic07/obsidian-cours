import json
import tempfile
import unittest
from pathlib import Path

import couleurs_graphe as cg


class TestCouleursGraphe(unittest.TestCase):
    def test_garde_les_autres_reglages(self):
        with tempfile.TemporaryDirectory() as d:
            chemin = Path(d) / "graph.json"
            chemin.write_text(json.dumps({"search": "path:Concepts", "colorGroups": [{"query": "x"}]}))
            cg.appliquer("annee", chemin)
            reglages = json.loads(chemin.read_text())
            self.assertEqual(reglages["search"], "path:Concepts")
            self.assertEqual(reglages["colorGroups"][1],
                             {"query": "tag:#year1", "color": {"a": 1, "rgb": 0x59A14F}})
            self.assertEqual(len(reglages["colorGroups"]), len(cg.JEUX["annee"]))

    def test_chaque_jeu_distingue_les_cartes_en_premier(self):
        # Une carte porte des tags d'année : si sa ligne venait après, elle prendrait la couleur d'une année.
        for jeu, lignes in cg.JEUX.items():
            if not lignes:
                continue
            requetes = [r for r, _ in lignes]
            self.assertIn('file:"(matière)"', requetes, jeu)
            avant = requetes[:requetes.index('file:"(matière)"')]
            self.assertFalse([r for r in avant if r.startswith("tag:")], jeu)

    def test_aucune_vide_les_couleurs(self):
        with tempfile.TemporaryDirectory() as d:
            chemin = Path(d) / "graph.json"
            chemin.write_text("{}")
            cg.appliquer("aucune", chemin)
            self.assertEqual(json.loads(chemin.read_text())["colorGroups"], [])

    def test_couleurs_des_jeux_valides(self):
        for jeu in cg.JEUX:
            for groupe in cg.groupes(jeu):
                self.assertLessEqual(groupe["color"]["rgb"], 0xFFFFFF)

    def test_couleur_invalide_refusee(self):
        cg.JEUX["essai"] = [("path:x", "#12")]
        try:
            with self.assertRaises(ValueError):
                cg.groupes("essai")
        finally:
            del cg.JEUX["essai"]

    def test_jeu_inconnu(self):
        self.assertEqual(cg.main(["inconnu"]), 1)


if __name__ == "__main__":
    unittest.main()
