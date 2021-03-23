def cipher_check(x, y):
    cipher = []
    result = []
    for z in range(0, y):
        cipher.append(10**(y - z - 1))
        temp = 0
    for c in cipher:
        temp = x / c
        temp = int(temp)
        result.append(temp)
        x = x - (temp * c)
    return result
