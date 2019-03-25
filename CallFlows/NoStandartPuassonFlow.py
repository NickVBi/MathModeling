import math
import matplotlib.pyplot as plt


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

        fig, ax = plt.subplots()
        ax.plot(range(k1),
                p[:k1],
                linestyle="solid")
        plt.show()

        t = 2

        print(self.lambda_function(t))

        self.m = round(self.m_function(t))
        print(self.m)

        for k_ in range(k1, k2):
            p[k_] = self.p_k_function(k_, t)

            print("P" + str(k_) + " = " + str(p[k_]))

        fig, ax = plt.subplots()
        ax.plot(range(k1, k2),
                p[k1:k2],
                linestyle="solid")
        plt.show()

    def p_k_function(self, k, tetra):
        return (self.m ** k) / math.factorial(k) * \
               math.exp(-self.m)

    def m_function(self, tetra):
        return (self.a * tetra ** 2) / 2 + \
               (self.a * self.t0 + self.b) * tetra

    def lambda_function(self, t):
        return self.a * t + self.b

if __name__ == "__main__":

    a = 4
    b = 1
    t0 = 0.2

    p = PuassonFlow(a, b, t0)