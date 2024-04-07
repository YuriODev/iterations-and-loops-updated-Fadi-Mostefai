# Your solution to Exercise 25
def car(d, t):
    total_distance = d
    days = 1
    while total_distance <= t:
        total_distance += 1.1 * d
        d = 1.1 * d
        days += 1
    return f"{total_distance:.2f} km, {days} days"

d = int(input())
t = int(input())
print(car(d,t))
