def min_cost(arr, n):
    cost = 0
    arr.sort()

    k = arr[n // 2]

    for i in xrange(0, n):
        cost = cost + abs(arr[i] - k)

    temp_cost = 0
    if n % 2 == 0:
        k = arr[n // 2 - 1]

    for i in xrange(0, n):
        temp_cost = temp_cost + abs(arr[i] - k)

    cost = min(cost, temp_cost)

    return cost


if __name__ == '__main__':
    estante = [1, 2, 3, 4, 5, 6]

    print(min_cost(estante, len(estante)))
