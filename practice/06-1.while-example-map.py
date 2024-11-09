X = ""
Y = ""
X = 0
Y = 0
a = ""
a = str(input("어디로 이동하시겠습니까"))
while a != "UP" or "DOWN" or "LEFT" or "RIGHT":
    input("어디로 이동하시겠습니까")
if a == "UP":
  X = X
  Y = Y + 1
  print((X,Y))

if a == "DOWN":
  X = X
  Y = Y - 1
  print((X,Y))

if a == "LEFT":
    X = X - 1
    Y = Y
    print((X,Y))

if a == "RIGHT":
  X = X + 1
  Y = Y
  print((X,Y))