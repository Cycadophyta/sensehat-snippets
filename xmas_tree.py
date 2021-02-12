from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

X = [0, 100, 0] # Green
O = [0, 0, 0] # Black
W = [255, 255, 255]  # White
B = [139, 69, 19] # Brown
U = [150, 219, 242] # Blue
R = [255, 0, 0] # Red

while True:
	xmas_tree= [
	O, O, O, R, X, O, O, O,
	O, O, X, X, R, X, O, O,
	O, X, R, X, X, X, R, O,
	O, O, X, X, R, X, O, O,
	O, R, X, R, X, X, R, O,
	X, X, X, X, R, X, X, X,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
	xmas_tree = [
	O, O, O, X, U, O, O, O,
	O, O, X, U, X, X, O, O,
	O, X, X, X, X, U, X, O,
	O, O, U, X, X, X, O, O,
	O, X, X, X, U, X, X, O,
	X, U, X, X, X, U, X, U,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
'''	
        xmas_tree = [
	O, O, O, X, X, O, O, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	X, X, X, X, X, X, X, X,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
	xmas_tree = [
	O, O, O, X, X, O, O, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	X, X, X, X, X, X, X, X,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]
	sense.set_pixels(xmas_tree)
	sleep(3)
'''
