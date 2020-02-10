import math

"""TASK 3
Write function in def funcFrom
And program find the root of equation with accuracy which you entered"""


def multiplying_less_than_zero(par1, par2):
    result = par1 * par2
    return result < 0

def middleMean(x1, x2):
    return (x1 + x2) / 2

def apprMean(x1, x2):
    return math.fabs(x1 - x2) / 2

def searchOnInterval(funct,epsilon,x1, x2):
    f1 = funct(x1)
    appr = apprMean(x1, x2)
    middle_x = middleMean(x1, x2)

    iteration = 0
    while appr > epsilon:
        store = middle_x
        if multiplying_less_than_zero(f1, funct(store)):
            x2 = store
        else:
            x1 = store
        iteration += 1
        middle_x = middleMean(x1, x2)
        appr = apprMean(x1, x2) / 2

        print(f"{iteration:}. F(X) = {funct(middle_x):-9};  \t{('X =' + str(middle_x)).rjust(30)}")
    return middle_x


if __name__ == "__main__":
    def funcFrom(x):
        return x ** 4 - 2 * x - 1

    print("""Please, enter only the float nums!""")
    _from_ = float(input("Start of interval: "))
    _to_ = float(input("End of interval: "))
    epsilon = float(input("Accuracy: "))

    print("The root of the equation: ", searchOnInterval(funcFrom,epsilon,_from_, _to_),
          ". With accuracy: ", epsilon)