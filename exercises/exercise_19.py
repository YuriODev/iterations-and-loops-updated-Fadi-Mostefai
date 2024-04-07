# Your solution to Exercise 19

def squares(n):
    for i in range(10, 100):
        str_num = str(i)
        if ((int(str_num[0]) ** 2) + (int(str_num[1]) ** 2)) % n != 0:
            continue
        print(i, end=", ")

n = int(input())
squares(n)
