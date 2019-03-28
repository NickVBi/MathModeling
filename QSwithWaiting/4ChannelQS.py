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

        B = sum([((lambda_ ** k) / math.factorial(k)) for k in range(nChannel + 1)]) + \
            lambda_ / (nChannel - lambda_) * \
            lambda_ ** nChannel / math.factorial(nChannel)

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


if __name__ == "__main__":

    lambda_ = 3.21

    p = Channel4QS(lambda_)