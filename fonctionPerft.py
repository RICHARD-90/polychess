# -*- coding: utf-8 -*-
"""
@author: yawoumihani Hassani

Fonction perft
Cette fonction permet de déboguer les mouvements de la machine autrement dit 
de s'assurer de la validité de la génération des mouvements de la machine pour 
une profondeur donnée.

"""
import chess

board = chess.Board()

def perft(profondeur):
    moves = board.legal_moves
    noeuds = 0
    if profondeur == 0:
       return 0 
    for move in moves:
        chess.Move.from_uci(move) #vérifier si c'est bien cette fonction qui va marcher sinon créer une fonction MakeMove
        noeuds += perft(profondeur - 1)
        board.pop() #Undo the last move
    return noeuds()




