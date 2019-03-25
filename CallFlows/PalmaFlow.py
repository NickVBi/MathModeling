import math


class PuassonFlow:

    def __init__(self, p, q, r, alpha, beta, gamma):
        self.p = p
        self.q = q
        self.r = r
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        lambda_ = self.lambda_function()
        print(lambda_)

    def lambda_function(self, t):
        return 1 /
        (self.p /self.alpha +
         self.q / self.beta +
         self.r / self.gamma)

if __name__ == "__main__":

    p = 0.2
    q = 0.3
    r = 0.5
    alpha = 1
    beta = 2
    gamma = 4

    p = PuassonFlow(p, q, r, alpha, beta, gamma)