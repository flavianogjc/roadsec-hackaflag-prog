def bad_solution(arr, cota):
    bigger, a, b = -1, None, None
    for i in xrange(len(arr)):
        for j in xrange(i, len(arr)):
            s = sum(arr[i:j + 1])
            p = j - i + 1

            if s > p * cota and p > bigger:
                bigger, a, b = p, i, j

    if a is None or b is None:
        return 0
    else:
        return abs(b - a) + 1


def search(arr, s, e, key):
    ans = -1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] - key > 0:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


def longest_subarray(arr, n):
    suffix_sum = [0]*(n + 1)

    for i in xrange(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    search_space, index = [0]*n, [0]*n

    resp, j = 0, 0
    for i in xrange(n):
        if j == 0 or (suffix_sum[i] > search_space[j - 1]):
            search_space[j] = suffix_sum[i]
            index[j] = i
            j += 1

        idx = search(search_space, 0, j - 1, suffix_sum[i + 1])

        if idx != -1:
            resp = max(resp, i - index[idx] + 1)

    return resp


def good_solution(arr, cota):
    new_arr = map(lambda x: x - cota, arr)

    return longest_subarray(new_arr, len(new_arr))


if __name__ == '__main__':
    acessos, cota = [10, 7, 6, 14, 14, 13, 8, 6, 14], 7

    print(bad_solution(acessos, cota))
    print(good_solution(acessos, cota))
