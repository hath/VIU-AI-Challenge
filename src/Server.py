import socket
import Connection, Message

BUFFER_SIZE = 1024

class Server():

    def __init__(self, port=9989):
        self.port = port
        self.host = '127.0.0.1'

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        conn, self.addr = s.accept()
        self.conn = Connection.Connection(conn)
        msg = self.conn.getMessage()
        print msg.decoded['hello']

    def end(self):
        self.conn.close()

    def sendState(self, map):
        pass

    def getPlayerMoves(self):
        pass

        
