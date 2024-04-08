# Your solution to Exercise 29
def series():
    num = int(input())
    sum1 = num
    sum2 = num ** 2
    while sum1 != 0:
        num = int(input())
        sum1 += num
        sum2 += num ** 2
    return sum2

print(series())
    