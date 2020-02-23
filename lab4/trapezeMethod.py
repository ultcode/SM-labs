def func(x):
    return x ** 2 / (625 - x ** 4)


def summing(h, x0, xk):
    iterations = (xk - x0) / h
    counter = 1
    storeX = x0
    secondPart = 0
    firstPart = h * (func(x0) + func(xk)) / 2

    while counter != iterations - 1:
        storeX += h
        secondPart += h * func(storeX)
        counter += 1
    return firstPart + secondPart


if __name__ == "__main__":
    a = 0
    b = 4
    stepForFirst = 1
    stepForSecond = 0.5
    first = summing(stepForFirst, a, b).__round__(7)
    second = summing(stepForSecond, a, b).__round__(7)
    print("First integral (step=1): " + str(first))
    print("Second integral (step=0.5): " + str(second))
    print("Runge (I(n) + (I(2n) - I(n)): " + str((second + (second - first)/3).__round__(7)))
    print("Error: " + str(abs((first - second)*1/3).__round__(7)))
