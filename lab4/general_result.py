from rectanglemethod import count_integral_with_rectangle_method
from trapezemethod import count_integral_with_trapeze_method
from simpsonmeth import count_integral_with_simpson_method


def apply_rungle_rule(funct,calc_funct,a,b,step,p):
	res1 = calc_funct(funct,a,b,step)
	res2 = calc_funct(funct,a,b,step/2)

	result = res2 + (res2 - res1) / (2**p - 1)
	return result


if __name__ == "__main__":
	def my_function(x):
		return (x**2) / (625 - x**4)


	print("Integration results")
	x0 = 0
	xi = 4
	print("For step 1:")
	step = 1
	print("Rectangle method: ",
		count_integral_with_rectangle_method(my_function,x0,xi,step))
	print("Trapez method:    ",
		count_integral_with_trapeze_method(my_function,x0,xi,step))
	print("Simpson method:   ",
		count_integral_with_simpson_method(my_function,x0,xi,step))

	print()
	print("More accurate ones:")
	print("Rectangle method: ",
		apply_rungle_rule(my_function,count_integral_with_rectangle_method
			              ,x0,xi,step,1))
	print("Trapez method:    ",
		apply_rungle_rule(my_function,count_integral_with_trapeze_method
			              ,x0,xi,step,2))
	print("Simpson method:   ",
		apply_rungle_rule(my_function,count_integral_with_simpson_method
			              ,x0,xi,step,4))

	print()
	print("For step 0.5:")
	step = 0.5
	print("Rectangle method: ",
		count_integral_with_rectangle_method(my_function,x0,xi,step))
	print("Trapez method:    ",
		count_integral_with_trapeze_method(my_function,x0,xi,step))
	print("Simpson method:   ",
		count_integral_with_simpson_method(my_function,x0,xi,step))


	print()
	print("More accurate ones:")
	print("Rectangle method: ",
		apply_rungle_rule(my_function,count_integral_with_rectangle_method
			              ,x0,xi,step,1))
	print("Trapez method:    ",
		apply_rungle_rule(my_function,count_integral_with_trapeze_method
			              ,x0,xi,step,2))
	print("Simpson method:   ",
		apply_rungle_rule(my_function,count_integral_with_simpson_method
			              ,x0,xi,step,4))