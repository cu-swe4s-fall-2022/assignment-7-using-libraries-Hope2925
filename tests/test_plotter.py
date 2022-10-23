import unittest
import sys
sys.path.append("..")
import unittest
import pandas as pd
import plotter as pl
from os import path
import matplotlib.pyplot as plt

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get dataframe
        cls.df = pd.read_csv("iris.data", delimiter=",", header=None)
        # add column names
        cls.df.columns = ["sepal_width", "sepal_length",
                          "petal_width", "petal_length",
                          "Iris_species"]
        # choose x for scatter
        # choose y for scatter


    @classmethod
    def tearDownClass(cls):
        cls.df = None

    def test_dfboxplotter(self):
        # assert file is produced with proper name
        written_file_name = 'test_boxplot.png'
        pl.dfboxplotter(self.df, "cm", written_file_name)
        # confirm path created for file with appropriate name in same folder
        self.assertEqual(path.exists(written_file_name), True)
        # confirm file is actually a file
        self.assertEqual(path.isfile(written_file_name), True)
    #def test_dfscatterer(self):


if __name__ == '__main__':
    unittest.main()
