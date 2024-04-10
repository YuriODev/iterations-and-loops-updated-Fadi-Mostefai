# Your solution to Exercise 39

def digit(n):
    sum = 0
    if n < 0:
        n = n * -1
    while n != 0:
        last_digit = n % 10
        n = n // 10
        sum += last_digit
    return sum

n = int(input())
print(digit(n))