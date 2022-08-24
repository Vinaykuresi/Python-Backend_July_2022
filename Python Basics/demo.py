rows = 5
for row in range(rows, 0, -1):
    for col in range(rows-row):
        print(" ", end="")
    for col in range(2*row-1):
        print("*", end="")
    print()