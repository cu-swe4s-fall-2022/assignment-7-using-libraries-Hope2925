import unittest
import sys
sys.path.append("..")
import unittest
import pandas as pd
import plotter as pl
from os import path

class MyTestCase(unittest.TestCase):
    def setUpClass(cls):
        # get dataframe
        cls.df = pd.read_csv("iris.data", delimiter=",")
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
        self.assertEqual(True, False)
    #def test_dfscatterer(self):


if __name__ == '__main__':
    unittest.main()
