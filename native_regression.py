from matrix import *
import matplotlib.pyplot as plt
import sys

def main ():
    measurements = loadtxt(sys.argv[1])
    transposed = transpose(measurements)

    x = transposed[0]
    y = transposed[1]

    Xp = powers(x, 0, 1)
    Yp = powers(y, 1, 1)
    Xpt = transpose(Xp)

    [[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    y2 = []
    for i in range(len(x)):
        y2.append(b + m * x[i])

    plt.plot(x, y, 'ro')
    plt.plot(x, y2)
    plt.show()

# Starts the program
if __name__ == "__main__":
    main()