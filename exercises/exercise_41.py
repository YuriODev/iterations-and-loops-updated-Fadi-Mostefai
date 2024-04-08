# Your solution to Exercise 41

def fib_digit(n):
    term1 = 0
    term2 = 1
    if n == 1:
        return term2
    else:
        term = 0
        for _ in range(n-1):
            term = term1 + term2
            term1 = term2
            term2 = term
        return term
    
n = int(input())
print(fib_digit(n))