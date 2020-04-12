a = [0,    -8,   6, -8,   5]
b = [10,   16, -16, 16, -13]
c = [-1,    1,   6, -5,   0]
d = [16, -110,  24, -3,  87]

### MATRIX ###
row_1 = [b[0], c[0],    0,    0,    0]
row_2 = [a[1], b[1], c[1],    0,    0]
row_3 = [   0, a[2], b[2], c[2],    0]
row_4 = [   0,    0, a[3], b[3], c[3]]
row_5 = [   0,    0,    0, b[4], b[4]]

P0 = -c[0] / b[0]
Q0 =  d[0] / b[0]

P1 = -c[1]              / (b[1] + a[1] * P0)
Q1 = (d[1] - a[1] * Q0) / (b[1] + a[1] * P0)

P2 = -c[2]              / (b[2] + a[2] * P1)
Q2 = (d[2] - a[2] * Q1) / (b[2] + a[2] * P1)

P3 = -c[3]              / (b[3] + a[3] * P2)
Q3 = (d[3] - a[3] * Q2) / (b[3] + a[3] * P2)

P4 = 0
Q4 = (d[4] - a[4] * Q3) / (b[4] + a[4] * P3)

x4 = Q4
x3 = x4*P3 + Q3
x2 = x3*P2 + Q2
x1 = x2*P1 + Q1
x0 = x1*P0 + Q0

print(x4)
print(x3)
print(x2)
print(x1.__round__(1))
print(x0)