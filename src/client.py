import socket
import connection
import message

class Client():

    def __init__(self, host="localhost", port=9989):
        self.port = port
        self.host = host
        self.running = False

    def start(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))
        self.conn = connection.Connection(conn)

        msg = self.conn.get_message()
        print msg.decoded

        msg = message.Message()
        msg.encode({'username':'enter_name_here'})
        self.conn.send_message(msg)
        
        self.running = True

    def get_game_state(self):
        msg = self.conn.get_message()
        if msg.decoded['game_status'] == 'over':
            self.running = False
        return msg.decoded

    def send_moves(self, moves):
        # TODO: validate moves
        msg = message.Message()
        msg.encode(moves)
        self.conn.send_message(msg)
