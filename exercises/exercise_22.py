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