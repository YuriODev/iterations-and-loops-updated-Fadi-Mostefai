# Your solution to Exercise 38

def even_diff(n):
    small = 0
    large = 0
    if len(str(n)) <= 1:
        return "False"
    else:
        for digit in str(n):
            if int(digit) > large:
                if small >= large or small == 0:
                    small = large
                large = int(digit)
            elif int(digit) < small:
                small = int(digit)
            elif small == 0:
                small = int(digit)
        return "True" if (large - small) % 2 == 0 else "False"

n = int(input())
print(even_diff(n))