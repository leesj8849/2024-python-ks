inventory = {}
#사용자 모드

#남아있는 음료 확인
#사용자 입력 받기

#관리자 모드

#음료 관리

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