import unittest

"""
Count names with more than seven letters
"""

def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return more_than_seven


class TestNamesMethod(unittest.TestCase):

    def setUp(self):
        self.prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandra"]

    def test_prenoms(self):
        self.assertEqual(names(self.prenoms), 4)

    def test_vide(self):
        self.assertEqual(names([]), 0)

    def test_court(self):
        self.assertEqual(names(["Lea", "Leo",]), 0)

    def test_long(self):
        self.assertEqual(names(["Alexandre", "Cassandra", "Guillaume"]), 3)

    def test_limites(self):
        self.assertEqual(names(["12345678"]), 1)
        self.assertEqual(names(["1234567"]), 0)

if __name__ == "__main__":
    unittest.main()