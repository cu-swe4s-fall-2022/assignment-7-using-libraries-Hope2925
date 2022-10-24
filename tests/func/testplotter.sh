test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../..
pwd
# test runs without error
run basic_main python plotter.py --png_name ./tests/func/test_combined.png
# sys.exit should lead to 0
assert_exit_code 0
