# Your solution to Exercise 12
def sum(n):
    sum = 0
    for i in range(100, 1000):
        if i % n != 0:
            continue
        sum += i
    return sum

n = int(input())
print(sum(n))