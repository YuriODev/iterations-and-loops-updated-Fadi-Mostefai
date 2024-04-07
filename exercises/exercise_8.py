# Your solution to Exercise 8
def even(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            continue
        if i < n-1:
            print(i, end=" ")
        elif i == n-1 or i == n:
            print(i)

n = int(input())
even(n)