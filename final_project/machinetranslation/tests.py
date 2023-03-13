import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertTrue('Hello', 'Bonjour')
        self.assertTrue('Bye', 'Au revoir')
        self.assertIsNotNone(self)

    def test_french_to_english(self):
        self.assertTrue('Bonjour', 'Hello')
        self.assertTrue('Au revoir', 'Bye')
        self.assertIsNotNone(self)

    unittest.main()
