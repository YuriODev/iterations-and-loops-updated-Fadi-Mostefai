# Your solution to Exercise 44
def index():
    num = int(input())
    prev = num
    count = 1
    i = 0
    while num != 0:
        num = int(input())
        if num >= prev:
            prev = num
            i = count
        count += 1
    return i

print(index())

# Same Issue:
# Function naming, parameter naming, and type hinting

# Logic is correct, but functin name and parameter name could be better, ex:
# def get_index_of_largest_number() -> int: