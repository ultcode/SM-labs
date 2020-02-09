import math as m

"""TASK 3
Write function in def funcFrom
And program find the root of equation with accuracy which you entered"""


def multiplying_less_than_zero(par1, par2):
    result = par1 * par2
    if result < 0:
        return True
    return False


def middleMean(x1, x2):
    return (x1 + x2) / 2


def apprMean(x1, x2):
    return m.fabs(x1 - x2) / 2


def searchOnInterval(x1, x2):
    f1 = funcFrom(x1)
    appr = apprMean(x1, x2)
    middle_x = middleMean(x1, x2)
    iterator = 0

    while appr > epsilon:
        store = middle_x
        if multiplying_less_than_zero(f1, funcFrom(store)):
            x2 = store
        else:
            x1 = store
        iterator += 1
        middle_x = middleMean(x1, x2)
        appr = apprMean(x1, x2) / 2
        print(f"{iterator:}.F(X) = {funcFrom(middle_x):-9};  \t{('X =' + str(middle_x)).rjust(30)}")
        # print(f"{iterator:}.F(X) = {funcFrom(middle_x):-9};\nX = {str(middle_x)}", end='\n\n')
    return middle_x


if __name__ == "__main__":
    def funcFrom(x):
        return x ** 4 - 2 * x - 1
    print("""Please, enter only the float nums!""")
    _from_ = float(input("Start of interval: "))
    _to_ = float(input("End of interval: "))
    epsilon = float(input("Accuracy: "))
    print("The root of the equation: ", searchOnInterval(_from_, _to_), ". With accuracy: ", epsilon)
