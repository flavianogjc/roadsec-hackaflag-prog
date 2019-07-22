# -*- coding: utf-8 -*-

import socket, sys

from algorithm_solver import min_cost
from utils import *

if __name__ == "__main__":
    host, port = '142.93.73.149', 11349

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    try:
        sock.connect((host, port))
    except Exception as error:
        print('-' * 20 + ' Unable to connect ' + '-' * 20)
        print(error)
        sock.close()
        sys.exit()

    # Start game
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
            if 'A resposta é:' in data:
                input_data += data

                values = get_estane(input_data)

                resp = str(min_cost(values, len(values))) + '\n'

                sys.stdout.write(resp)
                sock.send(resp)

                input_data = ''
            elif 'HACKAFLAG{' in data:
                break
            else:
                input_data += data

    sock.close()
