import numpy as np


def gen_slar(x_val,y_val, h):
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

def count_q(matrix):
    a_coef = []
    a_coef.append(-matrix[0][1]/matrix[0][0])
    a_coef.append(-matrix[1][2]/(matrix[1][1] + matrix[1][0]*a_coef[0]))
    a_coef.append(0)

    b_coef = []
    b_coef.append((matrix[0][2])/(matrix[0][0]))
    b_coef.append((matrix[1][3] - matrix[1][0]*a_coef[0]) /
                  (matrix[1][1] + matrix[1][0]*a_coef[0]))
    b_coef.append((matrix[2][2] - matrix[2][0]*a_coef[1]) / 
                  (matrix[2][1] + matrix[2][0]*a_coef[0]))
    q_container = []
    q_container.append(0)
    q_container.append(a_coef[2] + b_coef[2])
    q_container.append(a_coef[1]*q_container[1] + b_coef[1])
    q_container.append(a_coef[0]*q_container[2] + b_coef[0])
    q_container.append(0)

    return q_container

def count_interp_value(q_container, x_val, y_val, x, h):
    if (x >= x_val[0] and x <= x_val[1]):
        segment_number = 0
    elif (x >= x_val[1] and x <= x_val[2]):
        segment_number = 1
    elif (x >= x_val[2] and x <= x_val[3]):
        segment_number = 2
    elif (x >= x_val[3] and x <= x_val[4]):
        segment_number = 3
    else:
        raise ValueError("x not in range of interpolation")

    i = segment_number
    result = (q_container[i]/6*h * (x_val[i+1] - x)**3)  + \
             (q_container[i+1]/(6*h) * (x - x_val[i])**3) + \
             ((y_val[i]/h - q_container[i]/6 * h) * (x_val[i+1] - x)) + \
             ((y_val[i+1]/h - q_container[i+1]* h/6)*(x - x_val[i]))

    return result

def gen_interp_functions(x_val,y_val,h):
    q = count_q(gen_slar(x_val,y_val,h))
    def function(x):
        return count_interp_value(q,x_val,y_val,x,h)

    return function


if __name__ == "__main__":
    x_val = [-0.4,-0.1,0.2,0.5,0.8]
    y_val = [-0.81152,-0.20017,0.40136,1.0236,1.7273]
    h = 0.3
    interp_funct = gen_interp_functions(x_val,y_val,h)
    for x in [0.1,-0.4,-0.1,0.2,0.5,0.8]:
        print(interp_funct(x))

    import matplotlib.pyplot as plt 
    fig,ax = plt.subplots()
    ax.plot([x*0.01 for x in range(-40,81,1)],
        [interp_funct(x*0.01) for x in range(-40,81,1)],color="blue")
    ax.plot(x_val,y_val,"ro")
    plt.show()