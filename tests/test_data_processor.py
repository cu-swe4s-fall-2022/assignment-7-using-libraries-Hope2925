import sys
sys.path.append("../")
import unittest
import data_processor as dp
import random


class MyTestCase(unittest.TestCase):
    def test_get_random_matrix(self):
        # ensure the correct # rows & # columns are used
        num_rows = random.randint(1, 30)
        num_cols = random.randint(1, 30)
        self.assertEqual(dp.get_random_matrix(num_rows, num_cols).shape,
                         (num_rows, num_cols))
        # ensure all values are above 0 and can include 1 but not higher
        for rownum in range(num_rows):
            for colnum in range(num_cols):
                self.assertTrue(0 <
                    dp.get_random_matrix(num_rows, num_cols)[rownum][colnum]
                    <= 1)


if __name__ == '__main__':
    unittest.main()
