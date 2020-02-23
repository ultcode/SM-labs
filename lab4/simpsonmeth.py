def funct(x):
    return ((x**2)/(625 - x**4))


def count_integral_with_simpson_method(funct,a,b,step):
  result = 0;

  x_left = a + step
  i_counter = 1;
  while (x_left != b):
    if i_counter % 2 != 0:
      result += 4 * funct(x_left)
    x_left += step
    i_counter += 1

  x_left = a + step
  i_counter = 1;
  while (x_left != b - step):
    if i_counter % 2 == 0:
      result += 2 * funct(x_left)
    x_left += step
    i_counter += 1

  result += funct(a) + funct(b)
  result *= step/3
  return result



if __name__=="__main__":

    m= 0
    b = 4
    step1 = 1.0
    step2 = 0.5
    lastX = 4


    print ("Результат з кроком 1:", count_integral_with_simpson_method(funct,m,b,step2))

    print("Результат з кроком 0.5:", count_integral_with_simpson_method(funct,m,b,step1))
