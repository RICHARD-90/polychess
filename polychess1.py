# -*- coding: utf-8 -*-
class Piece :
    def __init__(self, nom):
        self.nom = nom
        
class Joueur:
    def __init__(self, nom, nature, couleur):
        self.nom = nom
        self.nature = nature
        self.couleur = couleur
        self.coups_joues = 0
        
    def set_NbPieces(self):
        self.Roi = 1
        self.Dame = 1
        self.Fou = 2
        self.Cavalier = 2
        self.Tour = 2
        self.Pion = 8
    
    def liste_de_pieces(self):
        Roi = [Piece('Roi')]
        Dame = [Piece('Dame')]
        Cavalier = [Piece('Cavalier')]*2
        Fou = [Piece('Fou')]*2
        Tour = [Piece('Tour')]*2      
        Pion = [Piece('Pion')]*8
        return Roi + Dame + Cavalier + Fou + Pion + Tour
    
    def mise_a_jour(self):
        if self.losePiece == True:
            liste_de_pieces.remove('la piece')
    
Dora = Joueur('Dora', 'Personne', 'Rose')
print (Dora.liste_de_pieces())
        
        
    
                
                
            
    
    
