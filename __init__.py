import chess


def polyglot(board):
    position = list() # position dans polyglot
    #access the Polyglot book
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            position.append((entry.move, entry.weight, entry.learn))
    return position
#=================================================================
def MineMax(etatcourant,prof,boolean):
    if (prof==0 or etatcourant.is_game_over()):
        return ponderation(etatcourant) #ne bouge pas
    elif boolean==False:
        valeur=-9999
        for child in etatcourant.legal_moves :
            etatcourant = etatcourant.push(chess.Move.from_uci(child))
            valeur=max(valeur,MineMax(child,prof-1,False))
        return valeur
    else:
        valeur=9999
        for child  in etatcourant.legal_moves:
            etatcourant = etatcourant.push(chess.Move.from_uci(child))
            valeur=min(valeur,MineMax(child,prof-1,True))
        return valeur
#=============================================================
def alpha_betaA(profondeur, board, a, b):
	if profondeur == 0:
		return ponderation(board)
	v = -9999
	bestmove = None
	moves = board.legal_moves
	for move in moves:
		board.push(chess.Move.from_uci(str(move)))
		v = max(v, alpha_betaB(profondeur - 1, board, a, b))
		if v > b : 
			bestmove = chess.Move.from_uci(move)
			print(bestmove, v)
			return v
		a = max(v,a)
		return v

def alpha_betaB(profondeur, board, a, b):
	if profondeur == 0:
		return ponderation(board)
	v = 9999
	bestmove = None
	moves = board.legal_moves
	for move in moves:
		board.push(chess.Move.from_uci(str(move)))
		v = min(v, alpha_betaA(profondeur-1, board, a, b))
		if v <= a :
			bestmove = chess.Move.from_uci(move)
			print(bestmove, v)()
		b = min(v, b)
	return v
#============================================================
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
