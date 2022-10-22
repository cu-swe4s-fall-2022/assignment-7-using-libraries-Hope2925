import sys
sys.path.append("../")
import unittest
import data_processor as dp
import random


class MyTestCase(unittest.TestCase):
    def test_get_random_matrix(self):
        # ensure the correct # rows & # columns are used
        num_rows = random.randint(0, 30)
        num_cols = random.randint(0, 30)
        self.assertEqual(dp.get_random_matrix(num_rows, num_cols).shape,
                         (num_rows, num_cols))


if __name__ == '__main__':
    unittest.main()
