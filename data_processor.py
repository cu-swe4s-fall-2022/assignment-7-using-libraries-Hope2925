# remember to import your libraries!
import numpy as np
import random


def get_random_matrix(num_rows, num_columns):
	"""
	This function will create an return an N(rows) by M(col)
	matrix of random floating point numbers sampled from a uniform
	distribution with a range of (0,1] (inclusive of 1)
	Parameters:
		- num_rows: integer desired # rows
		- num_columns: integer desired # columns
	Returns:
		- 2D numpy array [rows][columns]
	"""
	# since normally [low, high) need to do 0.00000001 & 1.00000001 for range
	low, high = 0.00000001, 1.00000001
	uniform_matrix = np.random.uniform(low=low,
									high=high,
									size=(num_rows, num_columns))
	return uniform_matrix

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
