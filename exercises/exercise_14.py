# Your solution to Exercise 14
def count(n):
    sum = 0
    for _ in range(n):
        num = int(input())
        if num == 0:
            sum += 1
    return sum

n = int(input())
print(count(n))