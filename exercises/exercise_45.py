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