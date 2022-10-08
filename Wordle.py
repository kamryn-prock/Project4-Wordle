# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

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
    
    print("N_ROWS:", N_ROWS)
    print("N_COLS:", N_COLS)
    print("Word to guess is: " + wordToGuess) 

    def randWordToFirstRow() :
        for x in range(len(wordToGuess)):
            gw.set_square_letter(0, x, wordToGuess[x])

    #This is what executes when you hit enter
    def enter_action(s):

        remainingLetters = list(wordToGuess)
        
        #makes a list for the keystrokes
        keystrokes = []

        #gets the keystrokes
        #variable keystrokes is a list of letters ogtten from the current row
        #variable currentGuessWord is a string comprised of all those letters
        for i in range(0,5):
            letter = gw.get_square_letter(gw.get_current_row(),i) 
            keystrokes.append(letter.lower())
           

        #makes list of keystrokes into a word
        currentGuessWord = ''.join(keystrokes)      

        #Checks if words match and sets all squares to green if they do
        if wordToGuess == currentGuessWord:
            for x in range(0, N_COLS):
                gw.set_square_color(gw.get_current_row(), x , CORRECT_COLOR)
                gw.set_key_color(currentGuessWord[x].upper(), CORRECT_COLOR)
            
            gw.show_message("You guessed it!")
            gw.set_current_row(gw.get_current_row() + 1)

        #If word is in wordlist, 
        elif currentGuessWord in FIVE_LETTER_WORDS:
            gw.show_message("Is in word list")
            print("New valid guess: " + currentGuessWord)
            
            #This for loop takes care of all the greens
            for x in range(0, N_COLS):
                if wordToGuess[x] == keystrokes[x]:
                    gw.set_square_color(gw.get_current_row(), x, CORRECT_COLOR)
                    print("Set row " + str(gw.get_current_row()) + " and column " + str(x) + " to green")
                    gw.set_key_color(keystrokes[x].upper(), CORRECT_COLOR)
                    print("Removing " + str(keystrokes[x]) + " from remaining letters and keystrokes")
                    for i in range (0, len(remainingLetters)):
                        if remainingLetters[i] == keystrokes[x]:
                            print("Removing " + str(remainingLetters[i]) + " from remainingLetters")
                            remainingLetters.pop(i)
                            break
                    keystrokes[x] = ''
                    for letter in keystrokes:
                        print(letter)
            print("All green letters marked.")

            #All remaining letters are not in the correct positions
            for x in range(0, N_COLS):
                if keystrokes[x] == '':
                    pass
                elif keystrokes[x] in wordToGuess and keystrokes[x] in remainingLetters:
                    print("Verified keystroke is in word to guess and also if in remaining letters")
                    print("Remaining letters are: " + str(remainingLetters))
                    print(str(keystrokes[x]) + " is in word to guess.")
                    gw.set_square_color(gw.get_current_row(), x, PRESENT_COLOR)
                    print("Set row " + str(gw.get_current_row()) + " and column " + str(x) + " to yellow")
                    if gw.get_key_color(keystrokes[x].upper()) != CORRECT_COLOR:
                        gw.set_key_color(keystrokes[x].upper(), PRESENT_COLOR)
                    print("Removing " + str(keystrokes[x]) + " from keystrokes and remaining letters")
                    for i in range (0, len(remainingLetters)):
                        if remainingLetters[i] == keystrokes[x]:
                            print("Removing " + str(remainingLetters[i]) + " from remainingLetters")
                            remainingLetters.pop(i)
                            break
                    for letter in keystrokes:
                        print(letter)
                    keystrokes[x] = ''
                else:
                    gw.set_square_color(gw.get_current_row(), x, MISSING_COLOR)
                    if gw.get_key_color(keystrokes[x].upper()) != CORRECT_COLOR:
                        if gw.get_key_color(keystrokes[x].upper()) != PRESENT_COLOR:
                            gw.set_key_color(keystrokes[x].upper(), MISSING_COLOR)

                    print(str(wordToGuess[x]) + " not found...keystrokes are")
                    for letter in keystrokes:
                        print(letter)

                # elif wordToGuess[x] in currentGuessWord: 
                #     color = PRESENT_COLOR

                # else :
                #     color = MISSING_COLOR
                #     print("x:", x)
                
                # if color == CORRECT_COLOR:
                #     gw.set_key_color(currentGuessWord[x].upper(), color)
                # elif color == PRESENT_COLOR:
                #     if gw.get_key_color(currentGuessWord[x].upper()) == CORRECT_COLOR:
                #         pass
                #     else:
                #         gw.set_key_color(currentGuessWord[x].upper(), color)
                # else:
                #     if gw.get_key_color(currentGuessWord[x].upper()) != MISSING_COLOR:
                #         pass
                #     else: 
                #         gw.set_key_color(currentGuessWord[x].upper(), color)

                # gw.set_key_color(currentGuessWord[x].upper(), color)

            gw.set_current_row(gw.get_current_row() + 1)
            #Color the word appropriately

        else:
            gw.show_message("Not in word list")
            #gw. clear out the current row bc the word is not in word list

    gw = WordleGWindow()
    #randWordToFirstRow()
    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()

