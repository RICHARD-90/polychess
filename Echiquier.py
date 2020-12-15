#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:20:11 2020

@author: abdoumahamadouzakariyaou
"""
#from Pieces import *
import chess  
class Echiquier:
    # Constructor
   coord=[    # la map etant composé de 64 cases dont 8 colonne (a-h) et 8 ligne(1-8)
    [80,81,82,83,84,85,86,87],
    [70,71,72,73,74,75,76,77],
    [60,61,62,63,64,65,66,67],
    [50,51,52,53,54,55,56,57],
    [40,41,42,43,44,45,46,47],
    [30,31,32,33,34,35,36,37],
    [20,21,22,23,24,25,26,27],
    [10,11,12,13,14,15,16,17]
    ]
    
   def __init__(self):
       self.init()
       self.long=8
       self.larg=6
        
   def init(self):
       #placement des pieces sur l'echequier car au début de la partie, les pièces sont toujours placées de la même façon
       self.cases = [ 
       Piece('TOUR','noir'),Piece('CAVALIER','noir'),Piece('FOU','noir'),Piece('DAME','noir'),Piece('ROI','noir'),Piece('FOU','noir'),Piece('CAVALIER','noir'),Piece('TOUR','noir'),
       Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
       Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
       Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
       Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
       Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
       Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
       Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
       ]
        
   #Echiquier =chess.Board()
   #print(Echiquier)