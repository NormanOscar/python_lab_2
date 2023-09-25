from numpy import *
import matplotlib.pyplot as plt
import sys
import math

def main ():
    measurements = loadtxt(sys.argv[1])
    transposed = transpose(measurements)
    n = sys.argv[2]

    x = transposed[0]
    y = transposed[1]

    Xp = powers(x, 0, n)
    Yp = powers(y, 1, 1)
    Xpt = transpose(Xp)

    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[: ,0]

    n = (x[-1]-x[0])/0.2
    x2 = linspace(int(x[0]), int(x[-1]), int(n)).tolist()

    y2 = []
    for i in range(len(x2)):
        y2.append(poly(a, x2[i]))

    plt.plot(x, y, 'ro')
    plt.plot(x2, y2)
    plt.show()

def powers (matrix, start, end):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(start, int(end) + 1):
            new_matrix[i].append(math.pow(matrix[i], j))
    return array(new_matrix)

def poly(a, x):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * math.pow(x, i)
    return sum

# Starts the program
if __name__ == "__main__":
    main()