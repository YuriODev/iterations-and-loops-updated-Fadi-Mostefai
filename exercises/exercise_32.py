# Your solution to Exercise 32

def speed(n):
    small = 0
    large = 0
    count = 0
    if n == 1:
        num = int(input())
        count = 1 if num <= 30 else 0
        return f"{0}\n{count}"
    else:
        for _ in range(n):
            num = int(input())
            if num >= large:
                if small >= large or small == 0:
                    small = large
                large = num
            if num <= 30:
                count += 1
        return f"{large - small}\n{count}"

n = int(input())
print(speed(n))
    