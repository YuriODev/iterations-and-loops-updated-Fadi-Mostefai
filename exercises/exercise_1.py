# Your solution to Exercise 1
def countdown(n):
    for num in range(n, 0, -1):
        print(num)
    print("Start!")

n = int(input())

countdown(n)