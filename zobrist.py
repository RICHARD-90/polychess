# -*- coding: utf-8 -*-
#importation des modules
import chess
import chess.polyglot
import random

#definition de l'echequier
board = chess.Board()

zob = [[[random.randint(1,2**64-1) for i in range(12)] for j in range(8)] for k in range(8)]

def index(piece):
    #les pieces en majuscules sont noires et celles en minuscules sont blanches
    if piece == 'P':
        return 0
    if piece == 'N':
        return 1
    if piece == 'B':
        return 2
    if piece == 'R' :
        return 3
    if piece == 'K':
        return 4
    if piece == 'Q':
        return 5
    if piece == 'p':
        return 6
    if piece == 'n':
        return 7
    if piece == 'b':
        return 8
    if piece == 'r':
        return 9
    if piece == 'k':
        return 10
    if piece == 'q':
        return 11
    else:
        return -1
    
def zobrist(board):
    z = 0
    for i in range(8):
        for j in range (8):
            if board[i][j] != '-':
                piece = index(board[i][j])
                z = zob[i][j][piece]
    return z

def hachage():
    val_hachee = zobrist(board)
    print ("L'échéquier actuel est :")
    for i in board:
        for j in i:
            print (j)
        print (i)
        
    print ("Le hachage actuel est :", val_hachee)

"""https://github.com/niklasf/python-chess/blob/master/chess/polyglot.py"""
