def calculate(x):
    return 3*x + 5

print( calculate(5) )
print( calculate(3) )
print (calculate(1) )

print("##########################################")

def warm_up():
    print("음료를 데웁니다.")

def add_ice():
    print("얼음을 넣습니다")

def add_esspresso():
    print("esspresso를 넣습니다.")

def add_water():
    print("물을 넣습니다.")

def add_milk():
    print("우유를 넣습니다.")

def add_cocoa():
    print("코코아를 넣습니다.")

print("메뉴:핫에스프레소/아이스아메리카노/핫모카라떼/아이스라떼/아이스코코아")

a = ""

a = str(input("메뉴를 입력해주세요"))

if a == "핫에스프레소":
    add_esspresso()

if a == "아이스아메리카노":
    add_ice()
    add_water()
    add_esspresso()

if a == "핫모카라떼":
    add_milk()
    warm_up()
    add_esspresso()
    add_cocoa()

if a == "아이스라떼":
    add_ice()
    add_milk()
    add_esspresso()

if a == "아이스코코아":
    add_ice()
    add_milk()
    add_cocoa()

def calculate_payment(drinks, quantity):

    prices = {
        '커피': 2000,
        '차': 1500,
        '주스': 2500,
        '물': 1000
    }

    if quantity >= 1 and drinks in prices:
        total_price = prices[drinks] * quantity
        print(f'{drinks} {quantity}개에 대한 총 금액은 {total_price}원입니다.')
    else:
        print('음료 또는 수량이 유효하지 않습니다.')


calculate_payment('커피', 2)
calculate_payment('주스', 0)