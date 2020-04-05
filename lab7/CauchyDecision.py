import math as m


def accuracy_control(k1, k2, k3, lim_down, lim_up, step):
    if lim_down > abs((k2 - k3) / (k1 - k2)) or lim_down > abs((k2 - k3) / (k1 - k2)):
        return step + step / 1000
    if abs((k2 - k3) / (k1 - k2)) > lim_up or abs((k2 - k3) / (k1 - k2)) > lim_up:
        return step - step / 1000
    return step


def main_func(step, x_start, x_end,y,z,g,exact_design):

    x = x_start

    # # x_vals = [i/10 for i in range(10,21)]
    # x_vals = [i/10 for i in range(0,11,2)]
    # my_vals = []
    # exact_vals = []


    counter = 0
    while x <= x_end:

        # !!!
        # my_vals.append(y)
        # exact_vals.append(exact_design(x))

        K1 = step * z
        L1 = step * g(x, y, z)

        K2 = step * (z + L1 / 2)
        L2 = step * g(x + step / 2, y + K1 / 2, z + L1 / 2)

        K3 = step * (z + L2 / 2)
        L3 = step * g(x + step / 2, y + K2 / 2, z + L2 / 2)

        K4 = step * (z + L3)
        L4 = step * g(x + step, y + K3, z + L3)

        delta_y = (K1 + 2 * K2 + 2 * K3 + K4) / 6
        delta_z = (L1 + 2 * L2 + 2 * L3 + L4) / 6


        print(f"k={counter}; x={x.__round__(1)}; y={y.__round__(7)}; z={z.__round__(4)}; " +
              f"▲y={delta_y.__round__(7)}; ▲z={delta_z.__round__(7)}; " +
              f"exact={exact_design(x).__round__(7)}; " + 
              f"error={abs(exact_design(x) - y).__round__(7)}; " +
              f"test:{(z - x * y) / 2}")


        x += step
        y += delta_y
        z += delta_z
        counter += 1

    # import matplotlib.pyplot as plt
    # fig,ax = plt.subplots()
    # print(my_vals)
    # ax.plot(x_vals,my_vals,"ro",color="blue")
    # ax.plot(x_vals,exact_vals,"ro")
    # plt.show()




if __name__ == "__main__":
    def exact_design(x):
        return (m.cos(2) - m.sin(2)) * m.cos(2 * x) + (m.sin(2) + m.cos(2)) * m.sin(2 * x)

    def g(x, y, z):
        return 1

    h = 0.1
    x_left = 1
    x_right = 2
    y = 1
    z = 1
    main_func(h, x_left, x_right,y,z,g,exact_design)


    def exact_design1(x):
        return -x**3 + 3*x + 1

    def g1(x,y,z):
        return (2*x*z)/(x**2 + 1)

    y1 = 1
    z1 = 3
    x_left1 = 0
    x_right1 = 1
    h1 = 0.2
    main_func(h1,x_left1,x_right1,y1,z1,g1,exact_design1)
