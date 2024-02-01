# https://docs.circuitpython.org/en/8.2.x/shared-bindings/espnow/index.html

# Sender

import espnow
print('sender')
e = espnow.ESPNow()
# peer = espnow.Peer(mac=b'\xff\xff\xff\xff\xff\xff')

# sender 8552FE9B7F to receiver 615271857F
peer = espnow.Peer(mac=b'\x64\xb7\x08\xb7\x9d\xa8') 

# sender 615271857F to receiver 8552FE9B7F 
peer = espnow.Peer(mac=b'\x64\xb7\x08\xb8\x58\x1c')

e.peers.append(peer)

e.send("Starting...")
for i in range(10):
    e.send(str(i)*20)
e.send(b'end')