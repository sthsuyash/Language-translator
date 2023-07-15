import unittest
from translator import *


class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertTrue(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        self.assertTrue(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
