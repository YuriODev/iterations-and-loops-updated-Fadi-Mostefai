# Your solution to Exercise 43
def sec_largest():
    num = int(input())
    second_large = 0
    large = num
    while num != 0:
        num = int(input())
        if num > large:
            if second_large == 0:
                second_large = large
            large = num
        elif second_large < num <= large:
            second_large = num
    return second_large

print(sec_largest())