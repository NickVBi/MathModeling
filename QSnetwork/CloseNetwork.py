import math
import matplotlib.pyplot as plt

def printPlot(x, y, legend = []):
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(x, y, linestyle="solid")
    ax.fill_between(x, y, where = y > [0],
                    color='green', alpha=0.3)
    if legend:
        lgnd = ax.legend(legend, loc='upper center', shadow=True)
        lgnd.get_frame().set_facecolor('#ffb19a')
    plt.show()

class Channel4QS:

    def __init__(self, M, Z, q14, q24, q34, V1, V2, V3, p, t):

        V4 = V1 * q14 + V2 * q24 + V3 * q34

        U4 = p / 100
        S4 = t / 1000

        X0 = U4 / (V4 * S4)

        R = M / X0

        N = R * X0

        print("V4 =", V4)
        print("U4 =", U4)
        print("S4 =", S4)
        print("X0 =", X0)
        print("R =", R)
        print("N =", N)


if __name__ == "__main__":

    M = 20
    Z = 25
    q14 = 0.5
    q24 = 0.7
    q34 = 0.85
    V1 = 12
    V2 = 17
    V3 = 19
    p = 50
    t = 25

    p = Channel4QS(M, Z, q14, q24, q34, V1, V2, V3, p, t)
    print()
    M = 35
    Z = 25
    q14 = 0.19
    q24 = 0.25
    q34 = 0.36
    V1 = 12
    V2 = 18
    V3 = 23
    p = 80
    t = 20

    p = Channel4QS(M, Z, q14, q24, q34, V1, V2, V3, p, t)