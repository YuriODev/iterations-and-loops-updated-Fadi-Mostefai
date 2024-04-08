# Your solution to Exercise 39

def digit(n):
    sum = 0
    if n < 0:
        n = n * -1
    for digit in str(n):
        sum += int(digit)
    return sum

n = int(input())
print(digit(n))