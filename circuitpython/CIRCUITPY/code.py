import board
import time
import neopixel_write
import digitalio

# pin = digitalio.DigitalInOut(board.NEOPIXEL)
# pin.direction = digitalio.Direction.OUTPUT
# # G,R,B color format
# # example sending data to 3 pixels
# # 1,2,3 pixels: [G1,R1,B1, G2,R2,B2, G3,R3,B3 ]
# pixel_off = bytearray([0, 0, 0]) # pixel 1: green
# pixel_off = bytearray([255, 0, 0])

# pixel_off = bytearray([
#     255,0,0, 
#     255,255,0, 
#     0,255,255,
#     0,0,255])

# b = 20

# pixel_off = bytearray([
#     b,0,0, 
#     b,b,0, 
#     0,b,b,
#     0,0,b])
# neopixel_write.neopixel_write(pin, pixel_off)

# pin = digitalio.DigitalInOut(board.D25)
# pin.direction = digitalio.Direction.OUTPUT

lcd = board.DISPLAY
while True:
    print('         NEOPIXEL  ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')