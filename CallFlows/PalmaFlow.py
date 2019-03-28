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

    def lambda_function(self):
        return 1 /  (self.p /self.alpha + self.q / self.beta + self.r / self.gamma)

if __name__ == "__main__":

    p = 0.6
    q = 0.2
    r = 0.2
    alpha = 1
    beta = 4
    gamma = 3

    p = PuassonFlow(p, q, r, alpha, beta, gamma)