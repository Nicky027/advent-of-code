from packets import compare, Outcome
import unittest


class TestCompare(unittest.TestCase):
    def test_numbers_lt(self):
        x = [1, 1, 3, 1, 1]
        y = [1, 1, 5, 1, 1]
        result = compare(x, y)
        self.assertEqual(result, Outcome.LESS_THAN)

    def test_numbers_gt(self):
        x = [1, 1, 5, 1, 1]
        y = [1, 1, 3, 1, 1]
        result = compare(x, y)
        self.assertEqual(result, Outcome.GREATER_THAN)

    def test_lists_lt(self):
        x = [1, [1, 2, 3]]
        y = [1, [1, 2, 4]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.LESS_THAN)

    def test_lists_gt(self):
        x = [1, [1, 2, 4]]
        y = [1, [1, 2, 3]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.GREATER_THAN)

    def test_number_list_lt(self):
        x = [[1], 2]
        y = [[1], [4, 5, 6]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.LESS_THAN)

    def test_number_list_gt(self):
        x = [[1], 5]
        y = [[1], [4, 5, 6]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.GREATER_THAN)

    def test_list_number_lt(self):
        x = [[1], [2, 3, 4]]
        y = [[1], 4]
        result = compare(x, y)
        self.assertEqual(result, Outcome.LESS_THAN)

    def test_list_number_gt(self):
        x = [[1], [5, 3, 4]]
        y = [[1], 4]
        result = compare(x, y)
        self.assertEqual(result, Outcome.GREATER_THAN)

    def test_list_less_elements_left(self):
        x = [[1], [5]]
        y = [[1], [5, 6, 7]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.LESS_THAN)

    def test_list_less_elements_right(self):
        x = [[1], [5, 6, 7]]
        y = [[1], [5]]
        result = compare(x, y)
        self.assertEqual(result, Outcome.GREATER_THAN)


if __name__ == "__main__":
    unittest.main()
