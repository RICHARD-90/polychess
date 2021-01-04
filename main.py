# tant que le jeu n'est pas terminé, on joue
tour = 0 # permet de determiner a qui le tour
while not(board.is_game_over()):
  
  cap_K = True
  if tour % 2 == 0:
    moves = board.legal_moves
    for move in moves :
      for deplacemennt in polyglot():
        if move == deplacement[0]:
            cap_K = False
            print(deplacement[0],deplacement[1])
  if cap_K:
    appel a alphabeta
  move_util = input('entrer votre movement:')
  board.push(chess.Move.from_uci(str(move_util)))
        
  else:
    ******
  tour = tour +1 

# condition d'arret
if (board.is_game_over()):
    print("The game is over")
    print(board.result())
