import unittest

import requested_amount as ra

class TestRequestedAmount(unittest.TestCase):
    def test_modifier(self):
        cases = [
            (-100000.0, 0),
            (0.0, 0),
            (100000.0, 5)
        ]

        for row in cases:
            got = ra.modifier(row[0])
            self.assertEqual(got, row[1], "error with {0}".format(row[0]))


if __name__ == "__main__":
    unittest.main()