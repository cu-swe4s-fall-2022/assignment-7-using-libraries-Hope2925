# Your code to create majestic plots goes in here!
# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dfboxplotter(df, ylabel, file_name):
    """
    This function takes in a dataframe and
    returns a boxplot of all columns that are
    quantitative with appropriate x and y labels.
    The x labels use the column names integrated into
    the dataframe.
    Parameters:
        - df: dataframe (pandas object) of data with columns to plot
        - ylabel: y axis label to plot (string)
        - xlabels: x labels to plot (list of column names)
        - filename: desired file name to save plot as
    Returns:
        - png format of boxplot with file name
    """
    # make a figure & axis
    fig = plt.figure()
    ax = fig.add_subplot()
    # plot a boxplot using built in pandas method
    #   this method automatically ignores nonquantitative columns
    ax = df.boxplot(grid=False)
    # add y labels
    ax.set_ylabel(ylabel)
    # save figure
    plt.savefig(file_name)



# def dfscatterer(df, file_name, x, y):
#     # something
#
# def multi_paneler(df, file_name):
#     """
#
#     :param df:
#     :param file_name:
#     :return:
#     """