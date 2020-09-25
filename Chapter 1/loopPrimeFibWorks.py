#Justin Cortez Wartell

#Backwards Loop
begin = 5
lines = begin
for line in range(lines):
    for number in range(begin-line,0,-1):
        print(number, end=' ')
    print()
print()

#Prime Numbers
start = 25
end = 50

for i in range(start,end):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
print()

#Fibonacci Sequence
def fib(number_of_terms):
   counter = 0

   first = 0
   second = 1
   temp = 0

   while counter <= number_of_terms:
      print(first)
      temp = first + second
      first = second
      second = temp
      counter = counter + 1

fib(9)
