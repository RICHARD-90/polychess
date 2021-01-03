import chess

board = chess.Board()
#board.push
print(board) 

# condition d'arret : 

# Si la piece est le roi blanc, qu'il est en echec et qu'il n'a plus de coup disponible, alors il y a echec et mat.
def isEchecEtMatBlanc(self):
    for i in range(0,63):
        if self.fonction1(i).couleur == 'blanc' and self.fonction2(i) != []:
            return False
    return True
                
def isEchecEtMatNoir(self):
    for i in range(0,63):
        if self.fonction1(i).couleur == 'noir' and self.fonction2(i) != []:
            return False
    return True


# fonction1 : pour avoir la position des pièces
# fonction2 : la liste des coups possibles     