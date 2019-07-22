# -*- coding: utf-8 -*-


def get_acessos(txt):
    index = txt.index('Acessos: ') + 9
    acessos = ''
    while txt[index] != '\n':
        acessos += txt[index]
        index += 1

    return eval(acessos)


def get_cota(txt):
    index = txt.index('Cota: ') + 6
    cota = ''
    while txt[index] != '\n':
        cota += txt[index]
        index += 1

    return eval(cota)


if __name__ == '__main__':
    acessos = 'Acessos: [1, 2, 1, 11, 11, 5, 3, 1]\n'
    cota = 'Cota: 10\n'

    assert get_acessos(acessos) == [1, 2, 1, 11, 11, 5, 3, 1], 'Wrong list!'
    assert get_cota(cota) == 10, 'Wrong number!'
