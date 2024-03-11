# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Game
Date: 2024/3/9
Author: Abdelaziz Chatit
"""

import numpy as np
import random as ra 

# Global variables 
board = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
winner = None
currentPlayer = "X"

def printBoard():
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("---------")

def playerInput():
    """Handles player input for making moves."""
    global board, currentPlayer
    while True:
        try:
            row = int(input("Choose a row from (0-2): "))
            column = int(input("Choose a column from (0-2): "))
            if 0 <= row <= 2 and 0 <= column <= 2 and board[row, column] == "-":
                board[row, column] = currentPlayer
                break
        except ValueError:
            print("Invalid input! Please enter valid integers.")

def checkWin():
    """Checks if there's a winner or if it's a tie."""
    global winner, board, currentPlayer
    # Check horizontally, vertically, and diagonally for a win
    # (code for win checks omitted for brevity)
    for row in range(3):
        if board[row,0]==board[row,1]==board[row,2] and board[row,0]!="-":
            winner=board[row,0]
            return True
        #check virtacly 
        if board[0,row]==board[1,row]==board[2,row] and board[0,row]!="-":
            winner=board[0,row]
            return True
        
     #check diognaly   
    
    if board[0,0]==board[1,1]==board[2,2] and board[0,0]!="-":
        winner=board[0,0]
        return True
    if board[0,2]==board[1,1]==board[2,0] and board[0,2]!="-":
        winner=board[0,2]
        return True
    # Check for tie
    if "-" not in board:
        return True
    return False

def switchPlayer():
    """Switches the current player."""
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer():
    """Simulates computer moves."""
    global board, currentPlayer
    while True:
        row = ra.randint(0, 2)
        column = ra.randint(0, 2)
        if board[row, column] == "-":
            board[row, column] = currentPlayer
            switchPlayer()
            break

# Main game loop
while True:
    printBoard()
    playerInput()
    if checkWin():
        printBoard()  # Print the final board state
        if winner:
            print(f"The winner is {winner}")
        else:
            print("It's a tie!")
        break  # Exit the game loop
    switchPlayer()
    computer()
    if checkWin():
        printBoard()  # Print the final board state
        if winner:
            print(f"The winner is {winner}")
        else:
            print("It's a tie!")
        break  # Exit the game loop
