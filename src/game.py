#!/usr/bin/env python
'''
wait for connection from player
main loop:
    send game state to player AI
    wait for moves from player AI
    send game state to cat AI
    wait for moves from cat AI
'''
import map, server, cat_ai

SHUTDOWN = False

map = map.generateMap(21, 63)
server = server.Server()
cat = cat_ai.CatAI()

server.start()

while not SHUTDOWN:
    server.sendState(map)
    server.getPlayerMoves()

    cat.getCatMoves(map)
    
    SHUTDOWN = True
    
server.end()
