import random
import time

gameWords = ['pizza', 'spaghetti','tacos','salmon','meatball','hamburger','chicken','barbecue','steak','ramen']
scramble= random.choice(gameWords)
word =random.sample(scramble, len(scramble))

def main():
   menu()

def menu():
    print("************Welcome to Unscramble Game**************")
    print()

    choice = input("""
                      A: 1 Player
                      B: 2 Players

                      Please enter your choice: """)
    if choice == "A" or choice =="a":
        onePlayer()
    elif choice == "B" or choice =="b":
        twoPlayer()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

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
        print("Correct! Well Done! Want to play again?")
        end1 = input(input("""
                          A: Play Again
                          B: Back to Main Menu

                          Please enter your choice: """)
        if end1 == "A" or end1 =="a":
            oneWord()
        elif end1 == "B" or end1 =="b":
            menu()
        else:
            print("You must only select either A or B")
            print("Please try again")
            print(end1)
    else:
        print("try again")






scramble= random.choice(gameWords)
word =random.sample(scramble, len(scramble))
print (word)
