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
            num = num // 10
        if rev_num == temp:
            count += 1
        num = temp
        num += 1
        rev_num = 0
    return count

n = int(input())
print(num_pal(n))

# Same Issue:
# Function naming, parameter naming, and type hinting
# Approach is nice, well done! :)

# Refactored solution:
# def count_palindromic_numbers_up_to(target_number: int) -> int:
#     count = 0
#     current_number
#     reversed_number = 0
#     while current_number <= target_number:
#         temp_number = current_number
#         while current_number != 0:
#             last_digit = current_number % 10
#             reversed_number = reversed_number * 10 + last_digit
#             current_number //= 10
#         if reversed_number == temp_number:
#             count += 1
#         current_number = temp_number
#         current_number += 1
#         reversed_number = 0
#     return count

# I hope you can see how clear and readable this is compared to the original solution. :)