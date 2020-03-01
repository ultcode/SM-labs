import math

def gen_newtons_polinom(funct,points):
	"""Функция составляющяя функцию-полином для исходной функциипо точкам"""
	functions = []
	functions.append(lambda x: funct(points[0]))
	for i in range(2,len(points)):
		functions.append(gen_summand(funct,points[0:i]))

	def new_funct(x):
		result = 0
		for part_funct in functions:
			part_result = part_funct(x)
			result += part_result
		return result

	return new_funct

def gen_summand(funct,points):
	"""функция ченерирурующая отедльное слагаемое для полинома"""
	multiplications = []
	coef = recurs_gen_coef(funct,points)
	multiplications.append(lambda x: coef)
	# gen_lambda нужна чтоб избежать того, что все лямбды
	# извлекают последнее значение xk и ипсользуют его
	def gen_lambda(xk) : return lambda x: x - xk
	for xk in points[0:-1]:
		multiplications.append(gen_lambda(xk))


	def new_funct(x):
		result = 1
		for funct in multiplications:
			result *= funct(x)
		return result
	return new_funct	

def recurs_gen_coef(funct,points):
	"""функция высчитывающая коэфицент слагаемого"""
	if len(points) == 1:
		return funct(points[0])

	result = (recurs_gen_coef(funct,points[1:])
			 - recurs_gen_coef(funct,points[0:-1]))
	result /= points[-1] - points[0]
	return result

if __name__ == "__main__":
	def function(x):
		return math.asin(x)

	a = gen_newtons_polinom(function,[-0.4,-0.1,0.2,0.5])
	for x in [-0.3,0,0.1,0.35]:
		print(x)
		print(a(x))
		print(function(x))
		print()