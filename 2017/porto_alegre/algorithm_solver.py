def brute_force(i, j):
    global array

    if j == i + 1:
        return max(array[i], array[j])
    else:
        return max(array[i] + max(brute_force(i + 1, j - 1), brute_force(i + 2, j)),
                   array[j] + max(brute_force(i + 1, j - 1), brute_force(i, j - 2)))


def solver(arr):
    size, r = len(arr), 0
    mem = [[0] * 4096, [0] * 4096]

    for i in xrange(0, size - 1):
        mem[r][i] = max(arr[i], arr[i + 1])

    for k in xrange(4, size + 1, 2):
        pr = r
        r = 1 - r
        for i in xrange(0, size - k + 1):
            j = i + k - 1
            pi = arr[i] + max(mem[pr][i + 1], mem[pr][i + 2])
            pj = arr[j] + max(mem[pr][i], mem[pr][i + 1])

            mem[r][i] = max(pi, pj)

    return mem[r][0]


if __name__ == '__main__':
    array = [0, 0, 20, 8, 10, 3, 2, 13, 10, 3, 11, 18, 7, 20]

    print solver(array)
    print brute_force(0, len(array) - 1)
