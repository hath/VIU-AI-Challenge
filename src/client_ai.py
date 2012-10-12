import client

client = client.Client()
client.start()

print client.get_game_state()
while client.running:
    client.send_moves({'moves':[([0,3], [0,4]), ([7,6],[6,5])]})
    print client.get_game_state()
