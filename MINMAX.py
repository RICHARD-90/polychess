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
        valeur=-99999
        for child in etatcourant.board.legal_moves :
            etatcourant=board.push(next)
            valeur=max(valeur,MineMax(child,prof-1,False))
           return valeur
    else:
        valeur=99999
        for child  in etatcourant.board.legal_moves:
            etatcourant=board.push(next)
            valeur=min(valeur,MineMax(child,prof-1,True))
        return valeur
                    
                    
                
            
            
        
    

