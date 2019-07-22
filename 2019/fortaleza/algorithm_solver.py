def bad_solution(a, b, digit):
    total_digit = 0
    digit = str(digit)
    for num in xrange(a, b + 1):
        total_digit += str(num).count(digit)

    return total_digit


def good_solution(a, b, digit):
    max_pow = 20
    resp = [0] * 10
    a -= 1
    arr = [pow(10, i) for i in xrange(max_pow+1)]

    for j in xrange(max_pow, -1, -1):
        if a >= arr[j]:
            c = a / arr[j]
            d = a % arr[j]
            e = c % 10
            c /= 10

            for i in xrange(0, e):
                resp[i] += arr[j] * (c + (1 if i else 0))

            resp[e] += arr[j] * (c - (0 if e else 1)) + d + 1

            for i in xrange(e + 1, 10):
                resp[i] += arr[j] * c

    for j in xrange(max_pow, -1, -1):
        if b >= arr[j]:
            c = b / arr[j]
            d = b % arr[j]
            e = c % 10
            c /= 10

            for i in xrange(0, e):
                resp[i] -= arr[j] * (c + (1 if i else 0))

            resp[e] -= arr[j] * (c - (0 if e else 1)) + d + 1

            for i in xrange(e + 1, 10):
                resp[i] -= arr[j] * c

    return abs(resp[digit])


if __name__ == '__main__':
    while True:
        a, b = map(int, raw_input().split())

        if a == 0 and b == 0:
            break

        d = input()

        resp1 = bad_solution(a, b, d)
        resp2 = good_solution(a, b, d)

        print resp1, resp2
