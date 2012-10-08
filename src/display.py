#!/usr/bin/python
'''
File:    Display.py
Created: Sun, Oct 7 at 01:11:19 PST
Author:  Tristan W. Bonsor

Description: Quick and dirty curses display interface.
'''
import curses
from collections import namedtuple
from vertex import Vertex
from terrain import *

Color_Pair = namedtuple('Color_Pair', ['fgc', 'bgc'])

color_map = dict()

visible_terrain     = dict()
non_visible_terrain = dict()

'''
Prints specified adjacency list, centered at specified vertex, to specified
screen. The refill parameter is set to true to fill screen with TERRAIN_WALL.
'''
def printAdjList(screen, L, vertex, refill = False):
    # terrain_id
    map_type = L['TYPE']
    # Map dimensions
    map_h = L['HEIGHT']
    map_w = L['WIDTH']
    # Center on map
    cy = vertex.y
    cx = vertex.x
    # Start of screen
    scr_y = 0
    scr_x = 0
    # Screen dimensions
    scr_h = screen.getmaxyx()[0]
    scr_w = screen.getmaxyx()[1]
    # Translates from map to screen
    dy = viewDiff(cy, scr_h, map_h)
    dx = viewDiff(cx, scr_w, map_w) 

    y_start = y_len = x_start = x_len = 0

    # Determine map rows to iterate
    if map_h <= scr_h:
        y_len = map_h
    # Snap to top
    elif dy == 0:
        y_len = scr_h
    # Snap to bottom
    elif dy == map_h - scr_h:
        y_start = map_h - scr_h
        y_len = map_h
    else:
        y_start = cy - int(scr_h / 2)

    # Determine map cols to iterate
    if map_w <= scr_w:
        x_len = map_w
    # Snap to left
    elif dx == 0:
        x_len = scr_w
    # Snap to right
    elif dy == map_w - scr_w:
        x_start = map_w - scr_w
        x_len = map_w
    else:
        x_start = cx - int(scr_w / 2)

    if refill:
        # Get terrain display data
        wall = visible_terrain[TERRAIN_WALL]
        pair = color_map[Color_Pair(wall[0], wall[1])]
        # Fill screen with visible walls
        for row in xrange(y_start, y_len):
            for col in xrange(x_start, x_len):
                try:
                    screen.addch(row - dy + scr_y, col - dx + scr_x,
                                 wall[2], curses.color_pair(pair))
                except Exception:
                    pass
                    endCurses(screen)
                    print('addch(' + str(row) + ', ' + str(col)
                          + ', "' + wall[2] + ', ' + str(curses.color_pair(pair))
                          + '"): A fatal error occured.')
                    quit()
    # Get terrain display data for adjacency list type
    terrain = visible_terrain[map_type]
    pair = color_map[Color_Pair(terrain[0], terrain[1])]
    # Create vertex list of relevant map area.
    V = []
    for row in xrange(y_start, y_len-1):
        for col in xrange(x_start, x_len-1):
            V.append(Vertex(col, row))
    # If vertex in adjacencey list is in vertex list, print it and it's neighbours,
    # removing them from the list.
    for key in V:
        for vertex in L[key]:
            try:
                V.remove(vertex)
            except Exception:
                pass
            try:
                screen.addch(vertex.y - dy + scr_y, vertex.x - dx + scr_x,
                             terrain[2], curses.color_pair(pair))
            except Exception:
                pass
    screen.refresh()

'''
Dark magic at work here.
'''
def viewDiff(p, s, m):
    if m <= s:
        return int((m - s) / 2)
    elif p < int(s / 2):
        return 0
    elif p > m - int(s / 2):
        return m - s
    return p - int(s / 2)

'''
Initializes curses terrain data.
'''
def initTerrainDisplay():
    visible_terrain[TERRAIN_WALL] = [curses.COLOR_RED, curses.COLOR_BLACK, "#"]
    visible_terrain[TERRAIN_FLOOR] = [curses.COLOR_WHITE, curses.COLOR_BLACK, "-"]
    non_visible_terrain[TERRAIN_WALL] = [curses.COLOR_RED, curses.COLOR_BLACK,
                                         "#"]
    non_visible_terrain[TERRAIN_FLOOR] = [curses.COLOR_WHITE, curses.COLOR_BLACK,
                                          "-"]


'''
Initializes display.
'''
def initDisplay(h = 24, w = 80):
    screen = initCurses(h, w)
    if screen != None:
        initTerrainDisplay()
    return screen

'''
Terminates display.
'''
def endDisplay(screen):
    endCurses(screen)

'''
Initializes curses and color.
'''
def initCurses(h = 24, w = 80):
    screen = curses.initscr()
    T = screen.getmaxyx()
    if T[0] < h or T[1] < w:
        endCurses()
        print 'Terminal h x w less than ' + str(h) + ' x ' + str(w) + '.'
        return None
    curses.noecho()
    curses.cbreak()
    screen.keypad(1)
    if curses.has_colors():
        curses.start_color()
        pair = 1
        for bgc in xrange(0, 8):
            for fgc in xrange(0, 8):
                curses.init_pair(pair, fgc, bgc)
                color_map[Color_Pair(fgc, bgc)] = pair
                pair = pair + 1
    else:
        endCurses(screen)
        print 'Terminal does not support color.'
        return None
    return screen

'''
Terminates curses.
'''
def endCurses(screen):
    curses.echo()
    curses.nocbreak()
    screen.keypad(0)
    curses.endwin()
