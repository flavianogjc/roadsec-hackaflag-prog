def get_n(txt):
    index = txt.index('- N:') + 4
    arr = ''
    while txt[index] != '\n':
        arr += txt[index]
        index += 1

    return eval(arr)


if __name__ == '__main__':
    chall = 'Desafio 1 - N: 7\n'

    assert get_n(chall) == 7, 'Wrong value!'
