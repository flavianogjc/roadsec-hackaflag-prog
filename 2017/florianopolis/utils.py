def get_lista(txt):
    index = txt.index('- (Challs):') + 11
    arr = ''
    while txt[index] != '\n':
        arr += txt[index]
        index += 1

    return eval(arr)


if __name__ == '__main__':
    chall = 'Desafio 1 - (Challs): [[3, 4, 0, 1], [4, 3, 2, 4], [2, 3, 0, 3]]\n'

    assert get_lista(chall) == [[3, 4, 0, 1], [4, 3, 2, 4], [2, 3, 0, 3]], 'Wrong value!'
