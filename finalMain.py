# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:26:10 2021

@author: Junio
"""
import chess
import chess.polyglot

board = chess.Board()
print(board)
# importer le fichier __init__()
import __init__ as m
# tant que le jeu n'est pas terminé, on joue
tour = 0 # permet de determiner a qui le tour
profondeur = 5

while not(board.is_game_over()):
    cap_K = True
    if tour % 2 == 0:
        moves = board.legal_moves
        for move in moves :
            for deplacement in m.polyglot(board):
                if move == deplacement[0]:
                    cap_K = False
                    print(deplacement[0],deplacement[1])
        if cap_K:
           a = m.MineMax(board, profondeur, True)
           b = m.MineMax(board, profondeur, False)
           m.alph_betaA(profondeur, board, a, b)
        valide = False
        while not valide:
            try:
                move_util = input('player 1:')
                board.push(chess.Move.from_uci(str(move_util)))
                print(board)
                valide = True
            except (ValueError):
                print('try again')
            except (TypeError):
                print('try again')
            
  
    else:
        moves = board.legal_moves
        for move in moves :
            for deplacement in m.polyglot(board): 
                if move == deplacement[0]:
                    cap_K = False
                    print(deplacement[0],deplacement[1])
        if cap_K:
            a = m.MineMax(board, profondeur, True)
            b = m.MineMax(board, profondeur, False)
            m.alph_betaA(profondeur, board, a, b)
        valide = False
        while not valide:
            try:
                move_util = input('player 1:')
                board.push(chess.Move.from_uci(str(move_util)))
                print(board)
                valide = True
            except (ValueError):
                print('try again')
            except (TypeError):
                print('try again')
             
    tour = tour +1 

    # condition d'arret
    if (board.is_game_over()):
       print("The game is over")
       print(board.result())

# regarder len(move) - 1