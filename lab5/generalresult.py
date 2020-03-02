import math

from newtons_meth import gen_newtons_polinom
from lagrang import get_lagrange_result
from error import upper_margin_value

points1 = [-0.4, -0.1, 0.2, 0.5]
points2 = [-0.4, 0, 0.2, 0.5]
x = 0.1
max_diff_4 = 14.36

def my_funct(x):
	return math.asin(x) + x

print("result for [-0.4, -0.1, 0.2, 0.5]")
print("lagrang methdod:",end=" ")
print(get_lagrange_result(my_funct,points1,x))
print("newtons method:",end="  ")
print(gen_newtons_polinom(my_funct,points1)(x))
print("exact result:   ",my_funct(x))
print("upper margin    ",upper_margin_value(max_diff_4, x, *points1))

print()

print("result for [-0.4, 0, 0.2, 0.5]")
print("lagrang methdod:",end=" ")
print(get_lagrange_result(my_funct,points2,x))
print("newtons method:",end="  ")
print(gen_newtons_polinom(my_funct,points2)(x))
print("exact result:   ",my_funct(x))
print("upper margin    ",upper_margin_value(max_diff_4, x, *points2))
print()
