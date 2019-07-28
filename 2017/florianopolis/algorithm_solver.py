def solver(array):
    soma = 0

    for arr in array:
        soma = (soma + sum(arr)) % 4

    return 1 if soma == 0 else 0


if __name__ == '__main__':
    L = [[4, 0, 0, 2], [2, 4, 0, 6], [2, 6, 6, 4], [2, 0, 4, 2], [6, 6, 4, 4], [4, 2, 2, 6], [0, 2, 0, 4], [2, 6, 6, 2],
         [2, 6, 2, 2], [2, 2, 4, 4]]
    print solver(L)
