def solve_system(matrix):
	if (len(matrix) != len(matrix[0]) - 1):
		raise ValueError("coeficent matrix isn't square")

	for i in range(len(matrix)):
		_make_column_zero(matrix,i)

	answers = [0 for i in range(len(matrix))]
	for i in range(len(matrix) - 1,-1,-1):
		answers[i] = _count_answer(matrix[i],i,answers)

	return answers





def _make_column_zero(matrix,column_number):
	leading_line = matrix[column_number]
	if leading_line[column_number] == 0:
		for i in range(column_number,len(matrix)):
			if matrix[i][column_number] != 0:
				leading_line = matrix[i]
				_swap_lines(matrix,column_number,i)
				break
	# case then whole column is zero already
		else:
			return

	for i in range(column_number + 1,len(matrix)):
		coefficient = -1 * matrix[i][column_number] / leading_line[column_number]
		for j in range(len(matrix[i])):
			matrix[i][j] += leading_line[j] * coefficient



def _swap_lines(matrix,a,b):
	buffer = matrix[a]
	matrix[a] = matrix[b]
	matrix[b] = buffer

def _count_answer(line,ansver_number,another_ansvers):
	first_part = line[-1]
	second_part = line[ansver_number]
	for i in range(ansver_number,len(another_ansvers)):
		first_part -= line[i] * another_ansvers[i]

	if first_part == 0 and second_part == 0:
		raise ValueError("system has infinity solutions")
	if first_part != 0 and second_part == 0:
		raise ValueError("line has no answer")
	return first_part/second_part

def count_determinate(matrix):
	line_moves = 0

	for i in range(len(matrix)):
		column_number = i

		leading_line = matrix[column_number]
		if leading_line[column_number] == 0:
			for j in range(column_number,len(matrix)):
				if matrix[j][column_number] != 0:
					line_moves += 1
					_swap_lines(matrix,column_number,j)
					leading_line = matrix[column_number]
					break
			else:
				return

		for k in range(column_number + 1,len(matrix)):
			coefficient = -1 * matrix[k][column_number] / leading_line[column_number]  
			for j in range(len(matrix[i])):
				matrix[k][j] += leading_line[j] * coefficient


	result = (-1)**line_moves
	for i in range(len(matrix)):
		result *= matrix[i][i]
	return result

def invert_matrix(matrix):
	# matrix check??

	#creating identiti matrix
	result_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
	for i in range(len(matrix)):
		result_matrix[i][i] = 1

	for column_number in range(len(matrix)):

		leading_line = matrix[column_number]
		leading_line1 = result_matrix[column_number]
		if leading_line[column_number] == 0:
			for i in range(column_number,len(matrix)):
				if matrix[i][column_number] != 0:
					leading_line = matrix[i]
					leading_line1 = result_matrix[i]
					_swap_lines(matrix,column_number,i)
					_swap_lines(result_matrix,column_number,i)
					break
			

		for i in range(column_number + 1,len(matrix)):
			coefficient = -1 * matrix[i][column_number] / leading_line[column_number]  
			for j in range(len(matrix[i])):
				matrix[i][j] += leading_line[j] * coefficient

				result_matrix[i][j] += leading_line1[j] * coefficient


	for column_number in range(len(matrix) - 1,-1,-1):
		leading_line = matrix[column_number]
		leading_line1 = result_matrix[column_number]

		for i in range(column_number - 1,-1,-1):
			coefficient = -1 * matrix[i][column_number] / leading_line[column_number]
			for j in range(len(matrix)):
				matrix[i][j] += leading_line[j] * coefficient
				result_matrix[i][j] += leading_line1[j] * coefficient



	for i in range(len(matrix)):
		coefficient = 1/ matrix[i][i]
		matrix[i] = [el * coefficient for el in matrix[i]]
		result_matrix[i] = [el * coefficient for el in result_matrix[i]]

	return result_matrix



if __name__ == "__main__":
	system_matrix = [[15,0,7,5,176],
				     [-3,0,-6,1,-111],
				     [-2,9,13,2,74],
				     [4,-1,3,9,76]]

	system_matrix1 = [[-8,5,8,-6,-144],
	                  [2,7,-8,-1,25],
	                  [-5,-4,1,-6,-21],
	                  [5,-9,-2,8,103]]

	from fractions import Fraction
	system_matrix = [list(map(Fraction,line)) for line in system_matrix]
	system_matrix1 = [list(map(Fraction,line)) for line in system_matrix1]

	for x in invert_matrix([x[:-1] for x in system_matrix]):print([float(i) for i in x]) 

	print([float(x) for x in solve_system(system_matrix1)])
	print(count_determinate(system_matrix1))