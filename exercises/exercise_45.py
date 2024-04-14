# Your solution to Exercise 45
def sign_changes():
    num = int(input())
    prev = num
    count = 0
    while num != 0:
        num = int(input())
        if (prev < 0 and num > 0) or (prev > 0 and num < 0):
            count += 1
        prev = num
    return count

print(sign_changes())

# Same Issue:
# Function naming, parameter naming, and type hinting

# Note:
# Can change function name to get_sign_changes() -> int:
# Or get_count_of_sign_changes() -> int:

# Logic is indeed correct, but can be even more simplified like in the solution
# but I still like the approach, well done :)