# Your solution to Exercise 46

def search(nums, num):
    count = 1
    last_digit = nums % 10
    new_nums = nums // 10
    while True:
        if last_digit == num:
            return count
        elif new_nums == 0:
            return 0
        last_digit = new_nums % 10
        new_nums = new_nums // 10
        count += 1
        
    
nums = int(input())
num = int(input())
print(search(nums, num))
            
# Same Issue:
# Function naming, parameter naming, and type hinting

# Note:
# Could have used variable naming provided in readme: 'n' and 'd'.
# Function MUST clarify what it does, so 'search' is not a good name.
# 'get_index_of_digit' would be better.

# Trick with return statements is nice, well done! :)

# Refactored solution:
# def get_index_of_digit(n: int, target_digit: int) -> int:
#     index = 1
#     last_digit = n % 10
#     new_n = n // 10
#     while True:
#         if last_digit == target_digit:
#             return index
#         elif new_n == 0:
#             return 0
#         last_digit = new_n % 10
#         new_n = new_n // 10
#         index += 1
# 
# I hope you can see how clear and readable this is compared to the original solution. :)
