inventory = {}
#사용자 모드

if not inventory :
    print("X")
elif inventory :
    answer = input("선택")
    if inventory.key == answer:
        print("O")
    else:
        print("X")

#관리자 모드
c = input("입력")
if c in inventory:
    print()
elif not c in inventory:
    print()