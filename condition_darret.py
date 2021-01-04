import chess
import random

board = chess.Board()
#board.push
print(board) 


#moves = board.legal_moves
#print(moves.count())

while (not board.is_game_over()):
    moves=board.legal_moves
    listMoves=[]
    for move in moves:
        listMoves.append(move)
    next=listMoves[random.randint(0,moves.count()-1)]
    board.push(next)
    
# si le joueur n'a pas de coups disponible alors il est en échec et mat
    if next ==  [] :
        print("joueur en échec et mat")
        
        
    


    #display the move
    print(move)
    
    #save the current position
    current_board = board
    
    #do the move
    board.push(move)
    
    #display the board
    print(board)
    
    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))
    
    #undo the move
    board.pop()
    
    
    
    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())


























   é