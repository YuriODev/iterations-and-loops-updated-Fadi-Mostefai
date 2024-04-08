# Your solution to Exercise 11

def series(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i)/(i+1)
    sum = round(sum, 2)
    if len(str(sum)) == 3:
        return str(sum) + "0"
    else:
        return sum

n = int(input())
print(series(n))
