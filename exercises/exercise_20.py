# Your solution to Exercise 20
def odd(b):
    for i in range(1, b+1, 2):
        print(i, end=" ")

b = int(input())
odd(b)