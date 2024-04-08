# Your solution to Exercise 37

def div(a, b):
    rem = 0
    count = 0
    while True:
        if a - b < 0:
            rem = a
            break
        a -= b
        count += 1
    return f"{count} {rem}"

a = int(input())
b = int(input())
print(div(a,b))