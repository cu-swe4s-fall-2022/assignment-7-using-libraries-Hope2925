import sys
import data_processor as dp
import argparse

sys.path.append("../../")


def main():
    # will read arguments through command line
    parser = argparse.ArgumentParser()
    # add an argument
    parser.add_argument('--num_rows', dest='num_rows',
                        type=int, required=True)
    parser.add_argument('--num_cols', dest='num_cols',
                        type=int, required=True)
    # grab the arguments where arg is a dict
    arg = parser.parse_args()

    # basically run unit tests
    # use the write_matrix_to_file to test get random matrix
    dp.write_matrix_to_file(arg.num_rows, arg.num_cols, 'func.csv')
    # print the file dimensions
    print(dp.get_file_dimensions('func.csv'))


if __name__ == "__main__":
    main()
