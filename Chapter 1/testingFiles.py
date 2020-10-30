#Justin Cortez Wartell
#10/28/20
#Learning about Files
myFile = open("newFile.txt", "w")
myFile.write("I am adding some stuff")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()
myFile = open("newFile.txt", "w")
myFile.write("I deleted some stuff")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()
myFile = open("newFile.txt", "a")
myFile.write("I am adding even more stuff")
myFile.close()
myFile = open("newFile.txt", "r")
print(myFile.read())
myFile.close()


with open(input(), 'rU') as input_file:
    answer = input()
    print("Your answer was: " + answer)
foo
