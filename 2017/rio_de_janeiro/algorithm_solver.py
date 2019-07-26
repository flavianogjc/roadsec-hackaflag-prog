def is_bug(n):
    ant = 0

    while n > 0:
        res = n % 2
        if res == 1 and ant == 1:
            return 1
        ant = res
        n -= res
        n /= 2

    return 0


def brute_force(n):
    cont = 0
    for i in xrange(n):
        cont += is_bug(i)
    return n - cont


def n_bugs(n):
    fibonacii = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269,
                 2178309, 3524578, 5702887, 9227465]

    if n == 0 or n == 1:
        cont = n
    else:
        num = bin(n)[2::]
        cont = 0

        while len(num) >= 2:
            while num[0] == '0':
                num = num[1:]
                if num == '':
                    break

            if len(num) >= 2:
                index = len(num) - 1
                if num[0] == '1' and num[1] == '1':
                    cont += fibonacii[index] + fibonacii[index - 1]
                    return cont
                else:
                    cont += fibonacii[index]
            else:
                cont += num == '1'
            num = num[1:]

    return cont


if __name__ == '__main__':
    print n_bugs(123)
    print brute_force(123)
