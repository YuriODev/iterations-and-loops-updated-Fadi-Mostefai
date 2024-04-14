# Your solution to Exercise 52

def odd_num(a,b):
    i = (a - 1) * (a % 2 == 0) + a * (a % 2 == 1)
    while b <= i <= a:
        print(i, end=" ")
        i -= 2

a = int(input())
b = int(input())
odd_num(a,b)

# Same Issue:
# Function naming, parameter naming, and type hinting

# That's definitely the most unique solution I've seen so far! :D
# while loop condition is still branchy, but it's okay, it's unique! :)