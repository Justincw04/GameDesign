x=0
#controls where it wil finish
#will break if number is over 10
y=10
for line in range(x,y):
    #mkae sure each number is on a diffrent line
    print()
#both loops uses line to control flow
    for space in range (9-line):
        #prints spaces on first side
        print(" ",end='')
    for number in range (line,0,-1):
        #prints the first side numbers
        print (line,end ='')
        line=line-1
    #prints space in between both sides
    print (' ',end ='')
    for number in range(line-1):
        #prints the second set of numbers
        print (number, end = '')
print()
print()

num=int(9)
for i in range(1,num+1):
          # Print leading space
          for j in range(1,num-i+1):
               print(end=" "),
          # Print numbers
          for j in range(i, 0, -1):
               print(j,end="")
          for j in range(2, i + 1):
               print(j,end="")
          print()
