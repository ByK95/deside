import unittest
from app import Parser, FileReader, Cls

class TestStringMethods(unittest.TestCase):
    test_file = "./sample.py"

    def test_parents(self):
        text = FileReader.read(self.test_file)
        refs = Parser.parse(text)
        self.assertEqual(refs["Multiple"].parents, ['Primary', 'Secondary'], "Should be equal")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()