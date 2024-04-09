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