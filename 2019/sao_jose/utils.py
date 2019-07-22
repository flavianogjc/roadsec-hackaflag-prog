# -*- coding: utf-8 -*-


def get_carteira(txt):
    index = txt.index('Valores: ') + 9
    valores = ''
    while txt[index] != '\n':
        valores += txt[index]
        index += 1

    return eval(valores)


def get_interval(txt):
    index = txt.index('Intervalo: ') + 11
    limits = ''
    while txt[index] != '\n':
        limits += txt[index]
        index += 1

    return eval(limits)


if __name__ == '__main__':
    carteira = 'Valores: [1, 3, 5, 7, 9]\n'
    intervalo = 'Intervalo: [8, 10]\n'

    assert get_carteira(carteira) == [1, 3, 5, 7, 9], 'Wrong values!'
    assert get_interval(intervalo) == [8, 10], 'Wrong interval!'
