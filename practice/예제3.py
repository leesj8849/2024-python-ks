a = str(input("당신은 주말에 집에서 혼자 시간을 보내는 것을 선호하나요? (Y/N)"))
print(a)

if a == ("Y" or "y"):
    print("E")
elif a == ("N" or "n"):
    print("I")

b = str(input("꼬리에 꼬리를 무는 밸런스 게임(만약에~)을 하면 힘든가요?(Y/N)"))
print(b)

if b == ("Y" or "y"):
    print("S")
elif b == ("N" or "n"):
    print("N")

c = str(input("슬픔을 둘로 나누면 슬과 픔이다?(Y/N)"))
print(c)

if c == ("Y" or "y"):
    print("T")
elif c == ("N" or "n"):
    print("F")

d = str(input("계획했던 식당이 갑자기 휴무면 오히려 새로운 식당을 가볼수 있어서 개이득인가요?(Y/N)"))
print(d)

if d == ("Y" or "y"):
    print("P")
elif d == ("N" or "n"):
    print("J")