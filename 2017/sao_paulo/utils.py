def get_itp(txt):
    index = txt.index(' - (I, T, P): ') +14
    number = '['
    while txt[index] != '\n':
        number += txt[index]
        index += 1

    return eval(number + ']')


if __name__ == '__main__':
    entry = 'Teste 1 - (I, T, P): 1, 4, 3\n'

    assert get_itp(entry) == [1, 4, 3], 'Wrong value!'
