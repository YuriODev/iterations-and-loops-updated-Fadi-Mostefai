# Your solution to Exercise 33
def table(n):  # Function naming, parameter naming, and type hinting. 'print_table' is a better name.
    '''  # Docstring missing. ''' # In such short functions, docstrings can help to understand the purpose of the function.
    for i in range(n):
        print(("-1\t" * i) + "0\t" + ("1\t" * (n-i-1)))

n = int(input())
table(n)
