import unittest
from machinetranslation.translator import french_to_english, english_to_french
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(french_to_english(None)) # test when Null is entered, Should return None.
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test when "Bonjour" is entered should return "Hello"
        
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(english_to_french(None)) # test when Null is entered, Should None.
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test when "Hello" is entered should return "Bonjour"    

unittest.main()