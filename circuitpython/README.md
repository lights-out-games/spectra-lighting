rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
flash read err, 1000
ets_main.c 371 
(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ esptool.py --chip esp32 --port /dev/cu.usbserial-8552FE9B7F write_flash -z 0x0 '/Users/mgarrido
/Downloads/adafruit-circuitpython-m5stack_atom_lit
e-en_US-8.2.9.bin'
esptool.py v4.7.0
Serial port /dev/cu.usbserial-8552FE9B7F
Connecting.....
Chip is ESP32-PICO-D4 (revision v1.1)
Features: WiFi, BT, Dual Core, 240MHz, Embedded Flash, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 64:b7:08:b8:58:1c
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00000000 to 0x0014afff...
Compressed 1352736 bytes to 909290...
Wrote 1352736 bytes (909290 compressed) at 0x00000000 in 81.4 seconds (effective 133.0 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ mpremote
Connected to MicroPython at /dev/cu.usbserial-8552FE9B7F
Use Ctrl-] or Ctrl-x to exit this shell

Adafruit CircuitPython 8.2.9 on 2023-12-06; M5Stack Atom Lite with ESP32
>>> 
>>> import network
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: no module named 'network'
>>> import espnow
>>> 

(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ esptool.py --chip esp32 --port /dev/
cu.usbserial-615271857F write_flash -z 0x0 '/Users/mgarrido/Downloads/adafruit-circuitpytho
n-m5stack_atom_lite-en_US-8.2.9.bin'
esptool.py v4.7.0
Serial port /dev/cu.usbserial-615271857F
Connecting....
Chip is ESP32-PICO-D4 (revision v1.1)
Features: WiFi, BT, Dual Core, 240MHz, Embedded Flash, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 64:b7:08:b7:9d:a8
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00000000 to 0x0014afff...
Compressed 1352736 bytes to 909290...
Wrote 1352736 bytes (909290 compressed) at 0x00000000 in 81.0 seconds (effective 133.5 kbit/s)...
Hash of data verified.


/dev/cu.usbserial-8552FE9B7F
MAC: 64:b7:08:b8:58:1c

Serial port /dev/cu.usbserial-615271857F
MAC: 64:b7:08:b7:9d:a8


https://docs.circuitpython.org/en/8.2.x/shared-bindings/espnow/index.html

# Sender

import espnow

e = espnow.ESPNow()
peer = espnow.Peer(mac=b'\xff\xff\xff\xff\xff\xff')

peer = espnow.Peer(mac=b'\x64\xb7\x08\xb7\x9d\xa8')
peer = espnow.Peer(mac=b'\x64\xb7\x08\xb8\x58\x1c')
e.peers.append(peer)

e.send("Starting...")
for i in range(10):
    e.send(str(i)*20)
e.send(b'end')


# Receiver

import espnow

e = espnow.ESPNow()
packets = []

while True:
    if e:
        packet = e.read()
        packets.append(packet)
        if packet.msg == b'end':
            break

print("packets:", f"length={len(packets)}")
for packet in packets:
    print(packet)