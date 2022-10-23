import sys
sys.path.append("..")
import unittest
import data_processor as dp
import random

class TestUtils(unittest.TestCase):
    # set up shared data to test with
    @classmethod
    def setUpClass(cls):
        # random row & col numbers
        cls.num_rows = random.randint(1, 30)
        cls.num_cols = random.randint(1, 30)
        # iris data with known dimensions
        cls.iris_file_name = 'iris.data'
        # fake tab delimited file
        cls.tbd_file_name = "extbdfile.txt"


    @classmethod
    def tearDownClass(cls):
        cls.list_of_chars = None
        cls.list_of_ints = None
        cls.list_of_4ints = None
        cls.bin_list_of_chars = None
        cls.ins_bin_list_of_chars = None
        cls.bin_list_of_chars_rep = None

    def test_get_random_matrix(self):
        # ensure the correct # rows & # columns are used
        self.assertEqual(dp.get_random_matrix(self.num_rows,
                                              self.num_cols).shape,
                         (self.num_rows, self.num_cols))
        # ensure all values are above 0 and can include 1 but not higher
        for rownum in range(self.num_rows):
            for colnum in range(self.num_cols):
                self.assertTrue(0 <
                    dp.get_random_matrix(self.num_rows,
                                         self.num_cols)[rownum][colnum]
                    <= 1)
        # ensure raises error if use 0 in either
        self.assertRaises(ValueError, dp.get_random_matrix, 0, self.num_cols)
        self.assertRaises(ValueError, dp.get_random_matrix, self.num_rows, 0)

    def test_get_file_dimensions(self):
        # use iris data which should have 150 rows & 5 columns
        self.assertEqual(dp.get_file_dimensions(self.iris_file_name), (150, 5))
        # if not csv then raises exception
        self.assertRaises(Exception, dp.get_file_dimensions, self.tbd_file_name)


if __name__ == '__main__':
    unittest.main()
