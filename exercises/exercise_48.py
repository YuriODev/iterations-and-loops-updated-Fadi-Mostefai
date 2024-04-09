# Your solution to Exercise 48
def num_pal(n):
    count = 0
    num = 1
    rev_num = 0
    while num <= n:
        temp = num
        while num != 0:
            last_digit = num % 10
            rev_num = rev_num * 10 + last_digit
            #print(f"Num: {num}, rev_num: {rev_num}")
            num = num // 10
        if rev_num == temp:
            count += 1
        num = temp
        num += 1
        rev_num = 0
    return count

n = int(input())
print(num_pal(n))