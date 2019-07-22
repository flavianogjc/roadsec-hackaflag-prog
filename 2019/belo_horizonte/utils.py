# -*- coding: utf-8 -*-


def get_copos(txt):
    index = txt.index('Copos: ') + 7
    valores = ''
    while txt[index] != '\n':
        valores += txt[index]
        index += 1

    return eval(valores)


if __name__ == '__main__':
    copos = 'Copos: [1, 2, 4, 8]\n'

    assert get_copos(copos) == [1, 2, 4, 8], 'Wrong values!'
