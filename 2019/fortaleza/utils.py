# -*- coding: utf-8 -*-


def get_digit(txt):
    index = txt.index('Dígito: ') + 8
    digit = ''
    while txt[index] != '\n':
        digit += txt[index]
        index += 1

    return int(digit)


def get_limits(txt):
    index = txt.index('Quartos: ') + 9
    interval = ''
    while txt[index] != '\n':
        interval += txt[index]
        index += 1

    return eval(interval)


if __name__ == '__main__':
    quartos = 'Quartos: [1, 10]\n'
    digito = 'Dígito: 1\n'

    assert get_limits(quartos) == [1, 10], 'Wrong interval!'
    assert get_digit(digito) == 1, 'Wrong digit!'


