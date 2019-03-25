import math
import matplotlib.pyplot as plt


class Channel4QS:

    def __init__(self, lambda_, N, alpha):

        nChannel = 4

        p = [0] * (nChannel + 1)

        p[0] = 1.0 / sum([((lambda_ ** k) / (math.factorial(k))) for k in range(nChannel + 1)])
        for k in range(1, nChannel + 1):

            p[k] = (lambda_** k) / math.factorial(k) * p[0]


        for i in p:
            print(i)

        if 1 - sum(p) < 0.0000001:
            print("OK")



        fig, ax = plt.subplots()
        ax.plot(range(5),
                p,
                linestyle="solid")
        plt.show()

        m_x = sum([p[i] * i for i in range(len(p))])
        print("Найдем среднее число занятых каналов:", m_x)
        m_x2 = sum([p[i] * i ** 2 for i in range(len(p))])
        d_x = m_x2 - m_x ** 2
        print("Дисперсия:", d_x)
        q_x = math.sqrt(d_x)
        print("Среднее квадратическое отклонение:", q_x)

        print()

        D_un = p[nChannel]
        Y = lambda_ * (1 - p[nChannel])
        A = lambda_
        A_ = lambda_
        A_un = A - Y
        A_und = A_ - Y
        D_t  = p[nChannel]
        D_i = A_un / A

        print("1.   Вероятность потери вызовов (вероятность отказа)", D_un)
        print("2.	Интенсивность обслуженной нагрузки", Y)
        print("3.	Интенсивность потенциальной нагрузки", A)
        print("4.	Интенсивность поступающей нагрузки", A_)
        print("5.	Интенсивность утраченной нагрузки", A_un)
        print("6.	Интенсивность избыточная", A_und)
        print("7.	Вероятность потери по времени (доля времени от всего времени обслуживания, когда все каналы заняты)", D_t)
        print("8.	Вероятность потери по нагрузке", D_i)

        print()

        C_t = sum((self.C(N, j) * alpha ** j) for j in range(1, nChannel + 1))

        p = [(self.C(N, k) * alpha **k) / C_t for k in range(nChannel + 1)]


        for i in p:
            print(i)

        if 1 - sum(p) < 0.0000001:
            print("OK")

        m_x = sum([p[i] * i for i in range(len(p))])
        print("Найдем среднее число занятых каналов:", m_x)
        m_x2 = sum([p[i] * i ** 2 for i in range(len(p))])
        print("M(X^2):", m_x2)
        d_x = m_x2 - m_x ** 2
        print("Дисперсия:", d_x)
        q_x = math.sqrt(d_x)
        print("Среднее квадратическое отклонение:", q_x)
        print("Вероятность того, что все каналы заняты:", p[nChannel])

        print()

        N -= 1

        C_t = sum((self.C(N, j) * alpha ** j) for j in range(1, nChannel + 1))

        p = [(self.C(N, k) * alpha **k) / C_t for k in range(nChannel + 1)]


        for i in p:
            print(i)

        if 1 - sum(p) < 0.0000001:
            print("OK")

        m_x = sum([p[i] * i for i in range(len(p))])
        print("Найдем среднее число занятых каналов:", m_x)
        m_x2 = sum([p[i] * i ** 2 for i in range(len(p))])
        print("M(X^2):", m_x2)
        d_x = m_x2 - m_x ** 2
        print("Дисперсия:", d_x)
        q_x = math.sqrt(d_x)
        print("Среднее квадратическое отклонение:", q_x)
        print("Среднее время занятости первого канала:", alpha / (1 + alpha))
        print("Вероятность того, что все каналы заняты:", p[nChannel])


        print()
        N += 1

        D_un = p[nChannel]
        Y = alpha * N * (1 - D_un) / (1 + alpha * (1 - D_un))
        A = N * alpha / (1 + alpha)
        A_ = alpha * N / (1 + alpha * (1 - D_un))
        A_un = A - Y
        A_und = A_ - Y
        D_t = p[nChannel]
        D_i = D_un / (1 + alpha * (1 - D_un))

        print("1.   Вероятность потери вызовов (вероятность отказа)", D_un)
        print("2.	Интенсивность обслуженной нагрузки", Y)
        print("3.	Интенсивность потенциальной нагрузки", A)
        print("4.	Интенсивность поступающей нагрузки", A_)
        print("5.	Интенсивность утраченной нагрузки", A_un)
        print("6.	Интенсивность избыточная", A_und)
        print("7.	Вероятность потери по времени (доля времени от всего времени обслуживания, когда все каналы заняты)", D_t)
        print("8.	Вероятность потери по нагрузке", D_i)

    def C(self, n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

if __name__ == "__main__":

    lambda_ = 4
    N = 6
    alpha = 2

    p = Channel4QS(lambda_, N, alpha)