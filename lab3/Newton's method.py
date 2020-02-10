
### Перевіряємо функцію на збіжність, проміжок
def function(x):
    return (x**4 - 2*x - 1)

def derivative1(x):
    return ((4*(x**3)) - 2)

def derivative2(x):
    return (12*(x**2))

def convengence (a, b):
    if ((function(a)* derivative2(a)) > 0):
        print("Умова збіжності виконується для першої границі, отже і для другої.")
        return a
    elif ((function(b)* derivative2(b)) > 0):
        print("Умова збіжності виконуються для другої границі, отже і для першої.")
        return b
    else:
        print("Умова не виконується для жодної з границь")
#Проводимо ітераюцію для необхідної точності

def iteration(x):
    for k in range(10):
        f = x - (function(x)/ derivative1(x))
    if (abs(function(f)) < 0.0001):
        print(f)
    else: iteration(f)


if __name__ == "__main__":
    a = float(input("Введіть значення початку границі:"))
    b = float(input("Введіть значення кінця границі:"))
    iteration(convengence(a,b))