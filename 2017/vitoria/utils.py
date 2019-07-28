def get_ps(txt):
    index = txt.index(' - (P, S):') + 10
    number = ''
    while txt[index] != '\n':
        number += txt[index]
        index += 1

    return eval(number)


if __name__ == '__main__':
    entry = 'Teste 1 - (P, S): 3, 2\n'

    assert get_ps(entry) == (3, 2), 'Wrong value!'
