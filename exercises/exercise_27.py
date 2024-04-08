# Your solution to Exercise 27

def picalc(n):
    Pi = 0
    count = 1
    for _ in range(n):
        if count % 4 == 1:
            Pi += 4/count
        elif count % 4 == 3:
            Pi -= 4/count
        count += 2
    return Pi

n = int(input())
print(picalc(n))