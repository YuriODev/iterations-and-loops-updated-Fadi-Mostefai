def convert(lb):
    for i in range(1, lb + 1):
        kg = i * 0.453
        kg = round(kg, 2)
        print(f"{i} {kg}")

lb = int(input())
convert(lb)

# Same issue here:
# Function naming, parameter naming, and type hinting.