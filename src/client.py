import socket
import connection, message

class Client():

    def __init__(self, host="localhost", port=9989):
        self.port = port
        self.host = host

    def start(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))
        self.conn = connection.Connection(conn)
        msg = self.conn.getMessage()
        print msg.decoded
        msg = message.Message()
        msg.encode({'hello':'world'})
        self.conn.sendMessage(msg)

        msg.encode({'moves':[[0,4],[0,5]]})
        self.conn.sendMessage(msg)

