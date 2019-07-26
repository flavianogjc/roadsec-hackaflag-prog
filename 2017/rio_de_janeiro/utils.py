def get_n(txt):
    index = txt.index(' - (N): ') + 8
    number = ''
    while txt[index] != '\n':
        number += txt[index]
        index += 1

    return eval(number)


if __name__ == '__main__':
    entry = 'Teste 1 - (N): 5\n'

    assert get_n(entry) == 5, 'Wrong value!'
