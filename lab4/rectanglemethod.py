def count_integral_with_rectangle_method(funct,a,b,step_length):
	xi = a;
	result = 0;
	while (xi <= b):
		result += funct(xi) * step_length
		xi += step_length
	return result

def _count_step_length(a,b,eps,funct_deviriate_max):
	step_length = (2*eps) / ( (b-1) * funct_deviriate_max)
	return step_length


if __name__ == "__main__":
	def my_function(x):
		return (x**2) / (625 - x**4)

	print(count_integral_with_rectangle_method(my_function,0,4,1))
	print(count_integral_with_rectangle_method(my_function,0,4,0.5))
	print(count_integral_with_rectangle_method(my_function,0,4,_count_step_length(0,4,0.00001,0.051)))

