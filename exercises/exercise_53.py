# Your solution to Exercise 53
def even_num(a, b):
    i = (a + 1) * (a % 2 == 1) + (a) * (a % 2 == 0)
    while a <= i <= b:
        print(i, end=" ")
        i += 2

a = int(input())
b = int(input())
even_num(a,b)