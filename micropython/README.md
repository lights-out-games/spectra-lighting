https://simonprickett.dev/micropython-on-the-m5stack-atom-matrix/
https://github.com/simonprickett/m5stack-atom-micropython

https://docs.espressif.com/projects/esptool/en/latest/esp32/
https://micropython.org/download/M5STACK_ATOM/

https://github.com/kdschlosser/micropython_fastled


(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ ls /dev/tty* 
/dev/tty                                /dev/ttys028
/dev/tty.Bluetooth-Incoming-Port        /dev/ttys029
/dev/tty.onnBoneConduction              /dev/ttys1
/dev/tty.usbserial-6552A47A8D           /dev/ttys2


python3 

esptool.py --chip esp32 --port /dev/tty.usbserial-6552A47A8D 

(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ esptool.py --chip esp32 --port /dev/tty.usbserial-6552A47A8D erase_flash
esptool.py v4.7.0
Serial port /dev/tty.usbserial-6552A47A8D
Connecting....
Chip is ESP32-PICO-D4 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, Embedded Flash, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: d4:d4:da:98:18:a4
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 8.2s
Hard resetting via RTS pin...


(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ esptool.py --chip esp32 --port /dev/tty.usbserial-6552A47A8D write_flash -z 0x1000 '/Users/mgarrido/Documents/GitHub/spectra-lighting/micropython/M5STACK_ATO
M-20240105-v1.22.1.bin'
esptool.py v4.7.0
Serial port /dev/tty.usbserial-6552A47A8D
Connecting.....
Chip is ESP32-PICO-D4 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, Embedded Flash, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: d4:d4:da:98:18:a4
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00001000 to 0x001a9fff...
Compressed 1738896 bytes to 1145415...
Wrote 1738896 bytes (1145415 compressed) at 0x00001000 in 102.8 seconds (effective 135.3 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...



(esptoolenv) mgarrido-mbp16:spectra-lighting mgarrido$ mpremote 
Connected to MicroPython at /dev/cu.usbserial-6552A47A8D
Use Ctrl-] or Ctrl-x to exit this shell
1+1
2
>>> 

esptool.py --chip esp32 --port /dev/tty.usbserial-6552A47A8D erase_flash
esptool.py --chip esp32 --port /dev/tty.usbserial-595271A98E erase_flash

esptool.py --chip esp32 --port /dev/tty.usbserial-6552A47A8D write_flash -z 0x1000 '/Users/mgarrido/Documents/GitHub/spectra-lighting/micropython/M5STACK_ATOM-20240105-v1.22.1.bin'
esptool.py --chip esp32 --port /dev/tty.usbserial-595271A98E write_flash -z 0x1000 '/Users/mgarrido/Documents/GitHub/spectra-lighting/micropython/M5STACK_ATOM-20240105-v1.22.1.bin'

source esptoolenv/bin/activate

mpremote connect list

mpremote connect id:6552A47A8D
MAC: d4:d4:da:98:18:a4

mpremote connect id:595271A98E
MAC: 64:b7:08:80:81:84

import atom
a = atom.Matrix()
a.set_pixels_color(16, 0, 0)
a.set_pixels_color(0, 16, 0)
a.set_pixels_color(0, 0, 16)



https://docs.micropython.org/en/latest/library/espnow.html

# Sender

import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)

# Sending to specific receiver

peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'   # MAC address of peer's wifi interface
peer = b'\x64\xb7\x08\x80\x81\x84' # 64:b7:08:80:81:84
e.add_peer(peer)      # Must add_peer() before send()

e.send(peer, "Starting...")
for i in range(100):
    e.send(peer, str(i)*20, True)
e.send(peer, b'end')


# Sending to any receiver

bcast = b'\xff' * 6
e.add_peer(bcast)
e.send(bcast, "Hello World!")


# Receiver

import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break


- How to connect and set roles?

- How to synchronize state?
- How to synchronize state: light pattern