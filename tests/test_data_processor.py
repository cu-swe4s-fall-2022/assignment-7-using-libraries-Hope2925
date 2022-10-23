import sys
sys.path.append("..")
from os import path
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
        cls.num_rows = None
        cls.num_cols = None
        cls.iris_file_name = None
        cls.tbd_file_name = None

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

    def test_write_matrix_to_file(self):
        written_file_name = 'written_file.csv'
        dp.write_matrix_to_file(self.num_rows, self.num_cols, written_file_name)
        # confirm path created for file with appropriate name in same folder
        self.assertEqual(path.exists(written_file_name), True)
        # confirm file is actually a file
        self.assertEqual(path.isfile(written_file_name), True)
        # confirm file made contains appropriate # dimensions (& csv file)
        self.assertEqual(dp.get_file_dimensions(written_file_name), (self.num_rows, self.num_cols))
        # raises error if file name does not end with csv
        self.assertRaises(Exception, dp.write_matrix_to_file, 1, 2, "nocsv.txt")

if __name__ == '__main__':
    unittest.main()
