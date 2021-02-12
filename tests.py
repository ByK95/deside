import unittest
from app import Parser, FileReader, Cls

class TestStringMethods(unittest.TestCase):

    def test_parrents(self):
        text = FileReader.read("./tests.py")
        refs = Parser.parse(text)
        self.assertEqual(refs[3].parents, ['Primary', 'Secondary'], "Should be equal")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class Primary():
    pass

class Secondary():
    pass

class Multiple(Primary, Secondary):
    pass

if __name__ == '__main__':
    unittest.main()