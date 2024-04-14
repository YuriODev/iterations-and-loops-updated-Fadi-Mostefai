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


# Same issue here:
# Function naming, parameter naming, and type hinting.

# A few important things to note here:
# 1) You were not supposed to use any string tricks to solve this problem.
# 2) sum += (i)/(i+1) is the same as sum += i/(i+1)
# 3) Could have used f-strings to format the output instead of rounding
# 4) No need to use else statement here. You can just return sum at the end.