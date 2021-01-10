# PolyChess

L'objectif de ce dépôt Git est de créer un jeu d'échecs dans un environnement Python, permettant à un utilisateur de lancer une partie d'échecs avec l'ordinateur ou avec un autre joueur, à l'aide du module chess de Python.

Il s'agit d'un projet dans le cadre du module PROJ531 de Polytech Annecy-Chambéry.


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

- On sauvegarde  une partie en cours au format PGN afin de ne pas perdre des données.

- On utilise la notation FEN (Forsyth Edward Notation) pour noter la position des pièces sur l'échéquier. Elle permet de retenir une position à étudier ultérieurement, mais également pour copier coller rapidement ces mêmes positions sur une interface graphique. Elle utilise la notation anglo-saxonne : K pour le Roi, Q pour la Dame, Q pour la Tour, N pour le Cavalier, B pour le Fou et P pour le Pion.



