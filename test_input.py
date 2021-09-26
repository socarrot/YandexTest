import unittest

import input
from gender import Gender
from income_source import IncomeSource
from purpose import Purpose
from config import Config
from validation import ValidationError

# Tests for input field variations
class TestInput(unittest.TestCase):
    def test_invalid(self):
        cases = [
            input.Input(17, Gender.F, IncomeSource.OWNER, 150000, 0, 100000, 5, Purpose.BUSINESS),
            input.Input(65, Gender.F, IncomeSource.PASSIVE, 500000, 1, 1000000, 15, Purpose.CONSUMER),
            input.Input(19, Gender.F, IncomeSource.PASSIVE, -10000000, 0, 1231231, 10, Purpose.CAR),
        ]

        for request in cases:
            self.assertRaises(ValidationError, request.validation)

    #
    def test_func_annual_payment(self):
        cases = [
            (100000, 1, 10, 110000),
            (100000, 10, 10, 20000),
            (1, 1, 1, 1),
            (1231231, 10, 4, 172372),
        ]

        for tc in cases:
            got = input.annual_payment(tc[0], tc[1], tc[2])
            self.assertEqual(got, tc[3], "row {0}".format(tc))

    def test_calculate_modifier(self):
        cases = [
            (input.Input(17, Gender.F, IncomeSource.OWNER, 150000, 0, 100000, 5, Purpose.BUSINESS), 4.75),
            (input.Input(65, Gender.F, IncomeSource.PASSIVE, 500000, 1, 1000000, 15, Purpose.CONSUMER), 5.75),
        ]

        for row in cases:
            self.assertEqual(row[0].calculate_modifier(), row[1])

    # Use the same values for testing as we use in the google sheets table
    def test_annual_payment(self):
        cases = [
            (input.Input(17, Gender.M, IncomeSource.UNEMPLOYED, 0, -2, 100000, 1, Purpose.CONSUMER), 0),
            (input.Input(18, Gender.M, IncomeSource.HIRED, 100000, -1, 555555, 5, Purpose.BUSINESS), 138918),
            (input.Input(19, Gender.M, IncomeSource.PASSIVE, 10000000, 0, 1231231, 10, Purpose.CAR), 144096),
            (input.Input(33, Gender.M, IncomeSource.OWNER, 50000000, 1, 3333333, 15, Purpose.BUSINESS), 321459),
            (input.Input(65, Gender.M, IncomeSource.PASSIVE, 5000000, 2, 10000000, 20, Purpose.MORTGAGE), 57500),
            (input.Input(17, Gender.F, IncomeSource.UNEMPLOYED, 0, -2, 100000, 1, Purpose.CONSUMER), 0),
            (input.Input(18, Gender.F, IncomeSource.HIRED, 100000, -1, 555555, 5, Purpose.BUSINESS), 138918),
            (input.Input(19, Gender.F, IncomeSource.PASSIVE, 10000000, 0, 1231231, 10, Purpose.CAR), 144096),
            (input.Input(33, Gender.F, IncomeSource.OWNER, 50000000, 1, 3333333, 15, Purpose.BUSINESS), 321459),
            (input.Input(60, Gender.F, IncomeSource.PASSIVE, 5000000, 2, 10000000, 20, Purpose.MORTGAGE), 57500),
        ]

        for row in cases:
            self.assertEqual(row[0].annual_payment(), row[1])


if __name__ == "__main__":
    unittest.main()
