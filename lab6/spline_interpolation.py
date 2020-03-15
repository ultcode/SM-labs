import numpy as np

def interpolate_funct(x_val,y_val):
	if len(x_val) != len(y_val):
		raise ValueError("Not same ammount of x and y")

	splines = []
	for i in range(len(x_val) - 1):
		splines.append(gen_spline(x_val[i],x_val[i+1],y_val[i],y_val[i+1]))

	def get_interpolation_result(x):
		if x < x_val[0] or x > x_val[-1]:
			raise ValueError("x not in range of interpolation")

		if x in x_val:
			return y_val[x_val.index(x)]

		for i in range(len(x_val) - 1):
			if x > x_val[i] and x < x_val[i+1]:
				return splines[i](x)

	return get_interpolation_result



def gen_spline(x1,x2,y1,y2):
	# ax1^3 + bx1^2 + cx1 + d = y1
	# ax2^3 + bx2^2 + cx2 + d = y2
	# 6ax1 + 2b = 0
	# 6ax2 + 2b = 0

	main_matrix = [[x1**3,x1**2,x1,1],
				   [x2**3,x2**2,x2,1],
				   [6*x1,2,0,0],
				   [6*x2,2,0,0]]

	values_vector = [y1,
					 y2,
					 y1,
					 y2]

	a,b,c,d = solve_sle(main_matrix,values_vector)

	return lambda x: a*x**3 + b*x**2 + c*x + d

def solve_sle(main_matrix,values_vector):
	main_matrix = np.array(main_matrix)
	values_vector = np.array(values_vector)
	return list(np.linalg.solve(main_matrix,values_vector))


if __name__ == "__main__":
	x_val = [-0.4,-0.1,0.2,0.5,0.8]
	y_val = [-0.81152,-0.20017,0.40136,1.0236,1.7273]
	# "производные на участках"
	for i in range(len(x_val) - 1):
		y_change = y_val[i+1] - y_val[i]
		x_change = x_val[i+1] - x_val[i]
		print(y_change/x_change)
	# удалить позже
	function = interpolate_funct(x_val,y_val)
	print(function(0.1))

	import matplotlib.pyplot as plt

	fig,ax = plt.subplots()
	ax.plot(x_val,y_val,"ro")
	ax.plot([x*0.01 for x in range(-40,81,1)],
		[function(x*0.01) for x in range(-40,81,1)])

	ax.plot(x_val,y_val)
	ax.set_xticks(x_val)
	plt.show()