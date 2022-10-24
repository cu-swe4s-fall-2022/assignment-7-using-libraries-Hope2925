. ssshtest

run outputcheck python func_dataprocessing.py --num_rows 3 --num_cols 5

# should make file of dimensions 3 & 3
assert_in_stdout "(3, 5)"
# sys.exit should be 0
assert_exit_code 0

run outputcheck python func_dataprocessing.py --num_rows 20 --num_cols 7

# should make file of dimensions 3 & 3
assert_in_stdout "(20, 7)"
# sys.exit should be 0
assert_exit_code 0

run outputcheck python func_dataprocessing.py --num_rows 0 --num_cols 5

# sys.exit should be 1
assert_exit_code 1

# delete made files
rm func.csv