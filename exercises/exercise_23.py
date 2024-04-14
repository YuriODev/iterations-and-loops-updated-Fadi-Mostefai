# Your solution to Exercise 23

def average():
    sum = 0
    count = 0
    num = int(input())
    if num == 0:
        count = 1
    else:
        while num != 0:
            sum += num
            count += 1
            num = int(input())
    av = sum / count
    return av

print(average())

# Issue here:
# Function naming, parameter naming, and type hinting.

# Notes:
# Line 7: if num == 0,  you could return 0.0 straight away without using
# else statement, which makes the code cleaner and less overwhemling.