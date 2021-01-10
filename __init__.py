import chess
import math as m
#from collections import namedtuple

#==============================================================================
def polyglot(board):
    position = list() # position dans polyglot
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            position.append((entry.move, entry.weight, entry.learn))
    return position
#==============================================================================
def minmax(depth, board, is_maximizing):
    
    # je copy le board
    board_copy = board.copy()
    
    if depth == 0 :
        # on evalue le board
        return ponderation(board_copy)
    
    possibleMoves = board_copy.legal_moves
    
    if is_maximizing:
        v = -9999
        for move in possibleMoves:
            move = chess.Move.from_uci(str(move))
            board_copy.push(move)
            v = max(v, minmax(depth-1, board_copy, not(is_maximizing)))
            board_copy.pop()
        return v
    else:
        v = 9999
        for move in possibleMoves:
            move = chess.Move.from_uci(str(move))
            board_copy.push(move)
            v = min(v, minmax(depth-1, board_copy, not(is_maximizing)))
            board_copy.pop()
        return v
#==============================================================================
def alphabeta(depth, board, is_maximizing):
	
	bestmove = None
	movepond = -m.inf
	print(bestmove, movepond)

	a = minmax(depth, board, is_maximizing)
	b = minmax(depth, board, not(is_maximizing))
	
	board1 = board.copy()
	moves = board1.legal_moves
	for k in moves:
		move = chess.Move.from_uci(str(k))
		board1.push(move)

		if is_maximizing:
			valeur = alpha(depth, board1, b, a)
		else:
			valeur = beta(depth, board1, b, a)

		board1.pop()
		if valeur > movepond:
			bestmove = move
			movepond = valeur
			print(bestmove, movepond)

	return bestmove
#==============================================================================
def alpha(depth, board, a, b):
    board1 = board.copy()
    
    if depth == 0:
        return ponderation(board1)
    valeur = - m.inf
    moves = board1.legal_moves
    try:
        for move in moves:
            x = chess.Move.from_uci(str(move))
            try:
                board1.push(x)
            except AssertionError:
                continue
            valeur = max(valeur, beta(depth-1, board1, a, b))
            if valeur >= b :
                return valeur
            a = max(valeur, a)
    except IndexError:
        pass
    return valeur 

def beta(depth, board, a, b):
    board2 = board.copy()
    
    if depth == 0:
        return ponderation(board2)
    valeur = m.inf
    moves = board2.legal_moves
    for depl in moves:
        k = chess.Move.from_uci(str(depl))
        try:
            board2.push(k)
        except AssertionError:
            continue
        valeur = min(valeur, alpha(depth-1, board2, a, b))
        if valeur <= a:
            return valeur 
        b = min(valeur, b)
    return valeur
#==============================================================================
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
#==============================================================================      
def ponderation(board):
    #on parcourt les differentes cases du board 
    p = 0
    #chaque fois que le board s'actualise, la ponderation change
    
    i = 0
    
    while i < 64 and get_piecevalue(str(board.piece_at(i))) != None:
    # for i in (0,63):
        p += get_piecevalue(str(board.piece_at(i)))
        i += 1
    return p
#==============================================================================

# test
# depth = 3
# board = chess.Board()
# print(board)
# #******************************************************************************
# i = 0
# while i<100:
#     if i%2 == 0:
#         alphabeta(depth, board, True)
#         move = input('player 1 :')
#         board.push_san(str(move))
#         print(board,'\n\n')
#     else:
#         move = alphabeta(depth, board, False)
#         board.push_san(str(move))
#         print(board,'\n\n')
#     i +=1

