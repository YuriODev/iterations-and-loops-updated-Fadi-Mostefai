# Your solution to Exercise 44
def index():
    num = int(input())
    prev = num
    count = 1
    i = 0
    while num != 0:
        num = int(input())
        if num >= prev:
            prev = num
            i = count
        count += 1
    return i

print(index())