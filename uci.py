# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 03:42:56 2021

@author: Junio
"""

from __future__ import print_function
from __future__ import division
import importlib
import re
import sys
import time
import logging
import argparse

import tools
import __init__ #__init__

#from tools import Unbuffered
import tools 

WHITE, BLACK = range(2)
# Disable buffering
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
        sys.stderr.write(data)
        sys.stderr.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('module', help='__init__.py file (without .py)', type=str, default='__init__', nargs='?')
    parser.add_argument('--tables', metavar='pst', help='alternative pst table', type=str, default=None)
    args = parser.parse_args()

    __init__ = importlib.import_module(args.module)
    if args.tables is not None:
        pst_module = importlib.import_module(args.tables)
        __init__.pst = pst_module.pst

    logging.basicConfig(filename='__init__.log', level=logging.DEBUG)
    out = Unbuffered(sys.stdout)
    def output(line):
        print(line, file=out)
        logging.debug(line)
    pos = tools.parseFEN(tools.FEN_INITIAL)
    searcher = __init__.Searcher()
    color = WHITE
    our_time, opp_time = 1000, 1000 # time in centi-seconds
    show_thinking = True

    stack = []
    while True:
        if stack:
            smove = stack.pop()
        else:
            smove = input()

        logging.debug(f'>>> {smove} ')

        if smove == 'quit':
            break

        elif smove == 'uci':
            output('id name __init__')
            output('id author Thomas Ahle & Contributors')
            output('uciok')

        elif smove == 'isready':
            output('readyok')

        elif smove == 'ucinewgame':
            stack.append('position fen ' + tools.FEN_INITIAL)

        # syntax specified in UCI
        # position [fen  | startpos ]  moves  ....

        elif smove.startswith('position'):
            params = smove.split(' ')
            idx = smove.find('moves')

            if idx >= 0:
                moveslist = smove[idx:].split()[1:]
            else:
                moveslist = []

            if params[1] == 'fen':
                if idx >= 0:
                    fenpart = smove[:idx]
                else:
                    fenpart = smove

                _, _, fen = fenpart.split(' ', 2)

            elif params[1] == 'startpos':
                fen = tools.FEN_INITIAL

            else:
                pass

            pos = tools.parseFEN(fen)
            color = WHITE if fen.split()[1] == 'w' else BLACK

            for move in moveslist:
                pos = pos.move(tools.mparse(color, move))
                color = 1 - color

        elif smove.startswith('go'):
            #  default options
            depth = 1000
            movetime = -1

            _, *params = smove.split(' ')
            for param, val in zip(*2*(iter(params),)):
                if param == 'depth':
                    depth = int(val)
                if param == 'movetime':
                    movetime = int(val)
                if param == 'wtime':
                    our_time = int(val)
                if param == 'btime':
                    opp_time = int(val)

            moves_remain = 40

            start = time.time()
            ponder = None
            for sdepth, _move, _score in searcher.search(pos):
                moves = tools.pv(searcher, pos, include_scores=False)

                if show_thinking:
                    entry = searcher.tp_score.get((pos, sdepth, True))
                    score = int(round((entry.lower + entry.upper)/2))
                    usedtime = int((time.time() - start) * 1000)
                    moves_str = moves if len(moves) < 15 else ''
                    output('info depth {} score cp {} time {} nodes {} pv {}'.format(sdepth, score, usedtime, searcher.nodes, moves_str))

                if len(moves) > 5:
                    ponder = moves[1]

                if movetime > 0 and (time.time() - start) * 1000 > movetime:
                    break

                if (time.time() - start) * 1000 > our_time/moves_remain:
                    break

                if sdepth >= depth:
                    break

            entry = searcher.tp_score.get((pos, sdepth, True))
            m, s = searcher.tp_move.get(pos), entry.lower
            # We only resign once we are mated.. That's never?
            if s == -__init__.MATE_UPPER:
                output('resign')
            else:
                moves = moves.split(' ')
                if len(moves) > 1:
                    output(f'bestmove {moves[0]} ponder {moves[1]}')
                else:
                    output('bestmove ' + moves[0])

        elif smove.startswith('time'):
            our_time = int(smove.split()[1])

        elif smove.startswith('otim'):
            opp_time = int(smove.split()[1])

        else:
            pass

if __name__ == '__main__':
    main()