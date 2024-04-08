# Your solution to Exercise 40

def fibonacci(n):
    fibonacci_seq = "1"
    term1 = 0
    term2 = 1
    while True:
        term = term1 + term2
        if term >= n:
            break
        fibonacci_seq += " " + str(term)
        term1 = term2
        term2 = term
    return fibonacci_seq

n = int(input())
print(fibonacci(n))