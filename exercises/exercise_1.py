# Your solution to Exercise 1
def countdown(n):
    for num in range(n, 0, -1):
        print(num)
    print("Start!")

n = int(input())

countdown(n)

# None of the problems required using functions, there is more theory on how
# to use functions in the next chapters with hint typing.

# For example, it's better to rewrite the function definition as:
# def print_countdown(n: int) -> None:


# Since the name of the function is `countdown`, it's better to rename the
# function to `print_countdown` to make it more clear that the function is
# printing the countdown.

# The function `countdown` is not returning anything, so it's better to
# annotate the function with `-> None` to indicate that the function is not
# returning anything.

# The parameter `n` is an integer, so it's better to annotate the parameter
# with `: int` to indicate that the parameter is an integer.

# I would also recommend to use a more descriptive name for the parameter `n`,
# such as `countdown_number` or `countdown_start` to indicate that the
# parameter represents the starting number of the countdown.

# Again, there is no need to use a function in this case, but if you want to
# use a function, the function definition should be annotated with type hints
# to make the code more readable and maintainable.

# You can read further chapters to learn more about functions and type hints.
# The earlier you develop the habits of writting clean code, the better you
# will become at it and the easier uni life will be.