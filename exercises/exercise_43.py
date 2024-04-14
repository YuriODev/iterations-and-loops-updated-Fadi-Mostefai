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

# Same Issue:
# Function naming, parameter naming, and type hinting

# Note:
# Better to avoid input() function in the function itself for future cases,
# but I understand that you can't do it in this case.

# Example how to improve:
# deg get_second_largest() -> int:
#     num = int(input())
#     second_largest = 0
#     largest = num
#     while num != 0:
#         num = int(input())
#         if num > largest:
#             if second_largest == 0:
#                 second_largest = largest
#             largest = num
#         elif second_largest < num <= largest:
#             second_largest = num
#     return second_largest


