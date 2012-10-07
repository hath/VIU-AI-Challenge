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
        self.encoded = data
        self.decoded = json.loads(data)
        return self.decoded
