# Your solution to Exercise 16
def pattern(n):
    for i in range(1, n+1):
        print((" " * (n-i)) + ("#" * i))

n = int(input())
pattern(n)