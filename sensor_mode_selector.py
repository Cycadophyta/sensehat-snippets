from sense_hat import SenseHat
import time
from statistics import mean
import pandas as pd

sense = SenseHat()

sense.low_light = True

green = (0, 100, 0)
red = (100, 0, 0)
blue = (0, 0, 100)
white = (100, 100, 100)


def show_t():
    sense.show_letter("T", text_colour=white, back_colour = red)
    time.sleep(.5)

def show_p():
    sense.show_letter("P", text_colour=white, back_colour = green)
    time.sleep(.5)

def show_h():
    sense.show_letter("H", text_colour=white, back_colour = blue)
    time.sleep(.5)

def selection_screen(mode):
    if mode == "temp":
        show_t()
    elif mode == "pressure":
        show_p()
    elif mode == "humidity":
        show_h()

def sensor_screen(mode):
    if mode == "temp":
        temp = sense.temp
        temp_value = temp / 2.5 + 16
        pixels = [red if i < temp_value else white for i in range(64)]
    elif mode == "pressure":
        pressure = sense.pressure
        pressure_value = pressure / 20
        pixels = [green if i < pressure_value else white for i in range(64)]
    elif mode == "humidity":
        humidity = sense.humidity
        humidity_value = 64 * humidity / 100
        pixels = [blue if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)

index = 0
sensors = ["temp", "pressure", "humidity"]

# Intro Animation

show_t()
show_p()
show_h()

sensor_screen("temp")

index = 0
sensors = ["temp", "pressure", "humidity"]

mode_selection = False
mode_selected = False

# Main loop

while True:
    current_mode = sensors[index % 3]
    sensor_screen(current_mode)
    events = sense.stick.get_events()
    for event in events:
        if event.action == 'held' and event.direction == 'middle':
            mode_selection = True
            print('select mode')
            sense.clear()

    while mode_selection == True:
        selection = False
        mode = False
        events = sense.stick.get_events()
        for event in events:
            if event.action == 'pressed':
                if event.direction == "left":
                    index -= 1
                    selection = True
                elif event.direction == "right":
                    index += 1
                    selection = True
                if event.direction == 'middle':
                    mode_selection = False
                    mode_selected = True
                if selection:
                    current_mode = sensors[index % 3]
                    selection_screen(current_mode)
                if mode_selected:
                    current_mode = sensors[index % 3]
                    sensor_screen(current_mode)  

        if not selection:      
            current_mode = sensors[index % 3]
            selection_screen(current_mode)
