# Your solution to Exercise 24
def even():
    count = 0
    num = int(input())
    while num != 0:
        if num % 2 == 0:
            count += 1
        num = int(input())
    return count

print(even())

# Same Issue:
# Function naming, parameter naming, and type hinting.
