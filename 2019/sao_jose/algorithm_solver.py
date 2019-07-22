def subset_sum(numbers, a, b, resp, partial=[]):
    s = sum(partial)

    if a <= s <= b:
        resp[0] += 1
    elif s > b:
        return 0

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, a, b, resp, partial + [n])

    return resp[0]


if __name__ == '__main__':
    carteira = [373855989138066, 556488356944812, 154705727082386, 168092805984127, 192060818031248, 106184696120671,
                407350722473536, 484755556412362, 257393022726648, 148071191691731, 471449453127929, 71294319498098,
                40902986764531, 207815624728425, 497928977965028, 241732567568920, 343836421729388, 308045109484220,
                278001755374495, 176300185843694, 500602745842102, 430715926410501, 489300745576939, 440178991589914,
                525447008611626, 13799867818919, 540847010654305, 316875074800483, 100339466859318, 390837174755932,
                66397537881064, 520661536457041, 237881861006016, 30406496951639, 219257285594114]
    intervalo = [88194738935762, 106727356134209]

    print(subset_sum(carteira, intervalo[0], intervalo[1], [0]))
