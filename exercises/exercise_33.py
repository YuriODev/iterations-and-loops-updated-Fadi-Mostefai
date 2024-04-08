# Your solution to Exercise 33
def table(n):
    for i in range(n):
        print(("-1\t" * i) + "0\t" + ("1\t" * (n-i-1)))

n = int(input())
table(n)