def brute_force(n):
    m = n + 1
    soma = 0

    for i in xrange(0, m):
        for j in xrange(0, m):
            soma += (i ^ j) == n

    return soma


def solver(n):
    soma = 0

    for i in xrange(n + 1):
        soma += (i ^ n) <= n

    return soma


if __name__ == '__main__':
    N = 7
    print solver(N)
    print brute_force(N)
