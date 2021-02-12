from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

sense.low_light = True

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
off = (0, 0, 0)

event = sense.stick.wait_for_event()
print(f'The joystick was {event.action} {event.direction}.')
sleep(0.1)
event = sense.stick.wait_for_event(emptybuffer=False)
print(f'The joystick was {event.action} {event.direction}.')
