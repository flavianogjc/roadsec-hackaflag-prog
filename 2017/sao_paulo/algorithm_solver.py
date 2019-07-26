from math import ceil


def brute_force(a, b, c):
    arr = []
    for i in range(a, b, c):
        arr.append(i)

    i, ope = 0, 1
    while True:
        if i % 2 == 0:
            brr = []
            len_a = len(arr)
            for j in range(0, len_a - 1):
                x = arr[j] + ope * arr[j + 1]
                brr.append(x)
                ope *= -1
        else:
            arr = []
            len_b = len(brr)
            for j in range(0, len_b - 1):
                x = brr[j] + ope * brr[j + 1]
                arr.append(x)
                ope *= -1
        if len(arr) == 1:
            return arr[0] % 2147483647
        elif len(brr) == 1:
            return brr[0] % 2147483647
        i += 1


def good(i, t, p):
    n = int(ceil(float(t-i)/p))

    resp = (alpha(n) * i + beta(n) * p) % 2147483647

    return resp


def beta(n):
    res = n % 4
    b, m = 1, 2147483647

    if res == 0:
        for i in range(0, (n / 2 - 1)):
            b = ((b % m) * 2) % m

        return -b
    elif res == 1:
        for i in range(0, (n / 2 - 1)):
            b = ((b % m) * 2) % m

        return ((n - 1) * b) % m
    elif res == 2:
        for i in range(0, (n - 2) / 4):
            b = ((b % m) * 4) % m

        return ((n - 1) * b) % m
    else:
        for i in range(0, (n - 3) / 4):
            b = ((b % m) * 4) % m

        return ((n - 3) * b) % m


def alpha(n):
    res = n % 4
    a, m = 1, 2147483647

    if res == 0:
        return 0
    elif res == 1:
        for i in range(0, (n - 1) / 4):
            a = ((a % m) * 4) % m

        return a
    else:
        for i in range(0, (n - 2) / 4):
            a = ((a % m) * 4) % m

        return (2 * a) % m


if __name__ == '__main__':
    I, T, P = 8, 40, 21
    print good(I, T, P)
    print brute_force(I, T, P)
