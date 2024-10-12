size = int(input("수학 시험 점수를 입력해주세요."))
print(size)

if size < 0 or size > 100:
    print("잘못된 정수입니다.")
else:
    if size >= 90:
        print("상반")
    elif size >= 70:
        print("중반")
    else:
        print("하반")