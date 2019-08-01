# -*- coding: utf-8 -*-


def get_interval(txt):
    index = txt.index('Número entre ') + 13
    arr = ''
    while txt[index] != '\n':
        arr += txt[index]
        index += 1

    return max(eval(arr))


def get_result_cmp(txt):
    index = txt.index('Comparação:') + 13
    arr = ''
    while txt[index] != '\n':
        arr += txt[index]
        index += 1

    return eval(arr)


if __name__ == '__main__':
    entry = 'Partida 1 \ 10 - Número entre [0, 10]\n'
    cmp = 'Comparação: 1\n'

    assert get_interval(entry) == max([0, 10]), 'Wrong value!'
    assert get_result_cmp(cmp) == 1, 'Wrong cmp!'
