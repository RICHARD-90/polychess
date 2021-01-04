import chess
board = chess.Board()

def get_piecevalue(piece):
    if piece == None:
        return 0
    elif piece == 'p' or piece == 'P':
        return 20
    elif piece == 'n' or piece == 'N':
        return 40
    elif piece == 'b' or piece == 'B':
        return 40
    elif piece == 'r' or piece == 'R':
        return 70
    elif piece == 'q' or piece == 'Q':
        return 100
    elif piece == 'k' or piece == 'K':
        return 1000
    
    
    

    
def ponderation(board):
    #on parcourt les differentes cases du board 
    p = 0
    #chaque fois que le board s'actualise, la ponderation change
    for i in (0,63):
            p = p + get_piecevalue(str(board.piece_at(i)))
        
    return p
