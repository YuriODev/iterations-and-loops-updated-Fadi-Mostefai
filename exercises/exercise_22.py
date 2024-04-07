# Your solution to Exercise 22
def pattern(num):
    str_num = str(num)
    if len(str_num) > 1:
        for _ in range(len(str_num) - 1):
            num = num // 10
            print(num)
    else:
        print(num)


n = int(input())
pattern(n)