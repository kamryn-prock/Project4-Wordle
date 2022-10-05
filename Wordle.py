# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from optparse import Values
import random
from secrets import choice
import WordleDictionary

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

CORRECT_COLOR = "#66BB66" # A shade of green
PRESENT_COLOR = "#CCBB66" # A shade of brownish yellow
MISSING_COLOR = "#999999" # grey

def wordle():

    #function that gets a random word
    def GetRandomWord() :
        wordToGuess = random.choice(FIVE_LETTER_WORDS)
        return wordToGuess

    #calls function that returns a random five letter word and sets it as the word to guess
    wordToGuess = GetRandomWord()

    def randwordtofirstRow() :
        for x in range(len(wordToGuess)):
            gw.set_square_letter(0, x, wordToGuess[x])

    #This is what executes when you hit enter
    def enter_action(s):
        
        #makes a list for the keystrokes
        keystrokes = []

        #gets the keystrokes
        for i in range(0,5):
            letter = gw.get_square_letter(gw.get_current_row(),i) 
            keystrokes.append(letter.lower())
           

        #makes list of keystrokes into a word
        currentGuessWord = ''.join(keystrokes)       

        #checks if the word is in the list
        if wordToGuess == currentGuessWord:
            for x in range(0, N_COLS):
                gw.set_square_color(gw.get_current_row(), x , CORRECT_COLOR)
            
            gw.show_message("You guessed it!")
            gw.set_current_row(N_ROWS + 1)

        elif currentGuessWord in FIVE_LETTER_WORDS:
            gw.show_message("Is in word list")
            
            for x in range(0, N_COLS):
                if wordToGuess[x] == currentGuessWord[x]:
                    color = CORRECT_COLOR

                elif wordToGuess[x] in currentGuessWord: 
                    color = PRESENT_COLOR

                else :
                    color = MISSING_COLOR
                    print("x:", x)

                gw.set_square_color(gw.get_current_row(), x , color)
                
                if color == CORRECT_COLOR:
                    gw.set_key_color(currentGuessWord[x].upper(), color)
                elif color == PRESENT_COLOR:
                    if gw.get_key_color(currentGuessWord[x].upper()) == CORRECT_COLOR:
                        pass
                    else:
                        gw.set_key_color(currentGuessWord[x].upper(), color)
                else:
                    if gw.get_key_color(currentGuessWord[x].upper()) != MISSING_COLOR:
                        pass
                    else: 
                        gw.set_key_color(currentGuessWord[x].upper(), color)

                gw.set_key_color(currentGuessWord[x].upper(), color)

            gw.set_current_row(gw.get_current_row() + 1)
            #Color the word appropriately
            print("N_ROWS:", N_ROWS)
            print("N_COLS:", N_COLS)
            print("Word to guess is: " + wordToGuess)
            print("Stored keystrokes are: ")
            for letter in keystrokes:
                print(letter)

        else:
            gw.show_message("Not in word list")
            #gw. clear out the current row bc the word is not in word list
            print(N_COLS)

    gw = WordleGWindow()
    randwordtofirstRow()
    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()

