# Your solution to Exercise 17
def pattern(n, m):
    for i in range(n):
        for _ in range(m):
            print(i, end="\t")
        print()
    print()
            

n = int(input())
m = int(input())
pattern(n,m)

#print("0\t0\t0\t\n1\t1\t1\t\n2\t2\t2\t\n3\t3\t3\t\n4\t4\t4\t\n5\t5\t5\t\n")

# Same issue here:
# Function naming, parameter naming, and type hinting.

# A few important things to note here:
# Amazing approach to printing the pattern.