import math
import copy

import numpy as np

import lab8.gaussmeth as gaussmeth


def solve_system(functions:"list", functions_derivatives:"list",start_approximations:"list", accuracity):
	old_values = start_approximations
	while True:
		print(old_values)
		yacobian_matrix = gen_yacobian_matrix(functions_derivatives,old_values)
		yacobian_matrix = gaussmeth.invert_matrix(yacobian_matrix[:])
		dx = np.dot(yacobian_matrix, [f(*old_values) for f in functions])


		new_values = []
		for i in range(len(old_values)):
			new_values.append(old_values[i] - dx[i])

		current_accuracity = count_accuracy(old_values,new_values)
		if current_accuracity < accuracity:
			return new_values

		old_values = new_values

	return new_values


def gen_yacobian_matrix(deriviates_matrix,variable_values:"tuple/list"):
	result_matrix = copy.deepcopy(deriviates_matrix)
	for i in range(len(result_matrix)):
		for j in range(len(result_matrix)):
			result_matrix[i][j] = result_matrix[i][j](*variable_values)

	return result_matrix


def count_accuracy(vector1,vector2):
	semi_result = []
	for i in range(len(vector1)):
		semi_result.append(vector2[i] - vector1[i])

	semi_result = list(map(lambda x: x**2, semi_result))
	semi_result = sum(semi_result)
	result = math.sqrt(semi_result)
	return result


if __name__ == "__main__":
	def f1(x1,x2):
		return x1**2 - 2*math.log(x2,10) - 1

	def f2(x1,x2):
		return x1**2 - x1*x2 + 1

	def dv1(x1,x2):
		return 2*x1

	def dv2(x1,x2):
		return -2 / (x2 * math.log(10,math.e))


	def dv3(x1,x2):
		return 2*x1 - 1 * x2

	def dv4(x1,x2):
		return -1*x1 

	functions = [f1,f2]
	dv = [[dv1,dv2],[dv3,dv4]]

	res = solve_system(functions,dv,[1,2],0.000001)

