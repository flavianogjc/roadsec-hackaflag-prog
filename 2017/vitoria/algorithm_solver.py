def binomial(n):
    c = [0] * (n + 1)
    c[0] = 1

    for i in xrange(1, n + 1):
        j = i
        while j > 0:
            c[j] = (c[j] + c[j - 1]) % 2147483647
            j -= 1

    return c


def solver(k, n):
    mod_ = 2147483647
    soma = 0

    cof = binomial(n)
    u = 1
    for i in xrange(n):
        soma += u * (cof[i] * pow(n - i, k, 2147483647)) % mod_
        u *= -1

    return soma % mod_


if __name__ == '__main__':
    P, S = 3, 2

    print solver(P, S)
