import random

from cipher_check import cipher_check


def number_guessing_game(num):

    random_number = []
    number_random = ""

    for k in range(0, num):
        if k == 0:
            p = random.randint(1, 9)
            random_number.append(p)
            number_random = number_random + str(p)
        else:
            p = random.randint(0, 9)
            random_number.append(p)
            number_random = number_random + str(p)

    seat = 0
    attempt = 1
    while True:
        seat = 0
        index_random = 0
        number = 0
        index_input = 0
        number_input = int(input("숫자를 입력하세요:"))
        input_result = cipher_check(number_input,num)

        dic_input = {}
        for x in range(0,10):
            y = input_result.count(x)
            dic_input[x] = y

        dic_random = {}
        for c in range(0, 10):
            v = random_number.count(c)
            dic_random[c] = v

        for index_random in range(0, num):
            for index_input in range(0, len(input_result)):
                if random_number[index_random] == input_result[index_input]:
                    if index_input == index_random:
                        seat = seat + 1
                        temp = random_number[index_random]
                        dic_random[temp] = dic_random[temp] - 1
                        dic_input[temp] = dic_input[temp] - 1

        for b in range(0, 10):
            while dic_random[b] > 0:
                if dic_input[b] > 0:
                    number = number + 1
                dic_random[b] = dic_random[b] - 1
                dic_input[b] = dic_input[b] - 1


        if seat > 0 or number > 0:
            if seat == num:
                print("정답입니다! 숫자는", number_random, "입니다.", attempt, "번의 시도를 통하여 맞추셨습니다.")
                break
            else:
                print(seat, "개의 숫자가 자리와 숫자가 일치합니다. ", number, "개의 숫자가 숫자만 일치합니다.")
        else:
            print("모든 숫자가 일치하지 않습니다. 또는 맞는 자리의 숫자를 입력하지 않았습니다.")
        attempt = attempt + 1


number_guessing_game(int(input("몇 자리의 수를 맞추시겠습니까? :")))