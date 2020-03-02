import math

def L(index, X, x ):
    a = 1;
    for i in range(len(X)):
        if ( i != index):
            a *= (x - X[i])/(X[index] - X[i])

    return a

def GetValue(X, Y, x):
    y = 0
    for j in range(len(X)):
        y += Y[j] * L(j, X, x)

    return y


def get_lagrange_result(function,points,x_to_calc):
    y = []
    for xi in points:
        y.append(function(xi))

    return GetValue(points,y,x_to_calc)


def myfunction(x):
    return (math.asin(x) + x)


if __name__ == "__main__":
    X = [-0.4, 0, 0.2, 0.5]
    X2 = [-0.4, -0.1, 0.2, 0.5]
    print(get_lagrange_result(myfunction,X,0.1))
    Y = []
    Y2 = []

    x = 0.1

    for j in range(len(X)):
        Y.append(myfunction(X[j]))

    y = GetValue(X, Y, x)
    print("Інтерполяція по Лагранжу для 1 діапазону x = ", {x}, "Y", {y})
    print("Дійсне значення X =", {x}, "Y", {myfunction(x)})

    for k in range(len(X2)):
        Y2.append(myfunction(X2[k]))

    y2 = GetValuet_with_step(X2, 0.3, Y2, x)
    print("Інтерполяція по Лагранжу для 2 діапазону x = ", {x}, "Y", {y2})
    print("Дійсне значення X = ", {x}, "Y", {myfunction(x)})