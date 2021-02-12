from sense_hat import SenseHat
from time import sleep
from statistics import mean
import pandas as pd
from datetime import datetime


## Variables ##

sense = SenseHat()

sense.low_light = True

green = (0, 100, 0)
red = (100, 0, 0)
blue = (0, 0, 100)
white = (100, 100, 100)

index = 0
sensors = ['time', 'temp', 'humidity', 'pressure']
selection = False


## Functions ##

def selection_screen(mode):
    if mode == "temp":
        show_t()
    elif mode == "pressure":
        show_p()
    elif mode == "humidity":
        show_h()

def sensor_screen(mode):
    if mode == 'time':
        time = datetime.now().strftime('%H:%M')
        sense.show_message(str(time), text_colour=white)
    elif mode == 'temp':
        temp = round(sense.temp, 1)
        sense.show_message(str(temp) + '\'C', text_colour=white)
    elif mode == 'humidity':
        humidity = round(sense.humidity, 1)
        sense.show_message(str(humidity) + '%', text_colour=white)
    elif mode == 'pressure':
        pressure = round(sense.pressure)
        sense.show_message(str(pressure) + ' mB', text_colour=white)


## Main loop ##

try:
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'middle':
                    selection = True
                elif event.direction == "left":
                    index -= 1
                    selection = True
                elif event.direction == "right":
                    index += 1
                    selection = True
                if selection:
                    current_mode = sensors[index % 3]
                    sensor_screen(current_mode)
                    selection = False
        if not selection:
            sense.clear()
except KeyboardInterrupt:
    sense.clear()

