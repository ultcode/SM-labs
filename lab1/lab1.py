def half_div_meth(funct,lefBord,rightBord,epsilon):
	if rightBord <= lefBord:
		raise ValueError("incorrect borders")
	elif funct(lefBord) * funct(rightBord) >= 0:
		raise ValueError("incorrect borders")

	if epsilon <= 1e-16:
		raise ValueError("such small epsilon is not supported by python")

	while (rightBord - lefBord > epsilon):
		middle = lefBord + (rightBord - lefBord)/2
		print(lefBord,middle,rightBord)

		midle_func_val = funct(middle)
		if midle_func_val == 0:
			break

		if midle_func_val * funct(lefBord) < 0:
			rightBord = middle
		else:
			lefBord = middle

	return middle


if __name__ == "__main__":

	def my_func(x):
		return x**4 - 2*x - 1

	print(half_div_meth(my_func,0,5,1e-3))