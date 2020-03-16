import math

import matplotlib.pyplot as plt

import spline_interpolation

def funct(x):
	return math.e**x
x_val = [x*0.1 for x in range(0,101)]
y_val = [funct(x) for x in x_val]

interp_funct = spline_interpolation.interpolate_funct(x_val,y_val)

interp_x = [x*0.01 for x in range(0,1001)]
interp_y = [interp_funct(x) for x in interp_x]

real_x = [x*0.01 for x in range(0,1001)]
real_y = [funct(x) for x in real_x]


fig,ax = plt.subplots()
ax.plot(x_val,y_val,"ro",label="interpolation points")
ax.plot(interp_x,interp_y,label="interpolation")
ax.plot(real_x,real_y,label="original_function")


ax.legend()
plt.show()
