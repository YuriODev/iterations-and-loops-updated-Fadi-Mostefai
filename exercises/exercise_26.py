# Your solution to Exercise 26
def intsum(n):
    count = 0
    for num in range(100, 1000):
        sum = 0
        while num != 0:
            last_digit = num % 10
            num = num // 10
            sum += last_digit
        if sum == n:
            count += 1
    return count

n = int(input())
print(intsum(n))
