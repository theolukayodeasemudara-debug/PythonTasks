""" type annotation in python...
what's the command for testing in python
python3 -m unittest filename """


from unittest import TestCase
import pybank

class TestValidateEmail(TestCase):

    def test_that_validate_email_exists(self):
        pybank.validate_email("seun@funmi.com")

    def test_that_validate_email_length_is_minimum_of_8_characters(self):
        is_valid = pybank.validate_email("seun@funmi.com")
        self.assertTrue(is_valid)

    def test_that_valid_email_length_less_than_8_characters_return_false(self):
        is_valid = pybank.validate_email("se@fu.c")
        self.assertFalse(is_valid)

    def test_that_invalid_email_raise_value_error(self):
        self.assertRaises(ValueError, pybank.validate_email, "seunfunmi.com")

    def test_that_valid_email_contains_special_character(self):
        is_valid = pybank.validate_email("seun@funmi.com")
        self.assertTrue(is_valid)

    def test_that_valid_email_does_not_start_with_special_character(self):
        message = pybank.validate_email("@seunfunmi.com")
        self.assertEqual(message, "Invalid email")

    def test_that_valid_email_does_not_end_with_sepcial_character(self):
        message = pybank.validate_email("@seunfunmi.com@")
        self.assertEqual(message, "Invalid email")

class TestCalculateBalance(TestCase):

    def test_that_calculate_balance_function_return_correct_balance(self):
        actual = pybank.calculate_balance([2500, 2000])
        expected = 4500
        self.assertEqual(actual, expected)

        actual = pybank.calculate_balance([5000, 2000])
        expected = 7000
        self.assertEqual(actual, expected)
        
        actual = pybank.calculate_balance([5000, -1000, 2000, -500])
        expected = 5500
        self.assertEqual(actual, expected)
