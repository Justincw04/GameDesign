#Justin Cortez Wartell
#game with files
import random
import time

gameWords = ['pizza', 'spaghetti','tacos','salmon','meatball','hamburger','chicken','barbecue','steak','ramen']
scramble= random.choice(gameWords)
word =random.sample(scramble, len(scramble))
oneScore = (0)
def main():
   menu()

#putting list into file
with open("wordFile", "w") as wordFile:
    wordFile.write("\n".join(gameWords))
#regular game
def menu():
    print("************Welcome to Unscramble Game**************")
    print()

    choice = input("""
                      A: 1 Player
                      B: 2 Players
                      C: See leaderboard

                      Please enter your choice: """)
    if choice == "A" or choice =="a":
        oneName()
    elif choice == "B" or choice =="b":
        twoPlayer()
    elif choice == "C" or choice =="c":
        print(LeadFile.read())
        leadmenu = input("""
                        A: Back to menu

                        Please enter your choice""")
            menu()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
def oneName():
    name1 = input("Please write your name:")
    onePlayer()
def onePlayer():
    print("1 Player")
    print()

    option1 = input("""
                      A: Get a Word
                      B: Back to Main Menu

                      Please enter your choice: """)
    if option1 == "A" or option1 =="a":
        oneWord()
    elif option1 == "B" or option1 =="b":
        menu()
    else:
        print("You must only select either A or B")
        print("Please try again")
        onePlayer()
def oneWord():
    print("Unscramble:")
    print()
    print(word)
    guess1 = input("What is the Word?")
    if guess1 == scramble:
        myFile = open("newFile.txt", "w")
        myFile.write(oneScore+1)
        myFile.close()
        print("Correct! Well Done! Want to play again?")
        end1 = input(input("""
                          A: Play Again
                          B: Back to Main Menu

                          Please enter your choice: """)
        if end1 == "A" or end1 =="a":
            oneWord()
        elif end1 == "B" or end1 =="b":

            leaderboard()
        else:
            print("You must only select either A or B")
            print("Please try again")
            print(end1)
    else:
        print("try again")
def leaderboard():
    print("Before you go...")
    date1 = input("Please enter the date")
    LeadFile = open("newFile.txt", "w")
    LeadFile.write("[", date1, oneName, oneScore, "]")
    LeadFile.close()
    menu()





scramble= random.choice(gameWords)
word =random.sample(scramble, len(scramble))
print (word)
