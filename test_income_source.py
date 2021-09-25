import unittest

import income_source


class TestIncomeSource(unittest.TestCase):
    def test_modifier_ok(self):
        got = income_source.modifier(income_source.IncomeSource.PASSIVE)
        self.assertEqual(got, 0.5)

    def test_modifier_other(self):
        got = income_source.modifier(42)
        self.assertEqual(got, 0)

if __name__ == "__main__":
    unittest.main()