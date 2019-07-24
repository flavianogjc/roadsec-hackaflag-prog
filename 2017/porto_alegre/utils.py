def get_cards(txt):
    index = txt.index(' - (L): ') + 8
    cards = ''
    while txt[index] != '\n':
        cards += txt[index]
        index += 1

    return eval(cards)


if __name__ == '__main__':
    cards = 'Desafio 1 - (L): [7, 1, 2, 4, 10, 2]\n'

    assert get_cards(cards) == [7, 1, 2, 4, 10, 2], 'Wrong values!'
