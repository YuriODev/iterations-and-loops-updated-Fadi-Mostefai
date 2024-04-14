# Your solution to Exercise 51

def three_digit(a,b):
    for i in range(a, b+1):
        set_num = set()
        num = i
        count1 = 0
        count2 = 0
        while num != 0:
            last_digit = num % 10
            set_num.add(last_digit)
            num = num // 10
        if len(set_num) <= 2:
            num = i
            for x in set_num:
                while num != 0:
                    last_digit = num % 10
                    if last_digit == x:
                        count1 += 1
                    else:
                        count2 += 1
                    num = num // 10
            if (count1 == 1 and count2 == 3) or (count1 == 3 and count2 == 1) or count1 == 4 or count2 == 4:
                print(i, end=" ")
a = int(input())
b = int(input())
three_digit(a,b)

# Same Issue:
# Function naming, parameter naming, and type hinting

# Notes:
# 1. Very confusing to understand what 'count1' and 'count2' are doing
# 2. Since we know limits of 4 digits, we can use a better approach, such as
# extracting all 4 digits and checking if they are all different without any
# need to use loops.
# 3. Using set is a good idea, but the implementation is not optimal, they are
# not needed at all in this case.

