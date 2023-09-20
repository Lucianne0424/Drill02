from pico2d import *
from math import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
moveD = 0
count = 36000

while 1:
	clear_canvas_now()
	grass.draw_now(400, 30)
	character.draw_now(x,y)

	if moveD == 0:
		x += 2
		if x == 700:
			moveD = 1
		elif x == 400:
			count = 36000
			moveD = 4
	elif moveD == 1:
		y += 2
		if y == 500:
			moveD = 2
	elif moveD == 2:
		x -= 2
		if x == 100:
			moveD = 3
	elif moveD == 3:
		y -= 2
		if y == 90:
			moveD = 0
	elif moveD == 4:
		r = 200
		x = 400 + r * cos(radians(count) * pi / 180)
		y = 290 + r * sin(radians(count) * pi / 180)
		count -= 100
		if count == 15000:
			x = 400
			y = 90
			moveD = 0
	delay(0.01)

close_canvas()
