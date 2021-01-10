# PolyChess

L'objectif de ce dépôt Git est de créer un jeu d'échecs dans un environnement Python, permettant à un utilisateur de lancer une partie d'échecs avec l'ordinateur ou avec un autre joueur, à l'aide du module chess de Python.

PolyChess (named polychess as Git repository) is a Chess engine written in Python and used as practicals for a course on project management at the engineering school Polytech Annecy-Chambéry. 

The aim of this repository is not to provide any complete Chess engine since students have to do it based on python-chess. As a consequence, persons interested in this project should check the different forks.

The required features for PolyChess are: 

* PolyChess is able to play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess

## Milestones for the project

Milestone 1:

PolyChess is able to play against user or another engine through UCI, has an opening book and an AI

Milestone 2:

PolyChess plays on Lichess (and FICS) 

Milestone 3:

Board representation and legal moves are no longer provided by python-chess but are students' responsibilities

## New techniques/skills/terms to get acquainted with

* Chess (maybe)
* Universal Chess Interface (UCI) (http://wbec-ridderkerk.nl/html/UCIProtocol.html)
* Portable General Notation (PGN)
* Board representation (bitboards, 0x88, 120-square representation, 64-square representation)
* MinMax (Negamax)
* Alpha-Beta pruning
* Chess rules (five fold repetition, seventy-five moves)
* Opening book (Polyglot)
* Forsyth-Edwards Notation (FEN) (https://www.chessprogramming.org/Forsyth-Edwards_Notation)
* Piece-Square table
* Move ordering
* Position evaluation
* Transposition table
* Zobrist key
* Perft

## Objectif
Le programme va permettre à l'utilisateur de commencer une partie d'échecs et donc de déplacer des pièces à sa guise, selon les mouvements qu'il juge stratégiques. Il jouera une partie standard, soit contre un autre joueur, soit contre une IA.

## Déroulement
Pour jouer aux échecs, il faudra :
- Un échéquier composé de 64 cases : 32 cases blanches et 32 cases noires. Il comporte 8 colonnes (de A à Z) et 8 lignes (de 1 à 8).
- Des pièces : 16 pièces noires pour un joueur et 16 pièces blanches pour un joueur. Chaque joueur dispose d'un Roi, une Dame, deux Tours, deux Fous, deux Cavaliers et huit Pions.

L'objectif est de mettre en échec et mat le Roi du joueur adverse, c'est-à-dire que l'échec ne peut plus être évité. Les deux joueurs jouent à tour de rôle en déplaçant une seule de leurs pièces  (le roque, que nous verrons plus loin, est une exception à cette règle). Si une pièce se déplace sur une case occupée par une pièce adverse, celle-ci est prise et enlevée de l’échiquier. Une pièce ne peut pas se placer sur une case occupée par une pièce de son propre camp. Seul le Cavalier peut sauter au-dessus des autres pièces.

## Caractéristiques du programme

- Interface d'échecs universelle (UCI)
Le moteur doit utiliser l'UCI (interface d'échecs universelle). Celle-ci sera envoyée une fois comme première commande après le démarrage du programme pour dire au moteur de passer en mode UCI. Après avoir reçu la commande UCI, le moteur doit s'identifier avec la commande "id" et envoyer les commandes "option" pour indiquer à l'interface graphique les paramètres de moteur pris en charge par le moteur, le cas échéant. Après cela, le moteur doit envoyer "uciok" pour accuser réception du mode UCI. Si aucun uciok n'est envoyé dans un certain laps de temps, la tâche du moteur sera supprimée par l'interface graphique.

- Polyglot : il s'agit d'une fonction qui retourne les positions statistiquement gagnantes répertoriées dans le livre: "bookfiss.bin" selon l'état de l'échéquier ainsi que leur pondération.

