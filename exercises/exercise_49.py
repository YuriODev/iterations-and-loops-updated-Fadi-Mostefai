# Your solution to Exercise 49

def pal(a,b):
    for i in range(a, b+1):
        num = i
        rev_num = 0
        while num != 0:
            last_digit = num % 10
            rev_num = rev_num * 10 + last_digit
            num = num // 10
        if rev_num == i:
            print(i, end=" ")

a = int(input())
b = int(input())
pal(a,b)