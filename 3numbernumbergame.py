import random

from cipher_check_3 import cipher_check_3

random_number = []

for k in range(0, 3):
    if k == 0:
        random_number.append(random.randint(1, 9))
    else:
        random_number.append(random.randint(0, 9))


s = 0
a = 1
while True:
    s = 0
    d = 0
    n = 0
    e = 0
    number_input = int(input("숫자를 입력하세요:"))
    input_result = cipher_check_3(number_input)

    dic_input = {}
    for x in range(0,10):
        y = input_result.count(x)
        dic_input[x] = y

    dic_random = {}
    for c in range(0, 10):
        v = random_number.count(c)
        dic_random[c] = v

    for d in range(0, 3):
        for e in range(0, len(input_result)):
            if random_number[d] == input_result[e]:
                if d == e:
                    s = s + 1
                    temp = random_number[d]
                    dic_random[temp] = dic_random[temp] - 1
                    dic_input[temp] = dic_input[temp] - 1

    for b in range(0, 10):
        while dic_random[b] > 0:
            if dic_input[b] > 0:
                n = n + 1
            dic_random[b] = dic_random[b] - 1
            dic_input[b] = dic_input[b] - 1


    if s > 0 or n > 0:
        if s == 3:
            print("정답입니다! 숫자는 ", random_number[0], random_number[1], random_number[2], "입니다. ", a, "번의 시도를 통하여 맞추셨습니다.")
            break
        else:
            print(s, "개의 숫자가 자리와 숫자가 일치합니다. ", n, "개의 숫자가 숫자만 일치합니다.")
    else:
        print("모든 숫자가 일치하지 않습니다. 또는 맞는 자리의 숫자를 입력하지 않았습니다.")
    a = a + 1