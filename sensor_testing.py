from sense_hat import SenseHat

sense = SenseHat()

red = (100, 0, 0)
green = (0, 100, 0)
white = (100, 100, 100)


def temp():
    t = round(sense.temp, 1)
    sense.show_message('T: ' + str(t), text_colour=white)
    
def pres():
    p = round(sense.pressure)
    sense.show_message('P: ' + str(p), text_colour=white)

def humi():
    h = round(sense.humidity, 1)
    sense.show_message('H: ' + str(h), text_colour=white)

index = 0
sensors = ["temp", "pres", "humi"]

def update_screen(mode):
    if mode == 'temp':
        temp()
    elif mode == 'pres':
        pres()
    elif mode == 'humi':
        humi()
    
while True:
    selection = False
    events = sense.stick.get_events()
    for event in events:
    # Skip releases
        if event.action != "released":
            if event.direction == "left":
                index -= 1
                selection = True
        elif event.direction == "right":
            index += 1
            selection = True
        if selection:
            current_mode = sensors[index % 3]
            update_screen(current_mode)
  
    if not selection:      
        current_mode = sensors[index % 3]
        update_screen(current_mode)
