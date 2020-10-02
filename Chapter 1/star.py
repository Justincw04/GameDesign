size=8
for line in range(size):
    for number in range(size-line,0,-1):
        print("*", end=' ')

    for number in range(begin):
        print("*", end=' ')
    print()

for line in range(1,10):
    print()
    for space in range(9-line):
        print(" ", end=' ')
    for number in range(line):
        print("*", end=' ')
