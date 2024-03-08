from machine import Pin
from time import sleep
from neopixel import NeoPixel

pin = Pin(48, Pin.OUT)
pixel = NeoPixel(pin, 1)

for i in range(2): # stop after 2 cycles
    print(f'[LED] {i+1} cycle..' )
    sleep(1)
    pixel[0] = (255,0,0) #red led
    pixel.write()
    print('[LED] display red for 5 seconds')
    sleep(5)
    pixel[0] = (0,255,0) #green led
    pixel.write()
    print('[LED] display green for 2 seconds')
    sleep(2)
    pixel[0] = (0,0,255) #blue led
    pixel.write()
    print('[LED] display blue for 4 seconds')
    sleep(4)

print('[LED] end of cycle..')