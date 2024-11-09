x = 0
y = 0
a = ""
a = str(input("어디로 이동하시겠습니까"))
while a != "UP" or "DOWN" or "LEFT" or "RIGHT":
    input("어디로 이동하시겠습니까")
if a == "UP":
  x = x
  y = y + 1
  print(x,y)

if a == "DOWN":
  x = x
  y = y - 1
  print(x,y)

if a == "LEFT":
    x = x - 1
    y = y
    print(x,y)

if a == "RIGHT":
  x = x + 1
  y = y
  print(x,y)