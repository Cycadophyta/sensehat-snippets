from sense_hat import SenseHat
import time

sense = SenseHat()

R = (200, 0, 0)
G = (0, 200, 0)
X = (0, 0, 0)

for i in range(9, -1, -1):
    if i < 4:
        text = R
    else:
        text = G
    sense.show_letter(str(i), text)
    time.sleep(1)
    
sense.clear()