from random import randint


def game(a, b):
    global X, Y

    if (a ^ X) > (b ^ Y):
        sgn = -1
    elif (a ^ X) == (b ^ Y):
        sgn = 0
    else:
        sgn = 1

    return sgn


def make_test(a, b):
    global tested

    if (a, b) in tested:
        sgn = tested[(a, b)]
    else:
        sgn = game(a, b)
        tested[(a, b)] = sgn

    return sgn


def recursion(x, y, n):
    if n < 0:
        return

    a = int(''.join(x[::-1]).replace('?', '0'), 2)
    b = int(''.join(y[::-1]).replace('?', '0'), 2)

    sgn = make_test(a, b)

    if sgn == -1:
        a = int(''.join(x[::-1]).replace('?', '0'), 2)
        b = 2 ** n + int(''.join(y[::-1]).replace('?', '0'), 2)

        sgn = make_test(a, b)

        if sgn == -1:  # (a^x)>(b^y)
            tipo = {2, 3}
        elif sgn == 0:  # (a^x)=(b^y)
            tipo = {2}
        else:  # (a^x)<(b^y)
            tipo = {1, 2}

        a = 2 ** n + int(''.join(x[::-1]).replace('?', '0'), 2)
        b = 2 ** n + int(''.join(y[::-1]).replace('?', '0'), 2)

        sgn = make_test(a, b)

        if sgn == -1:  # (a^x)>(b^y)
            tipo &= {1, 3}
        elif sgn == 1:  # (a^x)<(b^y)
            tipo &= {2}

        if tipo == {1}:
            x[n], y[n] = '0', '0'
        elif tipo == {2}:
            x[n], y[n] = '1', '0'
        elif tipo == {3}:
            x[n], y[n] = '1', '1'

    elif sgn == 1:
        a = int(''.join(x[::-1]).replace('?', '0'), 2)
        b = 2 ** n + int(''.join(y[::-1]).replace('?', '0'), 2)

        sgn = make_test(a, b)

        if sgn == -1:  # (a^x)>(b^y)
            tipo = {2, 3}
        elif sgn == 0:  # (a^x)=(b^y)
            tipo = {2}
        else:  # (a^x)<(b^y)
            tipo = {1, 2}

        a = 2 ** n + int(''.join(x[::-1]).replace('?', '0'), 2)
        b = 2 ** n + int(''.join(y[::-1]).replace('?', '0'), 2)

        sgn = make_test(a, b)

        if sgn == -1:  # (a^x)>(b^y)
            tipo &= {2}
        elif sgn == 1:  # (a^x)<(b^y)
            tipo &= {1, 3}

        if tipo == {1}:
            x[n], y[n] = '0', '0'
        elif tipo == {2}:
            x[n], y[n] = '0', '1'
        elif tipo == {3}:
            x[n], y[n] = '1', '1'
    else:
        a = int(''.join(x[::-1]).replace('?', '0'), 2)
        b = 2 ** n + int(''.join(y[::-1]).replace('?', '0'), 2)

        sgn = make_test(a, b)

        x[n] = '0' if sgn == 1 else '1'
        y[n] = x[n]

    recursion(x, y, n - 1)


def solver(m):
    global X, Y

    X = randint(0, m)
    Y = randint(0, m)

    n = len(bin(m)) - 3

    x = ['?'] * (n + 1)
    y = ['?'] * (n + 1)

    recursion(x, y, n)

    u = ''.join(x[::-1])
    v = ''.join(y[::-1])
    if X != int(u, 2) or Y != int(v, 2):
        print X, Y
        return False
    else:
        return True


X, Y = None, None
tested = {}
if __name__ == '__main__':
    M = 10000000000000
    while solver(M):
        tested = {}
        continue

    print "Deu mal!"
