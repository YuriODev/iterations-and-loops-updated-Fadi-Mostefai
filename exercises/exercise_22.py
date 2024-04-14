# Your solution to Exercise 22
def pattern(num):
    if num < 10:
        print(num)
    else:
        num = num // 10
        while num != 0:
            print(num)
            num = num // 10

n = int(input())
pattern(n)

# Same issue here:
# Function naming, parameter naming, and type hinting.

# Nice trick with line 3 to check if the number is less than 10,
# really liked it ! :)