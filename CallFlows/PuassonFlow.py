import math
import matplotlib.pyplot as plt
import numpy as np

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

    def __init__(self, lambda_, tetra, k1, k2, alpha1, alpha2, k_e):

        k = k2 + 1

        p = [] * k



        print("1. Запишем закон распределения числа поступлений вызовов за промежуток времени:")
        temp = lambda_ * tetra
        for k_ in range(k):
            p += [(temp ** k_) / math.factorial(k_) * math.exp(-temp)]

            print("P" + str(k_) + " = " + str(p[k_]))

        printPlot(range(k), p)

        print("\n\n2. Найдем наиболее вероятное число поступлений вызовов и его вероятность:")
        k_max = p.index(max(p))
        print(k_max, p[k_max])

        print("\n\n3. Найдем вероятность того, что число вызовов, которые поступят за промежуток времени :")

        for k_ in range(k1, k2 + 1):

            print("P" + str(k_) + " = " + str(p[k_]) + " +")
        sum_P_k = sum(p[k1:k2 + 1])
        print("=", sum_P_k)

        print("\n\n4. Найдем вероятность того, что число вызовов, которые поступят за промежуток времени :")

        print("\n\n5. Построим графики функции и плотности распределения :")


        printPlot(range(4), [self.distribution_density(lambda_, i) for i in range(4)], ["1 - e ^ (-6.5 * t)"])

        printPlot(range(4), [self.distribution_function(lambda_, i) for i in range(4)], ["6.5 * e ^ (-6.5 * t)"])

        print("Математическое ожидание: 1 /", lambda_, "=", 1 / lambda_)
        print("Дисперисия: 1 / (", lambda_, "^2 ) =", 1 / (lambda_ ** 2))
        print("Среднее квадратическое отклонение: 1 /", lambda_, "=", 1 / lambda_)
        print("Таким образом, Математическое ожидание = Среднее квадратическое отклонение, т.е. поток вызовов является простым")


        print("\n\n6. Найдем вероятность того, что длина промежутка времени между двумя вызовами находится в границах  :")
        print("F(", alpha2, ") - F(", alpha1, ") = ", self.distribution_function(lambda_, alpha2), "-", self.distribution_function(lambda_, alpha1), "=", self.distribution_function(lambda_, alpha2) - self.distribution_function(lambda_, alpha1))

        print("\n\n7. Рассчитаем поток Эрланга порядка k = 3")

        print("m = (", k_e, "+ 1) /", lambda_, "=", (k_e + 1) / lambda_)
        print("D = (", k_e, "+ 1) /", lambda_ ** 2, "=", (k_e + 1) / lambda_ ** 2)
        print("q = sqrt(", k_e, "+ 1) /", lambda_, "=", math.sqrt(k_e + 1) / lambda_)



    def distribution_function(self, lambda_, t):
        return 1 - math.exp(-lambda_ * t)

    def distribution_density(self, lambda_, t):
        return lambda_ * math.exp(-lambda_ * t)

if __name__ == "__main__":

    lambda_ = 6.5
    tetra = 1
    k1 = 10
    k2 = 16
    alpha1 = 0.5
    alpha2 = 2.5

    k_e = 3

    p = PuassonFlow(lambda_, tetra, k1, k2, alpha1, alpha2, k_e)