# Your solution to Exercise 47

def palindrome(n):
    last_pal = 1
    while True:
        print(last_pal, end=" ")
        if last_pal < 9:
            last_pal += 1
        elif last_pal == 9:
            last_pal += 2
        elif 11 <= last_pal < 99:
            last_pal += 11
        elif last_pal == 99:
            last_pal += 2
        elif ((last_pal // 10) % 10) == 9:
            last_pal += 11
        else:
            last_pal += 10
        if last_pal >= n:
            break
        

n = int(input())
palindrome(n)

# Same Issue:
# Function naming, parameter naming, and type hinting

# Notes:
# This is indeed a nice solution (!), but it is not a palindrome function.
# It is a function that prints palindromic numbers up to n.
# The function name should reflect this.

# The approach is really unique, I never saw this before, well done! :)
# Unfortunately, the solution will break once it reaches 1000, but it is still a nice approach!
# The tests didn't cover the case, I believe.

# I think you can try to refactor the code to make it work up to 10^5 using the same logic