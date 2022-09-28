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

selectedWord = ""

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()

def GetRandomWord() :
    selectedWord = random.choice(FIVE_LETTER_WORDS)
    print(selectedWord)
    return selectedWord