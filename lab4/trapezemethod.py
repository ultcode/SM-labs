def count_integral_with_trapeze_method(func,x0,xk,h):
    firstPart = (h/2) * (func(x0) + func(xk))

    iterations = (xk - x0) / h
    counter = 1
    xi = x0
    secondPart = 0

    # было
    # while counter != iterations - 1:
    # должно быть
    while counter <= iterations - 1:
    # получалось на одну итерацию меньше
        xi += h
        secondPart += h * func(xi)
        counter += 1
    return firstPart + secondPart


if __name__ == "__main__":
    def func(x):
        return x ** 2 / (625 - x ** 4)
    a = 0
    b = 4
    stepForFirst = 1
    stepForSecond = 0.5
    first = summing(funct, a, b,stepForFirst).__round__(7)
    second = summing(funct, a, b,stepForSecond).__round__(7)
    print("First integral (step=1): " + str(first))
    print("Second integral (step=0.5): " + str(second))
    print("Runge (I(n) + (I(2n) - I(n)): " + str((second + (second - first)/3).__round__(7)))
    print("Error: " + str(abs((first - second)*1/3).__round__(7)))
