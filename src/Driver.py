#!/usr/bin/python
'''
File:    Driver.py
Created: Fri, Oct 5 at 23:45:15 PST
Author:  Tristan W. Bonsor

Description: Proof of concept driver for map generation and display.
'''
from Map import *
from Display import *

MAX_H = 21
MAX_W = 63

M = generateMap(MAX_H, MAX_W)

D = createAdjList(M, TERRAIN_FLOOR)

S = initDisplay()

printAdjList(S, D, Vertex(0,0), True)

S.getch()
'''
printAdjList(S, D, Vertex(0,MAX_H-1), True)

S.getch()

printAdjList(S, D, Vertex(MAX_W-1,MAX_H-1), True)

S.getch()

printAdjList(S, D, Vertex(MAX_W-1,0), True)

S.getch()
'''
endDisplay(S)
