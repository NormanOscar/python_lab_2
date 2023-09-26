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

    # Calculate the coefficients
    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[: ,0]

    # Calculate the number of points to plot
    n = (x[-1]-x[0])/0.2

    # Create a new x-axis
    x2 = linspace(int(x[0]), int(x[-1]), int(n)).tolist()

    y2 = []
    # Calculate the y-axis
    for i in range(len(x2)):
        y2.append(poly(a, x2[i]))

    plt.plot(x, y, 'ro')
    plt.plot(x2, y2)
    plt.show()

# Computes a new matrix with the powers of the given matrix
def powers (matrix, start, end):
    new_matrix = []
    # For each row in the matrix
    for i in range(len(matrix)):
        new_matrix.append([])
        # For each column in the matrix
        for j in range(start, int(end) + 1):
            # Add the power of the matrix to the new matrix
            new_matrix[i].append(math.pow(matrix[i], j))
    return array(new_matrix)

# Computes the polynomial
def poly(a, x):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * math.pow(x, i)
    return sum

# Starts the program
if __name__ == "__main__":
    main()