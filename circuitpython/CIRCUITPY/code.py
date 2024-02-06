import board
import time
import neopixel_write
import digitalio
import rainbowio import colorwheel
import neopixel

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

pixel_pin = board.A1
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
