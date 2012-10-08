#!/usr/bin/python
'''
File:    Level.py
Created: Mon, Oct 1 at 10:13:34 PST
Author:  Tristan W. Bonsor

Description: Functions for level generation. All level_list parameters are assumed
             to be square 2 dimensional lists.
'''
import random
from terrain import *
from vertex import Vertex

'''
Accsessors for terrain sample list (see getSample()).
'''
TOP_LEFT     = 0
TOP          = 1
TOP_RIGHT    = 2
LEFT         = 3
CENTER       = 4
RIGHT        = 5
BOTTOM_LEFT  = 6
BOTTOM       = 7
BOTTOM_RIGHT = 8

'''
Level settings for generateLevel().
'''
CHAOTIC = 0
ANGBAND = 1


HEIGHT = 64
WIDTH  = 64
'''
Returns a 2 dimensional square list of terrain_id's.
'''
def generateLevel(h = HEIGHT, w = WIDTH, setting = CHAOTIC):
    random.seed()
    if h <= 0:
        h = HEIGHT
    if w <= 0:
        w = WIDTH
    M = initRawLevel(h, w)
    if setting == CHAOTIC:
        for i in xrange(int((h * w) / random.randrange(1, int((h * w) / 100)))):
            y = random.randrange(h)
            x = random.randrange(w)
            dy = random.randint(1, 10)
            dx = random.randint(1, 10)
            fillRect(M, y, x, dy, dx, TERRAIN_FLOOR)
    borderRect(M, 0, 0, h, w, TERRAIN_WALL)
    return M


'''
Returns adjacency list for all specified terrain_id in specified level_list.
The adjacency list is returned as dict data type using Vertex namedtuple as
they key, and list of all adjacent terrain_id's.

Also stores height and width of level_list in keys 'HEIGHT' and 'WIDTH'
respectively. Key 'TYPE' contains terrain_id.
'''
def createAdjList(level_list, terrain_id):
    D = dict()
    for y in xrange(len(level_list)):
        for x in xrange(len(level_list[y])):
            L = []
            pos = 0
            D[Vertex(x, y)] = []
            L = getSample(level_list, y, x)
            for cell in L:
                if pos == TOP_LEFT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x-1,y-1))
                if pos == TOP and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x,y-1))
                if pos == TOP_RIGHT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x+1,y-1))
                if pos == LEFT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x-1,y))
                if pos == CENTER and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x,y))
                if pos == RIGHT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x+1,y))
                if pos == BOTTOM_LEFT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x-1,y+1))
                if pos == BOTTOM and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x,y+1))
                if pos == BOTTOM_RIGHT and cell == terrain_id:
                    D[Vertex(x, y)].append(Vertex(x+1,y+1))
                pos += 1
    D['HEIGHT'] = len(level_list)
    D['WIDTH']  = len(level_list[0]) # Remember, square 2d lists.
    D['TYPE'] = terrain_id
    return D

'''
Returns a two dimensional list with num rows (or columns) of empty sublists.
If value in parameter is zero or less, an empty list is returned.
'''
def newMatrix(num):
    if num < 1:
        num = 0
    a = [[] for n in xrange(num)]
    return a


'''
Returns a 2 dimensional list initialized to TERRAIN_WALL ID value.
'''
def initRawLevel(h, w):
    raw_level = newMatrix(h)
    for row in raw_level:
        for col in xrange(w):
            row.append(TERRAIN_WALL)
    return raw_level

'''
Fills a rectangle in the specified 2d list with specified terrain_id. Paramters
x & y specify the upper left corner of rectangle, h & w specify height and width
of rectangle. Returns true if successful, false otherwise. Note that if rectangle
falls outside of outer boundery of level, operation will not complete and false is
returned.
'''
def fillRect(level_list, y, x, h, w, terrain_id):
    if y < 0 or x < 0:
        return False
    try:
        level_list[y+h-1][x+w-1] # Remember, square 2d lists.
    except IndexError:
        return False
    for row in xrange(y,y+h):
        for col in xrange(x,x+w):
            level_list[row][col] = terrain_id
    return True

'''
Borders specified rectangle dimensions with specified terrain_id. Paramters
x & y specify the upper left corner of rectangle, h & w specify height and width
of rectangle. Returns true if successful, false otherwise. Note that if rectangle
falls outside of outer boundery of level, operation will not complete and false is
returned.
'''
def borderRect(level_list, y, x, h, w, terrain_id):
    if y < 0 or x < 0:
        return False
    try:
        level_list[y+h-1][x+w-1] # Remember, square 2d lists.
    except IndexError:
        return False
    for col in xrange(x,x+w):
        level_list[y][col] = level_list[y+h-1][col] = terrain_id
    for row in xrange(y,y+h):
        level_list[row][x] = level_list[row][x+w-1] = terrain_id
    return True

'''
Returns true if specified terrain_id is found in specified rectangle dimensions.
Note that test is still performed even if part of the rectangular dimensions fall
outside of the specified level_list dimensions. Returns false if terrain_id is not
found.
'''
def testArea(level_list, y, x, h, w, terrain_id):
    offset_y = offset_x = 0
    if y < 0:
        offset_y = y
        y = 0
    if x < 0:
        offset_x = x
        x = 0
    for row in xrange(y,y+h+offset_y):
        for col in xrange(x,x+w+offset_x):
            try:
                result = (terrain_id == level_list[row][col])
            except IndexError:
                break
            else:
                if result:
                    return True
        try:
            level_list[row]
        except IndexError:
            return False
    return False

'''
Returns returns list of terrain_id's in order of row, left to right, of all 8
cells surrounding cell y,x; Cell y,x is included bringing the total to 9 list
items.
'''
def getSample(level_list, y, x):
    L = []
    for v in xrange(y-1,y+2):
        for u in xrange(x-1,x+2):
            if v < 0 or u < 0:
                L.append(None)
            else:
                try:
                    cell = level_list[v][u]
                except IndexError:
                    L.append(None)
                else:
                    L.append(cell)
    return L
