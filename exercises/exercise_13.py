# Your solution to Exercise 13
def validate(password):
    pw = int(input())
    while pw != password:
        print("Error")
        pw = int(input())
    print("Done")

password = int(input())
validate(password)

# Same issue here:
# Function naming, parameter naming, and type hinting.

# A few important things to note here:
# Don't hesite to use the same name for global and local variables since
# they are in different scopes.