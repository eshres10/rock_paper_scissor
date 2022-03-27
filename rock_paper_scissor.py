#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Created By  : Ena Shrestha
#Version : v1.0
# =============================================================================

# =============================================================================
"""
This is a simple yet the classic game of rock, paper and scissor.
"""
# =============================================================================
#Imports
# =============================================================================

import random
import sys
# =============================================================================

#Main Function

# =============================================================================

#function play_again restarts the game 
def play_again():
        x = input("Would you like to play again? y/n")
        if x == "y":
            play()
        elif x == "n":
            print("thank you for playing.")
            sys.exit()

#function play() starts the game
def play():
    print("Welcome to the classic game of rock, paper and scissors! The rules are simple: \nRock smashes scissor. \nScissor cuts paper. \nPaper wraps rock. \nReady to begin? ")
    user_input=input("Enter rock, paper, scissors: ")
    possible_input= ["rock", "paper", "scissor"]
    computer_input = random.choice(possible_input) #generates random from list possible_input
 
    if user_input == computer_input:
        print("I selected: ", computer_input)
        print("That's a tie!")
        play_again()
    if user_input == "rock":
        if computer_input == "paper":
            print("I selected: ", computer_input)
            print("Paper covers rock, You lose :'(")
            play_again()
    if user_input == "rock":
        if computer_input == "scissor":
            print("I selected: ", computer_input)
            print("Rock smashes scissor! You win :D!")
            play_again()
    if user_input == "paper":
        if computer_input == "scissor":
            print("I selected: ", computer_input)
            print("Scissor cuts paper. You lose :'(")
            play_again()
    if user_input == "paper":
        if computer_input == "rock":
            print("I selected: ", computer_input)
            print("Paper covers rock. You win! :D")
            play_again()
    if user_input == "scissor":
        if computer_input == "rock":
            print("I selected: ", computer_input)
            print("Rock smashes scissor. You lose :'(")
            play_again()
    if user_input == "scissor":
        if computer_input == "paper":
            print("I selected: ", computer_input)
            print("Scissor cuts paper. You win! :D")
            play_again()
# =============================================================================
#Calling Functions:
# =============================================================================
  
play() 

# =============================================================================
