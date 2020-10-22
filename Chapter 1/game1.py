import random
import time

name=input("What is your name? ")
print("Good luck! ", name)
gameWords=['python', 'java','PHP','javaScript', 'computer', 'geeks', 'keyboard','laptop', 'headphone', 'hardware','software' ]
# use the choice method of my random fucntion to pick a gameWords
answer=input('do you want to guess a word? ')
win = "no"
checkWord = ""
while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    turns=5
    win = 'no'

    while turns>0 and win == 'no':
        if checkWord !=word:
            for char in word:
                if char in guesses:
                    print(char, end = '')
                    checkWord += char
                else:
                    print('_', end = '')
                    checkWord += '_'
        print()

        if checkWord == word:
            print('you win!')
            win = yes
        else:
            guess = input("guess a letter or word. ")

            guesses += guess

            if guess in word:
                print('you have', turns, 'extra chances left.')
            else:
                turns-=1
                print('you have', turns, 'extra chances left.')
        if checkWord == word:
            win = 'yes'
        else:
            checkWord = ''
    else:
        turns = 0
        if word in final:
            print('you win')
            print("the word is: "+ word)
            break
        guess= input("give me a letter: ")
        print()
        count=0
        if guess not in guesses:
            count=word.count(guess[0])
            if guess not in word:
                turns=turns-1
        guesses += guess[0]
turns-=1

answer=input('do you want to play again ')
time.sleep(5)

if not answer is not"yes":
    print('thanks for playing')
