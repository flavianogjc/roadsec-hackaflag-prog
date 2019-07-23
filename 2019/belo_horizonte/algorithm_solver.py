def find_best_value(arr):
    arr.sort()

    size, i = len(arr), 0
    best_value = float('inf')
    while True:
        sl, sr = sum(arr[0:i]), sum(arr[i:])

        possible_best_value = (sr + 2.0 * sl) / (size + i)

        if best_value > possible_best_value:
            best_value = possible_best_value
        else:
            break

        i += 1

    return best_value


if __name__ == '__main__':
    copos = [1, 2, 4, 8]

    print(find_best_value(copos))
