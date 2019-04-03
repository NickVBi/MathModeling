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

    def __init__(self, lambda_):

        nChannel = 4

        n_p = 8
        p = [0] * n_p

        t0 = sum([((lambda_ ** k) / math.factorial(k)) for k in range(nChannel + 1)])
        t1 = lambda_ / (nChannel - lambda_)
        t2 = (lambda_ ** nChannel) / math.factorial(nChannel)
        B =  t0 + t1 * t2


        print(B)
        for k in range(n_p):
            p[k] = ((lambda_ ** k) / math.factorial(k)) / int(B)

        for i in p:
            print(i)

        if 1 - sum(p) < 0.0000001:
            print("OK")
        else:
            print(p, sum(p))

        printPlot(range(n_p), p)

        D_n = t1 * t2 / B

        print(t1)
        print(t2)
        print(D_n)
        t = 0.4

        pw = -(nChannel - lambda_) * t
        print(pw)
        P_t = D_n * math.exp(pw)
        print(P_t)

        S = lambda_ / (nChannel * lambda_) * D_n

        print(S)

        Y = S / lambda_

        print(Y)

        VP = (lambda_ / nChannel) ** (nChannel - 1) * D_n

        print(VP)

if __name__ == "__main__":

    lambda_ = 3.08

    p = Channel4QS(lambda_)