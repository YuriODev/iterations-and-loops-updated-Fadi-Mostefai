# Your solution to Exercise 36

def GCD(a, b):
    while True:
        if a == 0:
            return b
        elif b == 0:
            return a
        temp = a
        a = b
        b = temp % b

    #if a == 0:
        #return b
    #elif b == 0:
        #return a
    #else:
        #return GCD(b, a % b)
    
a = int(input())
b = int(input())
print(GCD(a,b))