from math import sqrt


def miller_test(m, base):
    k, q = 0, m - 1

    while q % 2 == 0:
        q >>= 1
        k += 1

    r, i = pow(base, q, m), 0
    while True:
        if (i == 0 and r == 1) or (i >= 0 and r == m - 1):
            return False

        i += 1
        r = pow(r, 2, m)
        if i >= k:
            return True


def is_prime(p):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if p == i:
            return True
        if miller_test(p, i):
            return False

    return True


def is_trimo(n):
    r = int(sqrt(n))
    if r * r == n and is_prime(r):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(is_trimo(91))
