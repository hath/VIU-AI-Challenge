import socket
import connection, message

class Server():

    def __init__(self, port=9989):
        self.port = port
        self.host = '127.0.0.1'

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        conn, self.addr = self.server_socket.accept()
        self.conn = connection.Connection(conn)

        msg = message.Message()
        msg.encode({'type': 'start', 'param':{'turnLimit':200}})
        self.conn.send_message(msg)

        msg = self.conn.get_message()
        print msg.decoded

    def end(self):
        msg = message.Message()
        msg.encode({'game_status':'over'})
        self.conn.send_message(msg)
        self.conn.close()
        self.server_socket.close()

    def send_state(self, lvl):
        msg = message.Message()
        msg.encode({'game_status':'running', 'map':lvl})
        self.conn.send_message(msg)

    def get_player_moves(self):
        msg = self.conn.get_message()
        print msg.decoded['moves']


        
