
class Map:

    def __init__(self, width=10, height=10):
        self.map = [[0]*width for x in xrange(height)]

    def getMap(self):
        return self.map
