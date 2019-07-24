def get_n(txt):
    index = txt.index(' - N: ') + 6
    n = ''
    while txt[index] != '\n':
        n += txt[index]
        index += 1

    return int(n)


if __name__ == '__main__':
    copos = 'Desafio 92 - N: 1276206274249\n'

    assert get_n(copos) == 1276206274249, 'Wrong value!'
