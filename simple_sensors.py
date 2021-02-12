from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

sense.low_light = True

green = (0, 100, 0)
red = (100, 0, 0)
blue = (0, 0, 100)
white = (100, 100, 100)

while True:
    events = sense.stick.get_events()
    for event in events:
        if event.action == 'pressed' and event.direction == 'middle':
            time = datetime.now().strftime('%H:%M')
            sense.show_message(str(time), text_colour=white)
            temp = round(sense.temp, 1)
            sense.show_message(str(temp) + '\'C', text_colour=white)
            humidity = round(sense.humidity, 1)
            sense.show_message(str(humidity) + '%', text_colour=white)
            pressure = round(sense.pressure)
            sense.show_message(str(pressure) + ' mB', text_colour=white)
            

