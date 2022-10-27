import unittest
import ex1
from datetime import datetime


class TestMain(unittest.TestCase):
    print('test')

    def test_hello_morning(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(ex1.bonjour(date), 'Allez on se réveille !')

    def test_hello_moon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(ex1.bonjour(date), 'Bonjour !')

    def test_hello_afternoon(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(ex1.bonjour(date), 'Bonsoir !')

    def test_goodbye_morning(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(ex1.aurevoir(date), 'On retourne se coucher !')

    def test_goodbye_moon(self):
        date = datetime.now().replace(hour=14)
        self.assertEqual(ex1.aurevoir(date), 'Bonne journée !')

    def test_goodbye_afternoon(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(ex1.aurevoir(date), 'Bonne soirée !')

    def test_mirror_true(self):
        self.assertEqual(ex1.miror('kayak'), 'kayak')

    def test_mirror_false(self):
        self.assertEqual(ex1.miror('test'), 'tset')





if __name__ == '__main__':
    unittest.main()