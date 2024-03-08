# boot

import ugit
from machine import Pin
from time import sleep
from neopixel import NeoPixel

pin = Pin(48, Pin.OUT)
pixel = NeoPixel(pin, 1)

pixel[0] = (0,255,0)
pixel.write()

ugit.pull_all()