### Перевіряємо функцію на збіжність, проміжок
def convengence (f,deriv2,a, b):
    if ((f(a)* deriv2(a)) > 0):
        print("Умова збіжності виконується для першої границі, отже і для другої.")
        return a
    elif ((f(b)* deriv2(b)) > 0):
        print("Умова збіжності виконуються для другої границі, отже і для першої.")
        return b
    else:
        print("Умова не виконується для жодної з границь")

#Проводимо ітераюцію для необхідної точності
def iteration(function,derivative1, x,eps,iter_numb):
    f = x - (function(x)/ derivative1(x))
    print(str(iter_numb) + ". " + str(f))
    if (abs(function(f)) < eps):
        return f
    else: 
        return iteration(function,derivative1, f,eps,iter_numb + 1)


if __name__ == "__main__":
    def function(x):
        return (x**4 - 2*x - 1)

    def derivative1(x):
        return ((4*(x**3)) - 2)

    def derivative2(x):
        return (12*(x**2))

    a = float(input("Введіть значення початку границі:"))
    b = float(input("Введіть значення кінця границі:"))
    eps = float(input("Введіть значення похибки:"))

    conv = convengence(function,derivative2,a,b)
    print(iteration(function,derivative1,conv,eps,0))