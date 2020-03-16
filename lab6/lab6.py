import numpy as np
def SlarGen(x_val,y_val, h):
    if len(x_val) != len(y_val):
        raise ValueError("Not same ammount of x and y")

    matrix_results = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
    matrix_results[0][0] = 2*h/3
    matrix_results[1][1] = 2*h/3
    matrix_results[2][1] = 2*h/3
    matrix_results[0][1] = h/6
    matrix_results[1][2] = h/6
    matrix_results[1][0] = h/6
    matrix_results[2][0] = h/6
    d1 = (y_val[2] - y_val[1])/h - (y_val[1] - y_val[0])/h
    d2 = (y_val[3] - y_val[2])/h - (y_val[2] - y_val[1])/h
    d3 = (y_val[4] - y_val[3])/h - (y_val[3] - y_val[2])/h
    matrix_results[0][2] = d1
    matrix_results[1][3] = d2
    matrix_results[2][2] = d3
    return matrix_results

def SlarCalc(s_values):
    AB_coef = []
    AB_coef.append(-s_values[0][1]/s_values[0][0])
    AB_coef.append(-s_values[1][2]/(s_values[1][1] + s_values[1][0]*AB_coef[0]))
    AB_coef.append(0)

    AB_coef.append((s_values[0][2])/(s_values[0][0]))
    AB_coef.append((s_values[1][3]-s_values[1][0]*AB_coef[0])/(s_values[1][1] + s_values[1][0]*AB_coef[0]))
    AB_coef.append((s_values[2][2]-s_values[2][0]*AB_coef[1])/(s_values[2][1] + s_values[2][0]*AB_coef[1]))

    q_container = []
    q_container.append(0)
    q_container.append(AB_coef[2] + AB_coef[5])
    q_container.append(AB_coef[1]*q_container[1] + AB_coef[4])
    q_container.append(AB_coef[0]*q_container[2] + AB_coef[3])
    q_container.append(0)

    return q_container

def SplainBuilder(q_container, x_val, y_val, x, h):
    s1 =  (q_container[0]/6*h * (x_val[1] - x)**3)  + (q_container[1]/(6*h) * (x - x_val[0])**3) + ((y_val[0]/h - q_container[0]/6 * h) * (x_val[1] - x)) + ((y_val[1]/h - q_container[1]* h/6)*(x - x_val[0]))
    s2 =  (q_container[1]/6*h * (x_val[2] - x)**3)  + (q_container[2]/(6*h) * (x - x_val[1])**3) + ((y_val[1]/h - q_container[1]/6 * h) * (x_val[2] - x)) + ((y_val[2]/h - q_container[2]* h/6)*(x - x_val[1]))
    s3 =  (q_container[2]/6*h * (x_val[3] - x)**3)  + (q_container[3]/(6*h) * (x - x_val[2])**3) + ((y_val[2]/h - q_container[2]/6 * h) * (x_val[3] - x)) + ((y_val[3]/h - q_container[3]* h/6)*(x - x_val[2]))
    s4 =  (q_container[3]/6*h * (x_val[4] - x)**3)  + (q_container[4]/(6*h) * (x - x_val[3])**3) + ((y_val[3]/h - q_container[3]/6 * h) * (x_val[4] - x)) + ((y_val[4]/h - q_container[4]* h/6)*(x - x_val[3]))

    if (x >= x_val[0] and x <= x_val[1]):
        return s1
    elif (x >= x_val[1] and x <= x_val[2]):
        return s2
    elif (x >= x_val[2] and x <= x_val[3]):
        return s3
    elif (x >= x_val[3] and x <= x_val[4]):
        return s4
    else:
        raise ValueError("x not in range of interpolation")
if __name__ == "__main__":
    x_val = [-0.4,-0.1,0.2,0.5,0.8]
    y_val = [-0.81152,-0.20017,0.40136,1.0236,1.7273]
    q_container = SlarCalc(SlarGen(x_val, y_val, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, 0.1, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, -0.4, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, -0.1, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, 0.2, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, 0.5, 0.3))
    print(SplainBuilder(q_container, x_val, y_val, 0.8, 0.3))