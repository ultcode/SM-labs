import numpy as np


def func(x):
    return np.arcsin(x) + x


def funcLa(x, x0, x1, x2, x3):
    return funcLa0(x, x0, x1, x2, x3) + funcLa1(x, x0, x1, x2, x3) + \
           funcLa2(x, x0, x1, x2, x3) + funcLa3(x, x0, x1, x2, x3)


def funcLa0(x, x0, x1, x2, x3):
    return func(x0) * (x - x1) * (x - x2) * (x - x3) / ((x0 - x1) * (x0 - x2) * (x0 - x3))


def funcLa1(x, x0, x1, x2, x3):
    return func(x1) * (x - x0) * (x - x2) * (x - x3) / ((x1 - x0) * (x1 - x2) * (x1 - x3))


def funcLa2(x, x0, x1, x2, x3):
    return func(x2) * (x - x0) * (x - x1) * (x - x3) / ((x2 - x0) * (x2 - x1) * (x2 - x3))


def funcLa3(x, x0, x1, x2, x3):
    return func(x3) * (x - x0) * (x - x1) * (x - x2) / ((x3 - x0) * (x3 - x1) * (x3 - x2))


def comparision_errors(error1, error2):
    return abs(error1 / error2)


def exact_error_value(x, x0, x1, x2, x3):
    return func(x) - funcLa(x, x0, x1, x2, x3)


def upper_margin_value(max_diff, x, x0, x1, x2, x3):
    return (x - x0) * (x - x1) * (x - x2) * (x - x3) * max_diff / 24


if __name__ == "__main__":
    x = 0.1
    x0 = -0.4
    x1 = 0
    x2 = 0.2
    x3 = 0.5
    max_diff_4 = 14.36
    upper_margin_value = upper_margin_value(max_diff_4, x, x0, x1, x2, x3)
    exact_error_value = exact_error_value(x, x0, x1, x2, x3)
    print(f"Верхня оцінка похибки більша у {comparision_errors(upper_margin_value, exact_error_value).__round__(3)} разів за абсолютну")
