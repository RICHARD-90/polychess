#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:17:10 2020

@author: abdoumahamadouzakariyaou
"""
import chess 
import random

board=chess.Board()

print(board)

while(not board.is_game_over()):
    moves=board.legal_moves
    listMoves=[]
    for move in moves:
        listMoves.append(move)
    next=listMoves[random.randint(0,moves.count()-1)]
    board.push(next)
    print(board)
    print("")
    
    
    
"Besoin de ponderation et de sa fonction inverse"

def MineMax(position):
    POSITION=""
    positionRecur=""
    ponderations=methodeponderation(position) #renvoie soit juste la ponderation de la position courante(board.legal_moves is None) ou une liste de ponderation
    ponderation=max(ponderations)
    if ponderation==ponderations[0]:
        POSITION=position #ne bouge pas
    elif ponderation!=ponderations[0]:
        POSITION=position(ponderation)# la il nous une fonction qui renvoie la position en fonction d'une seule ponderation
    elif position.board.legal_moves==None:# doute si c'est position.board.legal_moves ou position.legal_moves
        if True:
           POSITION=position
        else:
            for pos in board.legal_moves: # tout les deplacements poblible a partir de la position donnee
                POSITION=MineMax(pos)
    return POSITION
            
        
            
print(MineMax("gc"))


def MineMax(etatcourant,prof,boolean):
    if (prof==0 or conditiondarret):
        return etatcourant #ne bouge pas
    elif boolean==False:
        valeur=-9999
        for child in etatcourant.board.legal_moves :
            etatcourant=board.push(chess.Move.from_uci(move))
            valeur=max(valeur,MineMax(child,prof-1,False))
        return valeur
    else:
        valeur=9999
        for child  in etatcourant.board.legal_moves:
            etatcourant=board.push(chess.Move.from_uci(move))
            valeur=min(valeur,MineMax(child,prof-1,True))
        return valeur
    
def minimax(board, depth, alpha, beta, maximizing_player):

    board.is_human_turn = not maximizing_player 

    children = board.get_all_possible_moves()

    if depth == 0 or board.is_draw or board.is_check_mate:
        return None, evaluate(board)

    best_move = random.choice(children)

    if maximizing_player:
        max_eval = -math.inf
        for child in children:
            board_copy = copy.deepcopy(board)
            board_copy.move(child[0][0], child[0][1], child[1][0], child[1][1])
            current_eval = minimax(board_copy, depth - 1, alpha, beta, False)[1]
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = child
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        return best_move, max_eval

    else:
        min_eval = math.inf
        for child in children:
            board_copy = copy.deepcopy(board)
            board_copy.move(child[0][0], child[0][1], child[1][0], child[1][1])
            current_eval = minimax(board_copy, depth - 1, alpha, beta, True)[1]
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = child
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        return best_move, min_eval                    
                
            
            
        
    

