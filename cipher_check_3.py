def cipher_check_3(X):
    result = []
    if X < 1000 and X >= 100:
        cipher = [100, 10, 1]
        temp = 0
        for c in cipher:
            temp = X / c
            temp = int(temp)
            result.append(temp)
            X = X - (temp * c)
    else:
        print("3자리 숫자를 입력해주세요.")
    return result

