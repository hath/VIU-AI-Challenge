import json

class Message():

    def __init__(self):
        self.decoded = ""
        self.encoded = ""

    def encode(self, data):
        self.decoded = data
        # Condensing JSON encoding by removing spaces from the separators
        self.encoded = json.dumps(data, separators=(',', ':'))
        return self.encoded

    def decode(self, data):
        self.error = False
        self.encoded = data
        try:
            self.decoded = json.loads(data)
        except ValueError:
            self.decoded = ""

        return self.decoded
