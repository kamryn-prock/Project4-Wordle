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

    def GetRandomWord() :
        selectedWord = random.choice(FIVE_LETTER_WORDS)
        return selectedWord

    selectedWord = GetRandomWord()

    def randwordtofirstRow() :
        for x in range(len(selectedWord)):
            gw.set_square_letter(0, x, selectedWord[x])

    def enter_action(s):
        #gw.show_message("You have to implement this method.")
        inputs = [] #makes a list for the inputs

        #gets the inputs
        for i in range(0,5):
            letter = gw.get_square_letter(gw.get_current_row(),i) 
            inputs.append(letter.lower())
           

        #makes list of inputs into a word
        input_word = ''.join(inputs)       

        #checks if the word is in the list
        if selectedWord == input_word:
            for x in range(0, N_COLS):
                gw.set_square_color(gw.get_current_row(), x , CORRECT_COLOR)
            
            gw.show_message("You guessed it!")
            gw.set_current_row(N_ROWS + 1)

        elif input_word in FIVE_LETTER_WORDS:
            gw.show_message("Is in word list")
            
            for x in range(0, N_COLS):
                if selectedWord[x] == input_word[x]:
                    color = CORRECT_COLOR

                elif selectedWord[x] in input_word: 
                    color = PRESENT_COLOR

                else :
                    color = MISSING_COLOR
                    print("x:", x)

                gw.set_square_color(gw.get_current_row(), x , color)
                
                if color == CORRECT_COLOR:
                    gw.set_key_color(input_word[x].upper(), color)
                elif color == PRESENT_COLOR:
                    if gw.get_key_color(input_word[x].upper()) == CORRECT_COLOR:
                        pass
                    else:
                        gw.set_key_color(input_word[x].upper(), color)
                else:
                    if gw.get_key_color(input_word[x].upper()) != MISSING_COLOR:
                        pass
                    else: 
                        gw.set_key_color(input_word[x].upper(), color)

                gw.set_key_color(input_word[x].upper(), color)

            gw.set_current_row(gw.get_current_row() + 1)
            #Color the word appropriately
            print("N_ROWS:", N_ROWS)
            print("N_COLS:", N_COLS)
            print("Word to guess is: " + selectedWord)
            print("Stored inputs are: ")
            for letter in inputs:
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

