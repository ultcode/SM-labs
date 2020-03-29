import math as m


def exact_decision(x):
    # return (m.cos(2) - m.sin(2)) * m.cos(2 * x) + (m.sin(2) + m.cos(2)) * m.sin(2 * x)
    return -x**3 + 3*x + 1


def count_function_g(x, y, z):
    # return (z - 2 * y) / x
    return 2*x*z/(x**2 + 1)


def accuracy_control(k1, k2, k3, lim_down, lim_up, step):
    if lim_down > abs((k2 - k3) / (k1 - k2)) or lim_down > abs((k2 - k3) / (k1 - k2)):
        return step + step / 1000
    if abs((k2 - k3) / (k1 - k2)) > lim_up or abs((k2 - k3) / (k1 - k2)) > lim_up:
        return step - step / 1000
    return step


def main_func(step_x, x_start, x_end):
    step = step_x
    counter = 0

    x = x_start
    y = 1
    z = 3

    accuracy_down = 0.01
    accuracy_up = 0.1

    while x <= x_end:
        K1 = step * z
        L1 = step * count_function_g(x, y, z)

        K2 = step * (z + L1 / 2)
        L2 = step * count_function_g(x + step / 2, y + K1 / 2, z + L1 / 2)

        K3 = step * (z + L2 / 2)
        L3 = step * count_function_g(x + step / 2, y + K2 / 2, z + L2 / 2)

        K4 = step * (z + L3)
        L4 = step * count_function_g(x + step, y + K3, z + L3)

        print(f"k={counter}; " + f"x={x.__round__(1)}; " + f"y={y.__round__(7)}; " + f"z={z.__round__(4)}; " +
              f"▲y={((K1 + 2 * K2 + 2 * K3 + K4) / 6).__round__(7)}; " +
              f"▲z={((L1 + 2 * L2 + 2 * L3 + L4) / 6).__round__(7)}; " +
              f"exact={exact_decision(x).__round__(7)}; " + f"error={abs(exact_decision(x) - y).__round__(7)};" +
              f"test:{(z - x * y) / 2}")

        # step = accuracy_control(K1, K2, K3, accuracy_down, accuracy_up, step)
        # step = accuracy_control(L1, L2, L3, accuracy_down, accuracy_up, step)

        x += step
        y += (K1 + 2 * K2 + 2 * K3 + K4) / 6
        z += (L1 + 2 * L2 + 2 * L3 + L4) / 6

        counter += 1


if __name__ == "__main__":
    h = 0.2
    x_left = 0
    x_right = 1
    main_func(h, x_left, x_right)
