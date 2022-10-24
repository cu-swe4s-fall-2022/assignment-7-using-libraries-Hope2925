# remember to import your libraries!
import numpy as np
import pandas as pd
import random
import sys
sys.path.append("./tests/")


def get_random_matrix(num_rows, num_columns):
    """
    This function will create an return an N(rows) by M(col)
    matrix of random floating point numbers sampled from a uniform
    distribution with a range of (0,1] (inclusive of 1)
    Parameters:
        - num_rows: integer desired # rows, must be > 0
        - num_columns: integer desired # columns, must be > 0
    Returns:
        - 2D numpy array [rows][columns]
    """
    # check that input is greater than 0
    if (num_rows > 0 and num_columns > 0):
        # since normally [low, high) do 0.00000001 & 1.00000001 for range
        low, high = 0.00000001, 1.00000001
        uniform_matrix = np.random.uniform(low=low,
                                           high=high,
                                           size=(num_rows, num_columns))
    else:
        raise ValueError("# of cols & rows must be an int > 0")
    return uniform_matrix


def get_file_dimensions(file_name):
    """
    This function takes in the name of a comma separated value (csv)
    file, reads in the file, and returns the dimensions of the tabular data
    (rows, columns).
    Parameters:
        file_name: string of a csv file to check dimensions of
    Returns:
        tuple of file dimensions (#rows, #cols)
    """
    # open file
    f = open(file_name, 'r')
    # start count
    num_rows = 0
    fin_num_cols = 0
    for line in f:
        # get the # cols for first line (if empty would be 0)
        num_cols = len(line.split(sep=","))
        # if not an empty line
        if (num_cols > 1):
            # add 1 to count for each line
            num_rows += 1
            # get final # rows
            fin_num_cols = num_cols
        else:
            print("row", num_rows, "is not comma separated")
    # close file
    f.close()
    if fin_num_cols == 0:
        raise Exception("Unless there is 1 col, file is not comma separated")
    return (num_rows, fin_num_cols)


def write_matrix_to_file(num_rows, num_columns, file_name):
    """
    This function takes the number of desired rows and columns, and
    writes matrix of that size of random numbers from a uniform
    distribution within range (0, 1] and then writes it to a
    csv file.
    Parameters
        - num_rows: # of rows, integer > 0
        - num_columns: # of columns, integer > 0
        - file_name: name of a csv file to save the matrix in
            - (must end in .csv)
    Returns:
        - outputs a file of the given file name with the
            created matrix in csv form
    """
    # make an exception if file name does not end with csv
    file_name_split = file_name.split(sep=".")
    if file_name_split[len(file_name_split)-1] != "csv":
        # if not then add & raise exception to warn user
        file_name = file_name + ".csv"
        raise Exception("Original name did not end in csv so adding it")
    # make appropriately sized matrix
    matrix_to_write = get_random_matrix(num_rows, num_columns)
    # write matrix to file as csv
    np.savetxt(file_name, matrix_to_write, delimiter=',')
    return None
