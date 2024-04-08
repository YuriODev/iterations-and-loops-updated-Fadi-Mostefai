# Your solution to Exercise 30

def amoeba(t):
    num = t // 3
    sum = 1
    for _ in range(num):
        sum = sum * 2
    return sum

t = int(input())
print(amoeba(t))