def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'column':

		for i in range(len(matrix[0])):
			total = 0
			for j in range(len(matrix)):
				total += matrix[j][i]
			means.append(total/len(matrix))
		
	if mode == 'row':
		for i in range(len(matrix)):
			total = 0
			for j in range(len(matrix[i])):
				total += matrix[i][j]
			means.append(total/len(matrix[i]))	

			


	
	
	
	
	return means

