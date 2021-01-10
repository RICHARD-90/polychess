# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:21:48 2021

@author: Junio
"""

import chess
import chess.polyglot
import chess.pgn as p

board = chess.Board()
print(board, '\n\n')
print('**********************\n\n')

# importer le fichier __init__()
import __init__ as m
# tant que le jeu n'est pas terminé, on joue
tour = 0 # permet de determiner a qui le tour
profondeur = 3
# nom de la sauvegarde
nom_sauv = str(input('entrer un nom pour la partie _'))
game = p.Game() # etat du jeu

while not(board.is_game_over()):
    cap_K = True
    if tour % 2 == 0:
        moves = board.legal_moves
        maxi = 0
        for move in moves :
            for deplacement in m.polyglot(board): 
                if move == deplacement[0]:
                    if maxi < deplacement[1]:
                        maxi = deplacement[1]
                        move_util = deplacement[0]
                    cap_K = False
                    # print(deplacement[0],deplacement[1])
        if cap_K:
            move_util = m.alphabeta(profondeur, board, True)
        #test
        #print('**********************\n\n')
        #move_util = m.alphabeta(profondeur, board, True)
        valide = False
        while not valide:
            try:
                #move_util = input('player 2:')
                print("Computer1's turn ...")
                board.push(chess.Move.from_uci(str(move_util)))
                print(board, '\n\n')
                valide = True
            
            except (ValueError):
                print('try again')
            except (TypeError):
                print('try again')
    
    else:
        moves = board.legal_moves
        maxi = 0
        for move in moves :
            for deplacement in m.polyglot(board): 
                if move == deplacement[0]:
                    if maxi < deplacement[1]:
                        maxi = deplacement[1]
                        move_util = deplacement[0]
                    cap_K = False
                    # print(deplacement[0],deplacement[1])
        if cap_K:
            move_util = m.alphabeta(profondeur, board, True)
        #test
        #print('**********************\n\n')
        #move_util = m.alphabeta(profondeur, board, True)
        valide = False
        while not valide:
            try: 
                #move_util = input('player 2:')
                print("Computer2's turn ...")
                board.push(chess.Move.from_uci(str(move_util)))
                print(board, '\n\n')
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
    # sauvegarde au format pgn
    new_pgn = open(nom_sauv,'w')
    export = p.FileExporter(new_pgn)
    game.accept(export)

# regarder len(move) - 1
