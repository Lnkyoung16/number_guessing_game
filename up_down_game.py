import random

r = random.randint(0,100)
i = 0

while r == i:
    i = int(input("1~99사이의 숫자를 입력해주세요:"))
    if r > i:
        print("up")
    elif r < i:
        print("down")
    else:
        print("정답입니다.")
        break