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
        - filename: desired file name to save plot as
    Returns:
        - png format of boxplot with file name
    """
    # plot a boxplot using built in pandas method
    #   this method automatically ignores nonquantitative columns
    df.boxplot(grid=False)
    # add y labels
    plt.ylabel(ylabel)
    if file_name:
        # save figure
        plt.savefig(file_name)



def dfscatterer(df, file_name, x, y, subset):
    """
    This function makes a scatter plot between x and y (columns)
    in the dataframe df, with colored subsets of column subset.
    This plot is saved as file_name.
    Parameters:
        - df: dataframe with columns appropriately labeled
        - file_name: string file name as png
        - x & y: column names or indexes of dataframe df
            - columns must be of integers or floats
        - subset: column name or index by which the scatters
            of x and y should be labeled
    Returns:
        - png file of labeled scatterplot between x and y
    """
    # make a new figure
    fig = plt.figure()
    # iterate through species to have diff colors for each subset
    for subset_name in set(df[subset]):
        # make scatterplot of only things in that subset
        df_subset = df[df[subset] == subset_name]
        plt.scatter(df_subset[x], df_subset[y],
                    label=subset_name)
    # add legend and labels
    plt.legend()
    plt.xlabel(x)
    plt.ylabel(y)
    # save figure
    plt.savefig(file_name)

def main():
    # get dataframe data from iris
    file_name = "./tests/iris.data"
    iris_df = pd.read_csv(file_name, delimiter=",", header=None)
    # add column names
    iris_df.columns = ["sepal_width", "sepal_length",
                      "petal_width", "petal_length",
                      "Iris_species"]
    # remove the top and right borders
    # make figure with subplots side by side (1 row 2 cols)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(12, 6)
    # make boxplot
    iris_df.boxplot(grid=False, ax=ax1)
    ax1.set_ylabel("cm")

    # iterate through species to have diff colors for each subset
    for subset_name in set(iris_df["Iris_species"]):
        # make scatterplot of only things in that subset
        df_subset = iris_df[iris_df["Iris_species"] == subset_name]
        ax2.scatter(df_subset["petal_length"], df_subset["petal_width"],
                    label=subset_name)
    # add legend and labels
    ax2.legend()
    ax2.set_xlabel("petal_length")
    ax2.set_ylabel("petal_width")

    # remove right and top spines of both axes
    for ax in (ax1, ax2):
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

    # save the figure
    plt.savefig("test_combined.png")


if __name__ == "__main__":
    main()

