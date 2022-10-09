# File: Wordle.py

"""
This module is the completed Wordle assignment.

Project Manager: Sloan Nelson
Scrum Master: Jackson Washburn
Developers:
    Stephen Sorensen
    Kamryn Prock
    Spencer Jackson
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    # This function gets a random word from WordleDictionary.py
    def GetRandomWord() :
        wordToGuess = random.choice(FIVE_LETTER_WORDS)
        return wordToGuess

    #This uses a function to return a random five letter word and set it as the word to guess
    wordToGuess = GetRandomWord()
    print("Word to guess is: " + wordToGuess + "\n") 

    #This was for milestone 1 and it's use was discontinued during milestones 3&4 to be like "real" wordle
    #Grader, please see comment near bottom of code
    def RandomWordToFirstRow() :
        for x in range(len(wordToGuess)):
            gw.set_square_letter(0, x, wordToGuess[x])

    #This is the function/code that executes when you hit enter
    def enter_action(s):

        #Put letters of the word that need to be guessed into a list
        remainingLetters = list(wordToGuess)
        
        #Make a list for letters of the user's guess
        keystrokes = []

        #Get the user inputs from wordle and place them in keystrokes list
        for i in range(0,5):
            letter = gw.get_square_letter(gw.get_current_row(),i) 
            keystrokes.append(letter.lower())
           

        #makes list of keystrokes into a string
        currentGuessWord = ''.join(keystrokes)
        print("**********")
        print("Users' guess is: " + currentGuessWord)

        #Checks if guess and answer match and sets all squares to green if they do
        if wordToGuess == currentGuessWord:
            for x in range(0, N_COLS):
                gw.set_square_color(gw.get_current_row(), x , CORRECT_COLOR)
                gw.set_key_color(currentGuessWord[x].upper(), CORRECT_COLOR)
            
            gw.show_message("You guessed it!")
            print("The user guessed the word correctly")
            gw.set_current_row(gw.get_current_row() + 1)

        #If word is not a match, verify that it is acceptable guess in wordlist 
        elif currentGuessWord in FIVE_LETTER_WORDS:
            gw.show_message("Is in word list")
            print(currentGuessWord + " is a valid guess\n")
            
            #This for loop takes care of all letter/keys that should be green
            #It removes the correct letters from the user's keystrokes the letters that remain to be guessed
            print("Marking letters that are in the correct position")
            for x in range(0, N_COLS):
                if wordToGuess[x] == keystrokes[x]:
                    print("Positon " + str(x) + " is a match")
                    gw.set_square_color(gw.get_current_row(), x, CORRECT_COLOR)
                    print("Set row " + str(gw.get_current_row()) + " and column " + str(x) + " to green")
                    gw.set_key_color(keystrokes[x].upper(), CORRECT_COLOR)
                    for i in range (0, len(remainingLetters)):
                        if remainingLetters[i] == keystrokes[x]:
                            print("Removing " + str(remainingLetters[i]) + " from remainingLetters")
                            remainingLetters.pop(i)
                            break
                    print("Removing " + str(keystrokes[x]) + " from keystrokes")
                    keystrokes[x] = ''
                    print("Remaining letters are: " + str(remainingLetters))
                    print("Remaining keystrokes are: " + str(keystrokes) + "\n")
            print("All green letters, if any, are marked\n")

            #All remaining letters are not in the correct positions
            print("Marking letters that are present but in wrong location as well as letters not present")
            for x in range(0, N_COLS):
                print("Checking letter " + str(x) + " of user's guess")
                if keystrokes[x] == '':
                    print("Letter " + str(x) + " of user's guess already previously marked correct")
                    print("Moving to next letter\n")
                elif keystrokes[x] in wordToGuess and keystrokes[x] in remainingLetters:
                    print("Remaining letters are: " + str(remainingLetters))
                    print("Verified letter " + str(x) + "-" + str(keystrokes[x]) + " of user's guess is in remaining letters")
                    gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                    print("Set row " + str(gw.get_current_row()) + " and column " + str(x) + " to yellow")
                    if gw.get_key_color(keystrokes[x].upper()) != CORRECT_COLOR:
                        gw.set_key_color(keystrokes[x].upper(), PRESENT_COLOR)
                        print("Since key " + str(keystrokes[x].upper()) + " is not marked correct, marked as present")
                    for i in range (0, len(remainingLetters)):
                        if remainingLetters[i] == keystrokes[x]:
                            print("Removing " + str(remainingLetters[i]) + " from remainingLetters")
                            remainingLetters.pop(i)
                            break
                    print("Remaining letters are: " + str(remainingLetters))
                    print("Removing " + str(keystrokes[x]) + " from keystrokes")
                    keystrokes[x] = ''
                    print("Remaining keystrokes are: " + str(keystrokes))
                    print("Moving to next letter\n")
                else:
                    print("Remaining letters are: " + str(remainingLetters))
                    print("Could not find letter " + str(x) + "-" + str(keystrokes[x]) + " of user's guess in remaining letters")
                    gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)
                    print("Set row " + str(gw.get_current_row()) + " and column " + str(x) + " to gray")
                    if gw.get_key_color(keystrokes[x].upper()) != CORRECT_COLOR:
                        if gw.get_key_color(keystrokes[x].upper()) != PRESENT_COLOR:
                            gw.set_key_color(keystrokes[x].upper(), MISSING_COLOR)
                            print("Since key " + str(keystrokes[x].upper()) + " is not marked correct or present, marked as not present")

                    print("Moving to next letter\n")

            #Move to next row when done processing valid user entry
            print("There are no letters remaining...user input processed")
            gw.set_current_row(gw.get_current_row() + 1)
            print("Wordle set to next row...ready for input\n")

        #If word is not in wordlist, do nothing
        else:
            gw.show_message("Not in word list")
            print("User input " + currentGuessWord + " was not accepted because it is not in wordlist\n")

    gw = WordleGWindow()
    #****COMMENT FOR GRADER****
    #This can be uncommented for milestone 1. We assumed that we are supposed to build Wordle
    #the way it works in real life once we got to milestones 3/4, so we commented this next line out.
    #RandomWordToFirstRow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()

