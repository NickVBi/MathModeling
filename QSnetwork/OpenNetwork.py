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

    def __init__(self, M, Z, R_):

        X0_ = M / (Z + R_)

        X0_pXk = 0.9 / 0.04

        Xk_ = 10 * X0_
        Xk = X0_pXk - Xk_

        X0 = Xk / 5

        print("X0_ =", X0_)
        print("X0_pXk =", X0_pXk)
        print("Xk_ =", Xk_)
        print("Xk =", Xk)
        print("X0 =", X0)

        X0 = X0 * 3
        Xk = 5 * X0

        k = 1 / 0.04

        print("X0 =", X0)
        print("Xk =", Xk)
        print("k =", k)

        diration = k - Xk

        print("diration =", diration)

        diration12 = diration / 10

        print("diration12 =", diration12)

        diration13 = M / diration12 - Z

        print("diration13 =", diration13)


if __name__ == "__main__":

    M = 40
    Z = 15
    R_ = 5

    p = Channel4QS(M, Z, R_)

    print()
    M = 65
    Z = 25
    R_ = 15

    p = Channel4QS(M, Z, R_)