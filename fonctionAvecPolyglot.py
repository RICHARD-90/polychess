# -*- coding: utf-8 -*-
"""
@author: Hassani Yawoumihani

Fichier contenant la fonction permettant de proposer les positions initiales
statistiquement gagnantes, regarde les coups proposés avec les pondérations

Attention cette fonction ne prend pas en compte si la case est occupee ou non!

Voir avec Zakari pour le nom de la fonction:
Voir avec tout le monde si j'ai bien compris la tache qui m'a ete attribue :

"""
import chess
import chess.polyglot


board = chess.Board()

def fonctInitiale():
    """
    Cette fonction affiche les positions initiales statistiquement gagnantes
    avec leur ponderation
    """
    #Ouverture du livre de polyglot qu'on stocke dans une variable book
    book = chess.polyglot.open_reader("bookfish.bin")
    #on parcourt les elements du book et on affiche les positions(deplacements)
    #initiales statistiquement gagnantes avec leur ponderation
    for entry in book.find_all(board):
            print(entry.move, entry.weight)

fonctInitiale()
print ('test1 done','\n')


def fonction(position):
    """
    Cette fonction affiche la pondération du deplacment passe en argument
    """
    #Ouverture du livre de polyglot qu'on stocke dans une variable book
    book = chess.polyglot.open_reader("bookfish.bin")
    #on parcourt les elements du book
    for entry in book.find_all(board):
        #si la position(deplacement) est presente on l'affiche avec sa ponderation 
        if entry.move == position:
            print(entry.move, entry.weight)


move = chess.Move.from_uci("d2d4")
fonction(move)
print ('test2 done','\n')

def fonction2(positionD):
    """
    Cette fonction affiche le deplacement possible selon la position de depart 
    si elle est bien dans polyglot avec les pondérations correspondantes
    """
    #Ouverture du livre de polyglot qu'on stocke dans une variable book
    book = chess.polyglot.open_reader("bookfish.bin")
    #on parcourt les elements du book
    for entry in book.find_all(board):
        #On convertit l'objet move en str pour pouvoir le comparer a la position 
        #de depart
        m = str(entry.move)
        #Si la position de depart est a la premiere position de m alors on affiche
        #le deplacement possible et sa ponderation
        if m.find(positionD) == 0:
            print(entry.move, entry.weight)

positionD = 'g1'
fonction2(positionD)
print('test3 done','\n')









