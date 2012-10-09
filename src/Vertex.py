#!/usr/bin/python
'''
File:    Vertex.py
Created: Sat, Sep 29 at 00:33:57 PST
Author:  Tristan W. Bonsor

Description: Immutable vertex that represents an ordered pair (x,y).
             Immutability allows the vertex to act as a key (ie. hashable)
             in the adjacency list (python dict => hash table).
'''

from collections import namedtuple
Vertex = namedtuple('Vertex', ['x', 'y'])
