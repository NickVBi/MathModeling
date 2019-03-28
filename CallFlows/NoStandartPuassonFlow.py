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

class PuassonFlow:

    def __init__(self, a, b, t0):
        self.a = a
        self.b = b
        self.t0 = t0
        t = 1

        k1 = 8
        k2 = 18
        p = [0] * (k1 + k2)

        print(self.lambda_function(t))

        self.m = round(self.m_function(t))
        print(self.m)

        for k_ in range(k1):
            p[k_] = self.p_k_function(k_, t)

            print("P" + str(k_) + " = " + str(p[k_]))

        printPlot(range(k1), p[:k1])

        t = 2

        print(self.lambda_function(t))

        self.m = round(self.m_function(t))
        print(self.m)

        for k_ in range(k1, k2):
            p[k_] = self.p_k_function(k_, t)

            print("P" + str(k_) + " = " + str(p[k_]))

        printPlot(range(k1, k2), p[k1:k2])

    def p_k_function(self, k, tetra):
        return (self.m ** k) / math.factorial(k) * \
               math.exp(-self.m)

    def m_function(self, tetra):
        return (self.a * tetra ** 2) / 2 + \
               (self.a * self.t0 + self.b) * tetra

    def lambda_function(self, t):
        return self.a * t + self.b

if __name__ == "__main__":

    a = 6
    b = 1
    t0 = 0.9

    p = PuassonFlow(a, b, t0)