import socket
import Message

BUFFER_SIZE = 1024
MSG_DELIM = "\t"

class Connection():

    def __init__(self, conn):
        self.conn = conn
        self.buffer = ""

    def getMessage(self):
        data = self.conn.recv(BUFFER_SIZE)
        msg = Message.Message()
        msg.decode(data)
        return msg

    def sendMessage(self, msg):
        self.conn.sendall(msg.encoded)

    def close(self):
        self.conn.close()

