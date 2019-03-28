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

class Channel3QS:

    def __init__(self, lambda_):

        nChannel = 3

        p = [0] * (nChannel + 1)

        p[0] = 1.0 / sum([((lambda_ ** k) / (math.factorial(k))) for k in range(nChannel + 1)])
        for k in range(1, nChannel + 1):

            p[k] = (lambda_** k) / math.factorial(k) * p[0]


        for i in p:
            print(i)

        if sum(p) == 1:
            print("OK")

        printPlot(range(4), p)

        print("Вероятность потери вызовов (вероятность отказа)", p[nChannel])
        print("Найдем среднее число занятых каналов:", sum([p[i] * i for i in range(len(p))]))

if __name__ == "__main__":

    lambda_ = 7.5

    p = Channel3QS(lambda_)