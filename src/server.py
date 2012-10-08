import socket
import Connection, Message

class Server():

    def __init__(self, port=9989):
        self.port = port
        self.host = '127.0.0.1'

    def start(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(1)
        conn, self.addr = self.serverSocket.accept()
        self.conn = Connection.Connection(conn)
        msg = Message.Message()
        msg.encode({'type': 'start', 'param':{'turnLimit':200}})
        self.conn.sendMessage(msg)
        msg = self.conn.getMessage()
        print msg.decoded

    def end(self):
        self.conn.close()
        self.serverSocket.close()

    def sendState(self, map):
        pass

    def getPlayerMoves(self):
        msg = self.conn.getMessage()
        print msg.decoded['moves']


        
