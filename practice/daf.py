import random
value = random.randrange(start=1, stop=100)

fibonacci = 1
n = 0
m = 0
while fibonacci <100:
    print(fibonacci)
    m = n
    n = fibonacci
    fibonacci = m + n

fibonacci_list = [1,1]
n = 1


while fibonacci_list[-1] <100:
    value = fibonacci_list[n-1]+fibonacci_list[n] < 100
    fibonacci_list.append(fibonacci_list[n-1]+fibonacci_list[n])
    n = n + 1

print(fibonacci_list)
