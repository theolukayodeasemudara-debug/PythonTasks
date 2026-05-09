from unittest import TestCase

import fahrenheit_converter

class Fahrenheit_Converter_Test_App(TestCase):

    def test_that_function_exists(self):
        self.assertTrue(callable(fahrenheit_converter.fah_converter))
        self.assertTrue(callable(fahrenheit_converter.cel_converter))
        
        
    def test_that_function_converts_to_celsius(self):
        actual = fahrenheit_converter.cel_converter(20)
        expected = -6.67
        self.assertEqual(actual, expected)
        
    def test_that_function_converts_to_fahrenheit(self):
        actual = fahrenheit_converter.fah_converter(20)
        expected = 68.0
        self.assertEqual(actual, expected)
