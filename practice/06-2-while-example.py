import random
result = 0

while result // 100 == (result // 10) % 10 or result // 100 == result % 10 or (result // 10) % 10 == result % 10:
    result = random.randrange(1, 1000)
    print(result)

user_input = input("값을 맞춰보세요 ::")

S = 0
#B= 0

