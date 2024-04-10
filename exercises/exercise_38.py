# Your solution to Exercise 38

def even_diff(n):
    large = 0
    small = 0
    if n == 0:
        return False
    else:
        while n != 0:
            last_digit = n % 10
            n = n // 10
            if last_digit > large:
                if small == 0:
                    small = large
                large = last_digit
            elif small == 0:
                small = last_digit
            elif last_digit < small:
                small = last_digit
        return True if (large - small) % 2 == 0 else False

n = int(input())
print(even_diff(n))