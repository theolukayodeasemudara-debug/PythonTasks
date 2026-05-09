from unittest import TestCase

import discount_calculator

class Discount_Calculator_App(TestCase):
    
    def test_that_function_exists(self):
        self.assertTrue(callable(discount_calculator.ten_off_discount))
        self.assertTrue(callable(discount_calculator.fifty_off_discount))
