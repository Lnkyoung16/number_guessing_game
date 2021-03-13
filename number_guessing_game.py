import random

from cipher_check_3 import cipher_check_3

random_number = []

for n in range(0,3):
    random_number.append(random.randint(0,9))
s = 0
a = 1
while s < 3:
    s = 0
    d = 0
    n = 0
    e = 0
    number_input = int(input("숫자를 입력하세요:"))
    input_result = cipher_check_3(number_input)
    for d in range(0, 3):
        for e in range(0, 3):
            if random_number[d] == input_result[e]:
                if d == e:
                    s = s + 1
                else:
                    n = n + 1
    if s > 0 and n > 0:
        print(s, "개의 숫자가 자리와 숫자가 일치합니다. ", n, "개의 숫자가 숫자만 일차합니다.")
    else:
        print("모든 숫자가 일치하지 않습니다.")
    a = a + 1
    if s == 3:
        print("정답입니다! 숫자는 ", random_number[0], random_number[1], random_number[2], "입니다. ", a, "번의 시도를 통하여 맞추셨습니다.")
        break

