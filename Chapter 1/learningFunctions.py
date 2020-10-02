#Justin Cortez Wartell
#Learning About Functions
def testing_Functions(): #define the function and expects no parameters
    print("1\n"+"2\n"+"3\n"+"4\n")
    print("1\n")
    print("2 2\n")
    print("3 3 3\n" )
def running_Loops(lines):
    line=int(lines)
    for i in range(10):
        print(i)
    for j in range(1,10):
        print(j,end = '')
        print(" ", end= '')
    print()
    print("i am done")
    print("...")
def loops_rows_col(row,col):
    for rows in range(row):
        for cols in range(col):
            print('*',end='')
        print()
loops_rows_col(5,10)
running_Loops(1)
for y in range(1):
    testing_Functions()


names=["Ali","Justin","Daniel","Jake","Rohan"]
print(names[2])
for i in range(5):
    print(names[i])
