# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe  human vs human
Date: 2024/03/06
Author: Abdelaziz Chatit
"""
import numpy as np
# global variables 
board=np.array([["-","-","-"],["-","-","-"],["-","-","-"]])
winner=None
currentPlayer="X"
gameRunning=True

def printBoard():
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("---------")

def playerInput():
    """
    Handles player input for making moves.
    """
    global board,currentPlayer
    while True:
        try:
            row=int(input("choose a row from (0-2): "))
            collumn=int(input("choose a collumn from (0-2): "))
            if 0<=row<=2 and 0<=collumn<=2 and board[row,collumn]=="-":
                board[row,collumn]=currentPlayer
                break
        except ValueError:
            print("Invalid input!, please enter valid integers")

def checkWin():
    """
    Checks if there's a winner or if it's a tie.
    """
    global winner,board,currentPlayer,gameRunning
    #check horizontaly
    for row in range(3):
        if board[row,0]==board[row,1]==board[row,2] and board[row,0]!="-":
            gameRunning=False
            winner=board[row,0]
            return True
        #check virtacly 
        if board[0,row]==board[1,row]==board[2,row] and board[0,row]!="-":
            gameRunning=False
            winner=board[0,row]
            return True
        
     #check diognaly   
    
    if board[0,0]==board[1,1]==board[2,2] and board[0,0]!="-":
        gameRunning=False
        winner=board[0,0]
        return True
    if board[0,2]==board[1,1]==board[2,0] and board[0,2]!="-":
        gameRunning=False
        winner=board[0,2]
        return True
    
    #check Tie
    if "-" not in board:
        gameRunning=False
        return True
    
    return False


def switchPlayer():
    """
    Switches the current player.
    """
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"


while gameRunning:
    printBoard()
    playerInput()
    if checkWin():
        if winner:
            print(f"the winner is {winner}")
            
        else:
            print("it's a tie! ")
    switchPlayer()
    
    
printBoard()