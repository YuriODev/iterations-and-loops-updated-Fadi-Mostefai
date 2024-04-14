# Your solution to Exercise 19

def squares(n):
    for i in range(10, 100):
        str_num = str(i)
        if ((int(str_num[0]) ** 2) + (int(str_num[1]) ** 2)) % n != 0:
            continue
        print(i, end=", ")

n = int(input())
squares(n)

# Same issue here:
# Function naming, parameter naming, and type hinting.

# A few important things to note here:
# 1. Expected to use % and // operators to extract digits from a number.
# 2. Convertion to string is not necessary + can be memory intensive for large numbers.