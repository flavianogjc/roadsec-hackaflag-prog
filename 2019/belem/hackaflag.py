# -*- coding: utf-8 -*-

import socket
import sys

from utils import *


def question(a, b):
    global sock

    ask = 'pergunta %d %d\n' % (a, b)
    sys.stdout.write(ask)
    sock.send(ask)

    try:
        txt = sock.recv(4096)
        sys.stdout.write(txt)
        sgn = get_result_cmp(txt)

        txt = sock.recv(4096)
        sys.stdout.write(txt)
    except:
        txt = sock.recv(4096)
        sys.stdout.write(txt)
        sgn = get_result_cmp(txt)

    return sgn


def make_test(a, b):
    global tested

    if (a, b) in tested:
        sgn = tested[(a, b)]
    else:
        sgn = question(a, b)
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
    global tested

    n = len(bin(m)) - 3

    x = ['?'] * (n + 1)
    y = ['?'] * (n + 1)

    recursion(x, y, n)

    a, b = int(''.join(x[::-1]), 2), int(''.join(y[::-1]), 2)

    tested = {}

    return a, b


tested = {}
if __name__ == "__main__":
    host, port = '142.93.73.149', 10679

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    try:
        sock.connect((host, port))
    except Exception as error:
        print('-' * 20 + ' Unable to connect ' + '-' * 20)
        print(error)
        sock.close()
        sys.exit()

    sys.stdout.write(sock.recv(4096) + 'start\n')
    sock.send('start\n')

    input_data = ''
    sys.stdout.write(sock.recv(4096))
    while True:
        data = sock.recv(4096)
        if not data:
            print('-' * 20 + ' Connection closed ' + '-' * 20)
            break
        else:
            sys.stdout.write(data)
            if 'Partida ' in data:
                input_data += data

                abs_interval = get_interval(input_data)

                x, y = solver(abs_interval)

                resp = "resposta %d %d\n" % (x, y)
                sys.stdout.write(resp)
                sock.send(resp)

                input_data = ''
            elif 'HACKAFLAG{' in data:
                break
            else:
                input_data += data

    sock.close()
