# Your solution to Exercise 42

def num_seq():
    num = int(input())
    prev = num
    count = 0
    while num != 0:
        num = int(input())
        if prev > num:
            count += 1
        prev = num
    return count

print(num_seq())

# Same Issue:
# Function naming, parameter naming, and type hinting

# Note:
# Approach is nice, couldn't handle it better :)