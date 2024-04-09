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
            
