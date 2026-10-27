import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row = len(a) 
	col = len(a[0])
	if row*col != new_shape[0]*new_shape[1]:
		return []
	a = np.array(a)

	a = a.reshape(new_shape)

	b = a.tolist()

	return b
