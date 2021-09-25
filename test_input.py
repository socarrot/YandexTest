import unittest

import input
from gender import Gender
from income_source import IncomeSource
from purpose import Purpose
from config import Config
from validation import ValidationError

class TestInput(unittest.TestCase):
    def test_invalid(self):
        cases = [
            input.Input(17, Gender.F, IncomeSource.OWNER, 150000, 0, 100000, 5, Purpose.BUSINESS),
            input.Input(65, Gender.F, IncomeSource.PASSIVE, 500000, 1, 1000000, 15, Purpose.CONSUMER)
        ]

        for request in cases:
            self.assertRaises(ValidationError, request.validation)


# TODO check if annual payment is correct
    def test_func_annual_payment(self):
        cases = [
            (100000, 1, 10, 210000.0),
            (100000, 5, 10, 130000.0),
            (100000, 10, 10, 120000.0),
            (1, 1, 1, 2.01),
            (10, 1, 1, 20.099999999999998),
            (100, 1, 1, 200.99999999999997),
        ]

        for tc in cases:
            got = input.annual_payment(tc[0], tc[1], tc[2])
            self.assertEqual(tc[3], got)

    def test_percentage(self):
        cases = [
            (100, 5, 5),
            (1, 1, 0.01),
            (1, 100, 1),
            (100, 1, 1),
            (-100, 1, -1),
            (100, 0, 0),
            (0, 1, 0),
        ]

        for tc in cases:
            got = input.percentage(tc[0], tc[1])
            self.assertEqual(tc[2], got)

    def test_calculate_modifier(self):
        cases = [
            (input.Input(17, Gender.F, IncomeSource.OWNER, 150000, 0, 100000, 5, Purpose.BUSINESS), 10.25),
            (input.Input(65, Gender.F, IncomeSource.PASSIVE, 500000, 1, 1000000, 15, Purpose.CONSUMER), 10.5),
        ]

        for row in cases:
            self.assertEqual(row[0].calculate_modifier(), row[1])

    def test_annual_payment(self):
        cases = [
            (input.Input(18, Gender.F, IncomeSource.OWNER, 150000, 0, 100000, 5, Purpose.BUSINESS), 130250.0),
            (input.Input(65, Gender.F, IncomeSource.PASSIVE, 500000, 1, 1000000, 15, Purpose.CONSUMER), 1171666.6666666667),
        ]

        for row in cases:
            self.assertEqual(row[0].annual_payment(), row[1])

if __name__ == "__main__":
    unittest.main()