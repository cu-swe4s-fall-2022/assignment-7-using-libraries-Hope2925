import unittest
import sys
import unittest
import pandas as pd
from os import path
sys.path.append("../..")
import plotter as pl


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get dataframe
        cls.df = pd.read_csv("../iris.data", delimiter=",", header=None)
        # add column names
        cls.df.columns = ["sepal_width", "sepal_length",
                          "petal_width", "petal_length",
                          "Iris_species"]
        # choose x for scatter
        cls.x = "petal_width"
        # choose y for scatter
        cls.y = "petal_length"
        # choose subset
        cls.subset = 'Iris_species'

    @classmethod
    def tearDownClass(cls):
        cls.df = None

    def test_dfboxplotter(self):
        # assert file is produced with proper name
        written_file_name = 'test_boxplot.png'
        # make a figure
        pl.dfboxplotter(self.df, "cm", written_file_name)
        # confirm path created for file with appropriate name in same folder
        self.assertEqual(path.exists(written_file_name), True)
        # confirm file is actually a file
        self.assertEqual(path.isfile(written_file_name), True)

    def test_dfscatterer(self):
        written_file_name = 'test_scatter.png'
        pl.dfscatterer(self.df, written_file_name, self.x, self.y, self.subset)
        # confirm path created for file with appropriate name in same folder
        self.assertEqual(path.exists(written_file_name), True)
        # confirm file is actually a file
        self.assertEqual(path.isfile(written_file_name), True)


if __name__ == '__main__':
    unittest.main()
