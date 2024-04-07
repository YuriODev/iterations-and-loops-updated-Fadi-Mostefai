# Your solution to Exercise 21
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_factorial(n):
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)
    return sum

n = int(input())
print(sum_factorial(n))