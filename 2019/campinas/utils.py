# -*- coding: utf-8 -*-


def get_estane(txt):
    index = txt.index('/50: ') + 5
    valores = ''
    while txt[index] != '\n':
        valores += txt[index]
        index += 1

    return eval(valores)


if __name__ == '__main__':
    estante = 'Estante 1/50: [1, 2, 3, 4, 5, 6]\n'

    assert get_estane(estante) == [1, 2, 3, 4, 5, 6], 'Wrong values!'
