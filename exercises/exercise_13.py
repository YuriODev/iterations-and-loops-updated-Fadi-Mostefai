# Your solution to Exercise 13
def validate(password):
    pw = int(input())
    while pw != password:
        print("Error")
        pw = int(input())
    print("Done")

password = int(input())
validate(password)