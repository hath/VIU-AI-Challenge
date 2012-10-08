#!/usr/bin/env python
'''
wait for connection from player
main loop:
    send game state to player AI
    wait for moves from player AI
    send game state to cat AI
    wait for moves from cat AI
'''
import level, server, cat_ai

SHUTDOWN = False

lvl = level.generateLevel(21, 63)
server = server.Server()
cat = cat_ai.CatAI()

server.start()

while not SHUTDOWN:
    server.sendState(lvl)
    server.getPlayerMoves()

    cat.getCatMoves(lvl)
    
    SHUTDOWN = True
    
server.end()
